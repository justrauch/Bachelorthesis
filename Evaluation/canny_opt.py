# Hier kann man die beiden Canny-Verfahren optimieren
# für den erstellten Validierungs-Split der Trainingsdaten.
# Durch Umschalten von `use_relative` kann zwischen absolutem und relativem Ansatz gewechselt werden.

import cv2
import numpy as np
from pathlib import Path
import hashlib

use_relative = True  # ← True = Kantenanteil relativ zur Bildgröße; False = absolute Pixelanzahl

# Berechne den MD5-Hash eines Bildes zur Duplikaterkennung
def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# Führt das Canny-Verfahren durch und liefert entweder absolute oder relative Kantenanzahl
def sort(input_path):
    image = cv2.imread(str(input_path))

    if image is None:
        print(f"Bild konnte nicht geladen werden: {input_path}")
        return 0

    height, width = image.shape[:2]

    # Graustufenbild erzeugen
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny-Kantenerkennung mit festen Schwellenwerten:
    # 25 = untere Schwelle: Pixel unter diesem Wert werden ignoriert
    # 125 = obere Schwelle: Pixel über diesem Wert gelten sicher als Kante
    edges = cv2.Canny(gray, 25, 125)

    # Anzahl der Kantenpixel berechnen
    edge_count = np.sum(edges > 0)

    if use_relative:
        # Relativer Anteil der Kantenpixel im Verhältnis zur Bildfläche
        return edge_count / (height * width)
    else:
        # Absolute Anzahl der Kantenpixel
        return edge_count

# Pfad zur Validierungsmenge
source_folder = Path("../Training/data/val")

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

# Alle Bilddateien aus dem Val-Ordner rekursiv sammeln
files_glob = [f for f in source_folder.rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

# Duplikate über Hash entfernen
anz = 0
unique_hashes = set()
unique_files = []
for f in files_glob:
    h = file_hash(f)
    if h not in unique_hashes:
        unique_hashes.add(h)
        unique_files.append(f)
        anz += 1
files_glob = unique_files

# Zielklassen
valid_labels = ["chart", "infographic", "realistic", "tabel"]

best_grob = (0, 0, 0)

if use_relative:
    # Grobsuche: relative Werte
    for i in np.arange(0, 0.25, 0.05):  # untere Schwelle
        for j in np.arange(0.15, 0.65, 0.1):  # obere Schwelle
            if j <= i:
                continue

            r = 0

            for file in files_glob:
                if "file11" in file.name:
                    continue
                if file.name.lower().endswith(valid_extensions):
                    parent_folder = file.parent.name
                    edges = sort(file)

                    if i <= edges < j:
                        if parent_folder in valid_labels:
                            r += 1
                    else:
                        if parent_folder not in valid_labels:
                            r += 1

            if r > best_grob[2]:
                best_grob = (i, j, r)

            print(f"Grobe Suche (relativ) → i: {i:.3f}, j: {j:.3f} → Treffer: {r} von {anz}")

else:
    # Grobsuche: absolute Werte
    for i in np.arange(0, 50000, 5000):
        for j in np.arange(100000, 700000, 50000):
            if j <= i:
                continue

            r = 0

            for file in files_glob:
                if "file11" in file.name:
                    continue
                if file.name.lower().endswith(valid_extensions):
                    parent_folder = file.parent.name
                    edges = sort(file)

                    if i <= edges < j:
                        if parent_folder in valid_labels:
                            r += 1
                    else:
                        if parent_folder not in valid_labels:
                            r += 1

            if r > best_grob[2]:
                best_grob = (i, j, r)

            print(f"Grobe Suche (absolut) → i: {i:.0f}, j: {j:.0f} → Treffer: {r} von {anz}")

print(f"\nBeste grobe Werte: i = {best_grob[0]:.3f}, j = {best_grob[1]:.3f} mit {best_grob[2]} richtig sortierten Bildern von {anz} Bildern.")

# Feinsuche rund um die besten groben Werte
fine_best = (0, 0, 0)
i_start, j_start = best_grob[0], best_grob[1]

if use_relative:
    # Feinsuche: relative Werte
    for i in np.arange(max(i_start - 0.025, 0), min(i_start + 0.025, 1), 0.005):
        for j in np.arange(max(j_start - 0.1, 0), min(j_start + 0.1, 1), 0.01):
            if j <= i:
                continue

            r = 0
            for file in files_glob:
                if "file11" in file.name:
                    continue
                if file.name.lower().endswith(valid_extensions):
                    parent_folder = file.parent.name
                    edges = sort(file)

                    if i <= edges < j:
                        if parent_folder in valid_labels:
                            r += 1
                    else:
                        if parent_folder not in valid_labels:
                            r += 1

            if r > fine_best[2]:
                fine_best = (i, j, r)

            print(f"Feinsuche (relativ) → i: {i:.3f}, j: {j:.3f} → Treffer: {r} von {anz}")

else:
    # Feinsuche: absolute Werte
    for i in np.arange(max(i_start - 5000, 0), min(i_start + 5000, 700000), 500):
        for j in np.arange(max(j_start - 50000, 0), min(j_start + 50000, 700000), 5000):
            if j <= i:
                continue

            r = 0
            for file in files_glob:
                if "file11" in file.name:
                    continue
                if file.name.lower().endswith(valid_extensions):
                    parent_folder = file.parent.name
                    edges = sort(file)

                    if i <= edges < j:
                        if parent_folder in valid_labels:
                            r += 1
                    else:
                        if parent_folder not in valid_labels:
                            r += 1

            if r > fine_best[2]:
                fine_best = (i, j, r)

            print(f"Feinsuche (absolut) → i: {i:.0f}, j: {j:.0f} → Treffer: {r} von {anz}")

print(f"\nBeste Feinsuche-Werte: i = {fine_best[0]:.3f}, j = {fine_best[1]:.3f} mit {fine_best[2]} richtig sortierten Bildern von {anz} Bildern.")
