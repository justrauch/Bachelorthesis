import os
import dropbox
import re
import requests
import io
from PyPDF2 import PdfReader

ACCESS_TOKEN = ""

dropbox_upload = False

local_folder = "../Server/images"
dropbox_path = "/images"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

def list_dropbox_folder(folder_path):
    url = "https://api.dropboxapi.com/2/files/list_folder"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"path": folder_path, "recursive": False}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("entries", [])

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
    if response.status_code == 409:
        return get_existing_shared_link(path)
    response.raise_for_status()
    return response.json()["url"].replace("dl=0", "dl=1")

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

def extract_text_sections(text):
    matches = list(re.finditer(r'(Ziel:|Thema \d+:)', text))
    sections = [text[matches[i].start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                for i in range(len(matches))]
    return sections

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

if dropbox_upload:
    upload_folder("./keine-auswahl-Bild", "/no_select_image")
    upload_folder(local_folder, dropbox_path)

no_select_entry = list_dropbox_folder("/no_select_image")
image_link = get_shared_link(no_select_entry[0]["path_display"])

intro_codezeilen = [
    'import streamlit as st',
    'from streamlit_image_select import image_select',
    'import urllib.parse',
    '',
    'if "seite" not in st.session_state:',
    '    st.session_state.seite = "page1"',
    '',
    'if "auswahl" not in st.session_state:',
    '   st.session_state.auswahl = {}',
    '',
    'def wechsel_zu(seite):',
    '    st.session_state.seite = seite',
    '',
    'text = (',
    '    "Nachfolgend werden verschiedene Beschreibungen von PDFs angezeigt. "',
    '    "Jede Beschreibung besteht aus mehreren Themen. "',
    '    "Zu jedem Thema werden mehrere Bilder angezeigt. "',
    '    "Wähle das Bild aus, das deiner Meinung nach am besten zum jeweiligen Thema passt, "',
    '    "indem du es anklickst. "',
    '    "Falls keines der Bilder passt, wähle das erste Bild (Bild 0) als Platzhalter."',
    ')',
    '',
]

with open("app.py", "w", encoding="utf-8") as f:
    for zeile in intro_codezeilen:
        print(zeile, file=f)

    unterordner_anzahl = len([d for d in os.listdir(local_folder) if os.path.isdir(os.path.join(local_folder, d))])

    for index, (root, dirs, files) in enumerate(os.walk(local_folder)):
        if root == local_folder:
            continue

        print(root)

        FOLDER_PATH = f'/images/{os.path.relpath(root, local_folder)}'.replace("\\", "/")
        entries = list_dropbox_folder(FOLDER_PATH)
        ret = []
        pdf_link = ""

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
            continue

        response = requests.get(pdf_link)
        response.raise_for_status()
        pdf_bytes = io.BytesIO(response.content)
        reader = PdfReader(pdf_bytes)
        subject = reader.metadata.get("/Subject", "Kein Betreff gefunden")
        subjects = extract_text_sections(subject)

        print(f'if st.session_state.seite == "page{index}":', file=f)
        print(f'    st.title("Frage {index}")', file=f)
        print('    st.text(text)', file=f)
        print("", file=f)
        print(f'    pdf_url = "{pdf_link.replace("dl=1", "dl=0")}"', file=f)
        print('    st.markdown(f\'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>\', unsafe_allow_html=True)', file=f)
        print(f'    st.text({repr(subjects[0].split("Dargestellt durch:")[0])})', file=f)
        print("", file=f)

        for i in range(1, len(subjects)):
            print(f'    st.text({repr(subjects[i].split("Dargestellt durch:")[0])})', file=f)
            print("", file=f)
            print(f'    img{index}{i} = image_select(', file=f)
            print('        "Label",', file=f)
            print('        [', file=f)
            print(f'            "{image_link}",', file=f)
            for link in ret:
                if f"Section{i}" in link:
                    print(f'            "{link}",', file=f)
            print('        ],', file=f)
            print('        return_value="index",', file=f)
            print('        index=0,', file=f)
            print(f'        key="frage{index}{i}"', file=f)
            print('    )', file=f)
            print(f'    st.write(f"Du hast Bild Nr. {{img{index}{i}}} ausgewählt.")', file=f)
            print(f'    st.session_state.auswahl["Frage {index} Thema {i}"] = img{index}{i}', file=f)
            print("", file=f)

        if index == unterordner_anzahl:
            print(f'    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))', file=f)
        else:
            print(f'    st.button("Weiter zu Frage {index + 1}", on_click=lambda: wechsel_zu("page{index + 1}"))', file=f)
        print("", file=f)

    auswertung_codezeilen = [
        'elif st.session_state.seite == "auswertung":',
        '    st.title("Auswertung")',
        '    st.write("Du hast diese Bilder gewählt:")',
        '',
        '    auswertung_text = ""',
        '    letzte_frage = ""',
        '',
        '    for key, value in sorted(st.session_state.auswahl.items()):',
        '        frage, thema = key.split(" Thema ")',
        '        if frage != letzte_frage:',
        '            auswertung_text += f"\\n{frage}:\\n"',
        '            letzte_frage = frage',
        '        auswertung_text += f"  Thema {thema} → Bild {value}\\n"',
        '',
        '    st.text(auswertung_text.strip())',
        '',
        '    encoded_body = urllib.parse.quote(auswertung_text)',
        '    mailto_link = f"mailto:jstrauch@pagemachine.de?subject=Bilder-Umfrage&body={encoded_body}"',
        '',
        '    st.markdown(f"[Ergebnis per E-Mail senden]({mailto_link})", unsafe_allow_html=True)',
        '',
        '    st.button("Ändern", on_click=lambda: wechsel_zu("page1"))',
    ]

    for zeile in auswertung_codezeilen:
        print(zeile, file=f)