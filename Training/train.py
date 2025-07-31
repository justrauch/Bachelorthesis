# Hier kannst du das Modell trainieren, nachdem du die Trainingsdaten wie in der README.md beschrieben
# heruntergeladen und erstellt hast.
# Stelle sicher, dass du deinen Weights & Biases (wandb) Token in den Umgebungsvariablen gesetzt hast (z. B. WANNDB_TOKEN).

from transformers import ViTForImageClassification, ViTFeatureExtractor, TrainingArguments, Trainer
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch
from sklearn.metrics import accuracy_score
import wandb
import os

wandb.login(key=os.getenv("WANNDB_TOKEN"))

# Initialisiere ein neues wandb-Projekt und einen Run
wandb.init(project="vit-accuracy", name="run-with-accuracy")

# Lade das vortrainierte ViT-Modell und den zugehörigen Feature Extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)

# Definiere die Bild-Transformationen, passend zum Modell
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=feature_extractor.image_mean, std=feature_extractor.image_std),
])

# Lade Trainings- und Validierungsdaten
train_dataset = datasets.ImageFolder("data/train", transform=transform)
val_dataset = datasets.ImageFolder("data/val", transform=transform)

# Anzahl der Klassen im Datensatz
num_labels = len(train_dataset.classes)

# Lade das Modell mit angepasster Anzahl von Labels
model = ViTForImageClassification.from_pretrained(
    model_name,
    num_labels=num_labels,
    ignore_mismatched_sizes=True  # erlaubt Transfer Learning trotz unterschiedlicher Anzahl an Ziellabels,
                                  # da die neuen Labels die ursprünglichen des vortrainierten Modells ersetzen 
)

# Batch-Daten korrekt für den Trainer aufzubereiten
def collate_fn(batch):
    return {
        "pixel_values": torch.stack([x[0] for x in batch]),
        "labels": torch.tensor([x[1] for x in batch])
    }

# Metrikfunktion zur Evaluation, hier: Klassifikationsgenauigkeit
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = logits.argmax(-1)
    return {
        "accuracy": accuracy_score(labels, preds)
    }

# Trainingsargumente für den Huggingface-Trainer
training_args = TrainingArguments(
    output_dir="./vit_output",                   # Wohin das Modell gespeichert wird
    per_device_train_batch_size=8,               # Batch-Größe für Training
    per_device_eval_batch_size=8,                # Batch-Größe für Evaluation
    evaluation_strategy="epoch",                 # Evaluation nach jeder Epoche
    save_strategy="epoch",                       # Modell speichern nach jeder Epoche
    num_train_epochs=5,                          # Anzahl Trainingsdurchläufe
    logging_dir="./logs",                        # Logging-Verzeichnis für wandb
    report_to="wandb",                           # Logging an Weights & Biases senden
    logging_steps=10,                            # Wie oft Logs geschrieben werden
    load_best_model_at_end=True,                 # Bestes Modell automatisch am Ende laden
    metric_for_best_model="eval_loss",           # Beste Modell-Auswahl basiert auf Validierungsverlust
    greater_is_better=False                      # Geringerer eval_loss ist besser
)

# Initialisiere den Huggingface-Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=collate_fn,
    tokenizer=feature_extractor,                 # Wird verwendet, um die Inputs korrekt zu verarbeiten
    compute_metrics=compute_metrics
)

# Start
trainer.train()
