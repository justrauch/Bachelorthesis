# Diese Datei dient als Grundlage für eine Streamlit-App zur Visualisierung der Bildergebnisse,
# die im Image-Volume des Docker-Containers abgelegt wurden.

import os
import dropbox
import re
import requests
import io
from dotenv import load_dotenv
import numpy as np
from PyPDF2 import PdfReader, PdfWriter

# Laden der Umgebungsvariablen
load_dotenv()

# Zugriffstoken aus Umgebungsvariablen
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Lokaler Pfad zu den generierten Bildern
local_folder = "../Server/images"
# Zielpfad auf Dropbox
dropbox_path = "/images"

# Verbindung zu Dropbox initialisieren
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Listet Dateien und Ordner in einem bestimmten Dropbox-Pfad auf
def list_dropbox_folder(folder_path):
    url = "https://api.dropboxapi.com/2/files/list_folder"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"path": folder_path, "recursive": False}
    response = requests.post(url, headers=headers, json=data)
    # Wenn der Ordner nicht existiert, gib leere Liste zurück
    if response.json().get('error', {}).get('path', {}).get('.tag', "") == 'not_found':
        return []
    response.raise_for_status()
    return response.json().get("entries", [])

# Erstellt oder holt einen öffentlichen Freigabelink für eine Datei
def get_shared_link(path):
    url = "https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "path": path,
        "settings": {"requested_visibility": "public"}
    }
    response = requests.post(url, headers=headers, json=data)
    # Wenn Link bereits existiert, hole bestehenden
    if response.status_code == 409:
        return get_existing_shared_link(path)
    response.raise_for_status()
    return response.json()["url"].replace("dl=0", "dl=1")  # direkte Download-URL

# Holt bestehenden Freigabelink, falls vorhanden
def get_existing_shared_link(path):
    url = "https://api.dropboxapi.com/2/sharing/list_shared_links"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"path": path, "direct_only": True}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    links = response.json().get("links", [])
    if links:
        return links[0]["url"].replace("dl=0", "dl=1")
    return None

