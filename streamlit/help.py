import os
import dropbox
import re
import requests
import io
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
    if response.json().get('error', {}).get('path', {}).get('.tag', "") == 'not_found':
        return []
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
    matches = list(re.finditer(r'(Goal:|Topic \d+:)', text))
    sections = [text[matches[i].start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                for i in range(len(matches))]
    return sections

def delete_folder(folder_path):
    try:
        dbx.files_delete_v2(folder_path)
        print(f"Ordner {folder_path} erfolgreich gelöscht.")
    except Exception as e:
        print(f"Fehler beim Löschen: {e}")

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

if False:
    delete_folder("/no_select_image")
    upload_folder("./keine-auswahl-Bild", "/no_select_image")
    delete_folder("/bsp/Bsp1")
    upload_folder("./bsp/Bsp1", "/bsp/Bsp1")
    #delete_folder("/bsp/Bsp2")
    #upload_folder("./bsp/Bsp2", "/bsp/Bsp2")
    delete_folder(f"{dropbox_path}/valid")
    upload_folder(f"{local_folder}/valid", f"{dropbox_path}/valid")
    delete_folder(f"{dropbox_path}/not_valid")
    upload_folder(f"{local_folder}/not_valid", f"{dropbox_path}/not_valid")

no_select_entry = list_dropbox_folder("/no_select_image")
link1 = get_shared_link(no_select_entry[0]["path_display"])
link2 = get_shared_link(no_select_entry[1]["path_display"])
image_link = link1 if "bad-sets-komponenten-keine-auswahl" in link1 else link2
placeholder_link = link2 if "bad-sets-komponenten-keine-auswahl" in link1 else link1
bsp1 = [get_shared_link(entry["path_display"]) for entry in list_dropbox_folder("/bsp/Bsp1")]
bsp1_choise = next((x for x in bsp1 if "Bsp1_Wahl" in x), None)
bsp1.remove(bsp1_choise)
#bsp2 = [get_shared_link(entry["path_display"]) for entry in list_dropbox_folder("/bsp/Bsp2")]
#bsp2_choise = next((x for x in bsp2 if "Bsp2_Wahl" in x), None)
#bsp2.remove(bsp2_choise)

intro_codezeilen = [
    "import streamlit as st",
    "from streamlit_image_select import image_select",
    "from streamlit_scroll_to_top import scroll_to_here",
    "import urllib.parse",
    "import uuid",
    "",
    "if \"email_count\" not in st.session_state:",
    "    st.session_state.email_count = 0",
    "",
    "if \"seite\" not in st.session_state:",
    "    st.session_state.seite = \"page1\"",
    "",
    "if \"auswahl\" not in st.session_state:",
    "   st.session_state.auswahl = {}",
    "",
    "def wechsel_zu(seite):",
    "    st.session_state.scroll_to_top = True",
    "    st.session_state.seite = seite",
    "",
    "if \"reload_counter\" not in st.session_state:",
    "    st.session_state.reload_counter = 0",
    "",
    "if 'scroll_to_top' not in st.session_state:",
    "    st.session_state.scroll_to_top = False",
    "",
    "if st.session_state.scroll_to_top:",
    "    scroll_to_here(0, key='top')",
    "    st.session_state.scroll_to_top = False",
    "",
    "def scroll():",
    "    st.session_state.scroll_to_top = True",
    "",
]


with open("app.py", "w", encoding="utf-8") as f:
    for zeile in intro_codezeilen:
        print(zeile, file=f)

    unterordner_anzahl = len([d for d in os.listdir(f"{local_folder}/valid") if os.path.isdir(os.path.join(f"{local_folder}/valid", d))])

    for index, (root, dirs, files) in enumerate(os.walk(f"{local_folder}/valid")):
        if root == f"{local_folder}/valid":
            continue

        print(root)

        entries = list_dropbox_folder(f'/images/valid/{os.path.relpath(root, f"{local_folder}/valid")}'.replace("\\", "/"))
        not_valid_entries = list_dropbox_folder(f'/images/not_valid/{os.path.relpath(root, f"{local_folder}/valid")}'.replace("\\", "/"))
        ret = []
        not_valid_ret = []
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

        for entry in not_valid_entries:
            if entry[".tag"] == "file":
                try:
                    link = get_shared_link(entry["path_display"])
                    if link:
                        not_valid_ret.append(link)
                except Exception as e:
                    print(f"Fehler bei {entry['path_display']}: {e}")

        response = requests.get(pdf_link)
        response.raise_for_status()
        pdf_bytes = io.BytesIO(response.content)
        reader = PdfReader(pdf_bytes)
        subject = reader.metadata.get("/Subject", "Kein Betreff gefunden")
        subjects = extract_text_sections(subject)

        print(f'if st.session_state.seite == "page{index}":', file=f)
        print(f'    st.title("Seite {index}")', file=f)
        print("", file=f)
        print(f'    pdf_url = "{pdf_link.replace("dl=1", "dl=0")}"', file=f)
        print('    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."', file=f)
        print('        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")', file=f)
        print("    if st.button(\"Neuladen\"):", file=f)
        print("        st.session_state.reload_counter += 1", file=f)
        print("        st.rerun()", file=f)
        print('    st.markdown(f\'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>\', unsafe_allow_html=True)', file=f)
        print(f'    st.text({repr(subjects[0].split("Illustrated by:")[0])})', file=f)
        print("", file=f)

        for i in range(1, len(subjects)):
            print(f'    st.text("{104*"-"}")', file=f)
            splits = subjects[i].split("Illustrated by:")
            print(f'    st.text({repr(splits[0])})', file=f)
            tmp_ret_choice = [link for link in ret if f"Section{i}_choice" in link]
            if len(splits) > 1:
                print(f'    choice{index}{i}_arr = [', file=f)
                print(f'        "{tmp_ret_choice[0]}",', file=f)
                print(f'        "{image_link}",', file=f)
                print(f'    ]', file=f)
                print(f'    choice{index}{i}_tmp = st.session_state.reload_counter % 2', file=f)
                print(f'    if choice{index}{i}_tmp == 0:', file=f)
                print(f'        st.image(choice{index}{i}_arr[0 if choice{index}{i}_tmp == 0 else 1])', file=f)
                print(f'    else:', file=f)
                print(f'        st.image(choice{index}{i}_arr[0 if choice{index}{i}_tmp == 1 else 1])', file=f)
                print(f'    st.text({repr(splits[1])})', file=f)
            print("", file=f)
            
            tmp_ret = [link for link in ret if f"Section{i}" in link and f"Section{i}_choice" not in link]

            if len(tmp_ret) >= 1:
                print(f'    tmp{index}{i} = [', file=f)
                count = 0
                for link in tmp_ret:
                        count += 1
                        print(f'        "{link}",', file=f)
                print('    ]', file=f)
                print(f'    img{index}{i} = image_select(', file=f)
                print('        "Mögliche Valide Bilder:",', file=f)
                print(f'        tmp{index}{i},', file=f)
                print('        return_value="index",', file=f)
                print(f'        index=st.session_state.auswahl.get("Seite {index} Thema {i}", 0),', file=f)
                print(f'        key=f"frage{index}{i}_{{st.session_state.reload_counter}}"', file=f)
                print('    )', file=f)
                print(f'    st.session_state.auswahl["Seite {index} Thema {i}"] = img{index}{i}', file=f)
                print(f'    valid{index}{i}_tmp = st.session_state.reload_counter % 2', file=f)
                print(f'    if valid{index}{i}_tmp == 0:', file=f)
                print(f'        st.image(tmp{index}{i}[st.session_state.auswahl.get("Seite {index} Thema {i}", 0)] if valid{index}{i}_tmp == 0 else "{image_link}")', file=f)
                print(f'    else:', file=f)
                print(f'        st.image(tmp{index}{i}[st.session_state.auswahl.get("Seite {index} Thema {i}", 0)] if valid{index}{i}_tmp == 1 else "{image_link}")', file=f)
        

  
            tmp_not_valid_ret = [link for link in not_valid_ret if f"Section{i}" in link]

            if len(tmp_not_valid_ret) >= 1:
                print("", file=f)
                print(f'    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")', file=f)
                print("", file=f)
                print(f'    nvtmp{index}{i} = [', file=f)

                for link in tmp_not_valid_ret:
                    if f"Section{i}" in link:
                        count += 1
                        print(f'        "{link}",', file=f)
            
                print('    ]', file=f)
                print(f'    nvimg{index}{i} = image_select(', file=f)
                print('        "Nicht Valide Bilder:",', file=f)
                print(f'        nvtmp{index}{i},', file=f)
                print('        return_value="index",', file=f)
                print(f'        index=st.session_state.auswahl.get("nv Seite {index} Thema {i}", 0),', file=f)
                print(f'        key=f"nvfrage{index}{i}_{{st.session_state.reload_counter}}"', file=f)
                print('    )', file=f)
                print(f'    st.write(f"Du hast Bild Nr. {{nvimg{index}{i}}} ausgewählt.")', file=f)
                print(f'    st.session_state.auswahl["nv Seite {index} Thema {i}"] = nvimg{index}{i}', file=f)
                print(f'    nvalid{index}{i}_tmp = st.session_state.reload_counter % 2', file=f)
                print(f'    if nvalid{index}{i}_tmp == 0:', file=f)
                print(f'        st.image(nvtmp{index}{i}[st.session_state.auswahl.get("nv Seite {index} Thema {i}", 0)] if nvalid{index}{i}_tmp == 0 else "{image_link}")', file=f)
                print(f'    else:', file=f)
                print(f'        st.image(nvtmp{index}{i}[st.session_state.auswahl.get("nv Seite {index} Thema {i}", 0)] if nvalid{index}{i}_tmp == 1 else "{image_link}")', file=f)
                print("", file=f)


        if index < unterordner_anzahl:
            print(f'    st.button("(Nachfolgende) Seite {index + 1}", on_click=lambda: wechsel_zu("page{index + 1}"))', file=f)
            print("", file=f)

        x = index
        y = index + 1
        n = unterordner_anzahl

        zahlen = [i for i in range(1, n + 1) if i not in (x, y)]

        gruppen = [zahlen[i:i + 6] for i in range(0, len(zahlen), 6)]

        for gruppe in gruppen:
                print("    with st.container():", file=f)
                print("        cols = st.columns([2] * 6)", file=f)
                print(f"        fragen = {gruppe}", file=f)
                print("        for i, frage in enumerate(fragen):", file=f)
                print('            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))', file=f)
                print("", file=f)

        print(f'    st.button("Nach oben scrollen", on_click=scroll)', file=f)
        print("", file=f)