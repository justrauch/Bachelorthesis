from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Depends
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Job

import os
import zipfile
import io
from PyPDF2 import PdfReader, PdfWriter
import fitz
import shutil
import tempfile
import time
import traceback

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def write_metadata(pdf_bytes, name, output_io):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        text += f"Text: {page.extract_text()}"

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    i = sum(len(doc.get_page_images(p)) for p in range(len(doc)))
    text += f" Anzahl Bilder: {i}"

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata({"/Subject": text})
    writer.write(output_io)

@app.post("/api/process-zip")
async def process_zip(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks(),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Bitte eine ZIP-Datei hochladen.")

    in_progress_count = db.query(Job).filter(Job.job_status == "in_bearbeitung").count()

    if in_progress_count >= 3:
        raise HTTPException(status_code=429, detail="Die Verarbeitung ist derzeit ausgelastet.")

    zip_bytes = await file.read()

    job = Job(verarbeitet=0, gesamt=0, job_status="in_bearbeitung", response_file=file.filename)
    db.add(job)
    db.commit()
    db.refresh(job)

    background_tasks.add_task(process_zip_task, zip_bytes, job.id)

    return JSONResponse(status_code=202, content={"detail": "Datei wird verarbeitet", "job_id": job.id})

def process_zip_task(zip_bytes, job_id):
    db = SessionLocal()
    try:
        job = db.query(Job).get(job_id)
        temp_dir = tempfile.mkdtemp()

        output_zip_path = os.path.join(temp_dir, f"result{job.id}.zip")
        zip_out = zipfile.ZipFile(output_zip_path, "w")

        zip_io = io.BytesIO(zip_bytes)
        with zipfile.ZipFile(zip_io, "r") as zip_ref:
            pdf_dateien = [f for f in zip_ref.namelist() if f.lower().endswith(".pdf")]
            job.gesamt = len(pdf_dateien)
            db.commit()

            for index, pdf_name in enumerate(pdf_dateien):
                with zip_ref.open(pdf_name) as pdf_file:
                    pdf_bytes = pdf_file.read()
                    safe_name = pdf_name.replace("/", "_").replace(".pdf", "")
                    
                    output_pdf_io = io.BytesIO()
                    write_metadata(pdf_bytes, safe_name, output_pdf_io)

                    output_pdf_io.seek(0)
                    zip_out.writestr(f"{safe_name}.pdf", output_pdf_io.read())

                    job.verarbeitet = index + 1
                    db.commit()
                    time.sleep(5)

        zip_out.close()
        job.job_status = "bereit"
        job.result_path = output_zip_path
        db.commit()
    except Exception as e:
        job.job_status = f"fehlgeschlagen: {str(e)}"
        db.commit()
    finally:
        db.close()


@app.get("/api/status")
def get_all_statuses(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    if not jobs:
        return []

    return [
        {
            "id": job.id,
            "verarbeitet": job.verarbeitet,
            "gesamt": job.gesamt,
            "status": job.job_status,
            "response_file": job.response_file
        }
        for job in jobs
    ]

@app.get("/api/download/{job_id}")
def download_zip(job_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if not job or not job.result_path:
        raise HTTPException(status_code=404, detail="Keine Datei gefunden")

    if not os.path.exists(job.result_path):
        raise HTTPException(status_code=404, detail="Datei nicht mehr vorhanden")
    
    db.delete(job)
    db.commit()
    background_tasks.add_task(os.remove, job.result_path)
    print(job.result_path)
    return FileResponse(
        path=job.result_path,
        media_type="application/zip",
        filename="ergebnis_pdfs.zip",
        background=background_tasks
    )

@app.post("/api/metadata")
async def get_metadata(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    metadata = reader.metadata
    subject = metadata.get("/Subject", "Kein Betreff gefunden")
    return subject
