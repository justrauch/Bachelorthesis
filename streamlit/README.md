# Streamlit App Anleitung

## Dropbox Einrichtung

1. **Dropbox App erstellen**  
   - Gehe zu: [Dropbox Developer Apps](https://www.dropbox.com/developers/apps)  
   - Klicke auf **"Create app"**  
   - Wähle:
     - Scoped Access  
     - Full Dropbox  
     - App-Name: `pdf-image-app` (oder ähnlich)

2. **Berechtigungen konfigurieren**  
   Aktiviere:
   - `files.content.write`
   - `files.content.read`
   - `sharing.write`

3. **Access Token generieren**  
   - Gehe zu **OAuth 2**  
   - Klicke **Generate access token**  
   - Kopiere das Token

4. **In `.env` Datei einfügen**  
   Falls die `.env` Datei noch nicht existiert, erstelle sie im Verzeichnis `bachelorthesis/Bachelorthesis`.

   Füge dann Folgendes in `bachelorthesis/Bachelorthesis/.env` ein:

   ```python
   ACCESS_TOKEN=<dein Dropbox Access Token>
   # Auf True setzen, wenn du Uploads zu Dropbox durchführen möchtest.  
   # Auf False setzen, wenn du die Ordner bereits hochgeladen hast oder nur Änderungen im Code testen möchtest.
   DROPBOX_UPLOAD=True
   ```

> Hinweis: Dropbox Tokens können zeitlich begrenzt sein. Erstelle bei Ablauf ein neues.

---

## App für Visualisierung starten

Navigiere in den Streamlit-Ordner und installiere die Abhängigkeiten:

```bash
cd /bachelorthesis/Bachelorthesis/streamlit
pip install -r requirements.txt  # oder manuell installieren
```

Dann die App generieren und starten:

```bash
python3 help.py                  # Generiert app.py basierend auf Daten aus Bachelorthesis/Server/images
streamlit run app.py             # Startet die Streamlit-App
```

Mit `Ctrl + C` kannst du den Streamlit-Server beenden.

---

## App für Umfrage starten

Navigiere in denselben Ordner und führe Folgendes aus:

```bash
cd /bachelorthesis/Bachelorthesis/streamlit
pip install -r requirements.txt  # oder manuell installieren
```

Generiere und starte die Umfrage-App:

```bash
python3 help_survey.py           # Generiert survey.py basierend auf Daten aus Bachelorthesis/Server/images
streamlit run survey.py          # Startet die Umfrage-App
```

Mit `Ctrl + C` kannst du den Streamlit-Server beenden.
