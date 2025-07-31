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

"""
### Start the App for Visualization

Navigate to the Streamlit folder and install the requirements:

cd /bachelorthesis/Bachelorthesis/streamlit
pip install -r requirements.txt  # or install manually

Then generate the app and launch it:

python3 help.py                  # Generates app.py using data from Bachelorthesis/Server/images
streamlit run app.py             # Starts the Streamlit app

Use Ctrl + C to stop the Streamlit server.

---

### Start the App for the Survey

Navigate to the same folder and run the following:

cd /bachelorthesis/Bachelorthesis/streamlit
pip install -r requirements.txt  # or install manually

Generate and launch the survey app:

python3 help_survey.py           # Generates survey.py using data from Bachelorthesis/Server/images
streamlit run survey.py          # Starts the survey app

Use Ctrl + C to stop the Streamlit server.
"""
