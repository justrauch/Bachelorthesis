import os, io, re, time, json, tempfile, zipfile, traceback

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Depends
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Job

from PyPDF2 import PdfReader, PdfWriter
import pymupdf

import cv2
import numpy as np
from PIL import Image

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import requests
import base64
from io import BytesIO

# === INIT ===
Base.metadata.create_all(bind=engine)
app = FastAPI()

API_KEY = ''
API_URL_IMAGE_SELECTOR = "https://api.runpod.ai/v2/gya7rpmqp97v58"
API_URL_DESCRIPTION = "https://api.runpod.ai/v2/jh3t3ciq9y5su6"
API_URL_EMBEDDINGS = "https://api.runpod.ai/v2/22vlo1l1fn5xqc"

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

# --- Hilfsfunktionen zur Textextraktion und -strukturierung ---
def extract_text_sections(text):
    matches = list(re.finditer(r'(Ziel:|Thema \d+:)', text))
    sections = [text[matches[i].start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                for i in range(len(matches))]
    return sections

def extract_raw_text_from_pdf(pdf_bytes):
    with io.BytesIO(pdf_bytes) as buffer:
        reader = PdfReader(buffer)
        return "".join(page.extract_text() or "" for page in reader.pages)

def extract_text_pages_from_pdf(pdf_bytes):
    with io.BytesIO(pdf_bytes) as buffer:
        reader = PdfReader(buffer)
        return [page.extract_text() or "" for page in reader.pages]

# --- Ähnlichkeitsbewertung ---
def runpod_request_with_polling_embedding(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }

    response = requests.post(f"{API_URL_EMBEDDINGS}/runsync", headers=headers, json=payload)
    response_json = response.json()

    if response_json.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        job_id = response_json["id"]
        while True:
            status_url = f"{API_URL_EMBEDDINGS}/status/{job_id}"
            status_response = requests.get(status_url, headers=headers)
            status_response.raise_for_status()
            response_json = status_response.json()
            print(response_json)
            if response_json["status"] == "COMPLETED":
                break
            time.sleep(5)

    return response_json["output"]["data"]

def find_most_relevant_pages_with_embeddings(docs, query, doc_embeddings, top_k=5):
    query_embedding = runpod_request_with_polling_embedding({"input": {"input": f"query: {query}"}})[0]["embedding"]
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    ranked = sorted([(idx, score, docs[idx]) for idx, score in enumerate(similarities)], key=lambda x: x[1], reverse=True)
    
    return ranked[:top_k]

# --- Bildverarbeitung und -filterung ---
def is_valid_image(image_bytes):
    with Image.open(io.BytesIO(image_bytes)) as img:
        width, height = img.size
        if width < 50 or height < 50:
            return False
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    img_hsv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2HSV)
    avg_saturation = np.mean(img_hsv[:, :, 1])
    if np.count_nonzero(cv2.calcHist([img_hsv], [0], None, [256], [0, 256])) < 5 and avg_saturation > 40:
        return False

    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    if cv2.Laplacian(gray, cv2.CV_64F).var() < 50:
        return False

    return True

def extract_valid_images(pdf_bytes, page_numbers):
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    valid_images = []
    total_images = 0
    for page_number in page_numbers:
        images = doc[page_number].get_images(full=True)
        if total_images > 3:
            break
        total_images += len(images)
        for i, img in enumerate(images):
            try:
                image_data = doc.extract_image(img[0]).get("image")
                if image_data and is_valid_image(image_data):
                    valid_images.append(image_data)
            except Exception as e:
                print(f"Fehler beim Extrahieren von Bild (XREF {img[0]}): {e}")
    return valid_images

# --- Hilfsfunktionen für API-Requests ---
def encode_image_to_data_uri(image_bytes):
    try:
        buffer = BytesIO()
        Image.open(BytesIO(image_bytes)).convert("RGB").save(buffer, format="JPEG")
        return f"data:image/jpeg;base64,{base64.b64encode(buffer.getvalue()).decode('utf-8')}"
    except Exception as e:
        print(f"Fehler beim Kodieren des Bildes: {e}")
        return None

