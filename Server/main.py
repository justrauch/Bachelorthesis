from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import zipfile
import io
from PyPDF2 import PdfReader, PdfWriter
import fitz
import shutil
import tempfile
from typing import Optional
import time
import redis
import traceback

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0)
r.set(f"job:status", "bereit")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def write_metadata(pdf_bytes, name, output_dir):
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

    writer.add_metadata({
        "/Subject": text
    })

    output_path = os.path.join(output_dir, f"{name}.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)

@app.post("/api/process-zip")
async def process_zip(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):

    if r.get("job:status") and r.get("job:status").decode() == "in_bearbeitung":
        raise HTTPException(status_code=429, detail="Die Verarbeitung ist derzeit ausgelastet. Bitte versuche es später erneut.")
    
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Bitte eine ZIP-Datei hochladen.")

    zip_bytes = await file.read()

    r.set(f"job:status", "in_bearbeitung")
    print("n" + r.get("job:status").decode())
    background_tasks.add_task(process_zip_task, zip_bytes)

    return JSONResponse(
        status_code=202,
        content={"detail": "Datei wird verarbeitet"}
    )

def process_zip_task(zip_bytes):
    try:
        temp_dir = tempfile.mkdtemp()
        output_dir = os.path.join(temp_dir, "output")
        os.makedirs(output_dir, exist_ok=True)

        zip_io = io.BytesIO(zip_bytes)
        with zipfile.ZipFile(zip_io, "r") as zip_ref:
            pdf_dateien = [f for f in zip_ref.namelist() if f.lower().endswith(".pdf")]
            r.set(f"job:gesamt", len(pdf_dateien))
            for index, pdf_name in enumerate(pdf_dateien):
                with zip_ref.open(pdf_name) as pdf_file:
                    pdf_bytes = pdf_file.read()
                    safe_name = pdf_name.replace("/", "_").replace(".pdf", "")
                    write_metadata(pdf_bytes, safe_name, output_dir)
                    r.set(f"job:verarbeitet", index + 1)
                    time.sleep(5)

        output_zip_path = os.path.join(temp_dir, "result.zip")
        with zipfile.ZipFile(output_zip_path, "w") as zip_out:
            for file_name in os.listdir(output_dir):
                full_path = os.path.join(output_dir, file_name)
                zip_out.write(full_path, arcname=file_name)

        r.set(f"job:path", output_zip_path)
        r.set(f"job:status", "bereit")
    except Exception as e:
        r.set(f"job:status", f"fehlgeschlagen: {str(e)}")

@app.get("/api/status")
def get_status():
    verarbeitet = int(r.get(f"job:verarbeitet") or 0)
    gesamt = int(r.get(f"job:gesamt") or 0)
    status = r.get(f"job:status")
    file_path = r.get(f"job:path")

    return {
        "verarbeitet": verarbeitet,
        "gesamt": gesamt,
        "status": status.decode() if status else "unbekannt"
    }

@app.get("/api/download")
def download_zip(background_tasks: BackgroundTasks):
    file_path = r.get(f"job:path")
    if not file_path:
        raise HTTPException(status_code=404, detail="Keine Datei gefunden")

    file_path = file_path.decode()

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Datei nicht mehr vorhanden")

    background_tasks.add_task(os.remove, file_path)

    return FileResponse(
        path=file_path,
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