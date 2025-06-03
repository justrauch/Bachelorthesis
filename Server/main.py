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

from dotenv import load_dotenv

load_dotenv()

# === INIT ===
Base.metadata.create_all(bind=engine)
app = FastAPI()

API_KEY = os.getenv("API_KEY")
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
            #print(response_json)
            if response_json["status"] == "COMPLETED":
                break
            if response_json["status"] in ["FAILED", "CANCELLED"]:
                raise Exception(f"Job not successful.")
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

def extract_valid_images(pdf_bytes, page):
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    valid_images = []
    total_images = 0
    for idx, (page_number, page_score) in enumerate(page):
        images = doc[page_number].get_images(full=True)
        if not (total_images == 0 or (idx <= 4 and total_images + len(images) <= 12 and page_score/page[0][1] >= 0.90)):
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
        if status_json.get("status") in ["FAILED", "CANCELLED"]:
            raise Exception(f"Job not successful. Status: {status}")
        time.sleep(5)

def split_in_three(liste):
    return [liste[i:i+3] for i in range(0, len(liste), 3)]

def send_batch_request(encoded_images, section_text):
    selection_prompt = (
        f"Lies den folgenden Text:\n{section_text}\n\n"
        "Dir werden mehrere Bilder gezeigt.\n"
        "Analysiere alle Bilder sorgfältig.\n"
        "Welches Bild passt inhaltlich am besten zum Text?\n"
        "Antworte nur mit der Nummer des passenden Bildes – zum Beispiel: 1, 2, 3 usw.\n"
        "Wenn keines der Bilder zum Text passt, antworte mit 0.\n"
        "Keine Beschreibung. Keine Erklärung. Nur eine einzige Zahl."
    )

    payload = {
        "input": {
            "images": encoded_images,
            "prompt": selection_prompt
        }
    }

    selection_response = post_request(f"{API_URL_IMAGE_SELECTOR}/runsync", payload)

    if selection_response.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        selection_response = wait_for_completion(API_URL_IMAGE_SELECTOR, selection_response["id"])

    try:
        output = int(selection_response.get("output", {}).get("caption", "-1"))
    except ValueError:
        print("Ungültige Ausgabe – kein gültiger Integer.")
        return -1

    print("\nGewähltes Bild:")
    print(output)
    return output


def request_image_selection_and_caption(images, section_text):
    encoded_images = [encode_image_to_data_uri(img) for img in images if img]
    if not encoded_images:
        return ""

    batches = split_in_three(encoded_images)
    selected_images = []

    for batch in batches:
        if len(batch) >= 1:
            index = send_batch_request(batch, section_text)
            if index > 0 and index <= len(batch):
                selected_images.append(batch[index - 1])

    if not selected_images:
        print("Kein Bild wurde vom Modell ausgewählt.")
        return ""

    selected_index = send_batch_request(selected_images, section_text)

    if selected_index == 0:
        print("Keines der Bilder wurde als passend zum Text bewertet.")
        return ""

    if selected_index > len(selected_images) or selected_index < 0:
        print("Ausgewählter Bildindex liegt außerhalb des gültigen Bereichs.")
        return ""

    caption_prompt = (
        "Beschreibe das angegebene Bild.\n"
        "Gib ausschließlich eine Beschreibung des Bildes aus.\n"
        "Keine Erklärungen, keine zusätzlichen Informationen.\n"
        "Nur die Bildbeschreibung als Antwort.\n"
        "Nutze maximal einen Satz."
        "Die Bildbeschreibung muss auf Deutsch erfolgen.\n"
    )

    caption_payload = {
        "input": {
            "images": [selected_images[selected_index - 1]],
            "prompt": caption_prompt
        }
    }

    caption_response = post_request(f"{API_URL_IMAGE_SELECTOR}/runsync", caption_payload)
    if caption_response.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
        caption_response = wait_for_completion(API_URL_IMAGE_SELECTOR, caption_response["id"])

    return f"\nDargestellt durch: {caption_response.get('output', {}).get('caption', '')}\n"


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
            if response_json["status"] in ["FAILED", "CANCELLED"]:
                raise Exception(f"Job not successful. Status: {status}")
            time.sleep(5)

    return response_json["output"][0]["choices"][0]["tokens"][0]

