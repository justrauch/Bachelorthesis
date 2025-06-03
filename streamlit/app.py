import streamlit as st
from streamlit_image_select import image_select
from streamlit_scroll_to_top import scroll_to_here
import urllib.parse
import uuid

if "email_count" not in st.session_state:
    st.session_state.email_count = 0

st.session_state._back_to = "page1"
if "seite" not in st.session_state:
    st.session_state.seite = "page1"

if "auswahl" not in st.session_state:
   st.session_state.auswahl = {}

def wechsel_zu(seite):
    st.session_state.seite = seite

if "reload_counter" not in st.session_state:
    st.session_state.reload_counter = 0

if 'scroll_to_top' not in st.session_state:
    st.session_state.scroll_to_top = False

if st.session_state.scroll_to_top:
    scroll_to_here(0, key='top')
    st.session_state.scroll_to_top = False

def scroll():
    st.session_state.scroll_to_top = True

text = (
    "Nachfolgend werden verschiedene Beschreibungen von PDFs angezeigt. "
    "Jede Beschreibung besteht aus mehreren Themen. "
    "Zu jedem Thema werden mehrere Bilder angezeigt. "
    "Wähle das Bild aus, das deiner Meinung nach am besten zum jeweiligen Thema passt, "
    "indem du es anklickst. "
    "Falls keines der Bilder passt, wähle das erste Bild (Bild 0) als Platzhalter."
)
if st.session_state.seite == "page1":
    st.title("Frage 1")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/p60uobn5chib8bqls9lwn/40410000.pdf?rlkey=qwhxfmxs9n4uefprh53yxqsow&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Informieren über die Aufgaben, Organe und Bauten des deutschen Bundestages in der 20. Wahlperiode.')

    st.text('Thema 1: Aufgaben des Bundestages\n- Der Bundestag ist das einzige Staatsorgan, das direkt vom Volk gewählt wird und hat die Rolle des Gesetzgebers.\n\n')

    img11 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/q90hr6ae4gvgdknj1sxbg/Section1_Bild0.png?rlkey=62zxbxajvva1t1urvipdog2ke&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 1 Thema 1", 0),
        key=f"frage11_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img11} ausgewählt.")
    st.session_state.auswahl["Frage 1 Thema 1"] = img11

    st.text('Thema 2: Der Bundestag wählt den Bundeskanzler\n- Der Bundeskanzler wird durch die Abgeordneten des Bundestages gewählt und steht an der Spitze der Bundesregierung.\n\n')

    img12 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/2jgvwqx5gak2k1djutecn/Section2_Bild0.png?rlkey=omrqy05enu9oj0u96o9511mf9&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 1 Thema 2", 0),
        key=f"frage12_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img12} ausgewählt.")
    st.session_state.auswahl["Frage 1 Thema 2"] = img12

    st.text('Thema 3: Der Bundestag kontrolliert die Regierung\n- Der Bundestag übt die wichtige Kontrollfunktion aus und kann die Bundesregierung überwachen.\n\n')

    img13 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/wso0rjbgcc8jvnv0nmm93/Section3_Bild1.png?rlkey=o4h65kwh07r0cf23y9q1zxez3&dl=1",
            "https://www.dropbox.com/scl/fi/q0xqldr4gi9eag027n9wo/Section3_Bild0.png?rlkey=jx3e98m99otwaczpxbby93szs&dl=1",
            "https://www.dropbox.com/scl/fi/h4ud18acu0e4oxxuzeilo/Section3_Bild2.png?rlkey=wnswnt521dta4e020orrvzipd&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 1 Thema 3", 0),
        key=f"frage13_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img13} ausgewählt.")
    st.session_state.auswahl["Frage 1 Thema 3"] = img13

    st.text('Thema 4: Die Abgeordneten\n- Die Abgeordneten sind Vertreterinnen und Vertreter des ganzen Volkes und haben Rechte und Pflichten gemäß dem Grundgesetz.\n\n')

    img14 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/w8dmyp9j1dim9qp9pocff/Section4_Bild2.png?rlkey=9la3xotrcqlun3zkhixm87z8m&dl=1",
            "https://www.dropbox.com/scl/fi/t59c157l7e65rp774wdqc/Section4_Bild0.png?rlkey=31qw1qtqj3ips56402k2yqcfv&dl=1",
            "https://www.dropbox.com/scl/fi/gqg0znedz545xbn9j6dnn/Section4_Bild1.png?rlkey=g87jdnzv3dmuxhxlf7opzslz9&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 1 Thema 4", 0),
        key=f"frage14_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img14} ausgewählt.")
    st.session_state.auswahl["Frage 1 Thema 4"] = img14

    st.text('Thema 5: Wichtige Organe und Gremien\n- Die wichtigsten Organe und Gremien des Bundestages sind der Ältestenrat, die Ausschüsse, die Fraktionen und die Enquête-Kommissionen.')

    img15 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/ubyw3or2hotq26o2na98h/Section5_Bild11.png?rlkey=1tri1sb8lgvucsan585hhd3lz&dl=1",
            "https://www.dropbox.com/scl/fi/x4a153pi6wk5ew09mcqx9/Section5_Bild9.png?rlkey=cq8es77mqtyoen4h84w7rpn6r&dl=1",
            "https://www.dropbox.com/scl/fi/76rn47twxruel1st7t8it/Section5_Bild5.png?rlkey=adt2zg65601nq6fdmnplgauqo&dl=1",
            "https://www.dropbox.com/scl/fi/7megd8nwu6axy6xvu8kzb/Section5_Bild8.png?rlkey=adheomkbqwgi7pxy0flps4ohz&dl=1",
            "https://www.dropbox.com/scl/fi/k45t3vdym8kx047nfroo8/Section5_Bild0.png?rlkey=ppubjmp23uc1z2ovpr70mpweg&dl=1",
            "https://www.dropbox.com/scl/fi/x6wl494v4qtlr5mw9v2ic/Section5_Bild1.png?rlkey=3azd0rhcxued5xngmwfk4rfvu&dl=1",
            "https://www.dropbox.com/scl/fi/k8nzoqly54c6y7e3q4do1/Section5_Bild2.png?rlkey=edx8f4rnb3nbv4cbkdqi4814h&dl=1",
            "https://www.dropbox.com/scl/fi/c35iyvf419hoc531zfv2o/Section5_Bild7.png?rlkey=06b3xn9nvtb91p29fa2b7m6vn&dl=1",
            "https://www.dropbox.com/scl/fi/hkzisut6jgmb5n3530s99/Section5_Bild4.png?rlkey=jdis25kzcjvlmfxz6pbi9zmlb&dl=1",
            "https://www.dropbox.com/scl/fi/cva82jc8than0g3pt3qhs/Section5_Bild6.png?rlkey=3czprxsucepwakr2t6prkryar&dl=1",
            "https://www.dropbox.com/scl/fi/ea3pywnkr4pasdn2p1rls/Section5_Bild10.png?rlkey=k57cxlkmtyp2ljtwgkmtzjh98&dl=1",
            "https://www.dropbox.com/scl/fi/6u8c9jpcw64wc7e9o0pz1/Section5_Bild3.png?rlkey=rb3z5sx9xxow0cprmfcwss44w&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 1 Thema 5", 0),
        key=f"frage15_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img15} ausgewählt.")
    st.session_state.auswahl["Frage 1 Thema 5"] = img15

    st.button("(Nachfolgende) Frage 2", on_click=lambda: wechsel_zu("page2"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [3, 4, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page2":
    st.title("Frage 2")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/e4cc393wpkymln8njq0d4/potenzial_der_windenergie.pdf?rlkey=mmk65qlahx5js5lc5bru32e74&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Bestimmung und Bewertung des potentiellen technisch-ökologischen Nutzbaren Raums für Windenergieanlagen an Land in Deutschland einschließlich Einschränkungen und regionalen Unterschieden.')

    st.text('Thema 1: Methode\n- Basiert auf detaillierten digitalen Daten und gliedert sich in zwei Phasen: Festlegung der Flächenpotentiale und Modellierung des Leistungs- und Ertragspotenzials.\n\n')

    img21 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/4invzh5pkxz69qv6720sr/Section1_Bild0.png?rlkey=pbon7u6adtpwypz15nx01g2we&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 2 Thema 1", 0),
        key=f"frage21_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img21} ausgewählt.")
    st.session_state.auswahl["Frage 2 Thema 1"] = img21

    st.text('Thema 2: Flächenpotenziale & Exclusion Criteria\n- Enthält nur solche Flächen, die für andere Zwecke unbrauchbar sind, wie Baugebiete, Sonderartenschutzbereiche etc., aus denen Windenergieanlagen ausgeschlossen werden.')

    img22 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 2 Thema 2", 0),
        key=f"frage22_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img22} ausgewählt.")
    st.session_state.auswahl["Frage 2 Thema 2"] = img22

    st.text('Thema 3: Leistungs- und Ertragspotenzial\n- Berechnet das Potenzial mittels moderner Windenergieanlagen, indem sowohl schwache als auch starke Windanlagen betrachtet werden.')

    img23 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 2 Thema 3", 0),
        key=f"frage23_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img23} ausgewählt.")
    st.session_state.auswahl["Frage 2 Thema 3"] = img23

    st.text('Thema 4: Sensitivität und Regionalkontexte\n- Analysiert die Auswirkungen verschiedener Faktoren auf das Potenzial, wie Wahl der Referenzanlage, Abstand zur Wohnbebauung etc. und untersucht regionale Besonderheiten.')

    img24 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 2 Thema 4", 0),
        key=f"frage24_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img24} ausgewählt.")
    st.session_state.auswahl["Frage 2 Thema 4"] = img24

    st.text('Thema 5: Umsetzungsperspektive\n- Legt nahe, dass Windenergieanlagen an Land eine bedeutsame Rolle im deutschen Energiesystem haben könnten, jedoch hängt ihre Ausnutzung vom politischen Willen, regionalplanerischer Balance und Akzeptanzabwägung ab.\n\n')

    img25 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/j8bhoxa8tz5n6zxb63wdi/Section5_Bild0.png?rlkey=i2usrcygik602jpixosi5yc2x&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 2 Thema 5", 0),
        key=f"frage25_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img25} ausgewählt.")
    st.session_state.auswahl["Frage 2 Thema 5"] = img25

    st.button("(Nachfolgende) Frage 3", on_click=lambda: wechsel_zu("page3"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 4, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page3":
    st.title("Frage 3")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/jimpct7iv5zd4s9bg4xtz/Probe345Bd93.pdf?rlkey=iudqa545hcwvkulbo8jl4pdqi&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Klärung der Ursachen und Mechanismen des Aussters der Dinosaurier')

    st.text('Thema 1: Entstehung und Dominanz der Dinosaurier\n- Beschreibt die Entstehung der Dinosaurier aus den Archosauria und ihre rasche Dominanz gegenüber anderen Tiergruppen.\n\n')

    img31 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/atkbu7f6i60jjrh1l05ix/Section1_Bild0.png?rlkey=bdfbjjrq19iyne99yd95hec88&dl=1",
            "https://www.dropbox.com/scl/fi/l30oz2lyosgpkcq0zc4bj/Section1_Bild6.png?rlkey=9uph5spg64pwso4tjoduyjlmh&dl=1",
            "https://www.dropbox.com/scl/fi/eaij5io2ev411rkh9zxoh/Section1_Bild2.png?rlkey=l2n6v11pi2yr44jtpen6ac87a&dl=1",
            "https://www.dropbox.com/scl/fi/9u92w381v8n5pwocib7oa/Section1_Bild9.png?rlkey=gj0nxbl413wx4udor994cb8a8&dl=1",
            "https://www.dropbox.com/scl/fi/czgr3jr066lh7gigcs47q/Section1_Bild5.png?rlkey=l4ac36v06ahrkt5vqih8ho10i&dl=1",
            "https://www.dropbox.com/scl/fi/ltwc6i3ophbi186iogji3/Section1_Bild7.png?rlkey=81ttxau7r72n8mfbyopuxjtru&dl=1",
            "https://www.dropbox.com/scl/fi/y1suwdmdca2jv8u3jobgl/Section1_Bild4.png?rlkey=4hw9em4gizj5y2fwgieomxfb7&dl=1",
            "https://www.dropbox.com/scl/fi/rxoi9t5aqmwnc618xuehg/Section1_Bild8.png?rlkey=392fwokuxo67vgvsq0hdvminu&dl=1",
            "https://www.dropbox.com/scl/fi/5jpak9caixej3yq24171t/Section1_Bild1.png?rlkey=2tfikolzt80jxeqeug11uf8g2&dl=1",
            "https://www.dropbox.com/scl/fi/9in2v8t7y2ssx48tprnfv/Section1_Bild3.png?rlkey=vs14b0l5h398ud8nfckzd7iw8&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 3 Thema 1", 0),
        key=f"frage31_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img31} ausgewählt.")
    st.session_state.auswahl["Frage 3 Thema 1"] = img31

    st.text('Thema 2: Habitat und Ernährung\n- Erklärt die Lebensbedingungen und die Nahrungsmethoden der Dinosaurier.\n\n')

    img32 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/bs7i6dpnuxlf27xazen36/Section2_Bild1.png?rlkey=6n8sgc8744xdvhs0ldfad26bq&dl=1",
            "https://www.dropbox.com/scl/fi/v12tnksygpkvwon89lx8c/Section2_Bild3.png?rlkey=7dv71yl1lb3wqcbog75fvi997&dl=1",
            "https://www.dropbox.com/scl/fi/6eo8zpn32lqprl39ztvr3/Section2_Bild0.png?rlkey=5pvs7txngh3qne75h3vsdnepw&dl=1",
            "https://www.dropbox.com/scl/fi/qsb0bdi1g9cvbxfeuc9c0/Section2_Bild2.png?rlkey=7kbcq23ttbknznvibqg3mqsti&dl=1",
            "https://www.dropbox.com/scl/fi/b8mwq4gixcaolu4a4oi4i/Section2_Bild6.png?rlkey=rel8jcw19rae0rd019fyy2u37&dl=1",
            "https://www.dropbox.com/scl/fi/n1eykmb9yzxwz0fmsywjz/Section2_Bild4.png?rlkey=039987ekrurofc37c08h330t5&dl=1",
            "https://www.dropbox.com/scl/fi/9s88umjhy9kv35myspkhd/Section2_Bild5.png?rlkey=8q2i4qi3esax8oswphvdobuso&dl=1",
            "https://www.dropbox.com/scl/fi/fe58utq7pr09moun400zz/Section2_Bild7.png?rlkey=9cskxc694frz9cpk443ekouyu&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 3 Thema 2", 0),
        key=f"frage32_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img32} ausgewählt.")
    st.session_state.auswahl["Frage 3 Thema 2"] = img32

    st.text('Thema 3: Globales Klima und Umweltveränderungen\n- Berührt die Klimaveränderungen und Umweltkatastrophen, die möglicherweise zur Ausrottung der Dinosaurier beitragen konnten.\n\n')

    img33 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/rkum3r3odgcwmvna7nssb/Section3_Bild5.png?rlkey=4vvvbm2p8v4johnbd9hnhl793&dl=1",
            "https://www.dropbox.com/scl/fi/vq5pi8kf1ecaamz3yub1u/Section3_Bild1.png?rlkey=gi0ectays36dcied1l4gt3m0z&dl=1",
            "https://www.dropbox.com/scl/fi/kt3ialiha79vfur1sh9bp/Section3_Bild0.png?rlkey=prj279c8xbci5adnrf4k636w3&dl=1",
            "https://www.dropbox.com/scl/fi/r8a8rkofjpnjhxr0i6dbm/Section3_Bild4.png?rlkey=nfrh326bb5c1p42p86jijyu4e&dl=1",
            "https://www.dropbox.com/scl/fi/00503zmtdfwl3dzvj245b/Section3_Bild2.png?rlkey=0b5we0q4li1nwvfv2rr1sjw3w&dl=1",
            "https://www.dropbox.com/scl/fi/jzb2ylcvafxmq9ih9pdpv/Section3_Bild3.png?rlkey=mqdwnqfy6t0mrzudnvrl6gtlt&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 3 Thema 3", 0),
        key=f"frage33_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img33} ausgewählt.")
    st.session_state.auswahl["Frage 3 Thema 3"] = img33

    st.text('Thema 4: Meteoriteneinschlag und Vulkanismus\n- Discussiert die These, dass ein Meteoriteneinschlag oder massive Vulkanismus am Ende der Kreide maßgeblich zum Aussterben der Dinosaurier beigetragen haben könnten.\n\n')

    img34 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/lp2st9p6y6tu2rovq8yjb/Section4_Bild3.png?rlkey=tykmr5szytn9l81v0lppn3ac6&dl=1",
            "https://www.dropbox.com/scl/fi/1enpy721msbaedm8k7232/Section4_Bild6.png?rlkey=42nn1ud2mq0q4ftj9epm3sriu&dl=1",
            "https://www.dropbox.com/scl/fi/i4xsb2nt2jk3z1fhpbcq7/Section4_Bild2.png?rlkey=lkyh0naneemd9jvxco97mjhnx&dl=1",
            "https://www.dropbox.com/scl/fi/baodrhphuykz5jntoggtu/Section4_Bild8.png?rlkey=yf9xsfibqjtr5xyjreblrupub&dl=1",
            "https://www.dropbox.com/scl/fi/gm07udlf0hc6qrljdc91a/Section4_Bild0.png?rlkey=8ix7ntezk94ajywya6mavxx4d&dl=1",
            "https://www.dropbox.com/scl/fi/vgfczxeylrbq6y6sb0gjl/Section4_Bild4.png?rlkey=9nk6oyina0saahas797i80r11&dl=1",
            "https://www.dropbox.com/scl/fi/2x1kptk7yfraz7q8u81r2/Section4_Bild7.png?rlkey=mt2zsgu9bqe28msqy7sgzjk8u&dl=1",
            "https://www.dropbox.com/scl/fi/kh8q9jqt0nb3ryzbou8ce/Section4_Bild1.png?rlkey=cym43ty7hi3n2hayd6skbrns3&dl=1",
            "https://www.dropbox.com/scl/fi/3h6cmv3uk5axej08pp3u4/Section4_Bild5.png?rlkey=bvp1b4cfa24hf479kfmo8tv7o&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 3 Thema 4", 0),
        key=f"frage34_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img34} ausgewählt.")
    st.session_state.auswahl["Frage 3 Thema 4"] = img34

    st.text('Thema 5: Langfristige ökologische Veränderungen\n- Betrachtet die möglichen langfristigen ökologischen Veränderungen, die zur Ausrottung der Dinosaurier geführt haben könnten.\n\n')

    img35 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/tlrhzkii223ijcdcm9rtl/Section5_Bild5.png?rlkey=ja3iih829mv99li75tijrxz44&dl=1",
            "https://www.dropbox.com/scl/fi/2fs115sept3vt596i9dmb/Section5_Bild0.png?rlkey=pvy9ig49mdyg6euo3xsd7ima7&dl=1",
            "https://www.dropbox.com/scl/fi/lqkx1pj9zw0v5ens691mc/Section5_Bild1.png?rlkey=erk3yx5ov3c3r53496ztlikwn&dl=1",
            "https://www.dropbox.com/scl/fi/hpyvtaxi7vun9ne8nbkwt/Section5_Bild2.png?rlkey=o6i5crh21ckd7pv86ew0w81fs&dl=1",
            "https://www.dropbox.com/scl/fi/165uy8flozny8rog1r7ze/Section5_Bild4.png?rlkey=yzv9m0qklgrcrauhrc0vuwxbt&dl=1",
            "https://www.dropbox.com/scl/fi/aokbdzve4u578ufksrtp7/Section5_Bild3.png?rlkey=72eecgs7e5ypzqjs0wuvgid7c&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 3 Thema 5", 0),
        key=f"frage35_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img35} ausgewählt.")
    st.session_state.auswahl["Frage 3 Thema 5"] = img35

    st.button("(Nachfolgende) Frage 4", on_click=lambda: wechsel_zu("page4"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page4":
    st.title("Frage 4")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/sikf52yb7ve2bm6c0np3z/Zweiter_Weltkrieg_01.pdf?rlkey=vmebrqwya7j9k2tk4z0oprx0w&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Eine Übersicht über den Zweiten Weltkrieg und seine Ursachen, Verlauf und Folgen geben.')

    st.text('Thema 1: Ursachen des Zweiten Weltkriegs\n- Erklärt die politischen, wirtschaftlichen und ideologischen Ursachen des Zweiten Weltkriegs.\n\n')

    img41 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/9kykpez08fky24df98tkc/Section1_Bild0.png?rlkey=m6v42wmhiz4pguv6p9qlhcr0v&dl=1",
            "https://www.dropbox.com/scl/fi/2djhub1ev1alypi9n28pt/Section1_Bild1.png?rlkey=a6m2b2qgmaqydabkvr37v3zoy&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 4 Thema 1", 0),
        key=f"frage41_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img41} ausgewählt.")
    st.session_state.auswahl["Frage 4 Thema 1"] = img41

    st.text('Thema 2: Verlauf des Zweiten Weltkriegs\n- Beschreibt die Schlachten und Operationen des Zweiten Weltkriegs, von seinem Beginn bis zum Kriegsende.\n\n')

    img42 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/7w682ishp8o2o6t7jw147/Section2_Bild0.png?rlkey=ew0w38roabvnballksxp954x0&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 4 Thema 2", 0),
        key=f"frage42_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img42} ausgewählt.")
    st.session_state.auswahl["Frage 4 Thema 2"] = img42

    st.text('Thema 3: Alltagsleben während des Zweiten Weltkriegs\n- Erläutert die Lebensbedingungen der Zivilbevölkerung während des Zweiten Weltkriegs.\n\n')

    img43 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/ffpcie6nb0ero9853ebji/Section3_Bild1.png?rlkey=6b8q26iskur4qcr5bhccc57ob&dl=1",
            "https://www.dropbox.com/scl/fi/z369s44u6lwe50ltnt8fn/Section3_Bild0.png?rlkey=1lzndbjtwx12sael9tlwmldcz&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 4 Thema 3", 0),
        key=f"frage43_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img43} ausgewählt.")
    st.session_state.auswahl["Frage 4 Thema 3"] = img43

    st.text('Thema 4: Folgen des Zweiten Weltkriegs\n- Zeigt die politischen, wirtschaftlichen und gesellschaftlichen Folgen des Zweiten Weltkriegs auf.\n\n')

    img44 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/2vqdri7asvyznbt14m70v/Section4_Bild2.png?rlkey=plujeky3jvyp3xj3oj22zfpit&dl=1",
            "https://www.dropbox.com/scl/fi/8abt91tn33a62inpic5z9/Section4_Bild0.png?rlkey=h0n6k0zefouq3a10z33q5s7c7&dl=1",
            "https://www.dropbox.com/scl/fi/fhb5fxlmuskcadqbvkmjh/Section4_Bild1.png?rlkey=ohfv0nrlb4350q11spqhcksc0&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 4 Thema 4", 0),
        key=f"frage44_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img44} ausgewählt.")
    st.session_state.auswahl["Frage 4 Thema 4"] = img44

    st.text('Thema 5: Internationale Kooperation nach dem Zweiten Weltkrieg\n- Erklärt die Gründung der Vereinten Nationen und die europäische Integration als Antwort auf den Zweiten Weltkrieg.\n\n')

    img45 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/4zq97jetaki0i6wc8qmv0/Section5_Bild0.png?rlkey=iqw7smcftv2v0r9z66s8szgvy&dl=1",
            "https://www.dropbox.com/scl/fi/jvbpnfql47ntlfbiqqas9/Section5_Bild1.png?rlkey=m95s47yp0j281qome0bfjsqn7&dl=1",
            "https://www.dropbox.com/scl/fi/2y2ssz2pg518t6vudv9qj/Section5_Bild2.png?rlkey=gmu17wz2kcxcsdfp0bwi20gmb&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 4 Thema 5", 0),
        key=f"frage45_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img45} ausgewählt.")
    st.session_state.auswahl["Frage 4 Thema 5"] = img45

    st.button("(Nachfolgende) Frage 5", on_click=lambda: wechsel_zu("page5"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page5":
    st.title("Frage 5")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/3jl2q4edo0vxdhlbp3qdr/Broschuere_2013_hires.pdf?rlkey=4rbopzs7rxi1bhax71t7avs1t&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Unterrichten über die globale Erderwärmung und die Möglichkeiten klimapolitischer Maßnahmen, sowie die Entdeckung und Entwicklungen um Kometen.')

    st.text('Thema 1: Globale Erderwärmung - Definition und Ursachen\n- Begriffsklarstellung von Treibhausgas, CO₂-Emission und globaler Erwärmung, Historie der Emissionen dokumentiert.')

    img51 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/hv5xozqxq9gj3o5jlzz5s/Section1_Bild0.png?rlkey=j35pcegynodlghcvtdmqca9k8&dl=1",
            "https://www.dropbox.com/scl/fi/xn0kra35t765zq6gemlbj/Section1_Bild1.png?rlkey=3x7dafn4gvs5iosrllb6izcy5&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 5 Thema 1", 0),
        key=f"frage51_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img51} ausgewählt.")
    st.session_state.auswahl["Frage 5 Thema 1"] = img51

    st.text('Thema 2: Kometen - Entstehung und Typen\n- Beschreibung der Herkunft von Kometen im Kuipergürtel und Oort’sche Wolke, Unterschiede zwischen Short period comets, Long period comets und Hyperbolic Comets.')

    img52 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/0mqqxkl9yf0z927lqzrjt/Section2_Bild1.png?rlkey=4y3ah98un8h4jm4c0pwsk2v01&dl=1",
            "https://www.dropbox.com/scl/fi/a00p166rculb9ztc32z2s/Section2_Bild0.png?rlkey=nlpv36ovcvt0ivh5nsmd4p520&dl=1",
            "https://www.dropbox.com/scl/fi/9v6vh0h0lih6rywytwqn3/Section2_Bild2.png?rlkey=fhngcsg1kvu4atzetlbt35e6o&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 5 Thema 2", 0),
        key=f"frage52_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img52} ausgewählt.")
    st.session_state.auswahl["Frage 5 Thema 2"] = img52

    st.text('Thema 3: Effekte der Erderwärmung und Kometenorbits\n- Negative Auswirkungen der Erderwärmung auf Meere, Wälder, Tiere und Menschen beschrieben, Wechsel von Kometenperioden von Ruhephasen zu aktiven Phasen und die Rolle gravitativer Kräfte erklärt.\n\n')

    img53 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/vxnnk3w66t3m2c0rgun3b/Section3_Bild1.png?rlkey=pftvoc3owsozkgs3gehsj9e8i&dl=1",
            "https://www.dropbox.com/scl/fi/i4l00rotbq8272jbqb157/Section3_Bild0.png?rlkey=4vqdcu2tqvev8imgbjwx400j7&dl=1",
            "https://www.dropbox.com/scl/fi/k2ehf1mqfpttj5pf7ffni/Section3_Bild2.png?rlkey=kqxr59xxfiuq7ptl36u14wrxr&dl=1",
            "https://www.dropbox.com/scl/fi/q8guaq6vzc1uoivr0yw3l/Section3_Bild3.png?rlkey=xq1kbrc2kinxf6gmz7d2v256w&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 5 Thema 3", 0),
        key=f"frage53_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img53} ausgewählt.")
    st.session_state.auswahl["Frage 5 Thema 3"] = img53

    st.text('Thema 4: Alternative Energiestratégien und Komponenten von Kometen\n- Solar- und Windenergie sowie Elektromobilität als alternatives Optionsmodell zu fossiler Energie präsentiert, unterschiedliche Teile eines Kometen vorgestellt.\n\n')

    img54 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/mqvi3b4e1h6alkcj4gyf9/Section4_Bild2.png?rlkey=k2rpg9nv4tjjoowu6t1o0c9mw&dl=1",
            "https://www.dropbox.com/scl/fi/wkmd7w7i55tmvb5qpkba9/Section4_Bild0.png?rlkey=5frpo5o51zq0b1aaaqh2abh8x&dl=1",
            "https://www.dropbox.com/scl/fi/tj7iu2ozzc3b4dx5ap6m0/Section4_Bild1.png?rlkey=fbi0tgjlt9np1newfo0maek6g&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 5 Thema 4", 0),
        key=f"frage54_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img54} ausgewählt.")
    st.session_state.auswahl["Frage 5 Thema 4"] = img54

    st.text('Thema 5: Nationale und Internationale Klimapolicy und Datenbankplanetenbilder\n- National und international agierende Klimapolicy erläutert, Pariser Klimaabkommen behandelt, Übersicht über die RPIF als internationale Bibliothek für Planetardaten gegeben, Archivierung und Bereitstellung von Bild-, Spektral-Daten sowie Positionen der jeweiligen Sonde durch die RPIF.\n\n')

    img55 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/b5cxjvcj26dygpn3n8wcb/Section5_Bild0.png?rlkey=p1gv61a4c9z8uhm48h0lzomay&dl=1",
            "https://www.dropbox.com/scl/fi/08wg52l9fg9h9syrhhewj/Section5_Bild1.png?rlkey=kvlhnlvwayaqfswo6g5efndxl&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 5 Thema 5", 0),
        key=f"frage55_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img55} ausgewählt.")
    st.session_state.auswahl["Frage 5 Thema 5"] = img55

    st.button("(Nachfolgende) Frage 6", on_click=lambda: wechsel_zu("page6"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page6":
    st.title("Frage 6")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/yjaighb2xxsxb74ams6rn/Menschenaffen_Unterrichtsmaterial.pdf?rlkey=sq2dxtgtkcsecemo15mnb7z6y&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Dieser Unterrichtsleitfaden dient als Grundlage für das Lernen in verschiedenen Fächern und stellt Informationen über die Menschenaffen bereit.')

    st.text('Thema 1: Evolution, Merkmale und Fähigkeiten der Menschenaffen\n- Beschreibt die evolutionäre Entwicklung und physischen Merkmale der Menschenaffen, einschließlich ihrer genetischen Ähnlichkeit mit dem Menschen.\n\n')

    img61 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/7wo17fh71epsvp3ddawgu/Section1_Bild0.png?rlkey=8ca2y1xx41nfty3egc8sumgar&dl=1",
            "https://www.dropbox.com/scl/fi/09dx6ovjo584o8r8f2sby/Section1_Bild2.png?rlkey=zowvlw34mmot3uuq7mzh5ek37&dl=1",
            "https://www.dropbox.com/scl/fi/tf22jqzmznatek2eu4u5f/Section1_Bild4.png?rlkey=hp1hmel4f6frypsc9ju9ufqha&dl=1",
            "https://www.dropbox.com/scl/fi/qgc6x1o9m6c41cxcvta12/Section1_Bild1.png?rlkey=2gvj8knkkn07q70fg9p7mls7x&dl=1",
            "https://www.dropbox.com/scl/fi/6czjwdid59lzabqi39lu0/Section1_Bild3.png?rlkey=rc1b9r8r5arii72ultmpwb9me&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 6 Thema 1", 0),
        key=f"frage61_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img61} ausgewählt.")
    st.session_state.auswahl["Frage 6 Thema 1"] = img61

    st.text('Thema 2: Wie und wo Menschenaffen leben\n- Erläutert die Lebensweise und Verbreitung verschiedener Menschenaffenarten in Afrika und Südostasien.\n\n')

    img62 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/ba46v6z49do7sl7e5622q/Section2_Bild1.png?rlkey=obpthebr3tnl16wd7dcqto2mz&dl=1",
            "https://www.dropbox.com/scl/fi/c6lfjb6p27s7gs0c2boua/Section2_Bild3.png?rlkey=7cq07dw7gcew795y5g858pi7y&dl=1",
            "https://www.dropbox.com/scl/fi/5xffiz72ta2ky4xdqyyda/Section2_Bild0.png?rlkey=ewmplsgqkv8yhy6n2ovfp5wxd&dl=1",
            "https://www.dropbox.com/scl/fi/og5v4k0c45440u6lb7prv/Section2_Bild2.png?rlkey=kvxgsipcidql2gpdd0mcw71j2&dl=1",
            "https://www.dropbox.com/scl/fi/0ewj02v9xev337lprk1gp/Section2_Bild6.png?rlkey=ygjgbppbx3pcdhhlrq544lvpe&dl=1",
            "https://www.dropbox.com/scl/fi/jafa0gmpr31sem80eph13/Section2_Bild4.png?rlkey=tngnjps18v71gul7nv88o7ppx&dl=1",
            "https://www.dropbox.com/scl/fi/cf81bq7h69j7jz4p0n6p5/Section2_Bild5.png?rlkey=6law7ociggupwd2woxzhk7xow&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 6 Thema 2", 0),
        key=f"frage62_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img62} ausgewählt.")
    st.session_state.auswahl["Frage 6 Thema 2"] = img62

    st.text('Thema 3: Was Menschenaffen bedroht\n- Identifiziert Lebensraumverlust, Wilderei und Krankheitsübertragung als primäre Risiken für die Existenz der Menschenaffen.\n\n')

    img63 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/fhgyfxyqcpnqwyigbbiqn/Section3_Bild5.png?rlkey=217nlsunhoejmj1kql0mprz13&dl=1",
            "https://www.dropbox.com/scl/fi/6o35g1za1i2jf33cintbl/Section3_Bild1.png?rlkey=ytllp4jc2ozlbsjpsgj0j2tzg&dl=1",
            "https://www.dropbox.com/scl/fi/a9t96mwiw8c02twt35fxy/Section3_Bild0.png?rlkey=qt1p7ce792us1q3ey0kq6ho70&dl=1",
            "https://www.dropbox.com/scl/fi/tdg2gjmbrc0sobsuuoa95/Section3_Bild4.png?rlkey=n416883tyvqqt24wuymd35gqk&dl=1",
            "https://www.dropbox.com/scl/fi/x8ps2ir64wmiima0fg3ek/Section3_Bild2.png?rlkey=bwfv7u1ne2izx2rz0gvibo3m4&dl=1",
            "https://www.dropbox.com/scl/fi/2i7w0rbe4svqve8yzhpiu/Section3_Bild3.png?rlkey=v7os8eai9cowbj8b2sf317fem&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 6 Thema 3", 0),
        key=f"frage63_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img63} ausgewählt.")
    st.session_state.auswahl["Frage 6 Thema 3"] = img63

    st.text('Thema 4: Wie wir Menschenaffen helfen können\n- Präsentiert Maßnahmen des WWF und anderer Organisationen zum Schutz der Menschenaffen, einschließlich der Förderung von nachhaltiger Landwirtschaft und Öko-Tourismus.\n\n')

    img64 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/83af2xyn6hvgp3wno9hsg/Section4_Bild3.png?rlkey=xrha40wn3ffg088rpf6okybb5&dl=1",
            "https://www.dropbox.com/scl/fi/3w83latxzd7mnqektyojv/Section4_Bild6.png?rlkey=acpg5x1tlsqswj0k8fxnae80i&dl=1",
            "https://www.dropbox.com/scl/fi/0mg4qtf40vk4akl7dxw3q/Section4_Bild2.png?rlkey=qqfrdwhsktfoj3wu95sg39s2k&dl=1",
            "https://www.dropbox.com/scl/fi/n2aamnlgdji01uzbr40tn/Section4_Bild0.png?rlkey=vk3j1mcbpw3xnuncme502jef5&dl=1",
            "https://www.dropbox.com/scl/fi/jpwqk89zf0imjvbjtqrwv/Section4_Bild4.png?rlkey=b4hotjpqcbddtje1oajv4542l&dl=1",
            "https://www.dropbox.com/scl/fi/ig6xhcmhrzqgv3u4way2a/Section4_Bild7.png?rlkey=76r1chbz9s6vzooyd5wieaw9x&dl=1",
            "https://www.dropbox.com/scl/fi/jm4ujjxlllih5yckhjd20/Section4_Bild1.png?rlkey=vb40hzgwnhungxjy4077j805w&dl=1",
            "https://www.dropbox.com/scl/fi/ldcqfw4zxwmx27kavbpf4/Section4_Bild5.png?rlkey=twy1gp8r5dwotj9spjnhn2aap&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 6 Thema 4", 0),
        key=f"frage64_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img64} ausgewählt.")
    st.session_state.auswahl["Frage 6 Thema 4"] = img64

    st.text('Thema 5: Von Affen und Menschen\n- Discussiert die Beziehung zwischen Menschen und Menschenaffen und die ethischen Fragen, die sich daraus ergeben.\n\n')

    img65 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/2k9twkqzenv8xkq5zrayr/Section5_Bild0.png?rlkey=ea2bxbaz24awp6u8cl1e0ebjx&dl=1",
            "https://www.dropbox.com/scl/fi/svvmd0z3fxk9a25afes27/Section5_Bild1.png?rlkey=vlg9dtnrs39467lloqvh3vog8&dl=1",
            "https://www.dropbox.com/scl/fi/zaaeklhif6beqw42p3v7s/Section5_Bild2.png?rlkey=7gdt58ncy5f6ublaz0n6k0g2w&dl=1",
            "https://www.dropbox.com/scl/fi/a9bkwavdyhec9wo5cmjl1/Section5_Bild4.png?rlkey=ja03nlxtz5x7soynfqrbi6dht&dl=1",
            "https://www.dropbox.com/scl/fi/hsr6gfs54kyiatuw5qnzz/Section5_Bild3.png?rlkey=j4rowq7620etnsjkieol9xjju&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 6 Thema 5", 0),
        key=f"frage65_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img65} ausgewählt.")
    st.session_state.auswahl["Frage 6 Thema 5"] = img65

    st.button("(Nachfolgende) Frage 7", on_click=lambda: wechsel_zu("page7"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page7":
    st.title("Frage 7")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/64f0ikqlu16ialmuhkw84/O1A1-GE.pdf?rlkey=ht3k4mdyiyg04jiimjyarkof8&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Eine Übersicht über die Basisfunktionen und Anwendungen von 3D-Druck in Bildungseinrichtungen bieten sowie die unterschiedlichen Methoden und Materialien im Industrie-3D-Druck begründen.')

    st.text('Thema 1: 3D-Druckgrundlagen & Anwendungen in Schulen\n- Erklärt, welcher Vorteil 3D-Drucke für pädagogisches Lernen bringt und wie sich diese Technik in Unterrichtssituationen nutzen lässt.')

    img71 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/baer6sf3us6d0s0nxsciz/Section1_Bild0.png?rlkey=fyyfn5i11qnk5pzkphhrd6c53&dl=1",
            "https://www.dropbox.com/scl/fi/k88a2pzuuz88tprbe58m4/Section1_Bild2.png?rlkey=4lgwt8wcj4ratzwie1b1wcwrf&dl=1",
            "https://www.dropbox.com/scl/fi/00fpqunc5h4ng3l11xnud/Section1_Bild5.png?rlkey=0tjcryisxtl30cflw34r187m6&dl=1",
            "https://www.dropbox.com/scl/fi/k6va2j6v3jp6vxr12hpng/Section1_Bild4.png?rlkey=8a20sauqpoouyqo0tqubbd70a&dl=1",
            "https://www.dropbox.com/scl/fi/nknt0hoqgnhzodji3r5wd/Section1_Bild1.png?rlkey=g7iirytvpw92ohwg5br3c8k1a&dl=1",
            "https://www.dropbox.com/scl/fi/ohhf59w6kkk8q1vp3he0x/Section1_Bild3.png?rlkey=84x5igdhg26h9cdkq9fvg76mx&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 7 Thema 1", 0),
        key=f"frage71_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img71} ausgewählt.")
    st.session_state.auswahl["Frage 7 Thema 1"] = img71

    st.text('Thema 2: Häufigste 3D-Drucktechnologien\n- Listet die drei meistverwendeten 3D-Drucktechnologien auf (Fused Deposition Modeling, Stereolithografie und selectives Lasersinters), beschreibt ihre grundlegenden Merkmale und gibt Auskunft über ihre jeweils optimierten Anwendungsbereiche.\n\n')

    img72 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/moirk47ooxzxgokae5d0c/Section2_Bild1.png?rlkey=apucrr5okm6m09e1ci70dsun7&dl=1",
            "https://www.dropbox.com/scl/fi/kcgmbhsk5z30l6e8kxoy1/Section2_Bild3.png?rlkey=hz0h8iq7huvo32lvqvs5d0ri1&dl=1",
            "https://www.dropbox.com/scl/fi/bntemum4wjfwxc71xf0xv/Section2_Bild0.png?rlkey=tx47d4ivcikeoezooc3cqwdau&dl=1",
            "https://www.dropbox.com/scl/fi/psrcagl0bgekz7hpbi8li/Section2_Bild11.png?rlkey=rm5ygt7rllwd9caf53xe31voz&dl=1",
            "https://www.dropbox.com/scl/fi/ezraosgjtsf76c2c5po6w/Section2_Bild2.png?rlkey=vx4wrzfhesdo52reqk9yxumcg&dl=1",
            "https://www.dropbox.com/scl/fi/3cp5jg0h4wibxsqp9xlvf/Section2_Bild8.png?rlkey=yporozyrmu4bpt09o6ntldmpy&dl=1",
            "https://www.dropbox.com/scl/fi/zp01shdil1mp9rbmxkg8i/Section2_Bild6.png?rlkey=7pbwldihznkbbtku1rtgkcr13&dl=1",
            "https://www.dropbox.com/scl/fi/yqikgwsimtf078ymk7imy/Section2_Bild4.png?rlkey=su3agxr5vp4etzcxgi8ha3r82&dl=1",
            "https://www.dropbox.com/scl/fi/7612b3t2mxyt173ghsq64/Section2_Bild10.png?rlkey=74tkcqf1ec8swtd8pgxkbz8hq&dl=1",
            "https://www.dropbox.com/scl/fi/6ssyzb9r2yvska70mzyi5/Section2_Bild5.png?rlkey=7usbz1gfl219ph70hjrlbaupn&dl=1",
            "https://www.dropbox.com/scl/fi/oo44eag5rn04of5zncwub/Section2_Bild7.png?rlkey=geqg9yvi8wxim3f43mdu9ia6c&dl=1",
            "https://www.dropbox.com/scl/fi/5w42feki4d7rsa3j6i7xi/Section2_Bild9.png?rlkey=b0wy3d86zbl2uyxr0b9f0guzq&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 7 Thema 2", 0),
        key=f"frage72_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img72} ausgewählt.")
    st.session_state.auswahl["Frage 7 Thema 2"] = img72

    st.text('Thema 3: 3D-Druckproduktionsprozesse\n- Erläutert die Schritte vom Erstellen eines digitalen Modells bis zur Endabfertigung des gedruckten Teiles für jede oben genannte Technologie.\n\n')

    img73 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/jq06fg23hctcilguvo3k9/Section3_Bild5.png?rlkey=kthns4x658ouryrr6n1p55rr4&dl=1",
            "https://www.dropbox.com/scl/fi/79h8f2v055vn85yotuuzg/Section3_Bild1.png?rlkey=pamqx6wvukqcdhm7vg97afgd3&dl=1",
            "https://www.dropbox.com/scl/fi/0td755bi0vquadsi4r7m2/Section3_Bild0.png?rlkey=jis42mskj0uwjmzyj97crlmhq&dl=1",
            "https://www.dropbox.com/scl/fi/tm0rm7hr0decvbvibxm73/Section3_Bild4.png?rlkey=g0i3d8ubwebgbx628moboj8y9&dl=1",
            "https://www.dropbox.com/scl/fi/un7vznjvrhnwshvq58ohi/Section3_Bild6.png?rlkey=21k1nigikj65epkvsqpuns5w2&dl=1",
            "https://www.dropbox.com/scl/fi/soz2yu9rr54pidf3k98tg/Section3_Bild7.png?rlkey=vjhtzfza916551ugfv3phzrr7&dl=1",
            "https://www.dropbox.com/scl/fi/0cxiuzviypsmudozpsult/Section3_Bild2.png?rlkey=aznjdutb9x9mbvc4saxiycbpt&dl=1",
            "https://www.dropbox.com/scl/fi/ow9ls069p0u1vr9hs7q2y/Section3_Bild3.png?rlkey=tpcfe9d1qcvatnfs30g9l9fhd&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 7 Thema 3", 0),
        key=f"frage73_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img73} ausgewählt.")
    st.session_state.auswahl["Frage 7 Thema 3"] = img73

    st.text('Thema 4: Notwendige Softwarekomponenten\n- Nennte die Software, die für den 3D-Druck notwendig sind (Entwurf, Test, Reparatur und Generierung des G-Codes).\n\n')

    img74 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/4w0yrlb4kqzm2558y8eny/Section4_Bild3.png?rlkey=9as28iafxhkasdjcxn6mqdbpq&dl=1",
            "https://www.dropbox.com/scl/fi/y4cp7qmvwwpdthb40neo8/Section4_Bild6.png?rlkey=zc8tuti7bxkx2s46q6iv9j2ib&dl=1",
            "https://www.dropbox.com/scl/fi/92tl9pwqv1cxkfbx1duxh/Section4_Bild10.png?rlkey=cpfdqi0eozm9nku4bq8omynni&dl=1",
            "https://www.dropbox.com/scl/fi/xvmlc81y34jtxkxn994ih/Section4_Bild2.png?rlkey=8fnrrcx4ulbtat8g0aajdjkxk&dl=1",
            "https://www.dropbox.com/scl/fi/9ybb4q3nnyn3bkxxu9viw/Section4_Bild9.png?rlkey=mdtxrbgwt82rt93trvuufz3f1&dl=1",
            "https://www.dropbox.com/scl/fi/hddekcqvyhqdspsl38s9c/Section4_Bild8.png?rlkey=mvq6dvk4pajsg76iknivrsf5c&dl=1",
            "https://www.dropbox.com/scl/fi/3ps2pquk1k9i0c3b1rjfl/Section4_Bild0.png?rlkey=20gj6v1auwhhuah4qdkc1raf8&dl=1",
            "https://www.dropbox.com/scl/fi/v1pdpy26bp6lybq02ovy8/Section4_Bild4.png?rlkey=8xhbxe1e1nd5k6ua4zomu8dv9&dl=1",
            "https://www.dropbox.com/scl/fi/ghvxtr5wxxeuy8f0aaqfv/Section4_Bild7.png?rlkey=g4o789ybyjcy3ui07eg8zwuzv&dl=1",
            "https://www.dropbox.com/scl/fi/4zlev6pwkbadztyi6zrsm/Section4_Bild1.png?rlkey=umco90h7ajhvh9y96eoixf5ll&dl=1",
            "https://www.dropbox.com/scl/fi/bo46k63nyqg0o6hyfruq4/Section4_Bild5.png?rlkey=2u7gz6qbowh04lj48kzb7qtm5&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 7 Thema 4", 0),
        key=f"frage74_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img74} ausgewählt.")
    st.session_state.auswahl["Frage 7 Thema 4"] = img74

    st.text('Thema 5: 3D-Druckmaterialien\n- Baut auf die technisch relevanten Materialien auf (Polymere, Metalle, Ceramiken und Verbundwerkstoffe) und beschreibt ihre Eigenschaften.\n\n')

    img75 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/h9j2xdwp426cich8dvctt/Section5_Bild11.png?rlkey=1c6qu21nzb4t1ylmdw6pedkgt&dl=1",
            "https://www.dropbox.com/scl/fi/mka5jh35tdjv43qrenntc/Section5_Bild9.png?rlkey=huuxbei4p0t6bk124s8s1usmh&dl=1",
            "https://www.dropbox.com/scl/fi/b2osx4zmqcdeqjbbr6ygp/Section5_Bild5.png?rlkey=oc3yxplpnxosvvi63kjprbokp&dl=1",
            "https://www.dropbox.com/scl/fi/hk5aaf72r8zy74pjqcxsb/Section5_Bild8.png?rlkey=d7mdo25jl3cf9k9yw7cxq9bvh&dl=1",
            "https://www.dropbox.com/scl/fi/w846htzv2duza3swiq39d/Section5_Bild0.png?rlkey=2z2dghl643acky2y9ea4iplwb&dl=1",
            "https://www.dropbox.com/scl/fi/n6okgqly2sc1q95ru0quj/Section5_Bild1.png?rlkey=abbs7qljw2dbnm1v7nipaagoh&dl=1",
            "https://www.dropbox.com/scl/fi/lx9ewz8ru29b62nrww6h6/Section5_Bild2.png?rlkey=aemvzn8dosk7xrz5u2lw55axx&dl=1",
            "https://www.dropbox.com/scl/fi/ihvcma8dgdlaika0ey70r/Section5_Bild7.png?rlkey=xxd2m8d6wfcqx7fy2iug54vqw&dl=1",
            "https://www.dropbox.com/scl/fi/jhw3m6l61jqcj4v7axsoz/Section5_Bild4.png?rlkey=yexesvdgnzkzabv1xfsyx0jty&dl=1",
            "https://www.dropbox.com/scl/fi/m362c84igm9s9kkhh959u/Section5_Bild6.png?rlkey=jd3f8peo677nu20nz71y6itfp&dl=1",
            "https://www.dropbox.com/scl/fi/dbtvzhlewh7j1l6q10amh/Section5_Bild10.png?rlkey=7off7821n7j8n1ed7pitw9jj7&dl=1",
            "https://www.dropbox.com/scl/fi/x0hf98j8zrrxnjhift434/Section5_Bild3.png?rlkey=vemcgki0mu7u3vlqhf0oy3k6t&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 7 Thema 5", 0),
        key=f"frage75_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img75} ausgewählt.")
    st.session_state.auswahl["Frage 7 Thema 5"] = img75

    st.button("(Nachfolgende) Frage 8", on_click=lambda: wechsel_zu("page8"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page8":
    st.title("Frage 8")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/n5gm7vk4xb3rdjakncvah/MuM_Band_14.pdf?rlkey=7cy6fwixcrr56gdy8pke4446q&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Das Verständnis für die Bedeutung korallreicher Gebiete sowie die Herausforderungen und Schutzansätze umfangreich präsentieren.')

    st.text('Thema 1: Signifikanz von Korallenriffen\n- Beschreibt die Bedeutung von Korallenriffen für die maritime Vielfalt und die wirtschaftlichen Vorteile für die Menschheit.\n\n')

    img81 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/z2a1zafoozmcrw4oln7ag/Section1_Bild0.png?rlkey=zqtnxo5voioyr3qj22e99ning&dl=1",
            "https://www.dropbox.com/scl/fi/tfpdvm0hb2dyhs2fgvq35/Section1_Bild6.png?rlkey=i9h19h82a0cm21z5rck29xmtz&dl=1",
            "https://www.dropbox.com/scl/fi/mf7hni51pzo33ndhi7w5o/Section1_Bild2.png?rlkey=a9jr7mtstwoqxrek59f26jmz8&dl=1",
            "https://www.dropbox.com/scl/fi/j3mrdbmdmn7q9jgk0otwg/Section1_Bild5.png?rlkey=8393gpmipec0zu7hhp10b6vze&dl=1",
            "https://www.dropbox.com/scl/fi/563324klutw8jx2r212wj/Section1_Bild7.png?rlkey=6ksdr0yy0pzkj99978pkblhfo&dl=1",
            "https://www.dropbox.com/scl/fi/607g9dan4vjl72dbm2lhr/Section1_Bild4.png?rlkey=vm9jrkdbluflw0jwuqwomxtc3&dl=1",
            "https://www.dropbox.com/scl/fi/8wg6conpiqzidtn3rfzgf/Section1_Bild8.png?rlkey=tji3c0e4cftz61rcrmgqxe5u9&dl=1",
            "https://www.dropbox.com/scl/fi/zhw3j3s6ir8odsrfmbbi0/Section1_Bild1.png?rlkey=0r9oumcohzb4tfbikjhgakmq6&dl=1",
            "https://www.dropbox.com/scl/fi/lpso9rttf0zxf5rmui5t2/Section1_Bild3.png?rlkey=wm6r8053yn3i6h5a6txqai7iv&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 8 Thema 1", 0),
        key=f"frage81_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img81} ausgewählt.")
    st.session_state.auswahl["Frage 8 Thema 1"] = img81

    st.text('Thema 2: Entstehung und Entwicklungen\n- Erklärt die Entstehung von Korallenriffen und die Entwicklung über die Zeit.')

    img82 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/h7pxvzixu89oy3dl856dv/Section2_Bild1.png?rlkey=yzj0x5flrbhqbsvlkkkfvwefi&dl=1",
            "https://www.dropbox.com/scl/fi/ucuch4sxpjn8a429e53zr/Section2_Bild3.png?rlkey=8qojvuj2n1ffekr3oue70mrv2&dl=1",
            "https://www.dropbox.com/scl/fi/c8jkukoejinkh9bij888p/Section2_Bild0.png?rlkey=9g2oxqlmvtnetd08mia7xuyie&dl=1",
            "https://www.dropbox.com/scl/fi/pboj5vdo4c08jxydnvmsl/Section2_Bild2.png?rlkey=2lrtiyg4csaigfpw8fqacken4&dl=1",
            "https://www.dropbox.com/scl/fi/i1ti2yereueckt38yjedk/Section2_Bild6.png?rlkey=3ea0rzj6qyyg9dpq14rogsx4e&dl=1",
            "https://www.dropbox.com/scl/fi/ylayf4bmsegfblpbc8bs9/Section2_Bild4.png?rlkey=dpkf9aws7d557zd3wwsbperqc&dl=1",
            "https://www.dropbox.com/scl/fi/1qk2ucdc4guvuvaew9igw/Section2_Bild5.png?rlkey=hza24xfwj0hgg1hlp6px19uft&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 8 Thema 2", 0),
        key=f"frage82_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img82} ausgewählt.")
    st.session_state.auswahl["Frage 8 Thema 2"] = img82

    st.text('Thema 3: Rolle innerhalb von Ökosystemen\n- Beschreibt die Rolle von Korallenriffen innerhalb von Meeres- und Küstenökosystemen.\n\n')

    img83 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/8a43ihxfrze9mt3hdm44r/Section3_Bild5.png?rlkey=027yf9suqfu540vm3qleu67jv&dl=1",
            "https://www.dropbox.com/scl/fi/joy17nccr89nc0l9l07fc/Section3_Bild1.png?rlkey=4zzxxfc6jfpgfhudz5dogmdc3&dl=1",
            "https://www.dropbox.com/scl/fi/b58kxi5dhocjvbsexyqyu/Section3_Bild0.png?rlkey=7p1zaeytj38m9p7u7dq2vhhq2&dl=1",
            "https://www.dropbox.com/scl/fi/8folnlb9yrwvdfmyukw17/Section3_Bild4.png?rlkey=ndl6uncxjlabl5iqpbtcf1dik&dl=1",
            "https://www.dropbox.com/scl/fi/zw07q746heerns4mr6qui/Section3_Bild6.png?rlkey=gyzb2tb0chv3qn0jtmux476td&dl=1",
            "https://www.dropbox.com/scl/fi/zssepdxk2ztdp6ev95hfq/Section3_Bild7.png?rlkey=wnyiays73xr8vel19icf06rh7&dl=1",
            "https://www.dropbox.com/scl/fi/0eu3w89lcwkqs5btp8a5k/Section3_Bild2.png?rlkey=45mwab7qd0xacp6d22ayzm3qx&dl=1",
            "https://www.dropbox.com/scl/fi/dn7vxf9lu5nvwet0rblkx/Section3_Bild3.png?rlkey=ec9c5vf07u85wqdvpk7njrlw5&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 8 Thema 3", 0),
        key=f"frage83_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img83} ausgewählt.")
    st.session_state.auswahl["Frage 8 Thema 3"] = img83

    st.text('Thema 4: Bedrohungen und Risiken\n- Listet die Hauptbedrohungen für Korallenriffe auf und beschreibt die Auswirkungen auf die Ökosysteme.\n\n')

    img84 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/g7y6t4x5u839snoz7ezoe/Section4_Bild3.png?rlkey=a8qay1a0f2lmjtztdskqpbbuz&dl=1",
            "https://www.dropbox.com/scl/fi/ximdgfpk6ecun7h3g3y0k/Section4_Bild6.png?rlkey=zih839oczwklst44rsxcdszq9&dl=1",
            "https://www.dropbox.com/scl/fi/psbgfg644bpwsje2katxl/Section4_Bild2.png?rlkey=j6cclb7bqystyk38xbzrz7iiu&dl=1",
            "https://www.dropbox.com/scl/fi/u8iieckut3ornzoaakyle/Section4_Bild8.png?rlkey=rolzqi3sqjpk5i5yv74nzco8e&dl=1",
            "https://www.dropbox.com/scl/fi/fryjjrakn9598y26hu5x2/Section4_Bild0.png?rlkey=vrpz6qi4ulo3gokweiv2n77lg&dl=1",
            "https://www.dropbox.com/scl/fi/8cvxh1yvxujf7g3ievszo/Section4_Bild4.png?rlkey=79ek4phf0dqy9e0uowkt6f5p9&dl=1",
            "https://www.dropbox.com/scl/fi/phynydzbrloue92yuvcjr/Section4_Bild7.png?rlkey=lki76aazrpbh3dofyh27ecmxi&dl=1",
            "https://www.dropbox.com/scl/fi/lr15onclk9qaw12gckyds/Section4_Bild1.png?rlkey=jk60061s6dky35j93uar5azv3&dl=1",
            "https://www.dropbox.com/scl/fi/5vu9097a2zhbp2km8py4f/Section4_Bild5.png?rlkey=ubafwsk4ycewuyhkf5hqevp97&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 8 Thema 4", 0),
        key=f"frage84_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img84} ausgewählt.")
    st.session_state.auswahl["Frage 8 Thema 4"] = img84

    st.text('Thema 5: Internationale und lokale Schutzstrategien\n- Erläutert internationale und nationale Schutzinitiativen für Korallenriffe und beschreibt Methoden der Öffentlichkeitsarbeit.\n\n')

    img85 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/h59faj0uycb9yrocxpc9h/Section5_Bild5.png?rlkey=778pgfe6z8yp1u3o9ccesg3pa&dl=1",
            "https://www.dropbox.com/scl/fi/w9pykdvnukoviwhthx1wn/Section5_Bild0.png?rlkey=kg5f53cb032f0iipax5567x9j&dl=1",
            "https://www.dropbox.com/scl/fi/9qkk8065q8qkxtxkww7so/Section5_Bild1.png?rlkey=sggg4uvtthjbkl1a8o9iuvot7&dl=1",
            "https://www.dropbox.com/scl/fi/tx238r576rirw73i6g4q6/Section5_Bild2.png?rlkey=5fwa0g5nevv5q22zf6v80qfs6&dl=1",
            "https://www.dropbox.com/scl/fi/tc4sn3l805vg3qjnotlgn/Section5_Bild7.png?rlkey=dj0hm7fzdd8c3giwo0szhwt3n&dl=1",
            "https://www.dropbox.com/scl/fi/420j34x5bfgyehxrlmpme/Section5_Bild4.png?rlkey=mrg574d7j1fr0m3st47t9q4jm&dl=1",
            "https://www.dropbox.com/scl/fi/7sea4klcmxc7bbmyy9mbz/Section5_Bild6.png?rlkey=wmtfnhmckm8t7b73yoq0lk60e&dl=1",
            "https://www.dropbox.com/scl/fi/nb1vmqv2t4rle723eb9gn/Section5_Bild3.png?rlkey=0ag5rukxb0cd6mwjiah9gcriz&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 8 Thema 5", 0),
        key=f"frage85_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img85} ausgewählt.")
    st.session_state.auswahl["Frage 8 Thema 5"] = img85

    st.button("(Nachfolgende) Frage 9", on_click=lambda: wechsel_zu("page9"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page9":
    st.title("Frage 9")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/0knuct3z6q2aychadomw5/Probekapitel_Ernaehrungsberater_Ernaehrungslehre_ENB01-B.pdf?rlkey=wzjxx58qeu0tuttsonm2up0x5&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Eine grundlegende Kenntnis der Ernährungsphysiologie beim Menschen erwerben und die wichtigsten Begriffe der Ernährungslehre verstanden haben.')

    st.text('Thema 1: Definition und Aufgaben der Ernährung – Grundbegriffe\n- Definiere "Ernährung" und "Stoffwechsel".\n- Erkläre die wichtigsten Baustoffe des menschlichen Körpers.\n- Liste die wichtigsten Nahrungsbestandteile auf.')

    img91 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 9 Thema 1", 0),
        key=f"frage91_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img91} ausgewählt.")
    st.session_state.auswahl["Frage 9 Thema 1"] = img91

    st.text('Thema 2: Der Energiebedarf des Menschen\n- Erkläre den Energiebedarf des Menschen und seine Entstehung.\n- Liste die Energiequellen in der Nahrung auf.\n- Zeige die Methoden zur Bestimmung des Energiebedarfs auf.')

    img92 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 9 Thema 2", 0),
        key=f"frage92_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img92} ausgewählt.")
    st.session_state.auswahl["Frage 9 Thema 2"] = img92

    st.text('Thema 3: Grundumsatz (Ruhe-Nüchtern-Umsatz oder Basal Metabolischer Rate)\n- Erkläre den Grundumsatz und seine Bestimmung.\n- Zeige die Faktoren ein, die den Grundumsatz beeinflussen.')

    img93 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/dp1bbp12tpqs7ur7w8e0x/Section3_Bild1.png?rlkey=zop4zq4ohhws7q4spqrw4muuw&dl=1",
            "https://www.dropbox.com/scl/fi/9iq1eoa9rln5c19sla90q/Section3_Bild0.png?rlkey=jnvip4s7dryna8sinztuo9zh0&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 9 Thema 3", 0),
        key=f"frage93_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img93} ausgewählt.")
    st.session_state.auswahl["Frage 9 Thema 3"] = img93

    st.text('Thema 4: Definitionen zum Körpergewicht\n- Erkläre die Bedeutung des idealen, normalen und realen Körpergewichts.\n- Zeige die Methoden zur Bestimmung des Körpergewichts auf.\n\n')

    img94 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/3mielsywau4rz7wspt4pc/Section4_Bild0.png?rlkey=3m5xru7nrqug1vbxn3bn1dmlk&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 9 Thema 4", 0),
        key=f"frage94_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img94} ausgewählt.")
    st.session_state.auswahl["Frage 9 Thema 4"] = img94

    st.text('Thema 5: Leistungsumsatz (Energieumsaetze fuer korperliche Aktivitaet)\n- Erkläre den Leistungsumsatz und seine Bestimmung.\n- Zeige die Faktoren ein, die den Leistungsumsatz beeinflussen.')

    img95 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/xg7436qv9kc139j0rk2rn/Section5_Bild0.png?rlkey=dabke4jjxr37b86gost55qk9z&dl=1",
            "https://www.dropbox.com/scl/fi/8p3mdqnfhb5kru4ztxzte/Section5_Bild1.png?rlkey=th9eka1lwbvnjh1axsc9waj6k&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 9 Thema 5", 0),
        key=f"frage95_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img95} ausgewählt.")
    st.session_state.auswahl["Frage 9 Thema 5"] = img95

    st.button("(Nachfolgende) Frage 10", on_click=lambda: wechsel_zu("page10"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

if st.session_state.seite == "page10":
    st.title("Frage 10")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/i49yeqlxua95tvrt23dxp/bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All.pdf?rlkey=0ewy30a7kuptj4fij5k9pv8n3&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Ziel: Bericht über die Entdeckung und Bedeutung von Gravitationswellen durch Ligo und Virgo.')

    st.text('Thema 1: Was sind Gravitationswellen?\n- Gravitationswellen sind Wellen im Raum, die durch die Bewegung von massereichen Objekten wie Schwarzen Löchern oder Neutronensternen erzeugt werden.\n\n')

    img101 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/tppnl7djr3env7heljjo5/Section1_Bild0.png?rlkey=ao83v8x4nhtmbatqfn0bujxc8&dl=1",
            "https://www.dropbox.com/scl/fi/s1jxwj4dg2r893hmqjvhs/Section1_Bild2.png?rlkey=8e5sanfdd6zcjklzq7kjt5ro0&dl=1",
            "https://www.dropbox.com/scl/fi/yj9pmqq4e87hjnj3vrxx7/Section1_Bild4.png?rlkey=jzrepae1zwpzj7gytzku5d0ac&dl=1",
            "https://www.dropbox.com/scl/fi/1jlon2c35z9yk93cnn4q7/Section1_Bild1.png?rlkey=4xeq32cukirmijgriuo8to70c&dl=1",
            "https://www.dropbox.com/scl/fi/9pw0ciyltw47kkm1o4ge8/Section1_Bild3.png?rlkey=i7csn1547esm3tbdfunvsetmu&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 10 Thema 1", 0),
        key=f"frage101_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img101} ausgewählt.")
    st.session_state.auswahl["Frage 10 Thema 1"] = img101

    st.text('Thema 2: Erstmalige Entdeckung\n- Am 14. September 2015 wurde die erste Gravitationswelle offiziell bekanntgegeben, die von Ligo in Louisiana und Virgo in Italien gemessen wurde.\n\n')

    img102 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/pix3x0fnv58czwhju8m6e/Section2_Bild1.png?rlkey=zyit4dcls0n8f66lea48c2nov&dl=1",
            "https://www.dropbox.com/scl/fi/a1qegn3ymm72r77pgqbfk/Section2_Bild3.png?rlkey=vsaqolzhu5lkt0l3rdt2z2a3c&dl=1",
            "https://www.dropbox.com/scl/fi/25he9so8hqcp9a046d37a/Section2_Bild0.png?rlkey=2sy19qzcyx68ijrb4fqpzxzxd&dl=1",
            "https://www.dropbox.com/scl/fi/s679vybmhvpnxjananidx/Section2_Bild2.png?rlkey=7n3t7mav2k27fx6i5pudfz1g9&dl=1",
            "https://www.dropbox.com/scl/fi/fjwwuj8eflf1qku8r52db/Section2_Bild8.png?rlkey=4j2lowhj9su72n3s492zd9thn&dl=1",
            "https://www.dropbox.com/scl/fi/tglmrtauulhkk11hzuc7f/Section2_Bild6.png?rlkey=p7tqx2lqzxw8n114yshtf007z&dl=1",
            "https://www.dropbox.com/scl/fi/uot0bjy7fkvcaicmddzgx/Section2_Bild4.png?rlkey=krb0wlg9gq95jy51dc4t1y02t&dl=1",
            "https://www.dropbox.com/scl/fi/phgf5gpad2cq0tp00gibb/Section2_Bild5.png?rlkey=ekepzojdzol28a03is8vsm349&dl=1",
            "https://www.dropbox.com/scl/fi/yjbaybqygvus5pppmlwga/Section2_Bild7.png?rlkey=s0y3athhdetkhaxocqx0kz9ym&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 10 Thema 2", 0),
        key=f"frage102_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img102} ausgewählt.")
    st.session_state.auswahl["Frage 10 Thema 2"] = img102

    st.text('Thema 3: Technische Herausforderungen\n- Durch die Messung von Gravitationswellen gelang es erstmals, die Raumzeit selbst zu messen und dadurch astronomische Ereignisse zu beobachten, die sonst nicht sichtbar sind.\n\n')

    img103 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/1l944s9pf5ql18s32sx3n/Section3_Bild5.png?rlkey=uccziska4sfbzxw2nwq8rmulr&dl=1",
            "https://www.dropbox.com/scl/fi/atr1zz89mh2d802wmbx34/Section3_Bild1.png?rlkey=1tt7kwnjede7rllgmjcdnnxoz&dl=1",
            "https://www.dropbox.com/scl/fi/xdxmzppyrm939xphiybo5/Section3_Bild0.png?rlkey=pcn2osqknv3ijhmn1ocvmhpcw&dl=1",
            "https://www.dropbox.com/scl/fi/e6mr9xk397tgcadcgduqj/Section3_Bild4.png?rlkey=lgmx0nr0bgevk4t5646po7agu&dl=1",
            "https://www.dropbox.com/scl/fi/c4vwyzk2ucgdxs7alv22u/Section3_Bild2.png?rlkey=1nbqrd6eskuwqgsc6hdiv1ine&dl=1",
            "https://www.dropbox.com/scl/fi/4o46p6lhqn1rgczut68rd/Section3_Bild3.png?rlkey=zjowm3738kjrci7fk5ug49iwd&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 10 Thema 3", 0),
        key=f"frage103_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img103} ausgewählt.")
    st.session_state.auswahl["Frage 10 Thema 3"] = img103

    st.text('Thema 4: Bedeutung für die Physik und Astronomie\n- Die Messungen von Gravitationswellen liefern neue Einsichten in die Allgemeine Relativitätstheorie und helfen, die Entstehung und Entwicklung von Galaxien zu verstehen.\n\n')

    img104 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/sg7zzkfggrzbnl2w1x1ws/Section4_Bild3.png?rlkey=o17jg0ga1ttn4b1536dcl1vsh&dl=1",
            "https://www.dropbox.com/scl/fi/gtxjghmlw7fkka395etqo/Section4_Bild6.png?rlkey=rlnu0e9vkqlo1q5yuc2epmf0z&dl=1",
            "https://www.dropbox.com/scl/fi/q3j3ogiczp9r41npmlizy/Section4_Bild2.png?rlkey=lcbr5fhyehie0uawov3w8o1l3&dl=1",
            "https://www.dropbox.com/scl/fi/e9cj6h0y622duuoojro74/Section4_Bild0.png?rlkey=dpx77kdbg84uon5qmw9jzcmjr&dl=1",
            "https://www.dropbox.com/scl/fi/c5j7p82h5hj5pbs0zqepf/Section4_Bild4.png?rlkey=v2m553few0nu6kve7h443dn55&dl=1",
            "https://www.dropbox.com/scl/fi/wunjnbaquedzvrezno2cn/Section4_Bild7.png?rlkey=kte0rpv2m8cakuh6vwhalpicv&dl=1",
            "https://www.dropbox.com/scl/fi/3bzzej7hvggzic78gmprz/Section4_Bild1.png?rlkey=kx14149hyhik51xe032lmvu1i&dl=1",
            "https://www.dropbox.com/scl/fi/2gkugmr4ftm36embsb059/Section4_Bild5.png?rlkey=lmvver22yt7uecuia3iyiclnk&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 10 Thema 4", 0),
        key=f"frage104_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img104} ausgewählt.")
    st.session_state.auswahl["Frage 10 Thema 4"] = img104

    st.text('Thema 5: Perspektive für die Zukunft\n- Aufbauend auf den Erfahrungen mit Ligo und Virgo werden weitere Experimente wie Advanced Ligo und Kagra angestrebt, um die Reichweite und Empfindlichkeit der Messungen zu steigern und neue Erkenntnisse zu erhalten.\n\n')

    img105 = image_select(
        "Label",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/bnmrpj13da62cocwj6dk7/Section5_Bild5.png?rlkey=bvbx7iqawl5bqik33r92g0cx8&dl=1",
            "https://www.dropbox.com/scl/fi/r4jnt9f9e3f3s6zh618mj/Section5_Bild8.png?rlkey=oy393bkeog3rn7fhb043m427j&dl=1",
            "https://www.dropbox.com/scl/fi/d3yv5aaef6hsxnn9c3vr6/Section5_Bild0.png?rlkey=11kqi6yy3fc8uhlmxurvjfxff&dl=1",
            "https://www.dropbox.com/scl/fi/lzwketfvnbmntgj0u54u9/Section5_Bild1.png?rlkey=nyc65hf7m5albuwba9rve6qb2&dl=1",
            "https://www.dropbox.com/scl/fi/2omahz3rsov73w8ur85ae/Section5_Bild2.png?rlkey=5svxjhkrss3y0zqrkt3muov8n&dl=1",
            "https://www.dropbox.com/scl/fi/2mwjervc7ia0huix1n6g3/Section5_Bild7.png?rlkey=jqct4o8nsgqjtgzf5gxmkkqee&dl=1",
            "https://www.dropbox.com/scl/fi/fnymz4jvu54eiak64czic/Section5_Bild4.png?rlkey=312o2c5ddr1amlax5p9cmn2h9&dl=1",
            "https://www.dropbox.com/scl/fi/vpr0jv23fekvxpbtji11z/Section5_Bild6.png?rlkey=eocd69toknq6ixpl1zgvbdna6&dl=1",
            "https://www.dropbox.com/scl/fi/d107y3a63cqwh7729x6ak/Section5_Bild3.png?rlkey=1v0otsfz9rhchcui73hyeekdt&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=st.session_state.auswahl.get("Frage 10 Thema 5", 0),
        key=f"frage105_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img105} ausgewählt.")
    st.session_state.auswahl["Frage 10 Thema 5"] = img105

    st.button("(Nachfolgende) Frage 11", on_click=lambda: wechsel_zu("page11"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 8, 9]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Frage {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

elif st.session_state.seite == "auswertung":
    st.title("Auswertung")
    st.write("Du hast diese Bilder gewählt:")

    auswertung_text = ""
    letzte_frage = ""

    for key, value in sorted(st.session_state.auswahl.items()):
        frage, thema = key.split(" Thema ")
        if frage != letzte_frage:
            auswertung_text += f"\n{frage}:\n"
            letzte_frage = frage
        auswertung_text += f"  Thema {thema} → Bild {value}\n"

    st.text(auswertung_text.strip())

    encoded_body = urllib.parse.quote(auswertung_text)
    mailto_link = f"mailto:jstrauch@pagemachine.de?subject=Bilder-Umfrage&body={encoded_body}"

    if st.button("Ergebnis per E-Mail senden"):
        dummy_id = uuid.uuid4()
        js_code = f"""
        const dummy = \"{dummy_id}\";
        window.open(\"{mailto_link}\");
        """
        st.components.v1.html(f"<script>{js_code}</script>", height=0)

    st.button("Ändern", on_click=lambda: wechsel_zu("page1"))
