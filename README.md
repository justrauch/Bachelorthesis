
### Setup Guide for `bachelorthesis/Bachelorthesis/Server/`

#### This guide describes how to set up the RunPod endpoints and the local server environment using Docker.

---

### Prerequisites

- Docker is installed and running  
- You have a RunPod account with at least $5 in credits  
- You have a Hugging Face account with a valid `HF_TOKEN`  
- You have access to [`justrauch/gemma-captioner-images`](https://github.com/justrauch/gemma-captioner-images) or a fork of it  

---

### RunPod Setup

#### 1. Create RunPod Account & Add Credits
- Sign up at [https://runpod.io](https://runpod.io)  
- Add at least $5 in credits  

#### 2. Connect GitHub
- Go to **Settings > Connections > Edit Connections**  
- Authorize GitHub access  

---

### Create Serverless Endpoints

#### Image Captioning with Gemma-3

1. Go to **Serverless > New Endpoint**  
2. Select **GitHub Repo → Next**  
3. Enter:  
   ```
   https://github.com/justrauch/gemma-captioner-images
   ```
   *(or your fork)*  
4. Choose a GPU with **min. 80 GB RAM**  
5. Set:
   - Max Workers: `1`
   - Execution Timeout: `10000`
6. Add environment variables:
   ```
   HF_TOKEN=<your Huggingface token>
   MODEL_ID=google/gemma-3-12b-it
   CAPTION_PROMPT="Describe the content of the image in one sentence."
   ```
7. Save and wait for the build (see **Builds** tab)  
8. Copy the **Request URL** under **Requests**  

> To change Gemma model versions, update `MODEL_ID` to:  
> `google/gemma-3-1.1b-it`, `4b`, `12b`, or `24b`  
> *(Only Gemma-3 models are supported)*

More info:  
[Automated Image Captioning on RunPod](https://blog.runpod.io/automated-image-captioning-with-gemma-3-on-runpod-serverless/)

---

#### LLM & Embeddings

##### a) Mistral LLM (Text)
- Go to: **Serverless > New Endpoint > Preset Models > Text**  
- Select: `mistralai/Mistral-7B-Instruct-v0.3`  
- RAM: min. `48 GB`  
- Max Workers: `1`

##### b) Embeddings
- Go to: **Preset Models > Embedding**  
- Select: `intfloat/multilingual-e5-large`  
- RAM: min. `16 GB`  
- Max Workers: `1`

**RunPod Limit**: Max 5 workers total. Set workers = 1 per endpoint to avoid exceeding the limit.

---

### API Key Setup

1. Go to **Settings > API Key > Create API Key**  
2. Set:
   - Name: e.g. `BachelorProject`
   - Type: **Restricted**
   - Permissions:
     ```
     api.runpod.ai – read/write
     All 3 Endpoints – read/write
     ```
3. Copy the key and **store it securely**

---

### `main.py` Configuration

First, create a file named .env in the bachelorthesis/Bachelorthesis directory if it doesn't already exist.

Then, add the following variables to the .env file (bachelorthesis/Bachelorthesis/.env):

```python
API_URL_IMAGE_SELECTOR = "<RunPod URL for gemma-3>"
API_URL_DESCRIPTION = "<RunPod URL for mistralai>"
API_URL_EMBEDDINGS = "<RunPod URL for intfloat>"
API_KEY=<your RunPod API Key>
```

> **Note:** This key may be temporary. Please ensure it's still valid before use.

---

### Start Local Server with Docker

```bash
cd bachelorthesis/Bachelorthesis/Server/

# Start the Docker service (if not already running)
sudo service docker start     # or start Docker Desktop manually

# Build and start the containers (only needed the first time) Ctrl + C to stop
docker compose up --build

# Start the containers (after they've been built) Ctrl + C to stop
docker compose up # -d to run in the background

# Stop and remove the running containers
docker compose down

```

To remove all local data:

```bash
docker compose down -v
```

---

### Use the Web App

Open the following file in your browser:

```
bachelorthesis/Bachelorthesis/Client/index.html
```

> Disable built-in browser antivirus temporarily if there are issues with newline characters or metadata in downloads.

---

### Test PDFs

Use test files from:

```
bachelorthesis/Bachelorthesis/Bsp.zip
```

---

### Docker Volumes in `Server/docker-compose.yml`

```yaml
volumes:
  - ./images:/app/images
  - ./zip_folders:/app/zip_folders
  - appdata:/app/data
```

**Explanation:**

- `./images`: stores extracted images per PDF file
- `./zip_folders`: stores ZIP archives per PDF
- `appdata`: internal Docker volume for app-specific data

To avoid saving data on the host, comment out the bind mounts:

```yaml
volumes:
  # - ./images:/app/images
  # - ./zip_folders:/app/zip_folders
  - appdata:/app/data
```

To delete image & ZIP folders permanently:

```bash
cd /bachelorthesis/Bachelorthesis/Server
sudo rm -rf images/
sudo rm -rf zip_folders/
```

> These commands will irreversibly delete the contents. Backup first.

---