def post_request(url, payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def wait_for_completion(url_base, job_id):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    while True:
        response = requests.get(f"{url_base}/status/{job_id}", headers=headers)
        response.raise_for_status()
        status_json = response.json()
        if status_json.get("status") == "COMPLETED":
            return status_json
        time.sleep(5)

def request_image_selection_and_caption(images, section_text):
    encoded_images = [encode_image_to_data_uri(img) for img in images if img]
    if not encoded_images:
        return ""

    selection_prompt = (
        f"Lies den folgenden Text:\n{section_text}\n\n"
        "Dir werden mehrere Bilder gezeigt.\n"
        "Analysiere alle Bilder sorgfältig.\n"
        "Welches Bild passt inhaltlich am besten zum Text?\n"
        "Gib nur die Nummer des passenden Bildes an – z. B. 1, 2, 3.\n"
        "Wenn keines passt, gib 0 an. Keine Beschreibung. Keine Erklärung. Nur eine einzige Zahl."
    )

    selection_payload = {"input": {"images": encoded_images, "prompt": selection_prompt}}
    selection_response = post_request(f"{API_URL_IMAGE_SELECTOR}/runsync", selection_payload)
    if selection_response.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        selection_response = wait_for_completion(API_URL_IMAGE_SELECTOR, selection_response["id"])

    try:
        selected_index = int(selection_response.get("output", {}).get("caption", "-1"))
    except ValueError:
        return ""

    if selected_index == 0:
        print("Keines der Bilder wurde als passend zum Text bewertet.")
        return ""

    if selected_index > len(encoded_images) or selected_index < 0:
        print("Ausgewählter Bildindex liegt außerhalb des gültigen Bereichs.")
        return ""

    caption_prompt = (
        "Beschreibe das angegebene Bild.\n"
        "Gib ausschließlich eine Beschreibung des Bildes aus.\n"
        "Keine Erklärungen, keine weiteren Informationen.\n"
        "Nur die Bildbeschreibung."
    )

    caption_payload = {
        "input": {"images": [encoded_images[selected_index - 1]], 
                  "prompt": caption_prompt}
    }
    caption_response = post_request(f"{API_URL_IMAGE_SELECTOR}/runsync", caption_payload)
    if caption_response.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        caption_response = wait_for_completion(API_URL_IMAGE_SELECTOR, caption_response["id"])

    return f"\nWird dargestellt durch: {caption_response.get('output', {}).get('caption', '')}\n"

# --- Beschreibungsgenerierung aus PDF-Inhalt ---
def runpod_request_with_polling_summary(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}", 
        "Content-Type": "application/json"
    }

    response = requests.post(f"{API_URL_DESCRIPTION}/runsync", headers=headers, json=payload)
    response_json = response.json()

    if response_json.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        job_id = response_json["id"]
        while True:
            status_response = requests.get(f"{API_URL_DESCRIPTION}/status/{job_id}", headers=headers)
            status_response.raise_for_status()
            response_json = status_response.json()
            print(response_json)
            if response_json["status"] == "COMPLETED":
                break
            time.sleep(5)

    return response_json["output"][0]["choices"][0]["tokens"][0]

def get_pdf_description(pdf_bytes):
    raw_text = extract_raw_text_from_pdf(pdf_bytes)
    max_length = 80000
    text_chunks = [raw_text[i:i + max_length] for i in range(0, len(raw_text), max_length)]
    summaries = []

    for text in text_chunks:
        prompt = (
            f"<s>[INST] Lies den folgenden Text:\n{text}\n\n"
            "Gib zunächst das Ziel des Textes an und beginne mit 'Ziel:'. "
            "Nenne anschließend die zentralen Themen des Textes. "
            "Leite jedes Thema mit einer eigenen Überschrift ein, beginnend mit 'Thema 1:', 'Thema 2:', 'Thema 3:' usw. "
            "Beschreibe jedes Thema jeweils in ein bis zwei klaren, vollständigen Sätzen. "
            "Verwende ausschließlich Informationen aus dem Text. "
            "Füge keinerlei eigene Inhalte hinzu.[/INST]"
        )

        payload = {
            "input": {
                "prompt": prompt,
                "sampling_params": {
                    "min_tokens": 25,
                    "max_tokens": 500,
                    "temperature": 0.15,
                    "top_k": 25,
                    "top_p": 0.95,
                    "repetition_penalty": 1.3,
                }
            }
        }

        summary = runpod_request_with_polling_summary(payload)
        summaries.append(summary)

    summary_block = "\n\n".join([f"Summary {i+1}:\n{txt}" for i, txt in enumerate(summaries)])
    print(summary_block)
    merge_prompt = (
        f"<s>[INST] Die folgenden Abschnitte enthalten mehrere thematische Zusammenfassungen:\n{summary_block}\n\n"
        "Fasse sie alle zu einer einzigen, gemeinsamen Zusammenfassung zusammen.\n"
        "Formuliere ein gemeinsames, übergreifendes Ziel und beginne mit 'Ziel:'.\n"
        "Fasse anschließend alle Themen knapp und klar zusammen, in nummerierter Reihenfolge beginnend mit 'Thema 1:'.\n"
        "Fasse verwandte Themen sinnvoll zusammen, lasse aber keine relevanten Inhalte weg.\n"
        "Verwende ausschließlich Informationen aus den vorliegenden Zusammenfassungen.\n"
        "Keine eigenen Interpretationen. Keine Erfindungen.[/INST]"
    )

    merge_payload = {
        "input": {
            "prompt": merge_prompt,
            "sampling_params": {
                "min_tokens": 50,
                "max_tokens": 700,
                "temperature": 0.15,
                "top_k": 25,
                "top_p": 0.95,
                "repetition_penalty": 1.3,
            }
        }
    }

    final_summary = runpod_request_with_polling_summary(merge_payload)
    return final_summary

def write_metadata(pdf_bytes, name, output_io):
    description = get_pdf_description(pdf_bytes)
    sections = extract_text_sections(description)
    
    output_text = ""

    docs = extract_text_pages_from_pdf(pdf_bytes)
    doc_inputs = [f"passage: {doc}" for doc in docs]
    doc_embeddings = [item["embedding"] for item in runpod_request_with_polling_embedding({"input": {"input": doc_inputs}})]
    
    for section_index, section in enumerate(sections, 1):
        output_text += f"\n{section}\n"
        if section_index == 1:
            continue
        top_pages = find_most_relevant_pages_with_embeddings(docs, section, doc_embeddings, top_k=5)
        relevant_page_indices = [page_num for page_num, score, _ in top_pages]
        images = extract_valid_images(pdf_bytes, relevant_page_indices)
        image_result = request_image_selection_and_caption(images, section)
        print(image_result)
        output_text += image_result or ""

    print(f"response: {output_text}")

    meta = f"{output_text}"
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
        db.delete(job)
        db.commit()
        background_tasks.add_task(os.remove, job.result_path)
        raise HTTPException(status_code=404, detail="Keine Datei gefunden")
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
