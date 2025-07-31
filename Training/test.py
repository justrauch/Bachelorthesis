# Hier kann man nun das trainierte Modell anhand des Testsplits aus den Trainingsdaten bewerten

import shutil
import random
from pathlib import Path
from collections import Counter
import json

from transformers import ViTForImageClassification, ViTImageProcessor
import torch
from PIL import Image
from torchvision import transforms
from tqdm import tqdm

# Pfad zum Testverzeichnis
test_dir = Path("./data") / "test"

# Gültige Bildformate
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Lade das trainierte Modell und den zugehörigen ImageProcessor
model = ViTForImageClassification.from_pretrained("JustinStrauch/vit_fit_v3")
processor = ViTImageProcessor.from_pretrained("JustinStrauch/vit_fit_v3")
model.to(device)
model.eval()  # Evaluierungsmodus

# Transformationen, um Bilder in das Format zu bringen, das das Modell erwartet
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=processor.image_mean, std=processor.image_std),
])

# Cache zur Vermeidung mehrfacher Vorhersagen für dasselbe Bild
prediction_cache = {}

# Vorhersagefunktion für ein einzelnes Bild (gibt den Klassennamen zurück)
def predict(image_path):
    if image_path in prediction_cache:
        return prediction_cache[image_path]

    # Bild laden und vorbereiten
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    # Vorhersage
    with torch.no_grad():
        outputs = model(input_tensor)
        predicted_idx = outputs.logits.argmax(dim=1).item()

    # Index wieder in Klassennamen umwandeln
    predicted_label = subfolders[int(idx_to_class.get(predicted_idx, str(predicted_idx)))]
    prediction_cache[image_path] = predicted_label
    return predicted_label

# Prüft, ob die Vorhersage korrekt war (true/false) für ein einzelnes Bild
def get_prediction(path, label, test_label):
    result = [predict(str(path))]
    if label == test_label:
        if not test_label in result:
            print(f"for {path}: {label} -> {result}")
        return test_label in result
    else:
        if test_label in result:
            print(f"for {path}: {label} -> {result}")
        return not test_label in result

# Berechnet, wie oft das Ziel-Label korrekt erkannt wurde (Accuracy je Klasse)
def get_accuracy(file_list, label):
    positiv = {}
    for file in tqdm(file_list, desc=f"Testing label: {label}"):
        file_label = str(file).split("/")[-2]  # Annahme: Label = Ordnername
        positiv[file_label] = positiv.get(file_label, 0) + int(get_prediction(file, file_label, label))
    return positiv

# Liste aller Klassen (Ordner im Testverzeichnis)
subfolders = sorted([str(f).split("/")[-1] for f in test_dir.iterdir() if f.is_dir()])

# Initiale Liste aller Bilddateien im Testverzeichnis
files = [f for f in test_dir.rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]

# Evaluation: Berechne die Accuracy für jede Klasse
all_labels = 0
for sub in subfolders:
    sub_dir = test_dir / sub
    files = [f for f in sub_dir.rglob("*") if f.is_file() and f.suffix.lower() in image_extensions]
    tmp = get_accuracy(files, sub)
    acc = tmp[sub] / len(files)
    all_labels += acc
    print(f"Accuracy für {sub}: {acc:.3f}")

# Gesamtdurchschnitt der Accuracy über alle Klassen
print(f"\nGesamt-Accuracy über alle Klassen: {all_labels / len(subfolders):.3f}")
