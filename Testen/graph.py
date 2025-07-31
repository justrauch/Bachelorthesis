# Mit diesem Script können:
# - Sigmoid-Funktionen für Kantenanalyse (relativ & absolut) visualisiert werden.
# - Die durchschnittliche Pixelanzahl von Bildern in den Klassen chart, table und infographic analysiert werden.
# - Diagramme zur Auswertung von Benutzerumfragen erstellt werden (z. B. zur Bildbeschreibung).

import pytesseract
from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import hashlib
from tqdm import tqdm

# 0 → Sigmoid-Funktion plotten
# 1 → Analyse der Bildinhalte (OCR-Zeichenanzahl)
# 2 → Auswertung der Umfrageantworten als Balkendiagramm
diagramm = 1

# Definierte Sigmoid-Funktion mit unterschiedlichen Parametern für absolute oder relative Analyse
def custom_sigmoid(x, relative=True):
    if relative:
        center, scale_left, scale_right, left, right = 275000, 10000, 70000, 0.85, 1.9
    else:
        center, scale_left, scale_right, left, right = 925000, 10000, 165000, 1.05, 0.25
    if x < center:
        s = 1 / (1 + np.exp((x - center) / scale_left))
    else:
        s = 1 / (1 + np.exp((x - center) / scale_right))
    return right + (left - right) * s

# Plot der Sigmoid-Funktion

if diagramm == 0:
    #xs = np.linspace(450000, 1000000, 5000)  # für absolutes Verfahren
    xs = np.linspace(0, 750000, 5000)         # für relatives Verfahren
    ys = [custom_sigmoid(x) for x in xs]

    plt.plot(xs, ys)
    plt.title("Custom Sigmoid: center=925000, range 1.05 → 0.25")
    plt.grid(True)
    plt.show()

# Analyse der Bildfläche oder der Textmenge pro Bild

if diagramm == 1:
    source_folder = "../Training/data/val"
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
    files_glob = [f for f in Path(source_folder).rglob("*") if f.is_file() and f.parent.name in ["tabel", "chart", "infographic"] and f.suffix.lower() in image_extensions]
    mid = []

    for file in tqdm(files_glob):

        # Texterkennung
        image = Image.open(file)
        text = pytesseract.image_to_string(image, lang='deu+eng+rus')
        mid.append(len(text))

    # Statistische Auswertung der Pixelanzahl oder Texterkennung
    print(np.mean(mid))
    print(np.median(mid))

    bins = np.arange(0, 5000, 500)
    print(bins)
    counts, bin_edges = np.histogram(mid, bins=bins)
    labels = [f'{int(bin_edges[i])}-{int(bin_edges[i+1]-1)}' for i in range(len(bin_edges)-1)]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(labels, counts)
    plt.xticks(rotation=45)
    plt.xlabel('Anzahl erkannter Zeichen (Bereich)')
    plt.ylabel('Anzahl der Bilder')
    plt.title('Verteilung der OCR-erkannten Zeichen pro Bild')

    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


# Balkendiagramm zur Auswertung der Umfrage

if diagramm == 2:
    mid = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]  # Beispielantworten
    bins = np.arange(1, 5)
    counts, bin_edges = np.histogram(mid, bins=bins)
    labels = ["Image and Description good", "Description bad", "Description and Image bad"]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(labels, counts)
    plt.xticks(rotation=0)
    plt.xlabel('')
    plt.ylabel('Anzahl der Antworten')
    plt.title('Verteilung bei Frage 1')

    for bar in bars:
        height = bar.get_height()
        plt.annotate(f'{height}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

