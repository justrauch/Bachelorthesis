#### Setup Guide for bachelorthesis/Bachelorthesis/Server/

### This guide describes how to set up the RunPod endpoints and the local server environment using Docker.

## Prerequisites
- Docker is installed and running.
- You have a RunPod account with at least $5 in credits.
- You have a Hugging Face account with a valid HF_TOKEN.
- You have access to https://github.com/justrauch/gemma-captioner-images or a fork of it.

## RunPod Setup

1. Create RunPod Account & Add Credits
- Sign up at https://runpod.io
- Add at least $5 in credits

2. Connect GitHub
- Go to Settings > Connections > Edit Connections
- Authorize access to your GitHub account

## Create Serverless Endpoints

1. Image Captioning with gemma-3
- Go to Serverless > New Endpoint
- Select GitHub Repo → Next
- Enter: https://github.com/justrauch/gemma-captioner-images (or your fork) → Next
- Choose a GPU with at least 80 GB RAM
- Max Workers = 1, Execution Timeout = 10000
- Add Environment Variables:
  HF_TOKEN = <your Huggingface token>, 
  MODEL_ID = google/gemma-3-12b-it, 
  CAPTION_PROMPT = "Describe the content of the image in one sentence."
- Save endpoint
- You’ll find the request URL under "Requests"
- Monitor build status under "Builds"
- Pushes to the repo will trigger a rebuild
- To switch Gemma model versions, change MODEL_ID to 1B, 4B, 12B, or 24B (only gemma-3 models supported)

More info: https://blog.runpod.io/automated-image-captioning-with-gemma-3-on-runpod-serverless/

2. Serverless LLMs & Embeddings

a) Mistral LLM (mistralai/Mistral-7B-Instruct-v0.3)
- Go to Serverless > New Endpoint > Preset Models > Text
- Set model: mistralai/Mistral-7B-Instruct-v0.3
- RAM: min 48 GB
- Max Workers: 1

Tip: Each endpoint starts with 3 workers. Reduce to 1 before creating another. Max total: 5.

b) Embedding Model (intfloat/multilingual-e5-large)
- Go to Preset Models > Embedding
- Set model: intfloat/multilingual-e5-large
- RAM: min 16 GB
- Max Workers: 1

3. API Key Setup
- Go to Settings > API Key > Create API Key
- Name: e.g. BachelorProject
- Type: Restricted
- Permissions:
  api.runpod.ai – read/write
  All 3 Endpoints – read/write
- Copy the API key

## main.py Configuration
Set these variables in bachelorthesis/Bachelorthesis/Server/main.py:

API_KEY = "<your RunPod API Key>"
API_URL_IMAGE_SELECTOR = "<RunPod URL for gemma-3>"
API_URL_DESCRIPTION = "<RunPod URL for mistralai>"
API_URL_EMBEDDINGS = "<RunPod URL for intfloat>"

Also, add the following entry to your .env file located at bachelorthesis/Bachelorthesis/.env:

API_KEY = <your RunPod API Key>
Note: The API key may be temporary. Please make sure it is still valid before using it.

## Start Local Server with Docker

cd bachelorthesis/Bachelorthesis/Server/
sudo service docker start       # or start Docker Desktop manually
docker compose up --build       # Stop with Ctrl + C

Remove Local Database and Stored Files
docker compose down -v

## Use the Web App
Open bachelorthesis/Bachelorthesis/Client/index.html in a browser.
Disable built-in browser antivirus temporarily to avoid issues with \n or long metadata strings during downloads.

## Test PDFs
Sample PDFs for testing are in:
bachelorthesis/Bachelorthesis/Bsp.zip

## Volumes in Server/docker-compose.yml

volumes:
  - ./images:/app/images
  - ./zip_folders:/app/zip_folders
  - appdata:/app/data

Explanation:
- './images': Stores all extracted images on the host system,
             grouped into folders named after the processed files.
- './zip_folders': Stores generated ZIPs similarly on the host.
- 'appdata': Internal persistent volume for additional application data.

```yaml
volumes:
  # - ./images:/app/images
  # - ./zip_folders:/app/zip_folders
  - appdata:/app/data
```

Explanation:
- Comment out './images' and './zip_folders' if you do NOT want
  images and ZIP files to be stored on your host system.
- 'appdata' remains enabled as the internal persistent volume.

To permanently delete the folders and all their contents, run the following commands:

cd /bachelorthesis/Bachelorthesis/Server
sudo rm -rf images/
sudo rm -rf zip_folders/

Warning:
These commands will irreversibly delete the folders and everything inside them.
Make sure you back up any important data before proceeding.

### Streamlit App Instructions

## Dropbox Setup

To use your own Dropbox account for storing images, follow these steps:

1. **Create a Dropbox App**  
   - Visit: [https://www.dropbox.com/developers/apps](https://www.dropbox.com/developers/apps)  
   - Click **"Create app"**  
   - Choose:
     - **Scoped Access**
     - **Full Dropbox**
     - Give your app a unique name (e.g., `pdf-image-app`)  
   - Click **"Create app"**

2. **Configure Permissions**  
   - Under the **"Permissions"** tab, enable:
     - `files.content.write`
     - `files.content.read`
     - `sharing.write`  
   - Click **"Submit"**

3. **Generate an Access Token**  
   - Go to the **"OAuth 2"** section  
   - Click **"Generate access token"**  
   - Copy the generated token

4. **Update Your Script**  
   - Open the file:  
     `/bachelorthesis/Bachelorthesis/.env`  
   - Set the variable:  
      ACCESS_TOKEN=<your Dropbox Access Token>
      Note: This token may be temporary — please ensure it is still valid before use.

---

## Starting the App

1. Make sure the folder `\bachelorthesis\Bachelorthesis\Server\images` exists.  
   (It is defined as a volume in `Server/docker-compose.yml`.)

2. Add one or more subfolders inside the `images` folder.  
   Each subfolder should contain images and a corresponding PDF file.

3. Open a terminal and run the following commands:

```bash
cd /bachelorthesis/Bachelorthesis/streamlit
pip install dropbox requests PyPDF2 streamlit streamlit-image-select streamlit-scroll-to-top streamlit-js-eval
python3 help.py        # This generates the app.py file
streamlit run app.py   # Starts the app
# Press Ctrl+C to stop the app
