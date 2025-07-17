import os
import dropbox
import re
import requests
import io
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import numpy as np

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
    "    st.session_state.seite = \"start\"",
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
    "text = (",
    '    "The following pages will each present a short text along with an image that includes a textual description.\\n"',
    '    "You will first be asked whether this description meaningfully supports the topic, or if the image visually illustrates it well enough to be worth mentioning.\\n"',
    '    "This is followed by one or two tasks where you choose between multiple images.\\n"',
    '    "If you believe any of these new images better support the description or topic, please select it. "',
    '    "If none of the options seem appropriate, select the first image (index 0).\\n"',
    '    "Please note: the descriptions are generated by an AI model, which may not reliably recognize people or buildings. "',
    '    "Famous landmarks like the Eiffel Tower may be correctly identified, but regional or less-known locations often are not."',
    ")",
    "",
    'if st.session_state.seite == "start":',
    '    st.title("Explanation")',
    '',
    '    st.text("If the images are not displayed, please wait about 10 seconds and then click the “Reload” button. "',
    '        "Important: Do not reload the browser, otherwise all previous selections will be lost!")',
    "    if st.button(\"Reload\"):",
    "        st.session_state.reload_counter += 1",
    "        st.rerun()",
    "",
    '    st.markdown("## Example 1")',
    '    st.text(',
    '        "The following shows you some examples that illustrate "',
    '        "how a selection can be made. "',
    '        "These are only examples – no selection is required here."',
    '    )',
    '    st.text(',
    '        "Habitat of Zebras\\n"',
    '        "Zebras typically live in open savannahs and grasslands of Africa. An important component\\n"',
    '        "of their habitat are waterholes, which they regularly visit in groups. It can be observed\\n"',
    '        "that zebras often drink together to protect each other from potential predators."'
    '    )',
    '',
    '    img63 = image_select(',
    '        "Selection:",',
    '        [',
    f'            "{image_link}",',
    f'            "{bsp1[0]}",',
    f'            "{bsp1[1]}",',
    f'            "{bsp1_choise}",',
    '        ],',
    '        return_value="index",',
    '        index=0,',
    '        key=f"bsp_1_{st.session_state.reload_counter}"',
    '    )',
    '',
    '    st.text("Good choice:")',
    '    bsp1_arr = [',
    f'        "{bsp1_choise}",',
    f'        "{image_link}",',
    '    ]',
    '    bsp1_tmp = st.session_state.reload_counter % 2',
    '    if bsp1_tmp == 0:',
    '        st.image(bsp1_arr[0 if bsp1_tmp == 0 else 1])',
    '    else:',
    '        st.image(bsp1_arr[0 if bsp1_tmp == 1 else 1])',
    '    st.text("This is the description for the image above:")',
    '    st.text("Four zebras stand at the edge of a watering hole, with three of them drinking while their reflections are clearly visible in the calm water. The scene is set against a backdrop of dry grass and warm sunlight, evoking the African savanna.")',
    "",
    '    st.text('
    '       "Selection No. 4 is appropriate because the image very well illustrates the scene described in the text,\\n"',
    '       "in which several zebras drink together at a waterhole. It supports the depiction of the zebras\\n"',
    '       "typical habitat and highlights their social behavior while drinking.\\n"',
    '       "Image No. 3 fits the described scene less well because it shows zebras in motion rather than drinking.\\n"',
    '       "If selection No. 4 were not available, the best choice would be to select none of the shown images.\\n"',
    '    )',
    '',
    '    st.button(f"Page 1", on_click=lambda s=f"page1": wechsel_zu(s))',
    '    st.button("Results", on_click=lambda: wechsel_zu("auswertung"))',
    '    st.button("Scroll to top", on_click=scroll())'
]

use = {
    "40410000": [4],
    "Probe345Bd93": [1, 3],
    "Menschenaffen_Unterrichtsmaterial": [2],
    "Broschuere_2013_hires": [1],
    "bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All": [1]
}

len_use = np.sum([len(y) for (x, y) in use.items()])

