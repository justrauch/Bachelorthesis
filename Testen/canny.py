# Hier kann man sowohl das Modell als auch die beiden Canny-Verfahren – jeweils mit und ohne Sigmoid-Anpassung – testen.

import cv2
import numpy as np
import os
import shutil
from pathlib import Path
import hashlib
from transformers import ViTForImageClassification, ViTImageProcessor
import torch
from PIL import Image
from torchvision import transforms
from tqdm import tqdm
import pytesseract

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Pfad zum trainierten ViT-Modell
model_name = "JustinStrauch/vit_fit_v3"
model = ViTForImageClassification.from_pretrained(model_name)
processor = ViTImageProcessor.from_pretrained(model_name)
model.to(device)
model.eval()

# Transformation für Bilder, passend zum ViT-Modell
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=processor.image_mean, std=processor.image_std),
])

# Parameter für Verfahren
use_model = False         # Klassifikation mit Modell
use_relative = True       # True = Verhältnis edges/pixels; False = absolute edges
use_sigmoid = True        # True = dynamische Anpassung der Kantenzahl via Sigmoid-Funktion

# Dynamische Anpassung der Kantenzahl (abhängig vom Verfahren)
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

# Bildausschluss-Logik basierend auf Größe und Textmenge (OCR)
def filter_image(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width < 50 or height < 50:
                return True
            text = pytesseract.image_to_string(img)
            if len(text.strip()) > 3500:
                return True
            return False
    except Exception as e:
        print(f"Fehler in filter_image: {e}")
        return True

# Klassennamen aus Testverzeichnis extrahieren
test_dir = Path("../Training/data") / "test"
subfolders = sorted([str(f).split("/")[-1] for f in test_dir.iterdir() if f.is_dir()])

# Cache für Klassifikationsergebnisse
prediction_cache = {}

# Klassifikation mit ViT-Modell
def predict(image_path):
    if image_path in prediction_cache:
        return prediction_cache[image_path]
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(input_tensor)
        predicted_idx = outputs.logits.argmax(dim=1).item()
    predicted_label = subfolders[predicted_idx]
    prediction_cache[image_path] = predicted_label
    return predicted_label

# Datei-Hash zur Duplikatserkennung
def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Zählt die Anzahl der Canny-Kanten im Bild
# Die Zahlen 25 (low threshold) und 125 (high threshold) legen fest, ab welcher Kantenstärke ein Pixel als Kante erkannt wird
def sort(input_path):
    image = cv2.imread(input_path)
    if image is None:
        print(f"Bild konnte nicht geladen werden: {input_path}")
        return 0, 0
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 25, 125)
    edge_count = np.sum(edges > 0)
    height, width = image.shape[:2]
    return edge_count, (height * width)

