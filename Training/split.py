# Hier kann man nun die erstellten Trainingsdaten in Train-, Test- und Validation-Splits aufteilen
# für den jeweiligen Unterordner (Label-Klasse) innerhalb des Trainingsdatenverzeichnisses.

import shutil
import random
from pathlib import Path
import sys

# Zwei Argumente werden beim Aufruf erwartet:
# 1. Name des Quellordners innerhalb von "Training"
# 2. Ziel-Unterordnername (Klassenname für train/val/test)
first_arg = sys.argv[1]
second_arg = sys.argv[2] 

# Pfad zu den zu verarbeitenden Rohdaten
source_dir = Path.home() / "bachelorthesis" / "Bachelorthesis" / "Training" / first_arg

# Name des Ziel-Unterordners (z. B. „table“) innerhalb der train/val/test-Struktur
target_subfolder = second_arg

# Basisverzeichnis für aufgeteilte Daten
data_dir = Path.home() / "bachelorthesis" / "Bachelorthesis" / "Training" / "data"
data_dir.mkdir(parents=True, exist_ok=True)

# Zielpfade für die drei Daten-Splits
train_dir = data_dir / "train" / target_subfolder
val_dir   = data_dir / "val"   / target_subfolder
test_dir  = data_dir / "test"  / target_subfolder

# Erstelle die Zielordner, falls sie noch nicht existieren
train_dir.mkdir(parents=True, exist_ok=True)
val_dir.mkdir(parents=True, exist_ok=True)
test_dir.mkdir(parents=True, exist_ok=True)

# Unterstützte Bildformate
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

# Alle gültigen Bilddateien im Quellverzeichnis rekursiv sammeln
files = [f for f in source_dir.rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

# Optional: Begrenze auf die ersten 1000 Bilder
files = files[:1000]

# Zufällige Durchmischung (reproduzierbar durch festen Seed)
random.seed(42)
random.shuffle(files)

# Prozentuale Aufteilung in Training, Validierung und Test
train_split = 0.8
val_split = 0.1
test_split = 0.1

# Berechne tatsächliche Anzahl an Dateien pro Split
n_total = len(files)
n_train = int(n_total * train_split)
n_val = int(n_total * val_split)

# Dateilisten je nach Aufteilung
train_files = files[:n_train]
val_files   = files[n_train:n_train + n_val]
test_files  = files[n_train + n_val:]

# Funktion zum Verschieben von Dateien in den Zielordner
def move_files(file_list, target_dir, label):
    for file in file_list:
        new_path = target_dir / file.name
        if new_path.exists():
            print(f"Datei existiert bereits: {new_path.name} – wird übersprungen.")
            continue
        shutil.move(str(file), str(new_path))
        print(f"{label} Moved: {file.name} → {new_path}")

# Dateien in die entsprechenden Ordner verschieben
move_files(train_files, train_dir, "Train")
move_files(val_files, val_dir, "Val")
move_files(test_files, test_dir, "Test")

print("\nAlle Dateien erfolgreich auf train/val/test aufgeteilt.")
