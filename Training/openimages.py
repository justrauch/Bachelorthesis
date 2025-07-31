# Hier kann man die Bilder des realistischen Datensatzes von OpenImages herunterladen.
# Das Skript lädt eine bestimmte Anzahl zufällig gewählter Klassen mit zugehörigen Bildern herunter.

import csv
import requests
import random
from openimages.download import download_images
import os

# URL zur CSV-Datei mit Label-IDs und -Namen aus dem OpenImages-Datensatz
url = "https://storage.googleapis.com/openimages/v5/class-descriptions-boxable.csv"

# Lade die CSV-Datei von der URL
response = requests.get(url)
lines = response.text.strip().split("\n")
reader = csv.reader(lines)
next(reader)  # Überspringe die Kopfzeile

# Erstelle ein Dictionary: {Label-ID: Label-Name}
labels = {row[0]: row[1] for row in reader}
labels_items = list(labels.items())

# Mische die Label zufällig
random.seed(42)
selected_items = random.sample(labels_items, len(labels_items))

# Konfiguration
iter = 1  # Nur zur Namensgebung des Ausgabeordners
used_items = 0  # Zähler für verwendete Klassen
total = 0  # Zähler für insgesamt heruntergeladene Bilder
max_labels = 500  # Maximalzahl der zu ladenden Klassen
per_images = 2  # Anzahl Bilder pro Klasse
output_dir = f"/content/openimages/test{iter}"  # Zielverzeichnis

# Lade Bilder iterativ für zufällig gewählte Klassen
for label_id, label_name in selected_items:
    try:
        # Bilder für die aktuelle Klasse herunterladen (beschränkt durch 'per_images')
        download_images(output_dir, [label_name], None, limit=per_images)
        print(f"{label_name} ({label_id})")
    except Exception as e:
        print(f"Fehler bei {label_name} ({label_id}): {e}")
        continue

    # Pfad zum Unterordner mit den Bildern
    label_path = os.path.join(output_dir, label_name.lower(), "images")
    print(label_path)

    # Zähle die heruntergeladenen Bilder
    if os.path.exists(label_path):
        image_files = [f for f in os.listdir(label_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".svg"))]
        count = len(image_files)
        total += count
        print(f"{count} Bilder für {label_name}")
    else:
        print(f"Kein Verzeichnis gefunden für {label_name}")

    used_items += 1
    print(f"Verwendete Klassen: {used_items}")

    # Abbruchbedingung: gewünschte Anzahl an Klassen + Bildern erreicht
    if used_items >= max_labels and total >= max_labels * per_images:
        break

print(f"\nInsgesamt: {total} Bilder in {used_items} Klassen heruntergeladen.")