# Hauptauswertung
source_folder = "../data/val"
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
files_glob = [f for f in Path(source_folder).rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

valid_labels = ["chart", "infographic", "realistic", "tabel"]
unique_hashes = set()
anz = 0
skip = 0
acc = 0

# Statistiken pro Klasse vorbereiten
label_stats = {label: {"fp": 0, "fn": 0, "tp": 0, "tn": 0, "anz": 0} for label in valid_labels + [
    "design_element", "logo", "portrait", "qr_code", "unrealistic", "waste"
]}

# Bildklassifikation und Bewertung
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith(valid_extensions):
            source_path = os.path.join(root, file)
            for file_path in files_glob:
                if file_path.name == file:
                    parent_folder = file_path.parent.name

            h = file_hash(source_path)
            if h in unique_hashes:
                skip += 1
                continue
            unique_hashes.add(h)

            anz += 1
            label_stats[parent_folder]["anz"] += 1

            # Verfahren: Kantenzählung
            if not use_model:
                edges, pixels = sort(source_path)
                if use_sigmoid:
                    edges *= custom_sigmoid(pixels, relative=use_relative)
                score = edges / pixels if use_relative else edges

                # Definiere dynamisch die Schwellenwerte je nach Verfahren
                right = 0.08 if use_relative else 24000
                left = 0.37 if use_relative else 690000

                if right <= score < left:
                    if parent_folder in valid_labels:
                        acc += 1
                        label_stats[parent_folder]["tp"] += 1
                    else:
                        label_stats[parent_folder]["fp"] += 1
                else:
                    if parent_folder not in valid_labels:
                        acc += 1
                        label_stats[parent_folder]["tn"] += 1
                    else:
                        label_stats[parent_folder]["fn"] += 1

            # Alternativ: Modell-Vorhersage
            else:
                if filter_image(source_path):
                    if parent_folder not in valid_labels:
                        acc += 1
                        label_stats[parent_folder]["tn"] += 1
                    else:
                        label_stats[parent_folder]["fn"] += 1
                    continue

                result = predict(source_path)
                if result in valid_labels:
                    if parent_folder in valid_labels:
                        acc += 1
                        label_stats[parent_folder]["tp"] += 1
                    else:
                        label_stats[parent_folder]["fp"] += 1
                else:
                    if parent_folder not in valid_labels:
                        acc += 1
                        label_stats[parent_folder]["tn"] += 1
                    else:
                        label_stats[parent_folder]["fn"] += 1

# Ergebnis ausgeben
f1_v = {"tp": 0, "fp": 0, "tn": 0, "fn": 0}

for label, stats in label_stats.items():
    tp, fp, fn, tn, anz_l = stats["tp"], stats["fp"], stats["fn"], stats["tn"], stats["anz"]
    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0
    print(f"Label: {label}, TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}, Anz: {anz_l}")
    print(f"    Accuracy: {accuracy:.2%}")
    if label not in ["portrait", "waste"]:  # Optionaler Ausschluss
        for key in f1_v:
            f1_v[key] += 100 * (stats[key] / anz_l)

# F1-Score berechnen
tp, fp, fn = f1_v["tp"], f1_v["fp"], f1_v["fn"]
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print(f"F1: {f1:.2%}")

# Ausgaben für die jeweiligen Verfahren

"""
absolut 

real
ohne sigmoid
Label: chart, TP: 17, FP: 0, FN: 11, TN: 0, Anz: 28
    Accuracy: 60.71%
Label: infographic, TP: 22, FP: 0, FN: 18, TN: 0, Anz: 40
    Accuracy: 55.00%
Label: realistic, TP: 151, FP: 0, FN: 83, TN: 0, Anz: 234
    Accuracy: 64.53%
Label: tabel, TP: 3, FP: 0, FN: 0, TN: 0, Anz: 3
    Accuracy: 100.00%
Label: design_element, TP: 0, FP: 5, FN: 0, TN: 42, Anz: 47
    Accuracy: 89.36%
Label: logo, TP: 0, FP: 0, FN: 0, TN: 35, Anz: 35
    Accuracy: 100.00%
Label: portrait, TP: 0, FP: 1, FN: 0, TN: 20, Anz: 21
    Accuracy: 95.24%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 1, Anz: 1
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 3, FN: 0, TN: 25, Anz: 28
    Accuracy: 89.29%
Label: waste, TP: 0, FP: 199, FN: 0, TN: 103, Anz: 302
    Accuracy: 34.11%
F1: 62.99%

mit sigmoid
Label: chart, TP: 13, FP: 0, FN: 15, TN: 0, Anz: 28
    Accuracy: 46.43%
Label: infographic, TP: 19, FP: 0, FN: 21, TN: 0, Anz: 40
    Accuracy: 47.50%
Label: realistic, TP: 148, FP: 0, FN: 86, TN: 0, Anz: 234
    Accuracy: 63.25%
Label: tabel, TP: 3, FP: 0, FN: 0, TN: 0, Anz: 3
    Accuracy: 100.00%
Label: design_element, TP: 0, FP: 4, FN: 0, TN: 43, Anz: 47
    Accuracy: 91.49%
Label: logo, TP: 0, FP: 0, FN: 0, TN: 35, Anz: 35
    Accuracy: 100.00%
Label: portrait, TP: 0, FP: 1, FN: 0, TN: 20, Anz: 21
    Accuracy: 95.24%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 1, Anz: 1
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 3, FN: 0, TN: 25, Anz: 28
    Accuracy: 89.29%
Label: waste, TP: 0, FP: 151, FN: 0, TN: 151, Anz: 302
    Accuracy: 50.00%
F1: 65.98%

test
ohne sigmoid
Label: chart, TP: 13, FP: 0, FN: 137, TN: 0, Anz: 150
    Accuracy: 8.67%
Label: infographic, TP: 98, FP: 0, FN: 2, TN: 0, Anz: 100
    Accuracy: 98.00%
Label: realistic, TP: 88, FP: 0, FN: 12, TN: 0, Anz: 100
    Accuracy: 88.00%
Label: tabel, TP: 20, FP: 0, FN: 80, TN: 0, Anz: 100
    Accuracy: 20.00%
Label: design_element, TP: 0, FP: 9, FN: 0, TN: 3, Anz: 12
    Accuracy: 25.00%
Label: logo, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: portrait, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 12, FN: 0, TN: 88, Anz: 100
    Accuracy: 88.00%
Label: waste, TP: 0, FP: 0, FN: 0, TN: 0, Anz: 0
    Accuracy: 0.00%
F1: 61.19%

mit sigmoid
Label: chart, TP: 12, FP: 0, FN: 138, TN: 0, Anz: 150
    Accuracy: 8.00%
Label: infographic, TP: 94, FP: 0, FN: 6, TN: 0, Anz: 100
    Accuracy: 94.00%
Label: realistic, TP: 88, FP: 0, FN: 12, TN: 0, Anz: 100
    Accuracy: 88.00%
Label: tabel, TP: 23, FP: 0, FN: 77, TN: 0, Anz: 100
    Accuracy: 23.00%
Label: design_element, TP: 0, FP: 2, FN: 0, TN: 10, Anz: 12
    Accuracy: 83.33%
Label: logo, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: portrait, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 11, FN: 0, TN: 89, Anz: 100
    Accuracy: 89.00%
Label: waste, TP: 0, FP: 0, FN: 0, TN: 0, Anz: 0
    Accuracy: 0.00%
F1: 66.49%
"""

"""
relativ

real
ohne sigmoid
Label: chart, TP: 14, FP: 0, FN: 14, TN: 0, Anz: 28
    Accuracy: 50.00%
Label: infographic, TP: 9, FP: 0, FN: 31, TN: 0, Anz: 40
    Accuracy: 22.50%
Label: realistic, TP: 180, FP: 0, FN: 54, TN: 0, Anz: 234
    Accuracy: 76.92%
Label: tabel, TP: 0, FP: 0, FN: 3, TN: 0, Anz: 3
    Accuracy: 0.00%
Label: design_element, TP: 0, FP: 2, FN: 0, TN: 45, Anz: 47
    Accuracy: 95.74%
Label: logo, TP: 0, FP: 16, FN: 0, TN: 19, Anz: 35
    Accuracy: 54.29%
Label: portrait, TP: 0, FP: 20, FN: 0, TN: 1, Anz: 21
    Accuracy: 4.76%
Label: qr_code, TP: 0, FP: 1, FN: 0, TN: 0, Anz: 1
    Accuracy: 0.00%
Label: unrealistic, TP: 0, FP: 14, FN: 0, TN: 14, Anz: 28
    Accuracy: 50.00%
Label: waste, TP: 0, FP: 56, FN: 0, TN: 246, Anz: 302
    Accuracy: 81.46%
F1: 52.62%

mit sigmoid
Label: chart, TP: 19, FP: 0, FN: 9, TN: 0, Anz: 28
    Accuracy: 67.86%
Label: infographic, TP: 23, FP: 0, FN: 17, TN: 0, Anz: 40
    Accuracy: 57.50%
Label: realistic, TP: 174, FP: 0, FN: 60, TN: 0, Anz: 234
    Accuracy: 74.36%
Label: tabel, TP: 3, FP: 0, FN: 0, TN: 0, Anz: 3
    Accuracy: 100.00%
Label: design_element, TP: 0, FP: 3, FN: 0, TN: 44, Anz: 47
    Accuracy: 93.62%
Label: logo, TP: 0, FP: 11, FN: 0, TN: 24, Anz: 35
    Accuracy: 68.57%
Label: portrait, TP: 0, FP: 19, FN: 0, TN: 2, Anz: 21
    Accuracy: 9.52%
Label: qr_code, TP: 0, FP: 1, FN: 0, TN: 0, Anz: 1
    Accuracy: 0.00%
Label: unrealistic, TP: 0, FP: 6, FN: 0, TN: 22, Anz: 28
    Accuracy: 78.57%
Label: waste, TP: 0, FP: 161, FN: 0, TN: 141, Anz: 302
    Accuracy: 46.69%
F1: 65.24%

test
ohne sigmoid
Label: chart, TP: 77, FP: 0, FN: 73, TN: 0, Anz: 150
    Accuracy: 51.33%
Label: infographic, TP: 33, FP: 0, FN: 67, TN: 0, Anz: 100
    Accuracy: 33.00%
Label: realistic, TP: 64, FP: 0, FN: 36, TN: 0, Anz: 100
    Accuracy: 64.00%
Label: tabel, TP: 90, FP: 0, FN: 10, TN: 0, Anz: 100
    Accuracy: 90.00%
Label: design_element, TP: 0, FP: 0, FN: 0, TN: 12, Anz: 12
    Accuracy: 100.00%
Label: logo, TP: 0, FP: 44, FN: 0, TN: 56, Anz: 100
    Accuracy: 56.00%
Label: portrait, TP: 0, FP: 92, FN: 0, TN: 8, Anz: 100
    Accuracy: 8.00%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 40, FN: 0, TN: 60, Anz: 100
    Accuracy: 60.00%
Label: waste, TP: 0, FP: 0, FN: 0, TN: 0, Anz: 0
    Accuracy: 0.00%
F1: 65.99%

mit sigmoid
Label: chart, TP: 77, FP: 0, FN: 73, TN: 0, Anz: 150
    Accuracy: 51.33%
Label: infographic, TP: 84, FP: 0, FN: 16, TN: 0, Anz: 100
    Accuracy: 84.00%
Label: realistic, TP: 58, FP: 0, FN: 42, TN: 0, Anz: 100
    Accuracy: 58.00%
Label: tabel, TP: 89, FP: 0, FN: 11, TN: 0, Anz: 100
    Accuracy: 89.00%
Label: design_element, TP: 0, FP: 1, FN: 0, TN: 11, Anz: 12
    Accuracy: 91.67%
Label: logo, TP: 0, FP: 36, FN: 0, TN: 64, Anz: 100
    Accuracy: 64.00%
Label: portrait, TP: 0, FP: 87, FN: 0, TN: 13, Anz: 100
    Accuracy: 13.00%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 20, FN: 0, TN: 80, Anz: 100
    Accuracy: 80.00%
Label: waste, TP: 0, FP: 0, FN: 0, TN: 0, Anz: 0
    Accuracy: 0.00%
F1: 75.63%
"""

"""
test
Label: chart, TP: 150, FP: 0, FN: 0, TN: 0, Anz: 150
    Accuracy: 100.00%
Label: infographic, TP: 97, FP: 0, FN: 3, TN: 0, Anz: 100
    Accuracy: 97.00%
Label: realistic, TP: 100, FP: 0, FN: 0, TN: 0, Anz: 100
    Accuracy: 100.00%
Label: tabel, TP: 96, FP: 0, FN: 4, TN: 0, Anz: 100
    Accuracy: 96.00%
Label: design_element, TP: 0, FP: 0, FN: 0, TN: 12, Anz: 12
    Accuracy: 100.00%
Label: logo, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: portrait, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 0, FN: 0, TN: 100, Anz: 100
    Accuracy: 100.00%
Label: waste, TP: 0, FP: 0, FN: 0, TN: 0, Anz: 0
    Accuracy: 0.00%
F1: 99.12%

real
Label: chart, TP: 23, FP: 0, FN: 5, TN: 0, Anz: 28
    Accuracy: 82.14%
Label: infographic, TP: 37, FP: 0, FN: 3, TN: 0, Anz: 40
    Accuracy: 92.50%
Label: realistic, TP: 209, FP: 0, FN: 25, TN: 0, Anz: 234
    Accuracy: 89.32%
Label: tabel, TP: 3, FP: 0, FN: 0, TN: 0, Anz: 3
    Accuracy: 100.00%
Label: design_element, TP: 0, FP: 12, FN: 0, TN: 35, Anz: 47
    Accuracy: 74.47%
Label: logo, TP: 0, FP: 5, FN: 0, TN: 30, Anz: 35
    Accuracy: 85.71%
Label: portrait, TP: 0, FP: 2, FN: 0, TN: 19, Anz: 21
    Accuracy: 90.48%
Label: qr_code, TP: 0, FP: 0, FN: 0, TN: 1, Anz: 1
    Accuracy: 100.00%
Label: unrealistic, TP: 0, FP: 2, FN: 0, TN: 26, Anz: 28
    Accuracy: 92.86%
Label: waste, TP: 0, FP: 154, FN: 0, TN: 148, Anz: 302
    Accuracy: 49.01%
F1: 83.53%
"""