with open("survey.py", "w", encoding="utf-8") as f:
    for zeile in intro_codezeilen:
        print(zeile, file=f)

    #unterordner_anzahl = len([d for d in os.listdir(f"{local_folder}/valid") if os.path.isdir(os.path.join(f"{local_folder}/valid", d))])

    index = 0
    for (root, dirs, files) in os.walk(f"{local_folder}/valid"):
        if root == f"{local_folder}/valid":
            continue

        if len(use.get(root.split("/")[-1], [])) <= 0:
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

        for i in use.get(root.split("/")[-1], []):
            index += 1

            print(f'if st.session_state.seite == "page{index}":', file=f)
            print(f'    st.title("Page {index}")', file=f)
            print('    st.text(text)', file=f)
            print("", file=f)
            print(f'    pdf_url = "{pdf_link.replace("dl=1", "dl=0")}"', file=f)
            print('    st.text("If the images are not displayed, please wait about 10 seconds and then click the \'Reload\' button."', file=f)
            print('        "Important: Do not reload the browser, otherwise all previous selections will be lost!")', file=f)
            print("    if st.button(\"Reload\"):", file=f)
            print("        st.session_state.reload_counter += 1", file=f)
            print("        st.rerun()", file=f)
            print(f'    st.text({repr(subjects[0].split("Illustrated by:")[0])})', file=f)
            print("", file=f)

            splits = subjects[i].split("Illustrated by:")
            print(f'    st.markdown("## Question 1") ',file=f)
            print(f'    st.text({repr(splits[0].split(":")[1])})', file=f)
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
                print(f'    st.text("This is the description for the image above:")', file=f)
                print(f'    st.text({repr(splits[1])})', file=f)
                print("    st.markdown(", file=f)
                print("        \"<div style='font-size:18px; font-weight:bold;'>Does the description support the text when added with 'illustrated by', or is the image visually relevant enough to be mentioned on its own?</div>\",", file=f)
                print("        unsafe_allow_html=True", file=f)
                print("    )", file=f)
                print(f"    antwort{index}{i} = st.radio(", file=f)
                print("         \"\",", file=f)
                print("         [", file=f)
                print("             \"Yes – the description supports the topic and the image illustrates it well\",", file=f)
                print("             \"No – neither the description nor the image match the topic\",", file=f)
                print("             \"No – the description doesn't fit, but the image itself is interesting or relevant\"", file=f)
                print("         ],", file=f)
                print(f"         key=\"antwort{index}{i}\",", file=f)
                print(f"         label_visibility=\"collapsed\"", file=f)
                print("     )", file=f)
                print(f'    st.session_state.auswahl["Page {index} Question 1"] = antwort{index}{i}', file=f)
            print("", file=f)
            
            tmp_ret = [link for link in ret if f"Section{i}" in link and f"Section{i}_choice" not in link]

            if len(tmp_ret) >= 1:
                print(f'    st.markdown("## Question 2") ', file=f)
                print(f'    st.text("Think of each image as a one- or two-sentence visual description. As in Question 1, would any of these descriptions fit the text if introduced with \'illustrated by\'? If none of the images are appropriate, select the first one (index 0).") ', file=f)
                print(f'    tmp{index}{i} = [', file=f)
                print(f'        "{image_link}",', file=f)
                count = 0
                for link in tmp_ret:
                        count += 1
                        print(f'        "{link}",', file=f)
                
                fill = (4 - (count + 1) % 4) % 4
                for idx in range(fill):
                    print(f'        "{placeholder_link}",', file=f)

                print('    ]', file=f)
                print(f'    img{index}{i} = image_select(', file=f)
                print('        "Select the most appropriate image:",', file=f)
                print(f'        tmp{index}{i},', file=f)
                print('        return_value="index",', file=f)
                print(f'        index=st.session_state.auswahl.get("Page {index} Question 2", 0),', file=f)
                print(f'        key=f"frage{index}{i}_{{st.session_state.reload_counter}}"', file=f)
                print('    )', file=f)
                print(f'    st.session_state.auswahl["Page {index} Question 2"] = img{index}{i}', file=f)
                print(f'    valid{index}{i}_tmp = st.session_state.reload_counter % 2', file=f)
                print(f'    if valid{index}{i}_tmp == 0:', file=f)
                print(f'        st.image(tmp{index}{i}[st.session_state.auswahl.get("Page {index} Question 2", 0)] if valid{index}{i}_tmp == 0 else "{image_link}")', file=f)
                print(f'    else:', file=f)
                print(f'        st.image(tmp{index}{i}[st.session_state.auswahl.get("Page {index} Question 2", 0)] if valid{index}{i}_tmp == 1 else "{image_link}")', file=f)
                print(f'    st.text_input("Selected image", value=st.session_state.auswahl["Page {index} Question 2"], key="wv{index}{i}", disabled=True)', file=f)
            
            print(f"    st.markdown('## Comment on Page {index}')", file=f)
            print(f"    if 'Page {index} comments' not in st.session_state.auswahl:", file=f)
            print(f"        st.session_state.auswahl['Page {index} comments'] = ''", file=f)
            print(f"    st.session_state.auswahl['Page {index} comments'] = st.text_input(", file=f)
            print("        'Please provide a short justification for your choice (ideally in German):',", file=f)
            print(f"        value=st.session_state.auswahl['Page {index} comments']", file=f)
            print("    )", file=f)
            print('    st.text("You can now continue to the next question, view an explanation, or go to the results page.")', file=f)
            if index < len_use:
                print(f'    st.button("(Next) Page {index + 1}", on_click=lambda: wechsel_zu("page{index + 1}"))', file=f)
                print("", file=f)

            x = index
            y = index + 1
            n = len_use

            zahlen = [i for i in range(1, n + 1) if i not in (x, y)]

            gruppen = [zahlen[i:i + 6] for i in range(0, len(zahlen), 6)]

            for gruppe in gruppen:
                    print("    with st.container():", file=f)
                    print("        cols = st.columns([2] * 6)", file=f)
                    print(f"        fragen = {gruppe}", file=f)
                    print("        for i, frage in enumerate(fragen):", file=f)
                    print('            cols[i].button(f"Page {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))', file=f)
                    print("", file=f)

            print(f'    st.button("Results", on_click=lambda: wechsel_zu("auswertung"))', file=f)
            print("", file=f)
            print(f'    st.button("Explanation", on_click=lambda: wechsel_zu("start"))', file=f)
            print("", file=f)
            print(f'    st.button("Scroll to top", on_click=scroll)', file=f)
            print("", file=f)
            #break

    auswertung_codezeilen = [
        "elif st.session_state.seite == \"auswertung\":",
        "    st.title(\"Evaluation\")",
        "    st.write(\"You have selected the following images:\")",
        "",
        "    auswertung_text = \"\"",
        "",
        "    for key, value in sorted(st.session_state.auswahl.items()):",
        "        auswertung_text += f\"{key} → {value}\\n\"",
        "",
        "    st.text(auswertung_text.strip())",
        "",
        "    encoded_body = urllib.parse.quote(auswertung_text)",
        "    mailto_link = f\"mailto:jstrauch@pagemachine.de?subject=Image Survey&body={encoded_body}\"",
        "",
        "    if st.button(\"Send results via email\"):",
        "        dummy_id = uuid.uuid4()",
        "        js_code = f\"\"\"",
        "        const dummy = \\\"{dummy_id}\\\";",
        "        window.open(\\\"{mailto_link}\\\");",
        "        \"\"\"",
        "        st.components.v1.html(f\"<script>{js_code}</script>\", height=0)",
        "",
        '    st.text("If no email window opens after clicking the button, please enable pop-ups for this page in your browser. Alternatively, you can copy the results or take a screenshot and send them via email to jstrauch@pagemachine.de. Thank you!")',
        "",
        "    st.button(\"Modify\", on_click=lambda: wechsel_zu(\"start\"))"
    ]

    for zeile in auswertung_codezeilen:
        print(zeile, file=f)