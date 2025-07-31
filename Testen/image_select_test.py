# Mit diesem Skript kann getestet werden, wie gut das Modell "Gemma"
# ein thematisch passendes Bild zu einem gegebenen Text auswählen kann.

import os
import csv
import time
import random
import base64
import requests
from io import BytesIO
from PIL import Image
from pathlib import Path

# Laden der Umgebungsvariablen
load_dotenv()

# Zugriff auf Umgebungsvariablen für API-Key und URL
API_KEY = os.getenv("API_KEY")
API_URL_IMAGE_SELECTOR = os.getenv("API_URL_IMAGE_SELECTOR")

# Kodiert ein Bild zu einem base64-Daten-URI-String (JPEG)
def encode_image_to_data_uri(image_path):
    try:
        buffer = BytesIO()
        Image.open(image_path).convert("RGB").save(buffer, format="JPEG")
        return f"data:image/jpeg;base64,{base64.b64encode(buffer.getvalue()).decode('utf-8')}"
    except Exception as e:
        print(f"Fehler in encode_image_to_data_uri: {e}")
        return None

# Führt eine POST-Anfrage mit JSON-Payload an die API durch
def post_request(url, payload):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Fehler in post_request: {e}")
        return None

# Wartet, bis der API-Job abgeschlossen ist (Polling)
def wait_for_completion(url_base, job_id):
    try:
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
                raise Exception(f"Job not successful. Status: {status_json['status']}")
            time.sleep(5)
    except Exception as e:
        print(f"Fehler in wait_for_completion: {e}")
        return None

# Verzeichnis mit vorbereiteten Testbildern
source_folder = '/content/openimages'
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

# Liste aller Bilder im Verzeichnis
files_glob = [f for f in Path(source_folder).rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

# Extrahiere Kategorien (Verzeichnisnamen)
dirs_glob = set([file.parent.parent.name for file in files_glob])

# Statistiken
acc = 0
anz = 0
skip = 0

# CSV-Datei mit Themen (Spalte 0: Klasse, Spalte 1: Text)
with open('/content/Unique_Topic_Texts.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Überspringe Header
    for row in reader:
        # Wähle zufällig zwei andere Kategorien als Distraktoren
        available_dirs = list(dirs_glob - {row[0].lower()})
        random_dirs = random.sample(available_dirs, 2)

        # Auswahl: 2 Distraktoren + 1 korrekte Klasse, dann mischen
        final_selection = random_dirs + [row[0].lower()]
        random.shuffle(final_selection)

        final_files = [file for file in files_glob if file.parent.parent.name in final_selection]
        if len(final_files) <= 4:
            continue  # Zu wenig Daten

        # Wähle drei Bilder (2 Distraktoren + 1 richtig)
        encoded_images = []
        final_files_c = []
        for i in range(0, 6, 2):
            encoded = encode_image_to_data_uri(final_files[i])
            if encoded:
                encoded_images.append(encoded)
                final_files_c.append(final_files[i])

        final_files = final_files_c
        if len(final_files) != 3:
            continue

        # Prompt für Auswahl: Modell soll das am besten passende Bild zum Text wählen
        selection_prompt = (
            f"Read the following text:\n{row[1]}\n\n"
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

        # Anfrage an das Modell senden
        selection_response = post_request(f"{API_URL_IMAGE_SELECTOR}/runsync", payload)

        # Warte, falls das Modell im Hintergrund arbeitet
        if selection_response.get("status") in ["IN_PROGRESS", "IN_QUEUE"]:
            selection_response = wait_for_completion(API_URL_IMAGE_SELECTOR, selection_response["id"])

        # Antwort verarbeiten (Index des passenden Bildes)
        output = int(selection_response.get("output", {}).get("caption", "-1"))

        print(final_files)

        if output == 0:
            print(output)
            print(f"{row[0].lower()} → None selected")
            print(row[1])
            print()
            skip += 1

        elif 1 <= output <= len(final_files):
            selected_file = final_files[output - 1]
            is_correct = selected_file.parent.parent.name == row[0].lower()
            print(output)
            print(f"{row[0].lower()} → {selected_file.parent.parent.name}")
            print(selected_file)
            print(row[1])
            print()
            if is_correct:
                acc += 1
        else:
            print(f"Ungültiger Index: {output}")

        anz += 1

# Ausgabe der Gesamtstatistik
print(f"acc: {acc}")     # Richtige Auswahl
print(f"skip: {skip}")   # Keine Auswahl (Antwort = 0)
print(f"anz: {anz}")     # Anzahl getesteter Fälle
print(f"Top-1 accuracy inkl. None als gültige Wahl: {(acc + skip) / anz:.2%}")
