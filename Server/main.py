import os, io, re, time, json, tempfile, zipfile, traceback

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Depends
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Datenbank
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Job

# PDF-Verarbeitung
from PyPDF2 import PdfReader, PdfWriter
import pymupdf

# Bildverarbeitung
import cv2
import numpy as np
from PIL import Image

# Ähnlichkeitsvergleich
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# API-Anfragen & Encoding
import requests
import base64
from io import BytesIO

from dotenv import load_dotenv
import shutil
import random
from pathlib import Path
from collections import Counter

from transformers import ViTForImageClassification, ViTImageProcessor
import torch
import pytesseract  # OCR
from torchvision import transforms
from transformers import AutoTokenizer

# Hugging Face Login für Modellzugriff
from huggingface_hub import login

load_dotenv()

login(token=os.getenv("HUGGING_FACE_TOKEN"))

# Tokenizer vorbereiten
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.3")

# FASTAPI INITIALISIERUNG
Base.metadata.create_all(bind=engine)  # Datenbank-Tabellen erzeugen
app = FastAPI()  # Hauptobjekt für die API

# Wichtige API-Parameter aus Umgebungsvariablen
API_KEY = os.getenv("API_KEY")
API_URL_IMAGE_SELECTOR = os.getenv("API_URL_IMAGE_SELECTOR")
API_URL_DESCRIPTION = os.getenv("API_URL_DESCRIPTION")
API_URL_EMBEDDINGS = os.getenv("API_URL_EMBEDDINGS")

# CORS aktivieren
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB-Verbindung
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Gerät festlegen (GPU, falls verfügbar)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Modell für Bildklassifikation
model_path = "./models/vit_fit_v3"

# Falls Modell nicht lokal vorhanden, lade es von Hugging Face
if not os.path.exists(model_path):
    print("Modell wird von Hugging Face heruntergeladen...")
    model = ViTForImageClassification.from_pretrained("JustinStrauch/vit_fit_v3")
    processor = ViTImageProcessor.from_pretrained("JustinStrauch/vit_fit_v3")

    os.makedirs(model_path, exist_ok=True)
    model.save_pretrained(model_path)
    processor.save_pretrained(model_path)
    print("Modell wurde von Hugging Face heruntergeladen!!!")
else:
    # Modell lokal laden
    model = ViTForImageClassification.from_pretrained(model_path)
    processor = ViTImageProcessor.from_pretrained(model_path)

# Modell in den Eval-Modus setzen
model.to(device)
model.eval()

# Nur diese Klassen sind als "valide" gekennzeichnet
valid_labels = ["chart", "infographic", "realistic", "tabel"]
# Alle verwendeten Subfolder für Klassifikation
subfolders = sorted(valid_labels + ["design_element", "logo", "portrait", "qr_code", "unrealistic"])

# Bildvorverarbeitung
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=processor.image_mean, std=processor.image_std),
])

# Schlagwortsuche zum testen
def cossim(all_pages, topic):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([topic] + all_pages)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return similarities.flatten()

# Beispiel für die Bildklassifikation mit Gemma anhand von drei Bildern.
# Die Ausgabe erfolgt im Format: Index: True/False
def request_image_selection_and_caption(image_paths, text):
    try:
        encoded_images = []
        for path in image_paths:
            image_data_uri = encode_image_to_data_uri(path)
            if image_data_uri:
                encoded_images.append(image_data_uri)

        if not encoded_images:
            return None

        caption_prompt = (
            "You will receive a list of images. For each image, answer with 'True' or 'False' according to the following rules:\n"
            "- Answer 'True' if the image can be classified as one of the following: a table, graph, diagram, infographic, or a realistic photograph.\n"
            "- Answer 'False' if the image is any of the following: design elements, logos, cartoon-style scenes that are not part of an infographic, portrait photos, or any other decorative or illustrative artwork.\n"
            "Your response must be a numbered list, where each number corresponds to the index of the image in the input list.\n"
            "Format your output exactly like this:\n"
            "0: True\n"
            "1: False\n"
            "2: True\n"
            "...and so on.\n"
            "Do not include any explanations or additional text—only the numbered list of 'True' or 'False'."
        )

        full_prompt = f"{caption_prompt}"

        caption_payload = {
            "input": {
                "images": encoded_images,
                "prompt": full_prompt
            }
        }

        caption_response = runpod_post_with_polling(API_URL_IMAGE_SELECTOR, caption_payload)

        return f"\n{caption_response.get('caption', '')}\n"

    except Exception as e:
        print(f"Fehler in request_image_selection_and_caption: {e}")
        return None

