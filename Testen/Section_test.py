# Dieses Skript prüft, ob die vom Text-Zusammenfassungsmodell generierte Ausgabe dem gewünschten Format entspricht:
# Zunächst muss ein Abschnitt mit "Goal: <Text>" erscheinen, gefolgt von nummerierten Abschnitten im Format
# "Topic 1: <Titel>\n- <Beschreibung>", "Topic 2: ..." usw., jeweils in aufsteigender Reihenfolge.

import re
import numpy as np
import requests
from pathlib import Path
from PyPDF2 import PdfReader
import io
import time

# Laden der Umgebungsvariablen
load_dotenv()

# Zugriff auf Umgebungsvariablen für API-Zugriff
API_KEY = os.getenv("API_KEY")
API_URL_DESCRIPTION = os.getenv("API_URL_DESCRIPTION")

# Funktion zum Extrahieren von Text aus PDF-Dateien (als Bytes übergeben)
def extract_raw_text_from_pdf(pdf_bytes):
    try:
        with io.BytesIO(pdf_bytes) as buffer:
            reader = PdfReader(buffer)
            return "".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        print(f"Fehler in extract_raw_text_from_pdf: {e}")
        return ""

# Funktion zum Senden eines Requests an RunPod mit anschließendem Polling, bis das Ergebnis verfügbar ist
def runpod_request_with_polling_summary(payload):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Sofortiger API-Aufruf (runsync)
        response = requests.post(f"{API_URL_DESCRIPTION}/runsync", headers=headers, json=payload)
        response_json = response.json()

        # Falls der Job asynchron ist, Status regelmäßig abfragen
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
                    raise Exception(f"Job not successful. Status: {response_json['status']}")
                time.sleep(5)

        # Rückgabe des erzeugten Textes
        return response_json["output"][0]["choices"][0]["tokens"][0]
    except Exception as e:
        print(f"Fehler in runpod_request_with_polling_summary: {e}")
        return None

# Hauptfunktion zum Generieren und ggf. Zusammenführen von Text-Zusammenfassungen im gewünschten Format
def get_pdf_description(pdf_bytes):
    try:
        raw_text = extract_raw_text_from_pdf(pdf_bytes)
        if not raw_text:
            return "empty"

        # Zu lange PDFs werden übersprungen
        max_length = 80000
        if len(raw_text) > max_length:
            return "to long"

        # Längere Texte ggf. in Abschnitte teilen
        text_chunks = [raw_text[i:i + max_length] for i in range(0, len(raw_text), max_length)]
        summaries = []

        # Vorgabe des erwarteten Ausgabeformats
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
            "... (usw.)"
        )

        # Prompt wird für jeden Abschnitt erzeugt
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

            summary = runpod_request_with_polling_summary(payload)
            summaries.append(summary)

        summary_block = "\n\n".join([f"Summary {i+1}:\n{txt}" for i, txt in enumerate(summaries)])
        print(summary_block)

        # Falls mehrere Teile vorliegen → Zusammenführen in eine einheitliche Zusammenfassung
        if len(summaries) > 1:
            merge_prompt = (
                f"<s>[INST] The following sections contain multiple thematic summaries:\n{summary_block}\n\n"
                "Create a single, unified summary from them.\n\n"
                "**Requirements:**\n"
                "- Formulate one single overarching **goal** ...\n"
                "- Merge similar topics ...\n\n"
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
    except Exception as e:
        print(f"Fehler in get_pdf_description: {e}")
        return None

# Funktion zur Extraktion von Abschnitten aus dem generierten Text
def extract_text_sections(text):
    matches = list(re.finditer(r'(Goal:|Topic \d+:)', text))
    sections = [text[matches[i].start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                for i in range(len(matches))]
    return sections

# Verzeichnis mit zu analysierenden PDF-Dateien
source_folder = '/content/test'
files_glob = [f for f in Path(source_folder).rglob("*") if f.is_file()]

# Statistiken
acc = 0
skip = 0
anz = 0

# Hauptschleife über alle PDFs
for file in files_glob:
    with open(file, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        text = get_pdf_description(pdf_bytes)

        anz += 1

        if text in ["to long", "empty"]:
            skip += 1
            continue

        # Abschnittsprüfung: entspricht die Struktur dem Format?
        sections = extract_text_sections(text)

        acc_tmp = "Goal:" in sections[0]  # Goal muss am Anfang stehen

        # Jeder weitere Abschnitt muss Topic X sein
        for idx, section in enumerate(sections[1:], start=1):
            if not section.startswith(f"Topic {idx}:"):
                acc_tmp = False
                break

        acc += acc_tmp

# Auswertung
print(f"Acc: {acc}")
print(f"Skip: {skip}")
print(f"Anz: {anz}")
print(f"Accuracy: {acc / anz if anz > 0 else 0}")
