# Setup-Anleitung für `bachelorthesis/Bachelorthesis/Server/`

Diese Anleitung beschreibt, wie man die RunPod-Endpunkte und die lokale Server-Umgebung mit Docker einrichtet.

---

## Voraussetzungen

- Docker ist installiert und läuft
- Du hast ein RunPod-Konto mit mindestens 5 \$ Guthaben
- Du hast ein Hugging Face-Konto mit einem gültigen `HF_TOKEN`
- Du hast Zugriff auf [`justrauch/gemma-captioner-images`](https://github.com/justrauch/gemma-captioner-images) oder einen eigenen Fork

---

## RunPod-Einrichtung

### 1. RunPod-Konto erstellen & Guthaben hinzufügen

- Registriere dich unter [https://runpod.io](https://runpod.io)
- Lade mindestens 5 \$ Guthaben auf

### 2. GitHub verbinden

- Gehe zu **Settings > Connections > Edit Connections**
- Erlaube den GitHub-Zugriff

---

## Serverless Endpunkte erstellen

### Bildbeschreibung mit Gemma-3

1. Gehe zu **Serverless > New Endpoint**
2. Wähle **GitHub Repo → Next**
3. Trage ein:
   ```
   https://github.com/justrauch/gemma-captioner-images
   ```
   *(oder dein Fork)*
4. Wähle eine GPU mit **mindestens 80 GB RAM**
5. Setze:
   - Max Workers: `1`
   - Execution Timeout: `10000`
6. Füge folgende Umgebungsvariablen hinzu:
   ```
   HF_TOKEN=<dein Huggingface Token>
   MODEL_ID=google/gemma-3-12b-it
   CAPTION_PROMPT="Describe the content of the image in one sentence."
   ```
7. Speichern und auf den Build warten (siehe **Builds**-Tab)
8. Kopiere die **Request URL** unter **Requests**

> Um die Gemma-Modellversion zu ändern, `MODEL_ID` setzen auf:\
> `google/gemma-3-1.1b-it`, `4b`, `12b`, oder `24b`\
> *(Es werden nur Gemma-3 Modelle unterstützt)*

Mehr Infos:\
[Automatisierte Bildbeschreibung auf RunPod](https://blog.runpod.io/automated-image-captioning-with-gemma-3-on-runpod-serverless/)

---

### LLM & Embeddings

#### a) Mistral LLM (Text)

- Gehe zu: **Serverless > New Endpoint > Preset Models > Text**
- Wähle: `mistralai/Mistral-7B-Instruct-v0.3`
- RAM: mindestens `48 GB`
- Max Workers: `1`

#### b) Embeddings

- Gehe zu: **Preset Models > Embedding**
- Wähle: `intfloat/multilingual-e5-large`
- RAM: mindestens `16 GB`
- Max Workers: `1`

**RunPod Limit**: Maximal 5 Worker insgesamt. Setze pro Endpoint = 1, um das Limit nicht zu überschreiten.

---

## API-Key Einrichtung

1. Gehe zu **Settings > API Key > Create API Key**
2. Setze:
   - Name: z. B. `BachelorProject`
   - Typ: **Restricted**
   - Berechtigungen:
     ```
     api.runpod.ai – read/write
     Alle 3 Endpunkte – read/write
     ```
3. Schlüssel kopieren und sicher speichern

---

## Konfiguration von `main.py`

Erstelle zuerst eine Datei `.env` im Ordner `bachelorthesis/Bachelorthesis`, falls sie noch nicht existiert.

Füge dann folgende Variablen in die `.env`-Datei ein (`bachelorthesis/Bachelorthesis/.env`):

```python
API_URL_IMAGE_SELECTOR = "<RunPod URL für gemma-3>"
API_URL_DESCRIPTION = "<RunPod URL für mistralai>"
API_URL_EMBEDDINGS = "<RunPod URL für intfloat>"
API_KEY=<dein RunPod API Key>
```

> **Hinweis:** Dieser Schlüssel könnte zeitlich begrenzt sein. Bitte sicherstellen, dass er noch gültig ist.

---

## Lokalen Server mit Docker starten

```bash
cd bachelorthesis/Bachelorthesis/Server/

# Docker starten (falls nicht schon läuft)
sudo service docker start     # oder Docker Desktop manuell starten

# Container bauen und starten (nur beim ersten Mal)  Strg + C zum Stoppen
docker compose up --build

# Container starten (nachdem sie gebaut wurden)  Strg + C zum Stoppen
docker compose up # -d um im Hintergrund laufen zu lassen

# Laufende Container stoppen und entfernen
docker compose down
```

Um alle lokalen Daten zu löschen:

```bash
docker compose down -v
```

---

## Web-App starten

```bash
cd bachelorthesis/Bachelorthesis/Client

python3 -m http.server 5500 --bind 127.0.0.1 --directory .
```

Dann im Browser öffnen: [http://127.0.0.1:5500/](http://127.0.0.1:5500/)

---

## Test-PDFs

Verwende die Testdateien aus:

```
bachelorthesis/Bachelorthesis/Bsp.zip
```

---

## Docker Volumes in `Server/docker-compose.yml`

```yaml
volumes:
  - ./images:/app/images
  - ./zip_folders:/app/zip_folders
  - appdata:/app/data
```

**Erklärung:**

- `./images`: speichert extrahierte Bilder pro PDF
- `./zip_folders`: speichert ZIP-Archive pro PDF
- `appdata`: internes Docker-Volume für app-spezifische Daten

Um zu vermeiden, dass Daten auf dem Host gespeichert werden, auskommentieren:

```yaml
volumes:
  # - ./images:/app/images
  # - ./zip_folders:/app/zip_folders
  - appdata:/app/data
```

Um die Image- & ZIP-Ordner dauerhaft zu löschen:

```bash
cd /bachelorthesis/Bachelorthesis/Server
sudo rm -rf images/
sudo rm -rf zip_folders/
```

> Diese Befehle löschen den Inhalt unwiderruflich. Vorher ggf. Backup machen.

