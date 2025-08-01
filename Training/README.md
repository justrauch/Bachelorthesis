# Start

Zuerst alle benötigten Bibliotheken installieren:
```bash
cd /bachelorthesis/Bachelorthesis/Training
pip install -r requirements.txt
```

# Zum Herunterladen der Datensätze für das Training des Modells, folge den untenstehenden Anweisungen:

Um das TableBank-Dataset in einer WSL- oder Linux-Umgebung zu laden, nutze folgende Befehle. Diese laden den Datensatz in mehreren Teilen herunter, fügen sie zusammen und entpacken das Archiv:

```bash
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.001
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.002
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.003
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.004
wget https://huggingface.co/datasets/liminghao1630/TableBank/resolve/main/TableBank.zip.005

cat TableBank.zip.001 TableBank.zip.002 TableBank.zip.003 TableBank.zip.004 TableBank.zip.005 > TableBank.zip
unzip TableBank.zip -d TableBank
```

# Für die Datensätze Charts, Logos, Unrealistic Images und QR-Codes, führe folgendes Skript aus:

```python
cd bachelorthesis/Bachelorthesis/Datasets/
python3 download.py
```

# Um das Infographics-Dataset herunterzuladen, besuche die offizielle Wettbewerbsseite:

Gehe zu https://rrc.cvc.uab.es/?ch=17&com=downloads

Registriere dich oder logge dich ein

Scrolle zu “Task 3 – Infographics VQA”

Klicke auf den Hyperlink „images“, um den Download zu starten

danach:

```bash
cd /path/to/the/folder/where/the/file/is
tar -xzf infographicsvqa_images.tar.gz -C /path/to/target/folder
```

# Um den Datensatz mit realistischen Bildern (von OpenImages) herunterzuladen, führe folgendes Skript aus:

```python
cd bachelorthesis/Bachelorthesis/Datasets/
python3 openimages.py
```
Diese Datensätze sind erforderlich, um das Modell für visuelle Inhaltsklassifikationsaufgaben zu trainieren und zu evaluieren.

# Bachelorarbeit – Vision Transformer Workflow

## Datensätze zusammenstellen

Um den finalen Datensatz zu erstellen, nutze das Skript `split.py`:

Ausführung:
```bash
python3 split.py <bevorzugter_label_name> <zielordner_name>
```

Dieses Skript teilt die Bilder in `train`, `val` und `test` Sets auf.

Starte den Trainingsprozess für alle heruntergeladenen Ordner oder spezifische Labels, die du einbeziehen möchtest.

---

## Modell trainieren

Zum Trainieren des Modells nutze:
```
\bachelorthesis\Bachelorthesis\Training\train.py
```

Es verwendet die Daten, die von `split.py` erstellt wurden. Nach dem Training wird ein Ordner `vit_output` mit allen Modell-Checkpoints erstellt.

Zum Hochladen des Modells auf Hugging Face, nutze:
```
\bachelorthesis\Bachelorthesis\Training\upload.py
```

Achte darauf:

1. Den Ordnernamen anzupassen.  
2. Deinen Hugging Face Token in die `.env` Datei einzutragen:
```env
HUGGING_FACE_TOKEN=<Dein Token>
```

Oder nutze das `\bachelorthesis\Bachelorthesis\Training\Jupiter_Notebook.ipynb` und trage dort deine Hugging Face- und Weights & Biases-Tokens ein.

---

## Modell testen

Um das Modell zu testen, führe aus:
```
\bachelorthesis\Bachelorthesis\Training\test.py
```

Es verwendet die Testdaten aus:
```
\bachelorthesis\Bachelorthesis\Training\data\test
```

Achte darauf, dass der Modellname mit dem Ordner oder deinem Hugging Face Repo übereinstimmt.

---

## Optional: Eigene Bilder testen

Wenn du das Modell mit eigenen Bildern testen möchtest:

1. Nutze das Skript:
```
\bachelorthesis\Bachelorthesis\Training\get_images.py
```

Setze den Parameter `zip_path` auf den Speicherort deines ZIP-Ordners.  
Der ZIP-Ordner sollte nur PDF-Dateien enthalten.  
Das Skript extrahiert alle Bilder aus allen PDFs im Ordner.

2. Danach führe aus:
```
\bachelorthesis\Bachelorthesis\Training\model_sort.py
```

Dies erstellt einen `sample`-Ordner und sortiert die Bilder automatisch in Unterordner basierend auf den Vorhersagen des Modells.