# --- Hilfsfunktionen zur Textextraktion und -strukturierung ---

def extract_text_sections(text):
    # Teilt den Text in Abschnitte anhand der Überschriften "Goal:" und "Topic <Zahl>:"
    matches = list(re.finditer(r'(Goal:|Topic \d+:)', text))
    sections = [
        text[matches[i].start():matches[i + 1].start() if i + 1 < len(matches) else len(text)].strip()
        for i in range(len(matches))
    ]
    return sections

def extract_raw_text_from_pdf(pdf_bytes):
    # Extrahiert den gesamten Fließtext aus einem PDF als ein zusammenhängender String
    try:
        with io.BytesIO(pdf_bytes) as buffer:
            reader = PdfReader(buffer)
            return "".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        print(f"Fehler in extract_raw_text_from_pdf: {e}")
        return ""

def extract_text_pages_from_pdf(pdf_bytes):
    # Extrahiert den Text seitenweise aus einem PDF
    try:
        with io.BytesIO(pdf_bytes) as buffer:
            reader = PdfReader(buffer)
            return [page.extract_text() or "" for page in reader.pages]
    except Exception as e:
        print(f"Fehler in extract_text_pages_from_pdf: {e}")
        return []

# Hilfsfunktion für RunPod POST-Anfrage mit Polling und Retry
def runpod_post_with_polling(api_url, payload, retries=2):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",          # Authentifizierung über API-Key
            "Content-Type": "application/json"
        }

        # Erste Anfrage an /runsync
        response = requests.post(f"{api_url}/runsync", headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()

        # Falls der Job noch nicht abgeschlossen ist → Status polling starten
        if response_json.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
            job_id = response_json["id"]
            while True:
                status_response = requests.get(f"{api_url}/status/{job_id}", headers=headers)
                status_response.raise_for_status()
                response_json = status_response.json()

                if response_json["status"] == "COMPLETED":
                    break  # Erfolgreich abgeschlossen

                if response_json["status"] in ["FAILED", "CANCELLED"]:
                    print(f"Job status: {response_json['status']}. Retry in 10 seconds...")
                    if retries > 0:
                        time.sleep(10)  # Warten vor Retry
                        return runpod_post_with_polling(api_url, payload, retries=retries - 1)
                    else:
                        print("Maximale Anzahl an Wiederholungen erreicht. Rückgabe: [].")
                        return []  # Bei zu vielen Fehlern wird leere Liste zurückgegeben

                time.sleep(5)  # Warteintervall zwischen Polling-Anfragen

        return response_json.get("output")  # Rückgabe des fertigen Ergebnisses

    except Exception as e:
        print(f"Fehler in runpod_post_with_polling: {e}")
        return []

# --- Ähnlichkeitsbewertung ---
def find_most_relevant_pages_with_embeddings(docs, query, doc_embeddings, top_k=5):
    try:
        # Erzeuge Embedding für die Suchanfrage 
        query_embedding = runpod_post_with_polling(
            API_URL_EMBEDDINGS,
            {"input": {"input": f"query: {query}"}}
        )["data"][0]["embedding"]

        # Berechne die Kosinus-Ähnlichkeit zwischen Query und allen Seiten
        similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

        # Sortiere Seiten nach Ähnlichkeit absteigend
        ranked = sorted(
            [(idx, score, docs[idx]) for idx, score in enumerate(similarities)],
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]  # Gib die top_k ähnlichsten Seiten zurück

    except Exception as e:
        print(f"Fehler in find_most_relevant_pages_with_embeddings: {e}")
        return []


# --- Bildfilterung ---
#Filtert unerwünschte Bilder basierend auf Auflösung und Textmenge.
def filter_image(image_bytes):
    try:
        with Image.open(io.BytesIO(image_bytes)) as img:
            width, height = img.size

            # Verwerfe Bilder, die zu klein sind
            if width < 50 or height < 50:
                return True

            # Extrahiere erkannten Text (Deutsch + Englisch)
            text = pytesseract.image_to_string(img, lang='deu+eng')

            # Verwerfe Bilder mit extrem viel Text (z. B. eingescanntes PDF)
            if len(text.strip()) > 3500:
                return True

            # Bild wird akzeptiert
            return False

    except Exception as e:
        print(f"Fehler in filter_image: {e}")
        return True  # Im Fehlerfall lieber verwerfen

# Klassifiziert ein Bild mit dem ViT-Modell und gibt das vorhergesagte Label zurück.
def predict(image_bytes):
    try:
        with Image.open(io.BytesIO(image_bytes)).convert("RGB") as image:
            input_tensor = transform(image).unsqueeze(0)  # Bild vorbereiten für Modell

        with torch.no_grad():
            outputs = model(input_tensor.to(device))  # Vorwärtsdurchlauf ohne Gradienten
            predicted_idx = outputs.logits.argmax(dim=1).item()  # Index der höchsten Wahrscheinlichkeit

        print(f'Bild klassifiziert als: {predicted_idx}')
        return subfolders[int(predicted_idx)]
    except Exception as e:
        print(f"Fehler in predict: {e}")
        return True  # True = verwerfen

# Extrahiert gültige Bilder aus einem PDF-Dokument.
def extract_valid_images(pdf_bytes, page):
    try:
        doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        valid_images = []
        total_images = 0

        for idx, (page_number, page_score) in enumerate(page):
            images = doc[page_number].get_images(full=True)

            # Abbruchbedingung:
            # - Nur erste 5 Seiten erlaubt
            # - Max. 35 Bilder insgesamt erlaubt
            # - Seite muss ausreichend relevant sein
            if not (
                total_images == 0 or
                (idx <= 4 and total_images + len(images) <= 35 and page_score / page[0][1] >= 0.75)
            ):
                break  # Abbruch, wenn Bedingungen verletzt

            total_images += len(images)

            for i, img in enumerate(images):
                try:
                    # Bild aus PDF extrahieren
                    image_data = doc.extract_image(img[0]).get("image")

                    # Bild durchlaufen lassen: Filter + Klassifizierung
                    if image_data and not filter_image(image_data) and (predict(image_data) in valid_labels):
                        valid_images.append((image_data, True))  # Bild gültig
                    else:
                        valid_images.append((image_data, False))  # Bild ungültig
                except Exception as e:
                    print(f"Fehler beim Extrahieren von Bild (XREF {img[0]}): {e}")

        return valid_images
    except Exception as e:
        print(f"Fehler in extract_valid_images: {e}")
        return []


# --- Bild Auswahl und Beschreibung ---
# Wandelt ein Bild (Bytes) in eine base64-codierte Data-URI um.
def encode_image_to_data_uri(image_bytes):
    try:
        buffer = BytesIO()
        Image.open(BytesIO(image_bytes)).convert("RGB").save(buffer, format="JPEG")
        return f"data:image/jpeg;base64,{base64.b64encode(buffer.getvalue()).decode('utf-8')}"
    except Exception as e:
        print(f"Fehler in encode_image_to_data_uri: {e}")
        return None

# Teilt eine Liste in Dreiergruppen auf.
def split_in_three(liste):
    return [liste[i:i+3] for i in range(0, len(liste), 3)]

# Sendet eine Auswahlaufforderung an das Modell: Welches Bild passt am besten zum Text?
def send_batch_request(encoded_images, section_text):
    try:
        selection_prompt = (
            f"Read the following text:\n{section_text}\n\n"
            "You will be shown several images.\n"
            "Analyze all images carefully.\n"
            "Which image best matches the content of the text?\n"
            "Respond with only the number of the matching image – for example: 1, 2, 3, etc.\n"
            "If none of the images match the text, respond with 0.\n"
            "No description. No explanation. Only a single number."
        )

        payload = {
            "input": {
                "images": encoded_images,
                "prompt": selection_prompt
            }
        }

        try:
            output = int(runpod_post_with_polling(API_URL_IMAGE_SELECTOR, payload).get("caption", "-1"))
        except ValueError:
            print("Ungültige Ausgabe – kein gültiger Integer.")
            return -1

        print("\nGewähltes Bild:")
        print(output)
        return output
    except Exception as e:
        print(f"Fehler in send_batch_request: {e}")
        return None

# Bildauswahlprozess + Beschreibung:
# - Führt Auswahlprozess in mehreren Runden durch
# - Beschreibt das final gewählte Bild mit Hilfe eines Prompt
def request_image_selection_and_caption(images, section_text, path, section_index):
    try:
        encoded_images = [encode_image_to_data_uri(img) for img in images if img]
        if not encoded_images:
            return ""

        current_selection = encoded_images

        # Bildauswahl in mehreren Runden → immer nur Gewinner weiter
        while len(current_selection) > 1:
            batches = split_in_three(current_selection)
            next_selection = []

            for batch in batches:
                if len(batch) > 1:
                    index = send_batch_request(batch, section_text)
                    if index > 0 and index <= len(batch):
                        next_selection.append(batch[index - 1])
                elif len(batch) == 1:
                    next_selection.append(batch[0])  # Nur ein Bild → automatisch weiter

            if not next_selection:
                print("Kein Bild wurde vom Modell ausgewählt.")
                return ""

            current_selection = next_selection

        # Falls kein Bild passt
        if not current_selection:
            print("Keine finale Bildauswahl vorhanden.")
            return ""

        # Genau ein Bild wurde übriggelassen → abspeichern & beschreiben
        final_image_data_uri = current_selection[0]

        image_path = f"{path}/Section{section_index - 1}_choice.png"
        header, encoded = final_image_data_uri.split(",", 1)
        image_data = base64.b64decode(encoded)

        with open(image_path, "wb") as f:
            f.write(image_data)

        # Prompt zur Bildbeschreibung
        caption_prompt = (
            f"You will receive a text:\n{section_text}\n\n"
            "If the image matches the content write one sentence that blends the reason the image fits with the image description. "
            "This sentence must start like this:\n"
            "\"An image placed alongside this content in the PDF shows ...\"\n"
            "Briefly explain what is shown in the image and how it relates to the text, but don't mention the text directly. "
            "If the image does **not** match the text return ''. "
            "Do **not** include explanations or additional information. "
            "Return only the image sentence if applicable. "
            "Use **a maximum of one sentence** for the image description. "
            "The image description must be in **English**.\n\n"
            "Example (image and description fit):\n"
            "Output: An image placed alongside this content in the PDF shows a scientist in a lab coat working with test tubes and a microscope, visually reinforcing the focus on biomedical research and innovation.\n\n"
            "Example (image or description does not fit):\n"
            "Output:''"
        )

        caption_payload = {
            "input": {
                "images": [final_image_data_uri],
                "prompt": caption_prompt
            }
        }

        caption_response = runpod_post_with_polling(API_URL_IMAGE_SELECTOR, caption_payload)
        return f"\n{caption_response.get('caption', '')}\n"

    except Exception as e:
        print(f"Fehler in request_image_selection_and_caption: {e}")
        return None


# --- Text Beschreibung ---
# Teilt einen langen Text in mehrere Abschnitte, sodass er mit dem Prompt zusammen unter die Token-Grenze passt.
def split_text_by_tokens(prompt, text, max_tokens=32000):
    prompt_tokens = len(tokenizer.encode(prompt))
    input_ids = tokenizer.encode(text, add_special_tokens=False)

    # Text in maximal große Token-Stücke zerschneiden, die noch mit dem Prompt kombinierbar sind
    chunks = [input_ids[i:i+max_tokens - prompt_tokens] for i in range(0, len(input_ids), max_tokens - prompt_tokens)]
    decoded_chunks = [tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]
    return decoded_chunks

# Hauptfunktion zur Zusammenfassung von PDF-Inhalten
def get_pdf_description(pdf_bytes):
    try:
        # Text aus PDF extrahieren
        raw_text = extract_raw_text_from_pdf(pdf_bytes)

        # Formatvorlage für das LLM
        output_format = (
            "Goal: <A single clearly formulated sentence that summarizes the main purpose of the text. "
            "There must be only one goal section – no multiple 'Goal:' entries allowed.>\n\n"
            "Then list up to 5 main topics in the following format:\n"
            "Topic 1: <Short title>\n"
            "- <Brief and factual description>\n\n"
            "Topic 2: <Short title>\n"
            "- <Description>\n\n"
            "(Continue with Topic 3, 4, and 5 if applicable)\n\n"
            "**Strict formatting rules:**\n"
            "- The entire output must be in English.\n"
            "- Exactly one goal section is allowed – no repeated 'Goal:' entries.\n"
            "- The heading 'Topics:' is not allowed. Each topic must begin with 'Topic X:' (such as 'Topic 1:', 'Topic 2:', etc.).\n"
            "- Use only information from the original text – no invented or added content.\n"
            "- Keep all descriptions short, factual, and clear.\n"
            "- Do not use markdown formatting, quotation marks, or introductory phrases.\n\n"
            "**Example output:**\n\n"
            "Goal: Educate students about great apes and raise awareness for their protection.\n\n"
            "Topic 1: Evolution and Characteristics\n"
            "- Describes physical traits and genetic similarities between humans and great apes.\n\n"
            "Topic 2: Habitat and Distribution\n"
            "- Explains where different species of great apes live in Africa and Southeast Asia.\n\n"
            "Topic 3: Main Threats\n"
            "- Covers habitat loss, poaching, and disease transmission as major dangers.\n\n"
            "Topic 4: Conservation Measures\n"
            "- Highlights actions by WWF and other organizations to protect great apes.\n\n"
            "Topic 5: Educational Programs\n"
            "- Describes initiatives such as the Young Panda program for young learners.[/INST]"
        )

        # Text ggf. in mehrere Chunks aufteilen
        text_chunks = split_text_by_tokens(output_format, raw_text)

        summaries = []

        # Für jeden Abschnitt eine Einzelzusammenfassung generieren lassen
        for text in text_chunks:
            prompt = (
                f"<s>[INST] Read the following text:\n{text}\n\n"
                "Summarize the content using the **exact format** below:\n\n"
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

            # Ergebnisse des LLM-Aufrufs extrahieren
            try:
                summary = runpod_post_with_polling(API_URL_DESCRIPTION, payload)[0]["choices"][0]["tokens"][0]
                summaries.append(summary)
            except (IndexError, KeyError, TypeError) as e:
                print(f"Fehler beim Extrahieren des Tokens: {e}")
                return None

        # Alle Einzel-Summaries zusammenfügen für weitere Verarbeitung
        summary_block = "\n\n".join([f"Summary {i+1}:\n{txt}" for i, txt in enumerate(summaries)])
        print(summary_block)

        # Falls mehrere Teilzusammenfassungen: zu einer Gesamtsummary zusammenführen
        if len(summaries) > 1:
            merge_prompt = (
                f"<s>[INST] The following sections contain multiple thematic summaries:\n{summary_block}\n\n"
                "Create a single, unified summary from them.\n\n"
                "**Requirements:**\n"
                "- Formulate one single overarching **goal** that captures the common purpose of all included summaries.\n"
                "- Select **one to two topics** from each summary that represent its main content.\n"
                "- The final summary must contain **no more than 5 topics in total**.\n"
                "- Merge similar topics from different summaries into **one combined topic**, if they cover the same aspect.\n"
                "- The final summary must **include all thematic content from the original summaries**, but **without repetition**.\n"
                "- Use **only the information from the provided texts** – no own additions or invented content.\n\n"
                "**Strictly follow this format:**\n\n"
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

            try:
                final_summary = runpod_post_with_polling(API_URL_DESCRIPTION, merge_payload)[0]["choices"][0]["tokens"][0]
            except (IndexError, KeyError, TypeError) as e:
                print(f"Fehler beim Extrahieren des Tokens: {e}")
                return None

        # Nur ein Chunk – kein Merging notwendig
        elif len(summaries) == 1:
            final_summary = summaries[0]
        else:
            final_summary = "Kein Ergebnis"

        return final_summary
    except Exception as e:
        print(f"Fehler in get_pdf_description: {e}")
        return None

# Hilfsfunktion zur Erstellung eindeutiger Verzeichnisse
def make_unique_directory(base_path):
    """
    Erstellt ein neues Verzeichnis mit eindeutiger Benennung, indem ggf. Zähler angehängt werden.
    """
    counter = 1
    path = base_path

    while os.path.exists(path):
        path = f"{base_path}_({counter})"
        counter += 1

    os.makedirs(path)
    return path


# Schreibt Metadaten in eine PDF-Datei
def write_metadata(pdf_bytes, name, output_io):
    try:
        print("Start with description")
        description = get_pdf_description(pdf_bytes)
        sections = extract_text_sections(description)

        output_text = ""

        print("Start with Embeddings")
        docs = extract_text_pages_from_pdf(pdf_bytes)
        doc_inputs = [f"passage: {doc}" for doc in docs]  # Formatierung für Embedding-Modell

        # KI-Modell zur Berechnung der Embeddings
        try:
            response = runpod_post_with_polling(API_URL_EMBEDDINGS, {"input": {"input": doc_inputs}})["data"]
            doc_embeddings = [item["embedding"] for item in response]
        except Exception as e:
            print(f"Fehler beim Abrufen der Dokument-Embeddings: {e}")
            doc_embeddings = []

        print("Start with images")
        # Ordner vorbereiten für Bildspeicherung
        pfad = "./images"
        os.makedirs("./images/valid", exist_ok=True)
        os.makedirs("./images/not_valid", exist_ok=True)
        verzeichnis_valid = make_unique_directory(f"./images/valid/{name}")
        verzeichnis_not_valid = make_unique_directory(f"./images/not_valid/{name}")

        # Durchlaufen aller Abschnittsbeschreibungen
        for section_index, section in enumerate(sections, 1):
            output_text += f"\n{section}\n"
            if section_index == 1:
                continue  # erster Block ist nur das "Goal"

            # Seiten mit höchster Relevanz zur Sektion finden
            top_pages = find_most_relevant_pages_with_embeddings(docs, section, doc_embeddings, top_k=5)
            relevant_page_indices = [(page_num, score) for page_num, score, _ in top_pages]

            # Bilder dieser Seiten extrahieren und filtern
            images = extract_valid_images(pdf_bytes, relevant_page_indices)

            # Bilder abspeichern in valid / not_valid
            if os.path.exists(pfad) and os.path.isdir(pfad):
                for index, (img, valid) in enumerate(images):
                    image_path = f"{verzeichnis_valid if valid else verzeichnis_not_valid}/Section{section_index - 1}_Bild{index}.png"
                    if img:
                        with open(image_path, "wb") as f:
                            f.write(img)
                    else:
                        print(f"Kein Bild für Section {section_index - 1}, Bild {index}")

            # Bildauswahl und Bild Beschreibung
            image_result = request_image_selection_and_caption([img for (img, valid) in images if valid], section, verzeichnis_valid, section_index)
            print(image_result)
            output_text += image_result or ""

        print(f"response: {output_text}")

        # Metadaten in PDF schreiben
        meta = f"{output_text}"
        reader = PdfReader(io.BytesIO(pdf_bytes))
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.add_metadata({"/Subject": meta})
        writer.write(output_io)

        # Resultat abspeichern
        pdf_with_metadata_bytes = output_io.getvalue()
        pfad = f"{verzeichnis_valid}/{name}.pdf"
        with open(pfad, "wb") as f:
            f.write(pdf_with_metadata_bytes)
    except Exception as e:
        print(f"Fehler in write_metadata: {e}")
        return None

# === API-Endpunkt zum Hochladen einer ZIP-Datei ===
@app.post("/api/process-zip")
async def process_zip(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks(), db: Session = Depends(get_db)):
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Bitte eine ZIP-Datei hochladen.")
    if db.query(Job).filter(Job.job_status == "in_bearbeitung").count() >= 3:
        raise HTTPException(status_code=429, detail="Die Verarbeitung ist derzeit ausgelastet.")

    # Job anlegen
    zip_bytes = await file.read()
    job = Job(verarbeitet=0, gesamt=0, job_status="in_bearbeitung", response_file=file.filename)
    db.add(job)
    db.commit()
    db.refresh(job)

    # Verarbeitung im Hintergrund
    background_tasks.add_task(process_zip_task, zip_bytes, job.id)
    return JSONResponse(status_code=202, content={"detail": "Datei wird verarbeitet", "job_id": job.id})


# === Verarbeitung der ZIP-Datei im Hintergrund ===
def process_zip_task(zip_bytes, job_id):
    db = SessionLocal()
    try:
        job = db.query(Job).get(job_id)

        # Zielverzeichnis vorbereiten
        pfad = "./zip_folders"
        temp_dir = pfad if os.path.exists(pfad) else tempfile.mkdtemp()
        out_path = os.path.join(temp_dir, f"result{job.id}.zip")
        job.result_path = out_path
        db.commit()

        with zipfile.ZipFile(out_path, "w") as zip_out:
            with zipfile.ZipFile(io.BytesIO(zip_bytes), "r") as zip_ref:
                pdfs = [f for f in zip_ref.namelist() if f.lower().endswith(".pdf")]
                job.gesamt = len(pdfs)
                db.commit()

                # Jede PDF einzeln verarbeiten
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

# === Status aller Jobs abrufen ===
@app.get("/api/status")
def get_all_statuses(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return [{
        "id": j.id, 
        "verarbeitet": j.verarbeitet, 
        "gesamt": j.gesamt, 
        "status": j.job_status, 
        "response_file": j.response_file
    } for j in jobs]

# === Ergebnis-Download nach Abschluss ===
@app.get("/api/download/{job_id}")
def download_zip(job_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if not job or not job.result_path or not os.path.exists(job.result_path):
        db.delete(job)
        db.commit()
        background_tasks.add_task(os.remove, job.result_path)
        raise HTTPException(status_code=404, detail="Keine Datei gefunden")
    if job.job_status not in ["bereit", "fehlgeschlagen"]:
        raise HTTPException(status_code=403, detail="Die Datei wird derzeit noch bearbeitet. Bitte stoppen Sie den Prozess oder warten Sie, bis die Bearbeitung abgeschlossen ist.")
    return FileResponse(
        path=job.result_path, 
        media_type="application/zip", 
        filename=f"ergebnis_{job.response_file}", 
        background=background_tasks)

# === Abbrechen eines Jobs ===
@app.get("/api/stop/{job_id}")
def stop_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Keinen Job gefunden")
    job.job_status = "abgebrochen"
    db.commit()
    return {"message": f"Job {job_id} wurde zurückgesetzt"}

# === Extrahiert die Metadaten direkt aus einer PDF-Datei ===
@app.post("/api/metadata")
async def get_metadata(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    metadata = reader.metadata
    return metadata.get("/Subject", "Kein Betreff gefunden").replace("\n","<br>")
