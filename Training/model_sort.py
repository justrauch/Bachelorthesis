# Dieses Skript sortiert Bilder (z. B. aus einer Beispiel-ZIP oder einem Testdatensatz)
# automatisch in entsprechende Klassenordner, um sich einen Überblick zu verschaffen.
# Damit dieses Skript funktioniert, muss zuvor mit get_images.py der 'sample'-Ordner
# erstellt werden, der die Bilder der Testmenge enthält.
# Es verwendet das trainierte Modell und filtert unbrauchbare Bilder heraus.

import shutil
import random
from pathlib import Path
from collections import Counter

from transformers import ViTForImageClassification, ViTImageProcessor
import torch
from PIL import Image
import pytesseract
from torchvision import transforms
import json
from tqdm import tqdm

# Modell und Processor laden
model = ViTForImageClassification.from_pretrained("JustinStrauch/vit_fit_v3")
processor = ViTImageProcessor.from_pretrained("JustinStrauch/vit_fit_v3")
model.eval()  # Evaluierungsmodus

# Bildtransformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=processor.image_mean, std=processor.image_std),
])

# Gültige Klassen
valid_labels = ["chart", "infographic", "realistic", "tabel"]

# Ungültige Klassen
waste_labels = ["design_element", "logo", "portrait", "qr_code", "unrealistic", "waste"]

# Alle Klassennamen
subfolders = sorted(valid_labels + waste_labels)
print("Bekannte Klassen:", subfolders)

# Arbeitsverzeichnis, z. B. entpackter Beispiel-ZIP oder eigener Testordner
base_path = Path("./sample")

# Ordnerstruktur für jede Klasse anlegen und ggf. alte Inhalte löschen
for folder in subfolders:
    folder_path = base_path / folder
    folder_path.mkdir(parents=True, exist_ok=True)

    # Ordner leeren (alle Dateien/Unterordner löschen)
    for item in folder_path.iterdir():
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

    print(f"Ordner bereitgestellt und geleert: {folder_path.resolve()}")

# Filterfunktion: prüft, ob das Bild zu klein oder textüberladen ist (→ als "waste" behandeln)
def filter_image(path):
    try:
        with Image.open(path) as img:
            width, height = img.size

            if width < 50 or height < 50:
                print(f"{path} ist nur {width} x {height} Pixel groß")
                return True

            # OCR zur Erkennung von übermäßigem Textinhalt
            text = pytesseract.image_to_string(img)
            if len(text.strip()) > 3500:
                print(f"{path} enthält {len(text.strip())} Zeichen")
                return True

            return False

    except Exception as e:
        print(f"Fehler beim Verarbeiten von {path}: {e}")
        return True

# Vorhersagefunktion
def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        predicted_idx = outputs.logits.argmax(dim=1).item()
    
    predicted_class = subfolders[int(predicted_idx)]
    print(f"{image_path.name} → {predicted_class}")
    return predicted_class

# Unterstützte Bildformate
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

# Sammle alle Bilddateien rekursiv
files = [f for f in test_dir.rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

# Erneut alle Klassennamen ermitteln
subfolders = sorted([str(f).split("/")[-1] for f in test_dir.iterdir() if f.is_dir()], reverse=False)[:-1]
print("Erkannte Zielordner:", subfolders)

# Hauptverarbeitung: Filter → Vorhersage → Einsortierung
for file in tqdm(files, desc="Bilder werden sortiert"):
    if filter_image(file):
        # Bei "ungeeignetem" Bild direkt in den waste-Ordner
        shutil.copy(file, test_dir / "waste" / file.name)
        continue

    # Klassifizieren und ins passende Verzeichnis kopieren
    predicted_label = predict(file)
    shutil.copy(file, test_dir / predicted_label / file.name)
    print(f"Verschoben: {file.name} → {predicted_label}")
