## Streamlit App Instructions

### Dropbox Setup

1. **Create a Dropbox App**  
   - Go to: [Dropbox Developer Apps](https://www.dropbox.com/developers/apps)  
   - Click **"Create app"**
   - Choose:
     - Scoped Access  
     - Full Dropbox  
     - App Name: `pdf-image-app` (or similar)

2. **Configure Permissions**  
   Enable:
   - `files.content.write`
   - `files.content.read`
   - `sharing.write`

3. **Generate an Access Token**  
   - Go to **OAuth 2**  
   - Click **Generate access token**  
   - Copy the token

4. **Add to `.env` File**  
   If the .env file does not already exist, create one in the bachelorthesis/Bachelorthesis directory.

   Then, add the following to bachelorthesis/Bachelorthesis/.env:

   ``` python
   ACCESS_TOKEN=<your Dropbox access token>
   # Set to True if you want to upload to Dropbox.  
   # Set to False if you’ve already uploaded the folders or are just testing changes in the code.
   DROPBOX_UPLOAD=True
   ```

> Note: Dropbox tokens may be temporary. Re-generate if expired.

---

### Start the App

```bash
cd /bachelorthesis/Bachelorthesis/streamlit
pip install -r requirements.txt  # or install manually
python3 help.py                  # Generates the app.py file using the data from bachelorthesis/Bachelorthesis/Server/images
streamlit run app.py            # Launches the app
```

> Use `Ctrl + C` to stop the Streamlit server