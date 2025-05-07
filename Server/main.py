from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
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
async def process_zip(file: UploadFile = File(...)):

    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Bitte eine ZIP-Datei hochladen.")

    try:
        temp_dir = tempfile.mkdtemp()
        output_dir = os.path.join(temp_dir, "output")
        os.makedirs(output_dir, exist_ok=True)

        zip_bytes = await file.read()
        zip_io = io.BytesIO(zip_bytes)
        with zipfile.ZipFile(zip_io, "r") as zip_ref:
            pdf_dateien = [f for f in zip_ref.namelist() if f.lower().endswith(".pdf")]
            r.set("verarbeitung:gesamt", len(pdf_dateien))
            for index, pdf_name in enumerate(pdf_dateien):
                with zip_ref.open(pdf_name) as pdf_file:
                    pdf_bytes = pdf_file.read()
                    safe_name = pdf_name.replace("/", "_").replace(".pdf", "")
                    write_metadata(pdf_bytes, safe_name, output_dir)
                    r.set("verarbeitung:verarbeitet", index + 1)
                    time.sleep(5) 

        output_zip_path = os.path.join(temp_dir, "result.zip")
        with zipfile.ZipFile(output_zip_path, "w") as zip_out:
            for file_name in os.listdir(output_dir):
                full_path = os.path.join(output_dir, file_name)
                zip_out.write(full_path, arcname=file_name)

        return FileResponse(
            output_zip_path,
            media_type="application/zip",
            filename="ergebnis_pdfs.zip",
            background=lambda: shutil.rmtree(temp_dir)
        )

    except Exception as e:
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=f"Verarbeitung fehlgeschlagen: {e}")

@app.get("/api/status")
def get_status():
    verarbeitet = int(r.get("verarbeitung:verarbeitet") or 0)
    gesamt = int(r.get("verarbeitung:gesamt") or 0)
    return {
        "verarbeitet": verarbeitet,
        "gesamt": gesamt
    }

@app.post("/api/metadata")
async def get_metadata(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    metadata = reader.metadata
    subject = metadata.get("/Subject", "Kein Betreff gefunden")
    return subject