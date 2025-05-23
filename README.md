# Setup Guide for bachelorthesis/Bachelorthesis/Server/

# This guide describes how to set up the RunPod endpoints and the local server environment using Docker.

# Prerequisites
- Docker is installed and running.
- You have a RunPod account with at least $5 in credits.
- You have a Hugging Face account with a valid HF_TOKEN.
- You have access to https://github.com/justrauch/gemma-captioner-images or a fork of it.

# RunPod Setup

1. Create RunPod Account & Add Credits
- Sign up at https://runpod.io
- Add at least $5 in credits

2. Connect GitHub
- Go to Settings > Connections > Edit Connections
- Authorize access to your GitHub account

# Create Serverless Endpoints

1. Image Captioning with gemma-3
- Go to Serverless > New Endpoint
- Select GitHub Repo → Next
- Enter: https://github.com/justrauch/gemma-captioner-images (or your fork) → Next
- Choose a GPU with at least 80 GB RAM
- Max Workers = 1, Execution Timeout = 10000
- Add Environment Variables:
  HF_TOKEN = <your Huggingface token>
  MODEL_ID = google/gemma-3-12b-it
  CAPTION_PROMPT = Describe the content of the image in one sentence.
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

# main.py Configuration
Set these variables in bachelorthesis/Bachelorthesis/Server/main.py:

API_KEY = "<your RunPod API Key>"
API_URL_IMAGE_SELECTOR = "<RunPod URL for gemma-3>"
API_URL_DESCRIPTION = "<RunPod URL for mistralai>"
API_URL_EMBEDDINGS = "<RunPod URL for intfloat>"

# Start Local Server with Docker

cd bachelorthesis/Bachelorthesis/Server/
sudo service docker start       # or start Docker Desktop manually
docker compose up --build       # Stop with Ctrl + C

Remove Local Database
docker compose down -v

# Use the Web App
Open bachelorthesis/Bachelorthesis/Client/index.html in a browser.
Disable built-in browser antivirus temporarily to avoid issues with \n or long metadata strings during downloads.

# Test PDFs
Sample PDFs for testing are in:
bachelorthesis/Bachelorthesis/Bsp.zip
