# Dieses Skript optimiert die Parameter der Sigmoid-Funktion für die Bildklassifikation basierend auf Kantenzählung.
# Es unterstützt sowohl das relative Verfahren (edges/pixels) als auch das absolute Verfahren (nur edges).
# Ziel: Finde die Parameterkombination mit dem höchsten F1-Score.

import cv2
import numpy as np
import os
import shutil
from pathlib import Path
import hashlib
from PIL import Image
from tqdm import tqdm

# === Konfigurierbare Parameter ===
use_relative = True  # True: relative Methode (edges/pixels), False: absolute Methode (nur edges)
source_folder = "../Training/data/val"
valid_labels = ["chart", "infographic", "realistic", "tabel"]
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
valid_extensions = tuple(image_extensions)

# Berechnet einen stabilen Hash für eine Datei (zur Duplikatprüfung)
def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Custom Sigmoid-Funktion mit einstellbaren Parametern für beide Verfahren
def custom_sigmoid(x, center, scale_left, scale_right, left, right):
    if x < center:
        s = 1 / (1 + np.exp((x - center) / scale_left))
    else:
        s = 1 / (1 + np.exp((x - center) / scale_right))
    return right + (left - right) * s

# Zählt die Kanten in einem Bild mittels Canny-Filter und berechnet Pixelanzahl
def sort(input_path):
    image = cv2.imread(input_path)
    if image is None:
        print(f"Bild konnte nicht geladen werden: {input_path}")
        return 0, 0
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 25, 125)  # Canny mit Schwellwerten
    edge_count = np.sum(edges > 0)
    return edge_count, image.shape[0] * image.shape[1]

# Initialisierungen
files_glob = [f for f in Path(source_folder).rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]
label_stats = {label: {"fp": 0, "fn": 0, "tp": 0, "tn": 0, "anz": 0} for label in set(p.name for p in Path(source_folder).iterdir() if p.is_dir())}
fine_best = (0, 0, 0, 0, 0, 0)  # (F1, center, left, right, scale_left, scale_right)

# Grobsuche bzw Feinsuche nach besten Parametern
for i in range(1, 7000001, 50000):
    for j in np.arange(1.0, 2.0, 0.1):
        for k in np.arange(0.1, 1.0, 0.1):
            for l in range(1, 200001, 20000):
                for m in range(1, 200001, 20000):

                    acc = 0
                    skip = 0
                    prediction_cache = set()
                    unique_hashes = set()
                    current_stats = {k: {"fp": 0, "fn": 0, "tp": 0, "tn": 0, "anz": 0} for k in label_stats.keys()}

                    for file_path in tqdm(files_glob, desc="Testlauf"):
                        parent_label = file_path.parent.name
                        source_path = str(file_path)
                        h = file_hash(source_path)
                        if h in unique_hashes:
                            continue
                        unique_hashes.add(h)
                        current_stats[parent_label]["anz"] += 1

                        edges, pixels = sort(source_path)
                        if pixels == 0:
                            skip += 1
                            continue

                        # Modifiziere edges bei Bedarf mit Sigmoid
                        edges *= custom_sigmoid(pixels, center, scale_left, scale_right, left, right)

                        score = edges / pixels if use_relative else edges
                        threshold_low = 0.08 if use_relative else 24000
                        threshold_high = 0.37 if use_relative else 690000

                        if threshold_low <= score < threshold_high:
                            if parent_label in valid_labels:
                                acc += 1
                                current_stats[parent_label]["tp"] += 1
                            else:
                                current_stats[parent_label]["fp"] += 1
                        else:
                            if parent_label not in valid_labels:
                                acc += 1
                                current_stats[parent_label]["tn"] += 1
                            else:
                                current_stats[parent_label]["fn"] += 1

                    # F1-Berechnung
                    tp = sum(v["tp"] for v in current_stats.values())
                    fp = sum(v["fp"] for v in current_stats.values())
                    fn = sum(v["fn"] for v in current_stats.values())

                    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
                    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
                    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

                    if f1 > fine_best[0]:
                        fine_best = (f1, center, left, right, scale_left, scale_right)
                        print("Neues Bestes Ergebnis:")
                        print(f"F1: {f1:.4f}, center={center}, left={left:.2f}, right={right:.2f}, scale_left={scale_left}, scale_right={scale_right}")

print("\nBestes Ergebnis:")
print(f"F1: {fine_best[0]:.4f}, center={fine_best[1]}, left={fine_best[2]:.2f}, right={fine_best[3]:.2f}, scale_left={fine_best[4]}, scale_right={fine_best[5]}")