# Extrahiert strukturierte Textabschnitte basierend auf Keywords wie "Goal:" oder "Topic 1:"
def extract_text_sections(text):
    matches = list(re.finditer(r'(Goal:|Topic \d+:)', text))
    sections = [text[matches[i].start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                for i in range(len(matches))]
    return sections

# Löscht einen Ordner (rekursiv) in Dropbox
def delete_folder(folder_path):
    try:
        dbx.files_delete_v2(folder_path)
        print(f"Ordner {folder_path} erfolgreich gelöscht.")
    except Exception as e:
        print(f"Fehler beim Löschen: {e}")

# Lädt alle Dateien aus einem lokalen Ordner rekursiv in einen bestimmten Dropbox-Pfad hoch
def upload_folder(local_path, dropbox_path):
    for root, dirs, files in os.walk(local_path):
        print(root)
        for file in files:
            local_file = os.path.join(root, file)
            relative_path = os.path.relpath(local_file, local_path)
            dropbox_file = os.path.join(dropbox_path, relative_path).replace("\\", "/")

            with open(local_file, "rb") as f:
                print(f"Uploading {dropbox_file}")
                dbx.files_upload(f.read(), dropbox_file, mode=dropbox.files.WriteMode.overwrite)

# Dieser Block kann aktiviert werden, um gezielt Ordner zu löschen und neu hochzuladen
if False:
    delete_folder("/no_select_image")
    upload_folder("./keine-auswahl-Bild", "/no_select_image")
    delete_folder("/bsp/Bsp1")
    upload_folder("./bsp/Bsp1", "/bsp/Bsp1")
    delete_folder(f"{dropbox_path}/valid")
    upload_folder(f"{local_folder}/valid", f"{dropbox_path}/valid")
    delete_folder(f"{dropbox_path}/not_valid")
    upload_folder(f"{local_folder}/not_valid", f"{dropbox_path}/not_valid")

# Ruft die Links für das Platzhalterbild und die Option „Kein Bild ausgewählt“ ab
no_select_entry = list_dropbox_folder("/no_select_image")
link1 = get_shared_link(no_select_entry[0]["path_display"])
link2 = get_shared_link(no_select_entry[1]["path_display"])
image_link = link1 if "bad-sets-komponenten-keine-auswahl" in link1 else link2
placeholder_link = link2 if "bad-sets-komponenten-keine-auswahl" in link1 else link1

# Alle Bild-Links aus dem Beispiel-Ordner (Bsp1)
bsp1 = [get_shared_link(entry["path_display"]) for entry in list_dropbox_folder("/bsp/Bsp1")]
bsp1_choise = next((x for x in bsp1 if "Bsp1_Wahl" in x), None)
# Entferne das gewählte Bild aus der Liste, da es sonst zwei mal vorhanden ist
bsp1.remove(bsp1_choise)

intro_codezeilen = [
    "import streamlit as st",
    "from streamlit_image_select import image_select",
    "from streamlit_scroll_to_top import scroll_to_here",
    "import urllib.parse",
    "import uuid",
    "",

    # Initialisierung von Session-States zur Verwaltung von Zustand über Seitenwechsel hinweg
    "if \"email_count\" not in st.session_state:",
    "    st.session_state.email_count = 0",
    "",
    "if \"seite\" not in st.session_state:",
    "    st.session_state.seite = \"page1\"",
    "",
    "if \"auswahl\" not in st.session_state:",
    "   st.session_state.auswahl = {}",
    "",

    # Hilfsfunktion zur Navigation zwischen Seiten
    "def wechsel_zu(seite):",
    "    st.session_state.scroll_to_top = True",  # Bei Seitenwechsel: ganz nach oben scrollen
    "    st.session_state.seite = seite",
    "",

    # Reload-Zähler, um Cache-Umgehung für Bilder zu ermöglichen (über &nocache Parameter)
    "if \"reload_counter\" not in st.session_state:",
    "    st.session_state.reload_counter = 0",
    "",

    # Scroll-Verhalten initialisieren (wird durch 'wechsel_zu' gesetzt)
    "if 'scroll_to_top' not in st.session_state:",
    "    st.session_state.scroll_to_top = False",
    "",

    # Wenn Scroll-Flag gesetzt ist, nach oben scrollen und zurücksetzen
    "if st.session_state.scroll_to_top:",
    "    scroll_to_here(0, key='top')",
    "    st.session_state.scroll_to_top = False",
    "",

    # Hilfsfunktion, um das Scroll-Flag zu setzen (z. B. nach Button-Klick)
    "def scroll():",
    "    st.session_state.scroll_to_top = True",
    "",
]

with open("app.py", "w", encoding="utf-8") as f:
    # Einleitungscode
    for zeile in intro_codezeilen:
        print(zeile, file=f)

    # Zähle, wie viele Unterordner im Valid-Ordner vorhanden sind
    unterordner_anzahl = len([
        d for d in os.listdir(f"{local_folder}/valid") 
        if os.path.isdir(os.path.join(f"{local_folder}/valid", d))
    ])

    # Durchlaufe alle Unterverzeichnisse in valid/, jedes steht für eine eigene Seite
    for index, (root, dirs, files) in enumerate(os.walk(f"{local_folder}/valid")):
        if root == f"{local_folder}/valid":
            continue  # Überspringe das Wurzelverzeichnis selbst

        print(root)

        # Hole die Einträge  aus valid/ und not_valid/
        entries = list_dropbox_folder(f'/images/valid/{os.path.relpath(root, f"{local_folder}/valid")}'.replace("\\", "/"))
        not_valid_entries = list_dropbox_folder(f'/images/not_valid/{os.path.relpath(root, f"{local_folder}/valid")}'.replace("\\", "/"))

        ret = []              # Liste gültiger Bild-Links
        not_valid_ret = []    # Liste ungültiger Bild-Links
        pdf_link = ""         # Link zur zugehörigen PDF-Datei

        # Extrahiere Links zu PDF und Bildern
        for entry in entries:
            if entry[".tag"] == "file":
                try:
                    link = get_shared_link(entry["path_display"])
                    if entry["name"].lower().endswith(".pdf"):
                        pdf_link = link
                    elif link:
                        ret.append(link)
                except Exception as e:
                    print(f"Fehler bei {entry['path_display']}: {e}")

        if pdf_link == "":
            continue  # Keine PDF gefunden → Seite überspringen

        # Extrahiere die "nicht validen" Bilder
        for entry in not_valid_entries:
            if entry[".tag"] == "file":
                try:
                    link = get_shared_link(entry["path_display"])
                    if link:
                        not_valid_ret.append(link)
                except Exception as e:
                    print(f"Fehler bei {entry['path_display']}: {e}")

        # Lade und analysiere die PDF-Datei
        response = requests.get(pdf_link)
        response.raise_for_status()
        pdf_bytes = io.BytesIO(response.content)
        reader = PdfReader(pdf_bytes)
        subject = reader.metadata.get("/Subject", "Kein Betreff gefunden")
        subjects = extract_text_sections(subject)

        # Beginn des Seitenblocks in Streamlit
        print(f'if st.session_state.seite == "page{index}":', file=f)
        print(f'    st.title("Seite {index}")', file=f)
        print("", file=f)

        # Hinweis zur Anzeige und Button zum Neuladen
        print(f'    pdf_url = "{pdf_link.replace("dl=1", "dl=0")}"', file=f)
        print('    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."', file=f)
        print('        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")', file=f)
        print("    if st.button(\"Neuladen\"):", file=f)
        print("        st.session_state.reload_counter += 1", file=f)
        print("        st.rerun()", file=f)

        # Verlinkung zur zugehörigen PDF-Datei
        print('    st.markdown(f\'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>\', unsafe_allow_html=True)', file=f)

        # Thementext aus dem Subject anzeigen
        print(f'    st.text({repr(subjects[0].split("Illustrated by:")[0])})', file=f)
        print("", file=f)

        # Für jeden Abschnitt im PDF (z. B. Topic 1, Topic 2, ...) Bildauswahl und Text anzeigen
        for i in range(1, len(subjects)):
            print(f'    st.text("{104*"-"}")', file=f)  # Trennlinie
            splits = subjects[i].split("Illustrated by:")
            print(f'    st.text({repr(splits[0])})', file=f)

            # Vom Modell gewähltes Bild und dessen Beschreibung
            tmp_ret_choice = [link for link in ret if f"Section{i}_choice" in link]
            if len(splits) > 1:
                print(f'    st.image("{tmp_ret_choice[0]}" + f"&nocache={{st.session_state.reload_counter}}")', file=f)
                print(f'    st.text({repr(splits[1])})', file=f)
            print("", file=f)

            # Auswahl möglicher valider Bilder
            tmp_ret = [link for link in ret if f"Section{i}" in link and f"Section{i}_choice" not in link]
            if len(tmp_ret) >= 1:
                print(f'    tmp{index}{i} = [', file=f)
                for link in tmp_ret:
                    print(f'        "{link}",', file=f)
                print('    ]', file=f)

                # Bildauswahl-tool für valide Bilder
                print(f'    img{index}{i} = image_select(', file=f)
                print('        "Mögliche Valide Bilder:",', file=f)
                print(f'        tmp{index}{i},', file=f)
                print('        return_value="index",', file=f)
                print(f'        index=st.session_state.auswahl.get("Seite {index} Thema {i}", 0),', file=f)
                print(f'        key=f"frage{index}{i}_{{st.session_state.reload_counter}}"', file=f)
                print('    )', file=f)

                # Auswahl merken und Bild anzeigen
                print(f'    st.session_state.auswahl["Seite {index} Thema {i}"] = img{index}{i}', file=f)
                print(f'    st.image(tmp{index}{i}[st.session_state.auswahl.get("Seite {index} Thema {i}", 0)] + f"&nocache={{st.session_state.reload_counter}}")', file=f)

            # Auswahl für nicht valide Bilder
            tmp_not_valid_ret = [link for link in not_valid_ret if f"Section{i}" in link]
            if len(tmp_not_valid_ret) >= 1:
                print("", file=f)
                print(f'    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")', file=f)
                print("", file=f)

                print(f'    nvtmp{index}{i} = [', file=f)
                for link in tmp_not_valid_ret:
                    print(f'        "{link}",', file=f)
                print('    ]', file=f)

                # Bildauswahl für nicht valide Bilder
                print(f'    nvimg{index}{i} = image_select(', file=f)
                print('        "Nicht Valide Bilder:",', file=f)
                print(f'        nvtmp{index}{i},', file=f)
                print('        return_value="index",', file=f)
                print(f'        index=st.session_state.auswahl.get("nv Seite {index} Thema {i}", 0),', file=f)
                print(f'        key=f"nvfrage{index}{i}_{{st.session_state.reload_counter}}"', file=f)
                print('    )', file=f)

                # Auswahl speichern und Bild anzeigen
                print(f'    st.write(f"Du hast Bild Nr. {{nvimg{index}{i}}} ausgewählt.")', file=f)
                print(f'    st.session_state.auswahl["nv Seite {index} Thema {i}"] = nvimg{index}{i}', file=f)

                # Anzeige des gewählten Bildes
                print(f'    st.image(nvtmp{index}{i}[st.session_state.auswahl.get("nv Seite {index} Thema {i}", 0)] + f"&nocache={{st.session_state.reload_counter}}")', file=f)
                print("", file=f)

        # Weiter-Button zur nächsten Seite, falls vorhanden
        if index < unterordner_anzahl:
            print(f'    st.button("(Nachfolgende) Seite {index + 1}", on_click=lambda: wechsel_zu("page{index + 1}"))', file=f)
            print("", file=f)

        # Generiere Auswahl-Buttons für alle anderen Seiten in Gruppen (je 6 Buttons pro Zeile)
        zahlen = [i for i in range(1, unterordner_anzahl + 1) if i not in (index, index + 1)]
        gruppen = [zahlen[i:i + 6] for i in range(0, len(zahlen), 6)]
        for gruppe in gruppen:
            print("    with st.container():", file=f)
            print("        cols = st.columns([2] * 6)", file=f)
            print(f"        fragen = {gruppe}", file=f)
            print("        for i, frage in enumerate(fragen):", file=f)
            print('            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))', file=f)
            print("", file=f)

        # Button zum Scrollen ganz nach oben
        print(f'    st.button("Nach oben scrollen", on_click=scroll)', file=f)
        print("", file=f)