def get_pdf_description(pdf_bytes):
    raw_text = extract_raw_text_from_pdf(pdf_bytes)
    max_length = 80000
    text_chunks = [raw_text[i:i + max_length] for i in range(0, len(raw_text), max_length)]
    summaries = []
    output_format = (
        "Ziel: <Ein einziger klar formulierter Satz, der den Hauptzweck des Textes zusammenfasst. "
        "Es darf ausschließlich einen Ziel-Abschnitt geben – keine mehrfachen 'Ziel:'-Einträge.>\n\n"
        
        "Liste anschließend maximal 5 Hauptthemen in folgendem Format auf:\n"
        "Thema 1: <Kurzer Titel>\n"
        "- <Kurze und sachliche Beschreibung>\n\n"
        "Thema 2: <Kurzer Titel>\n"
        "- <Beschreibung>\n\n"
        "(Fahre mit Thema 3, 4 und 5 fort, falls zutreffend)\n\n"
        
        "**Strenge Formatierungsregeln:**\n"
        "- Der gesamte Output muss auf Deutsch erfolgen.\n"
        "- Genau ein Zielabschnitt erlaubt – keine mehrfachen 'Ziel:'-Abschnitte.\n"
        "- Verwende für die Themenstruktur immer das Format 'Thema X:' (z. B. Thema 1:, Thema 2:) – keine Nummerierungen wie '1.', '2.', usw.\n"
        "- Nutze ausschließlich Informationen aus dem Originaltext – keine Erfindungen oder Ergänzungen.\n"
        "- Halte alle Beschreibungen kurz, sachlich und klar.\n"
        "- Keine Markdown-Formatierungen, Anführungszeichen oder einleitende Formulierungen verwenden.\n\n"
        
        "**Beispielausgabe:**\n\n"
        "Ziel: Schülerinnen und Schüler über Menschenaffen aufklären und für deren Schutz sensibilisieren.\n\n"
        "Thema 1: Evolution und Merkmale\n"
        "- Beschreibt körperliche Merkmale und genetische Ähnlichkeiten zwischen Menschen und Menschenaffen.\n\n"
        "Thema 2: Lebensraum und Verbreitung\n"
        "- Erklärt, wo verschiedene Arten von Menschenaffen in Afrika und Südostasien leben.\n\n"
        "Thema 3: Hauptbedrohungen\n"
        "- Behandelt Lebensraumverlust, Wilderei und Krankheitsübertragung als zentrale Gefahren.\n\n"
        "Thema 4: Schutzmaßnahmen\n"
        "- Hebt Maßnahmen des WWF und anderer Organisationen zum Schutz der Menschenaffen hervor.\n\n"
        "Thema 5: Bildungsprogramme\n"
        "- Beschreibt Initiativen wie das Young Panda Programm für junge Lernende.[/INST]"
    )

    for text in text_chunks:
        prompt = (
            f"<s>[INST] Lies den folgenden Text:\n{text}\n\n"
            "Fasse den Inhalt mit dem **genauen Format** unten zusammen:\n\n"
        ) + output_format

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
    if len(summaries) > 1:
        merge_prompt = (
            f"<s>[INST] Die folgenden Abschnitte enthalten mehrere thematische Zusammenfassungen:\n{summary_block}\n\n"
                "Erstelle daraus eine einzige, einheitliche Zusammenfassung.\n\n"
                "**Anforderungen:**\n"
                "- Formuliere ein einziges gemeinsames **Ziel**, das den übergreifenden Zweck aller vorhandenen Zusammenfassungen vereint.\n"
                "- Wähle aus jeder einzelnen Zusammenfassung **ein bis zwei Themen**, die deren Hauptinhalte repräsentieren.\n"
                "- Insgesamt dürfen **nicht mehr als 5 Themen** in der finalen Zusammenfassung enthalten sein.\n"
                "- Kombiniere verwandte Themen aus verschiedenen Zusammenfassungen zu einem **gemeinsamen Thema**, wenn sie denselben Aspekt behandeln.\n"
                "- Die endgültige Zusammenfassung soll **alle thematischen Inhalte der Ursprungsfassungen abdecken**, aber **ohne inhaltliche Wiederholungen**.\n"
                "- Verwende **nur Informationen aus den vorliegenden Texten** – keine eigenen Ergänzungen oder Erfindungen.\n\n"
                "**Halte dich exakt an dieses Format:**\n\n"
        ) + output_format

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
    elif len(summaries) == 1: 
      final_summary = summaries[0]
    else:
      final_summary = "Kein Ergebnis"
    return final_summary

def make_unique_directory(base_path):
    counter = 1
    path = base_path

    while os.path.exists(path):
        path = f"{base_path}_({counter})"
        counter += 1

    os.makedirs(path)
    return path

def write_metadata(pdf_bytes, name, output_io):
    print("Start with description")
    description = get_pdf_description(pdf_bytes)
    sections = extract_text_sections(description)
    
    output_text = ""

    print("Start with Embeddings")
    docs = extract_text_pages_from_pdf(pdf_bytes)
    doc_inputs = [f"passage: {doc}" for doc in docs]
    doc_embeddings = [item["embedding"] for item in runpod_request_with_polling_embedding({"input": {"input": doc_inputs}})]
    
    print("Start with images")
    pfad = "./images"
    verzeichnis = make_unique_directory(f"./images/{name}")
    if os.path.exists(pfad) and os.path.isdir(pfad):

        for section_index, section in enumerate(sections, 1):
            output_text += f"\n{section}\n"
            if section_index == 1:
                continue
            top_pages = find_most_relevant_pages_with_embeddings(docs, section, doc_embeddings, top_k=5)
            relevant_page_indices = [(page_num, score) for page_num, score, _ in top_pages]
            images = extract_valid_images(pdf_bytes, relevant_page_indices)

            for index, img in enumerate(images):

                pfad = f"{verzeichnis}/Section{section_index - 1}_Bild{index}.png"

                with open(pfad, "wb") as f:
                    f.write(img)

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

    pdf_with_metadata_bytes = output_io.getvalue()
    pfad = f"{verzeichnis}/{name}.pdf"
    with open(pfad, "wb") as f:
        f.write(pdf_with_metadata_bytes)

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

        pfad = "./zip_folders"
        if os.path.exists(pfad) and os.path.isdir(pfad):
            temp_dir = "./zip_folders"
        else:
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
    return metadata.get("/Subject", "Kein Betreff gefunden").replace("\n","<br>")
