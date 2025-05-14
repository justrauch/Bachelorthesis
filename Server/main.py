from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Depends
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Job

import os
import zipfile
import io
import tempfile
import time
import json
import requests
import dropbox
import traceback

import fitz  # PyMuPDF
import pymupdf
import cv2
import numpy as np
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from openai import OpenAI
from typing_extensions import final
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === INIT ===
Base.metadata.create_all(bind=engine)
app = FastAPI()

DROPBOX_TOKEN = ""

dbx = dropbox.Dropbox(DROPBOX_TOKEN)

openrouter_token = ""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === UTILS ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def sanitize_metadata(text: str) -> str:
    return text.replace("\\n", " ").replace("\n", " ").strip()

# === AI + METADATA ===
def get_description(pdf_bytes):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = "".join(page.extract_text() or "" for page in reader.pages)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_token,
    )
    completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[{
            "role": "user",
            "content": f"<s>[INST] Bitte beschreibe in wenigen Sätzen, worum es in folgendem Text geht. Gib an, zu welchem Thema der Text gehört und was das Ziel des Textes ist: {text} [/INST]"
        }],
        temperature=0.3,
        top_p=0.65,
        frequency_penalty=0.35,
        presence_penalty=0.35
    )
    print(completion)
    return completion.choices[0].message.content

def cossim(page_text, description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([description, page_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

# === IMAGE HANDLING ===
def analyze_image(image_bytes):
    try:
        with Image.open(io.BytesIO(image_bytes)) as img:
            if img.width < 100 or img.height < 100:
                return False
    except Exception:
        return False

    img_array = np.frombuffer(image_bytes, np.uint8)
    img_cv = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if img_cv is None:
        return False

    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([img_hsv], [0], None, [256], [0, 256])
    avg_saturation = np.mean(img_hsv[:, :, 1])
    if np.count_nonzero(hist) < 10 and avg_saturation > 20:
        return False

    lap_var = cv2.Laplacian(cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()
    return lap_var >= 100

def upload_image_and_get_url(image_bytes, dropbox_path):
    dbx.files_upload(image_bytes, dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    try:
        shared = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    except dropbox.exceptions.ApiError as e:
        if e.error.is_shared_link_already_exists():
            shared = dbx.sharing_list_shared_links(path=dropbox_path, direct_only=True).links[0]
        else:
            raise e
    return shared.url.replace("?dl=0", "?raw=1")

def delete_dropbox_file(path):
    dbx.files_delete_v2(path)

def image_choises(image_urls, description):
    image_blocks = [{"type": "image_url", "image_url": {"url": url}} for _, url in image_urls]
    count = 3 if len(image_urls) >= 3 else max(len(image_urls) - 1, 1)
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {openrouter_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-4-scout:free",
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": f"Gib mir eine Beschreibung für {count} der folgenden Bilder, die inhaltlich am besten zu diesem Text passen: {description} Schreibe die Beschreibungen hintereinander weg getrennt mit Absätzen und füge keinen weiteren Text ein."}
                ] + image_blocks
            }]
        })
    )
    print(response)
    return response.json()["choices"][0]["message"]["content"]

def extract_and_analyze_images(doc, top10):
    urls, delete_paths = [], []
    for i, page in enumerate(doc):
        if i + 1 not in [idx for idx, _ in top10]:
            continue
        if len(urls) >= 5:
            break
        for j, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base = doc.extract_image(xref)
            if not base:
                continue
            image_bytes = base["image"]
            ext = base.get("ext", "png")
            filename = f"page{i+1}_img{j}.{ext}"
            if analyze_image(image_bytes):
                path = f"/{filename}"
                delete_paths.append(path)
                url = upload_image_and_get_url(image_bytes, path)
                urls.append((i + 1, url))
                break
    return delete_paths, urls

def get_image_description(pdf_bytes, description):
    reader = PdfReader(io.BytesIO(pdf_bytes))
    scores = [(i + 1, cossim(p.extract_text() or "", description)) for i, p in enumerate(reader.pages)]
    top10 = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    delete_paths, urls = extract_and_analyze_images(doc, top10)
    result = image_choises(urls, description)
    for path in delete_paths:
        delete_dropbox_file(path)
    return result

def write_metadata(pdf_bytes, name, output_io):
    description = "die beschreibung"
    #get_description(pdf_bytes)
    images = "die bilder"
    #sanitize_metadata(get_image_description(pdf_bytes, description))
    meta = f"{description} Folgende Bilder sind zu erwähnen: {images}"
    reader = PdfReader(io.BytesIO(pdf_bytes))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({"/Subject": meta})
    writer.write(output_io)

# === API ROUTES ===
@app.post("/api/process-zip")
async def process_zip(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks(), db: Session = Depends(get_db)):
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Bitte eine ZIP-Datei hochladen.")
    if db.query(Job).filter(Job.job_status == "in_bearbeitung").count() >= 3:
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
        out_path = os.path.join(temp_dir, f"result{job.id}.zip")
        job.result_path = out_path
        db.commit()

        with zipfile.ZipFile(out_path, "w") as zip_out:
            with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zip_ref:
                pdfs = [f for f in zip_ref.namelist() if f.lower().endswith(".pdf")]
                job.gesamt = len(pdfs)
                db.commit()

                for i, name in enumerate(pdfs):
                    with zip_ref.open(name) as f:
                        pdf_bytes = f.read()
                        output = io.BytesIO()
                        write_metadata(pdf_bytes, name.replace("/", "_").replace(".pdf", ""), output)
                        output.seek(0)
                        zip_out.writestr(f"{name}", output.read())
                        job.verarbeitet = i + 1
                        db.commit()
                        db.refresh(job)
                        time.sleep(3)
                        if job.job_status == "abgebrochen":
                            break

        job.job_status = "bereit"
        db.commit()
    except Exception as e:
        print(e)
        job.job_status = f"fehlgeschlagen"
        db.commit()
    finally:
        db.close()

@app.get("/api/status")
def get_all_statuses(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return [{
        "id": j.id, 
        "verarbeitet": j.verarbeitet, 
        "gesamt": j.gesamt, 
        "status": j.job_status, 
        "response_file": j.response_file} for j in jobs]

@app.get("/api/download/{job_id}")
def download_zip(job_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if not job or not job.result_path or not os.path.exists(job.result_path):
        raise HTTPException(status_code=404, detail="Keine Datei gefunden")
    db.delete(job)
    db.commit()
    background_tasks.add_task(os.remove, job.result_path)
    return FileResponse(
        path=job.result_path, 
        media_type="application/zip", 
        filename=f"ergebnis_{job.response_file}", 
        background=background_tasks)

@app.get("/api/stop/{job_id}")
def stop_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Keinen Job gefunden")
    job.job_status = "abgebrochen"
    db.commit()
    return {"message": f"Job {job_id} wurde zurückgesetzt"}

@app.post("/api/metadata")
async def get_metadata(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    metadata = reader.metadata
    return metadata.get("/Subject", "Kein Betreff gefunden")
