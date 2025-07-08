import streamlit as st
from streamlit_image_select import image_select
from streamlit_scroll_to_top import scroll_to_here
import urllib.parse
import uuid

if "email_count" not in st.session_state:
    st.session_state.email_count = 0

if "seite" not in st.session_state:
    st.session_state.seite = "start"

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

if st.session_state.seite == "start":
    st.title("Erklärung")
    st.text(text.replace("Im Folgenden", "Auf den nachfolgenden Seiten"))
    st.text(
        "Im Folgenden siehst du einige Beispiele, die veranschaulichen sollen, "
        "wie eine Auswahl getroffen werden kann. "
        "Es handelt sich lediglich um Beispiele – eine Auswahl ist hier nicht erforderlich."
    )

    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()

    st.text("Beispiel 1")
    st.text(
        "Thema 3: Was Menschenaffen bedroht\n"
        "- Identifiziert Lebensraumverlust, Wilderei und Krankheitsübertragung "
        "als zentrale Gefährdungen für das Überleben der Menschenaffen.\n"
    )
    img63 = image_select(
        "Auswahl:",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/bf18fv2si62f8naro66sj/Section3_Bild5.png?rlkey=zutrwmjgin0d0jgo8qtiscte9&dl=1",
            "https://www.dropbox.com/scl/fi/ob662h63qtnq2egvt2qxl/Section3_Bild1.png?rlkey=s8m19j27xsuzafp7ywd5f9d1v&dl=1",
            "https://www.dropbox.com/scl/fi/q59p8eewm3baqp5tjv7bg/Section3_Bild0.png?rlkey=35sms7zc1mgb1oa58n986azvq&dl=1",
            "https://www.dropbox.com/scl/fi/g4fujb7yj006klnxf0r8x/Bsp1_Wahl.png?rlkey=0i9tsshdrngsa05acbish8di7&dl=1",
            "https://www.dropbox.com/scl/fi/51pjhoeqjxekj9o6529do/Section3_Bild2.png?rlkey=6zamdzg38px5a2d3j8l8aq9fw&dl=1",
            "https://www.dropbox.com/scl/fi/o0iiha9hc9k0wo5hi5xs7/Section3_Bild3.png?rlkey=8qfalj5szr5ga7mkzn7k261ut&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=0,
        key=f"bsp_1_{st.session_state.reload_counter}"
    )

    st.text("Gute Wahl:")
    bsp1_arr = [
        "https://www.dropbox.com/scl/fi/g4fujb7yj006klnxf0r8x/Bsp1_Wahl.png?rlkey=0i9tsshdrngsa05acbish8di7&dl=1",
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
    ]
    bsp1_tmp = st.session_state.reload_counter % 2
    if bsp1_tmp == 0:
        st.image(bsp1_arr[0 if bsp1_tmp == 0 else 1])
    else:
        st.image(bsp1_arr[0 if bsp1_tmp == 1 else 1])

    st.text("Auswahl Nr. 4 ist als Wahl sinnvoll da es denn die im Text beschriebenen Dinge gut visualisiert.")

    st.text("Beispiel 2")
    st.text(
        "Thema 6: Astronomische Mediendatenbanken\n"
        "- Stellt die RPIF als internationales Netzwerk von Bilddatenbanken unter Leitung der NASA vor, "
        "mit Fokus auf astronomische Bilder, Daten und Dokumentationen.\n"
    )

    img55 = image_select(
        "Auswahl:",
        [
            "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
            "https://www.dropbox.com/scl/fi/x528mv52jfn69fxx7s254/Bsp2_Wahl.png?rlkey=xnh9bswf81grc9cyh6epvomz1&dl=1",
            "https://www.dropbox.com/scl/fi/45wvymwziunnfd1zsursw/Section5_Bild1.png?rlkey=xf6arwcz6dp3l051a88u7dmh8&dl=1",
            "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        ],
        return_value="index",
        index=0,
        key=f"bsp_2_{st.session_state.reload_counter}"
    )

    st.text("Weniger passende Wahl:")
    bsp2_arr = [
       "https://www.dropbox.com/scl/fi/x528mv52jfn69fxx7s254/Bsp2_Wahl.png?rlkey=xnh9bswf81grc9cyh6epvomz1&dl=1",
       "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
    ]
    bsp2_tmp = st.session_state.reload_counter % 2
    if bsp2_tmp == 0:
        st.image(bsp2_arr[0 if bsp2_tmp == 0 else 1])
    else:
        st.image(bsp2_arr[0 if bsp2_tmp == 1 else 1])

    st.text(
        "Auch wenn das Bild thematisch passt, bietet ein Logo als visuelles Element keinen nennenswerten Mehrwert für die inhaltliche Beschreibung."
    )

    st.button(f"Frage 1", on_click=lambda s=f"page1": wechsel_zu(s))
    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))
    st.button("Nach oben scrollen", on_click=scroll())
if st.session_state.seite == "page1":
    st.title("Seite 1")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/b8xnfbn9suybhooe5vhj9/40410000.pdf?rlkey=mewyd9ixhbscneamy9dks31s9&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide detailed information on the German Federal Parliament (Bundestag) during its 20th term, including its roles, structures, buildings, members, and election process.')

    st.text("Topic 1: Functions of the Bundestag\n- Outlines the role of the Bundestag as Germany's sole directly elected constitutional organ responsible for making federal laws, electing the chancellor, controlling the government, and participating in appointing various officials.\n\n")

    tmp11 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/zfqxjvodiy9zc1okmdjyl/Section1_Bild0.png?rlkey=ojnei2sc1uzrfbbh2w68l0ojp&dl=1",
        "https://www.dropbox.com/scl/fi/k7oeapd8my6qtwljbqr7q/Section1_Bild2.png?rlkey=v9amfpbtf523or8xom84eyl6j&dl=1",
        "https://www.dropbox.com/scl/fi/uzfhqmyci9qze2v7i5xqt/Section1_Bild1.png?rlkey=1mdwt8p5wv53n0qkznheaybqq&dl=1",
    ]
    img11 = image_select(
        "Auswahl:",
        tmp11,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 1", 0),
        key=f"frage11_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img11} ausgewählt.")
    st.session_state.auswahl["Seite 1 Thema 1"] = img11
    st.image(tmp11[st.session_state.auswahl.get("Seite 1 Thema 1", 0)])
    st.text('Topic 2: Composition of the Bundestag\n- Details how the parliament consists of 734 representatives who are chosen through direct elections every four years, with parties needing at least five percent support nationwide to enter the legislature unless they represent minority groups.\n\n')

    tmp12 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/jkyj2h2d65zdujlakv1di/Section2_Bild1.png?rlkey=2hsld6a220hh9pbbv26zm7z4l&dl=1",
        "https://www.dropbox.com/scl/fi/tasvnlwpjuyapxdajsdlp/Section2_Bild3.png?rlkey=33zgqiprb1oq27k7j9m5y7eof&dl=1",
        "https://www.dropbox.com/scl/fi/u05nbpdigebourazrwq5x/Section2_Bild0.png?rlkey=w2u9nnufhjpxurdvar4mbh12v&dl=1",
        "https://www.dropbox.com/scl/fi/7ly5ng5lxrza8o7sqh3fp/Section2_Bild2.png?rlkey=5jhilowov2xs6ame7z3fgvbad&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img12 = image_select(
        "Auswahl:",
        tmp12,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 2", 0),
        key=f"frage12_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img12} ausgewählt.")
    st.session_state.auswahl["Seite 1 Thema 2"] = img12
    st.image(tmp12[st.session_state.auswahl.get("Seite 1 Thema 2", 0)])
    st.text('Topic 3: Key Figures During the 20th Term\n- Introduces the coalition government formed by the Social Democratic Party (SPD), Alliance 90/The Greens, and Free Democrats (FDP), along with notable individuals like Chancellor Olaf Scholz, Vice President Bärbel Bas, and party leaders within each group.\n\n')

    tmp13 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/dr0k4cdwav1potf844l1d/Section3_Bild1.png?rlkey=alyp21jg5onxntbv5qwho6etx&dl=1",
        "https://www.dropbox.com/scl/fi/ny1vpuqlk50csqs6x9iux/Section3_Bild0.png?rlkey=jenmpsliuae1i78usoes0uhga&dl=1",
        "https://www.dropbox.com/scl/fi/r1sygqo4p17i1u67o6v79/Section3_Bild2.png?rlkey=o1c04qx4z60yaumo1ahz8hmcs&dl=1",
        "https://www.dropbox.com/scl/fi/fjdk6qbwwom7fwswmv1fr/Section3_Bild3.png?rlkey=z5epguu8g0n9qsdq2y5cc6xtr&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img13 = image_select(
        "Auswahl:",
        tmp13,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 3", 0),
        key=f"frage13_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img13} ausgewählt.")
    st.session_state.auswahl["Seite 1 Thema 3"] = img13
    st.image(tmp13[st.session_state.auswahl.get("Seite 1 Thema 3", 0)])
    st.text('Topic 4: Important Buildings Used by the Bundestag\n- Overviews several key locations used by the parliament, including the iconic Reichstag building, the Paul-Loebe House, the Marie-Elisabeth-Lueders House, the Jakob-Kaiser House, and the newly constructed Luisenblock West.\n\n')

    tmp14 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/h81xdyau83ujmxfo8sglw/Section4_Bild3.png?rlkey=y7b32p7jhcdhd1pj1o7sl5pfb&dl=1",
        "https://www.dropbox.com/scl/fi/2wv22g5sx6twe0ebq3zoo/Section4_Bild2.png?rlkey=x5lq52px1arcd6h6ltihwieff&dl=1",
        "https://www.dropbox.com/scl/fi/dxm3ionlfexeo98za1yzy/Section4_Bild0.png?rlkey=klvq8vy7m296h4gsws6dkbrkp&dl=1",
        "https://www.dropbox.com/scl/fi/2tf8vbrb509aie4t8fcj6/Section4_Bild1.png?rlkey=941q4529zy3ek2krkfue3mvwu&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img14 = image_select(
        "Auswahl:",
        tmp14,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 4", 0),
        key=f"frage14_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img14} ausgewählt.")
    st.session_state.auswahl["Seite 1 Thema 4"] = img14
    st.image(tmp14[st.session_state.auswahl.get("Seite 1 Thema 4", 0)])
    st.text('Topic 5: Process of Electing Members and Passing Laws\n- Breaks down the steps involved in passing legislation, starting with proposal submission followed by committee review, debate, voting, and final approval before becoming law. Also explains the procedure for choosing the chancellor and other high-level positions.\n\n')

    tmp15 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/kp9ol1kjzd68noksyabjd/Section5_Bild0.png?rlkey=6zb3og3bnbpfmnlsjrmz6t8dg&dl=1",
        "https://www.dropbox.com/scl/fi/xnzfyb1d89i6y24hkki0j/Section5_Bild1.png?rlkey=tj7kzy22nubr0t16nhxt8poo0&dl=1",
        "https://www.dropbox.com/scl/fi/yozszwensttyxool9hv4q/Section5_Bild2.png?rlkey=cpugxh6yqum9a4b43h1fnb7la&dl=1",
        "https://www.dropbox.com/scl/fi/lfquwhk2kx1w5mirjdtxr/Section5_Bild3.png?rlkey=so7q9fhrgg28yuyq32psxbr1m&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img15 = image_select(
        "Auswahl:",
        tmp15,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 5", 0),
        key=f"frage15_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img15} ausgewählt.")
    st.session_state.auswahl["Seite 1 Thema 5"] = img15
    st.image(tmp15[st.session_state.auswahl.get("Seite 1 Thema 5", 0)])
    st.button("(Nachfolgende) Seite 2", on_click=lambda: wechsel_zu("page2"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [3, 4, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page2":
    st.title("Seite 2")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/owtdmytwjgxtq0bcdcbxv/potenzial_der_windenergie.pdf?rlkey=xkfasmj27usqr5cgkb3pwbf7n&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Determine the maximum achievable wind energy production potential in Germany considering technological advancements, geographical distribution, and environmental implications.')

    st.text('Topic 1: Available Area Calculation & Reference Turbine Types\n- Details methodologies for calculating usable space for wind farms after accounting for restricted zones and presents two primary wind turbine models under evaluation.')

    st.text('Topic 2: Potential Power Generation Capacity & Regional Variability\n- Quantifies overall possible electricity generation capacity across Germany along with regional differences in suitability for wind energy projects.')

    st.text('Topic 3: Modern Technological Advancements & Sound Requirements Near Residences\n- Elaborates on improvements in wind turbine design enabling exploration of interior lands owing to increased height and reduced noise levels complying with urban regulations.')

    st.text('Topic 4: Ecological Restrictions & Practical Limitations\n- Identifies challenges posed by nature preservation laws, military installations, and local planning policies when implementing wind farms.')

    st.text('Topic 5: Comparison Between Realistic Implementation & Maximum Possible Output\n- Compares the realizable wind energy potential against theoretical estimates highlighting significant discrepancies caused by practical obstacles discussed throughout the report.\n\n')

    tmp25 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/t55mee3sfxq4m7lnduvgr/Section5_Bild0.png?rlkey=6mm5ib9my1mplf242m0kyk2no&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img25 = image_select(
        "Auswahl:",
        tmp25,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 2 Thema 5", 0),
        key=f"frage25_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img25} ausgewählt.")
    st.session_state.auswahl["Seite 2 Thema 5"] = img25
    st.image(tmp25[st.session_state.auswahl.get("Seite 2 Thema 5", 0)])
    st.button("(Nachfolgende) Seite 3", on_click=lambda: wechsel_zu("page3"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 4, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page3":
    st.title("Seite 3")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/azcxzjvsose6ojegh548b/Probe345Bd93.pdf?rlkey=7odduh6lqrolhemk8uox7qkm5&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Investigate the history, characteristics, distribution, threats, conservation efforts, and educational programs regarding dinosaurs.')

    st.text("Topic 1: History and Origin\n- Discusses when dinosaurs first emerged during Earth's history and how they evolved into various groups like sauropods, theropods, ceratopsians, and others.\n\n")

    tmp31 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/f6poki219ikeuis6dviqg/Section1_Bild0.png?rlkey=0c5v26jbu31zv1cjpnp6okw48&dl=1",
        "https://www.dropbox.com/scl/fi/88teazr6gybdhmkxrbv3c/Section1_Bild6.png?rlkey=ox1ro2q5or0m372lset8t3062&dl=1",
        "https://www.dropbox.com/scl/fi/lguc2369qc6a6tba2d5tf/Section1_Bild2.png?rlkey=9fo0e5ndg56wjosgrd0xunjfx&dl=1",
        "https://www.dropbox.com/scl/fi/s3n6panp30neqnqsy4qk5/Section1_Bild5.png?rlkey=7wdbzlr3kak0j9wstg4rgt83x&dl=1",
        "https://www.dropbox.com/scl/fi/2n2smnr9dj2wncdra7l79/Section1_Bild7.png?rlkey=tvb3xcki53346gqgmyc80dmpf&dl=1",
        "https://www.dropbox.com/scl/fi/qk0rr2ojv07hi72km5ubf/Section1_Bild8.png?rlkey=2hcd5sqhov20ezacnwjaxz3op&dl=1",
        "https://www.dropbox.com/scl/fi/65hwd2crflodgp9bmpeec/Section1_Bild1.png?rlkey=xwrsxlj9047khehhm67permqz&dl=1",
    ]
    img31 = image_select(
        "Auswahl:",
        tmp31,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 1", 0),
        key=f"frage31_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img31} ausgewählt.")
    st.session_state.auswahl["Seite 3 Thema 1"] = img31
    st.image(tmp31[st.session_state.auswahl.get("Seite 3 Thema 1", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp31 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/mud555cy7cgdec749kylz/Section1_Bild4.png?rlkey=08illts8i8on32ck7sgmzy8nx&dl=1",
        "https://www.dropbox.com/scl/fi/87a7xfohc544q62x2pepz/Section1_Bild3.png?rlkey=cf3yz9fl7rm0omzu9nz8o7l2t&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg31 = image_select(
        "Auswahl:",
        nvtmp31,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 3 Thema 1", 0),
        key=f"nvfrage31_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg31} ausgewählt.")
    st.session_state.auswahl["nv Seite 3 Thema 1"] = nvimg31
    st.image(nvtmp31[st.session_state.auswahl.get("nv Seite 3 Thema 1", 0)])

    st.text('Topic 2: Physical Features and Adaptations\n- Details the body structure, limbs, skull shape, and specializations found among different types of dinosaurs, such as the development of wings in pterosaurs and feathers in certain therapods.\n\n')

    tmp32 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/4ogkxkn958dpw71r4mhs7/Section2_Bild1.png?rlkey=yrbsk6ot133iqg59hs2zc3iwp&dl=1",
        "https://www.dropbox.com/scl/fi/cqgy8l09dlyy06q1eoiag/Section2_Bild3.png?rlkey=tvepa2r8u2ghncr5gupqttsx0&dl=1",
        "https://www.dropbox.com/scl/fi/cxmizx1pt855eu1l6efwy/Section2_Bild0.png?rlkey=icca13m7iurs3iluch9n82ir1&dl=1",
        "https://www.dropbox.com/scl/fi/kiiwgwenu22q4jtjka9hy/Section2_Bild2.png?rlkey=3ozmkktckgcioxd4su1z3j8kr&dl=1",
        "https://www.dropbox.com/scl/fi/3wr46v0lpp72vf3v4b0di/Section2_Bild8.png?rlkey=txcoow4mru00v2zndykudn17f&dl=1",
        "https://www.dropbox.com/scl/fi/i9wkcspba8thf1h0cv93h/Section2_Bild6.png?rlkey=6g3mpi1jy436lga50hgr6klp3&dl=1",
        "https://www.dropbox.com/scl/fi/ypky0137ijo4p5z75u4pi/Section2_Bild4.png?rlkey=ncdzxwh6635zwzowghconc7sn&dl=1",
        "https://www.dropbox.com/scl/fi/lq9iopmscufepmxcqhdqj/Section2_Bild5.png?rlkey=y05hprbee0195s2q8koq56qsu&dl=1",
        "https://www.dropbox.com/scl/fi/wx3w4xc75fgm2wicz6kjy/Section2_Bild7.png?rlkey=23kjmwq6oml3anjc0ap23jjy3&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img32 = image_select(
        "Auswahl:",
        tmp32,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 2", 0),
        key=f"frage32_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img32} ausgewählt.")
    st.session_state.auswahl["Seite 3 Thema 2"] = img32
    st.image(tmp32[st.session_state.auswahl.get("Seite 3 Thema 2", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp32 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/bobsgfsobtbnfffa7wkyc/Section2_Bild10.png?rlkey=64fmf1na0hjhirp2ivwgkltmr&dl=1",
        "https://www.dropbox.com/scl/fi/uekdjrgymf00z96j5mopw/Section2_Bild9.png?rlkey=bdivw7gigk3ybhdt36rjh1mtm&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg32 = image_select(
        "Auswahl:",
        nvtmp32,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 3 Thema 2", 0),
        key=f"nvfrage32_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg32} ausgewählt.")
    st.session_state.auswahl["nv Seite 3 Thema 2"] = nvimg32
    st.image(nvtmp32[st.session_state.auswahl.get("nv Seite 3 Thema 2", 0)])

    st.text('Topic 3: Diet and Food Source\n- Elucidates what dinosaurs ate based on fossil evidence, ranging from plants to meat depending on the specific type of dinosaur.\n\n')

    tmp33 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/oxmmdcueeriudwwsb51kz/Section3_Bild5.png?rlkey=uj6sokm6ud8jih3yv3ijf7x9m&dl=1",
        "https://www.dropbox.com/scl/fi/awa9qxsq4tdaz2ve4a44v/Section3_Bild1.png?rlkey=zgjdapg7l75fuibjv5l52p41x&dl=1",
        "https://www.dropbox.com/scl/fi/dzmhq92acnx7k64e3j9bz/Section3_Bild0.png?rlkey=l3wudb2z6mwuqcj1257oo0mrj&dl=1",
        "https://www.dropbox.com/scl/fi/a0mcifv4ebobqa99x4ftg/Section3_Bild4.png?rlkey=iabrii5zt36i8li5i5iwf25k3&dl=1",
        "https://www.dropbox.com/scl/fi/sc8moizkbqqn4b98flqba/Section3_Bild2.png?rlkey=vyt0wrvton859jbvjze8kesg2&dl=1",
        "https://www.dropbox.com/scl/fi/1f5yni1fsip0pcf8051m1/Section3_Bild3.png?rlkey=ype0exh7t1k3zofv25eh2ccxr&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img33 = image_select(
        "Auswahl:",
        tmp33,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 3", 0),
        key=f"frage33_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img33} ausgewählt.")
    st.session_state.auswahl["Seite 3 Thema 3"] = img33
    st.image(tmp33[st.session_state.auswahl.get("Seite 3 Thema 3", 0)])
    st.text('Topic 4: Global Presence and Range\n- Outlines the spread of dinosaurs across continents throughout the Mesozoic Era, including their presence in both tropical regions and near the poles.\n\n')

    tmp34 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/3cgyehlmlc7t9nk8c6hff/Section4_Bild3.png?rlkey=j7lmxxhtalf0rky0mduuv8olt&dl=1",
        "https://www.dropbox.com/scl/fi/db9tky51ac699ozy3rr1f/Section4_Bild2.png?rlkey=l6nxpwl75unyjgxkjjtx4phtq&dl=1",
        "https://www.dropbox.com/scl/fi/qglfk2dz3o7hip6tf27gx/Section4_Bild0.png?rlkey=i8ytbzlhyjvrks1yvethdfdtk&dl=1",
        "https://www.dropbox.com/scl/fi/k6n3ttwkj743glnorv459/Section4_Bild4.png?rlkey=346poj5dnwunq9nwvlsvlljh9&dl=1",
        "https://www.dropbox.com/scl/fi/mh0dxbqgowyr91l1e4j8f/Section4_Bild1.png?rlkey=0jngaob31vkhuab04clqznjxg&dl=1",
        "https://www.dropbox.com/scl/fi/jggrl6a32h0fftkbq7edz/Section4_Bild5.png?rlkey=5c0i5qyk7th4z4s3xi2fc2tlv&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img34 = image_select(
        "Auswahl:",
        tmp34,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 4", 0),
        key=f"frage34_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img34} ausgewählt.")
    st.session_state.auswahl["Seite 3 Thema 4"] = img34
    st.image(tmp34[st.session_state.auswahl.get("Seite 3 Thema 4", 0)])
    st.text('Topic 5: Decline and Extinction\n- Addresses theories behind why dinosaurs went extinct around 65 million years ago, focusing on potential factors like meteor impacts, volcanic activity, climate change, and competition with early mammals.\n\n')

    tmp35 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/7btgbwayg6xwyzpxxf5pa/Section5_Bild5.png?rlkey=kifg02bddrbafqavu2892pjst&dl=1",
        "https://www.dropbox.com/scl/fi/jmxjw70kub08a54c4bwfj/Section5_Bild8.png?rlkey=n9yzo9fw81rhkhet8ctfzcgra&dl=1",
        "https://www.dropbox.com/scl/fi/dzfmatz1y54b0dr20y56j/Section5_Bild0.png?rlkey=zw0ujfl25y56peokos8shlmnc&dl=1",
        "https://www.dropbox.com/scl/fi/8vs38oiqtse8r16taidiw/Section5_Bild1.png?rlkey=eszzw94gcz1teov7nvs6iatpk&dl=1",
        "https://www.dropbox.com/scl/fi/l205z8pgo6i0j2yh0jhdt/Section5_Bild2.png?rlkey=y7nh3nndb64b14943yyjj4hsm&dl=1",
        "https://www.dropbox.com/scl/fi/vb5qljvpndndglvxfqqzj/Section5_Bild7.png?rlkey=028srn3m6bl2p8045r5tgvxxl&dl=1",
        "https://www.dropbox.com/scl/fi/cpfx693cxyf6x7u9xofra/Section5_Bild4.png?rlkey=53kpcgund7nko9y3ebv9sqz4p&dl=1",
        "https://www.dropbox.com/scl/fi/128kr974kvte9voqh6am7/Section5_Bild6.png?rlkey=f4kkzgkx5mh7zupxy8xiejr7n&dl=1",
        "https://www.dropbox.com/scl/fi/3g43rl1dlzl0i8u3g7m0v/Section5_Bild3.png?rlkey=negsormlk1hxhmp2e9c2rkvj3&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img35 = image_select(
        "Auswahl:",
        tmp35,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 5", 0),
        key=f"frage35_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img35} ausgewählt.")
    st.session_state.auswahl["Seite 3 Thema 5"] = img35
    st.image(tmp35[st.session_state.auswahl.get("Seite 3 Thema 5", 0)])
    st.button("(Nachfolgende) Seite 4", on_click=lambda: wechsel_zu("page4"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 5, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page4":
    st.title("Seite 4")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/iyv9yl773seq19etmhriv/Zweiter_Weltkrieg_01.pdf?rlkey=2s7gk93ldax54v383aqrxa6bj&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text("Goal: To provide historical context on the causes, events, and consequences of World War II, particularly focusing on Austria's role during this period.")

    st.text('Topic 1: Pre-World War II Era\n- Details the dissolution of the monarchy in Austria-Hungary after World War I, establishment of the First Republic, Treaties of Versailles and Saint Germain assigning blame for World War I to Germany and Austria, economic struggles faced by the new republic in the 1920s.\n\n')

    tmp41 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/v1rfw1xx5kp7ftcxxrcca/Section1_Bild0.png?rlkey=cb26u6jua0nzm82y1fbetuzhm&dl=1",
        "https://www.dropbox.com/scl/fi/i4yxmdgwz8rgbmikq50eb/Section1_Bild2.png?rlkey=m73iq2oih8xnyqkaykyrxx5fi&dl=1",
        "https://www.dropbox.com/scl/fi/n78aqw6wvivv3hxkiqqjo/Section1_Bild1.png?rlkey=ccci67js2g2peenicfsi3rt21&dl=1",
        "https://www.dropbox.com/scl/fi/98xts6wyupmcmv26bvc7h/Section1_Bild3.png?rlkey=v7ly910j6912152abzgp4czdd&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img41 = image_select(
        "Auswahl:",
        tmp41,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 1", 0),
        key=f"frage41_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img41} ausgewählt.")
    st.session_state.auswahl["Seite 4 Thema 1"] = img41
    st.image(tmp41[st.session_state.auswahl.get("Seite 4 Thema 1", 0)])
    st.text('Topic 2: Authoritarian State and Annexation of Austria\n- Outlines political radicalization leading to the "authoritative state" under Chancellor Engelbert Dollfüss, his assassination followed by continuance of policies under Kurt Schuschnigg; discusses the 1938 annexation ("Anschluss") of Austria into Nazi Germany, popular support among some Austrian citizens.\n\n')

    tmp42 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/xn7f8ulfngz68hzxmb539/Section2_Bild1.png?rlkey=82zsbdgoj0inhhif4kqn48d64&dl=1",
        "https://www.dropbox.com/scl/fi/5omys06pxsgn3zfxt3onr/Section2_Bild3.png?rlkey=4r69wbc7tub7euskz79drxuzw&dl=1",
        "https://www.dropbox.com/scl/fi/tt0vy10nhy638jlhotaui/Section2_Bild0.png?rlkey=ispdm3gdvi4fu2uce4l8qi7dc&dl=1",
        "https://www.dropbox.com/scl/fi/u8vhnd81nhuap5r70etgp/Section2_Bild2.png?rlkey=gxa43jpl0l8zilsi6551hwenv&dl=1",
        "https://www.dropbox.com/scl/fi/zfyq6me7oxuuceczn0p7p/Section2_Bild4.png?rlkey=3lvy1q6astir2rqggum5qpkvv&dl=1",
        "https://www.dropbox.com/scl/fi/7quiix68dblqyxlnmu357/Section2_Bild5.png?rlkey=9sdwokb3wqp3c6g40sttqlloy&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img42 = image_select(
        "Auswahl:",
        tmp42,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 2", 0),
        key=f"frage42_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img42} ausgewählt.")
    st.session_state.auswahl["Seite 4 Thema 2"] = img42
    st.image(tmp42[st.session_state.auswahl.get("Seite 4 Thema 2", 0)])
    st.text('Topic 3: Ascendance of Nazism in Germany\n- Chronicles Adolf Hitler joining the precursor party of the Nazi Party early on, initial failed attempts at power seizure, prison term, rebuilding the Nazi Party, rise to leadership, creation of various affiliated groups like the Hitler Youth, gradual increase in popularity through the 1920s, reaching a third of votes cast in German elections in 1932.\n\n')

    tmp43 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/055e48igaor3gbfqkx0nc/Section3_Bild5.png?rlkey=mvmmwe6o64ytbapm3yecbh51d&dl=1",
        "https://www.dropbox.com/scl/fi/3i3tn7xiutqwa7rdo6dje/Section3_Bild1.png?rlkey=xe50ugwoxlxyofknoyfi9itir&dl=1",
        "https://www.dropbox.com/scl/fi/xp79k15mur7ctu3mu7oym/Section3_Bild4.png?rlkey=eogr7ob1jqrtwh0ncyb6lk1tg&dl=1",
        "https://www.dropbox.com/scl/fi/xegxjs8mdgvbb8wfz4zw9/Section3_Bild2.png?rlkey=7ifhjye8ywxtidyr1kae2u7am&dl=1",
        "https://www.dropbox.com/scl/fi/c9plvorg0ebq6bcjk03qk/Section3_Bild3.png?rlkey=n0zto2c4pxy2scclv3cg2kopz&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img43 = image_select(
        "Auswahl:",
        tmp43,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 3", 0),
        key=f"frage43_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img43} ausgewählt.")
    st.session_state.auswahl["Seite 4 Thema 3"] = img43
    st.image(tmp43[st.session_state.auswahl.get("Seite 4 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp43 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/au88m5skjtlo321f3apwb/Section3_Bild0.png?rlkey=ydemb4v1iywq0gwdxuls4p93s&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg43 = image_select(
        "Auswahl:",
        nvtmp43,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 4 Thema 3", 0),
        key=f"nvfrage43_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg43} ausgewählt.")
    st.session_state.auswahl["nv Seite 4 Thema 3"] = nvimg43
    st.image(nvtmp43[st.session_state.auswahl.get("nv Seite 4 Thema 3", 0)])

    st.text('Topic 4: Power Takeover by Hitler\n- Recounts appointment of Hitler as chancellor of Germany in January 1933, rapid consolidation of dictatorial powers, persecution and incarceration of opponents, suppression of free press, propaganda dominating media and cultural life, suspension of constitutional rights due to declared military emergency following the Reichstag fire in February 1933.\n\n')

    tmp44 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/n15elkxfognkfumk7rtie/Section4_Bild3.png?rlkey=q4va31skhk2a16np3efae3c7n&dl=1",
        "https://www.dropbox.com/scl/fi/wplz0bm62w8gtmdxezhbd/Section4_Bild2.png?rlkey=3l74dfy2gqb8ha9e7fh17rkjb&dl=1",
        "https://www.dropbox.com/scl/fi/uqokv4f148pc4svfgc1dn/Section4_Bild0.png?rlkey=zg79208pdi8qags1rdkn032b1&dl=1",
        "https://www.dropbox.com/scl/fi/jvj7urt3hgas17v7yb4xc/Section4_Bild4.png?rlkey=wl30zsavf5qg4jiyxeqy636p7&dl=1",
        "https://www.dropbox.com/scl/fi/1hajam5ev9dl0fv1s48ke/Section4_Bild5.png?rlkey=7aqddwjfsb3o3yakogt2qvg3x&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img44 = image_select(
        "Auswahl:",
        tmp44,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 4", 0),
        key=f"frage44_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img44} ausgewählt.")
    st.session_state.auswahl["Seite 4 Thema 4"] = img44
    st.image(tmp44[st.session_state.auswahl.get("Seite 4 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp44 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/v977us0q9kyz2hd06a1qn/Section4_Bild1.png?rlkey=dw208gkx5gj8a8kght6e26w92&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg44 = image_select(
        "Auswahl:",
        nvtmp44,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 4 Thema 4", 0),
        key=f"nvfrage44_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg44} ausgewählt.")
    st.session_state.auswahl["nv Seite 4 Thema 4"] = nvimg44
    st.image(nvtmp44[st.session_state.auswahl.get("nv Seite 4 Thema 4", 0)])

    st.text('Topic 5: Persecution of Jewish Population\n- Documents anti-Semitic measures initiated immediately upon taking office, including boycotting businesses owned by Jews, passage of discriminatory laws known as the "Nuremberg Race Laws," violent attacks against Jews culminating in the November 1938 Kristallnacht pogroms resulting in widespread destruction of property and deaths, forced expulsion and theft of assets from Jews throughout Europe.\n\n')

    tmp45 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/s3h1whx3xk3xid47ju0xo/Section5_Bild0.png?rlkey=695yx88qamo0kpxb4z75bywuw&dl=1",
        "https://www.dropbox.com/scl/fi/ktxwszv5d9inf8o80o3zg/Section5_Bild2.png?rlkey=1rzxp5vskk33lxzkm42bxkvnu&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img45 = image_select(
        "Auswahl:",
        tmp45,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 5", 0),
        key=f"frage45_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img45} ausgewählt.")
    st.session_state.auswahl["Seite 4 Thema 5"] = img45
    st.image(tmp45[st.session_state.auswahl.get("Seite 4 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp45 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/qzplm7ua4pimiboe9li05/Section5_Bild1.png?rlkey=ihb9fuvbs741pu219bq5bp924&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg45 = image_select(
        "Auswahl:",
        nvtmp45,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 4 Thema 5", 0),
        key=f"nvfrage45_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg45} ausgewählt.")
    st.session_state.auswahl["nv Seite 4 Thema 5"] = nvimg45
    st.image(nvtmp45[st.session_state.auswahl.get("nv Seite 4 Thema 5", 0)])

    st.button("(Nachfolgende) Seite 5", on_click=lambda: wechsel_zu("page5"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 6, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page5":
    st.title("Seite 5")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/tj9118fh20k79cwwv3tf8/Broschuere_2013_hires.pdf?rlkey=z7amkisyqbggjwtsna0svw7ms&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Understand the structure, key components, and ongoing exploration of our solar system, with a focus on Mars and accessible image data repositories.')

    st.text('Topic 1: Our Solar System Overview\n- Presents basic facts about each planet, moon, asteroid, comet, and dwarf planet, including size, composition, distances from the Sun, rotations, and orbits.')

    tmp51 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/n8a09wu9gucovku8ffm73/Section1_Bild0.png?rlkey=kpmr38mounnjsr3wm1ql7ac56&dl=1",
        "https://www.dropbox.com/scl/fi/ur9bs4vhmvortlydtgofw/Section1_Bild2.png?rlkey=4y3iimrurd1yki3ev7veog7uc&dl=1",
        "https://www.dropbox.com/scl/fi/nu4a3618nxoke5avpdffg/Section1_Bild1.png?rlkey=3kv4xv463iwr2yh334qd68ua1&dl=1",
    ]
    img51 = image_select(
        "Auswahl:",
        tmp51,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 1", 0),
        key=f"frage51_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img51} ausgewählt.")
    st.session_state.auswahl["Seite 5 Thema 1"] = img51
    st.image(tmp51[st.session_state.auswahl.get("Seite 5 Thema 1", 0)])
    st.text('Topic 2: Major Celestial Bodies - Detailed Analysis\n- Delves deeper into specific aspects of Mars, covering general information, surface features, historical climate change, and exploration mission details.')

    tmp52 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/vvicd2rc8pwbzeg5vvkh4/Section2_Bild1.png?rlkey=i125jdq9tlt3wrbob837zpyzy&dl=1",
        "https://www.dropbox.com/scl/fi/7mojc5vqfnlatz8q9lpsl/Section2_Bild0.png?rlkey=83rh47kdcbql0pq08a4qi4cxj&dl=1",
        "https://www.dropbox.com/scl/fi/aka484nq9wms21xjt1n1d/Section2_Bild2.png?rlkey=a6xruuu1vv4q0r9zegb09ttoz&dl=1",
    ]
    img52 = image_select(
        "Auswahl:",
        tmp52,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 2", 0),
        key=f"frage52_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img52} ausgewählt.")
    st.session_state.auswahl["Seite 5 Thema 2"] = img52
    st.image(tmp52[st.session_state.auswahl.get("Seite 5 Thema 2", 0)])
    st.text('Topic 3: Resources and Repositories\n- Introduces the Regional Planetary Image Facility (RPIF), part of an international network storing images, spectral data, and related materials collected by various missions.\n\n')

    tmp53 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/db2be56g54x1w9dpcqyve/Section3_Bild1.png?rlkey=ctkz2p9i5ljkgcbo5elts37xl&dl=1",
        "https://www.dropbox.com/scl/fi/ybba0cuz42w1oc5ck9078/Section3_Bild2.png?rlkey=vtzg8yw2gfuwr0n7uo32tkgz2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img53 = image_select(
        "Auswahl:",
        tmp53,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 3", 0),
        key=f"frage53_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img53} ausgewählt.")
    st.session_state.auswahl["Seite 5 Thema 3"] = img53
    st.image(tmp53[st.session_state.auswahl.get("Seite 5 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp53 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/d390j648toc8m0z4sfk97/Section3_Bild0.png?rlkey=ro01512l9zyxu1l1a68x3b9sp&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg53 = image_select(
        "Auswahl:",
        nvtmp53,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 5 Thema 3", 0),
        key=f"nvfrage53_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg53} ausgewählt.")
    st.session_state.auswahl["nv Seite 5 Thema 3"] = nvimg53
    st.image(nvtmp53[st.session_state.auswahl.get("nv Seite 5 Thema 3", 0)])

    st.text('Topic 4: Utilizing RPIF Data\n- Describes uses of RPIF data for scientific research, educational outreach activities, and planning future space missions.\n\n')

    tmp54 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/03i88mj2pypqmqst7k53n/Section4_Bild2.png?rlkey=uefwfpev13c2989vuryxw8fmg&dl=1",
        "https://www.dropbox.com/scl/fi/yhz82i0xli2yuut4cl35a/Section4_Bild1.png?rlkey=ozpoukchgupej2fk73ddkdzys&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img54 = image_select(
        "Auswahl:",
        tmp54,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 4", 0),
        key=f"frage54_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img54} ausgewählt.")
    st.session_state.auswahl["Seite 5 Thema 4"] = img54
    st.image(tmp54[st.session_state.auswahl.get("Seite 5 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp54 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/cjm033rg7mhldq54qwrca/Section4_Bild3.png?rlkey=udq9oygibpbe28q9qa1vbnkns&dl=1",
        "https://www.dropbox.com/scl/fi/wfe9r06x7hhot9r8f5d04/Section4_Bild0.png?rlkey=hc5hbwbmjbjxok61y7udlic0k&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg54 = image_select(
        "Auswahl:",
        nvtmp54,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 5 Thema 4", 0),
        key=f"nvfrage54_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg54} ausgewählt.")
    st.session_state.auswahl["nv Seite 5 Thema 4"] = nvimg54
    st.image(nvtmp54[st.session_state.auswahl.get("nv Seite 5 Thema 4", 0)])

    st.text('Topic 5: Ongoing and Upcoming Projects\n- Outlines current exploration efforts across our solar system and future plans involving Mars Sample Return, Human Exploration Campaign, and continued research towards understanding extraterrestrial environments.\n\n')

    tmp55 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/lefp3anaz4qll4et89akd/Section5_Bild0.png?rlkey=m1zyw95df6y7fr3hp1cspnw5p&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img55 = image_select(
        "Auswahl:",
        tmp55,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 5", 0),
        key=f"frage55_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img55} ausgewählt.")
    st.session_state.auswahl["Seite 5 Thema 5"] = img55
    st.image(tmp55[st.session_state.auswahl.get("Seite 5 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp55 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/r2m5z3nfa7izugo1fbc0x/Section5_Bild1.png?rlkey=z3nzkpjsh6vafjqz7179sb01x&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg55 = image_select(
        "Auswahl:",
        nvtmp55,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 5 Thema 5", 0),
        key=f"nvfrage55_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg55} ausgewählt.")
    st.session_state.auswahl["nv Seite 5 Thema 5"] = nvimg55
    st.image(nvtmp55[st.session_state.auswahl.get("nv Seite 5 Thema 5", 0)])

    st.button("(Nachfolgende) Seite 6", on_click=lambda: wechsel_zu("page6"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page6":
    st.title("Seite 6")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/zl5hgxuq23jq5jsaqjful/Menschenaffen_Unterrichtsmaterial.pdf?rlkey=r5b2314utj0d46ztiftcug8xi&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Providing educational resources for teachers to facilitate learning about great apes and conservation efforts led by WWF Germany\'s "Young Panda" project.')

    st.text('Topic 1: Introduction\n- Presents background information about the WWF organization and its focus on protecting endangered wildlife.\n\n')

    tmp61 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/4zzyvawi50jfo8jf9tcko/Section1_Bild6.png?rlkey=xds22ywx1ibiviy3m1tj5hg9m&dl=1",
        "https://www.dropbox.com/scl/fi/e2h8fhtqyi8pxdlre030c/Section1_Bild2.png?rlkey=ez7g8gxlddfrr94t30sp7delx&dl=1",
        "https://www.dropbox.com/scl/fi/whj266hs9tgjah2ube4po/Section1_Bild4.png?rlkey=izfce1sc6f1u5kgy129bocfai&dl=1",
        "https://www.dropbox.com/scl/fi/dim0pjuojri5uqcgfrocu/Section1_Bild10.png?rlkey=zbydm41h769iqx00jbqmao6wy&dl=1",
        "https://www.dropbox.com/scl/fi/9qbtuztqvnmcuo635hufx/Section1_Bild8.png?rlkey=4ofrw57o3qv3c0r8da384szqd&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img61 = image_select(
        "Auswahl:",
        tmp61,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 1", 0),
        key=f"frage61_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img61} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 1"] = img61
    st.image(tmp61[st.session_state.auswahl.get("Seite 6 Thema 1", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp61 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/gx2c74tcyg19n3ngsps8x/Section1_Bild0.png?rlkey=uso8shuxjrhn04013f8wu08ac&dl=1",
        "https://www.dropbox.com/scl/fi/xwq8kwrlaoyqrzem8was2/Section1_Bild9.png?rlkey=g97jc1dpkp461p17844oy3iqk&dl=1",
        "https://www.dropbox.com/scl/fi/t29rsohwzaym1zyaauqg6/Section1_Bild5.png?rlkey=4cbwof1hw36z9p4ljao3pm7pa&dl=1",
        "https://www.dropbox.com/scl/fi/00u167iyxbb8ry4aesq31/Section1_Bild7.png?rlkey=n65odybszve8mx8c7poca7jg3&dl=1",
        "https://www.dropbox.com/scl/fi/wx09blodgcsjfd2oteyf3/Section1_Bild11.png?rlkey=b35vbdmwgiaoc3p6hih702uri&dl=1",
        "https://www.dropbox.com/scl/fi/op8p9msy92hx7okqh83vw/Section1_Bild1.png?rlkey=xnhvqiz189h1yzev861u4tyzd&dl=1",
        "https://www.dropbox.com/scl/fi/4v3u153h6x8ufnhhxnb7p/Section1_Bild3.png?rlkey=b41pr61wu6ost4cv3vvy7fmtw&dl=1",
    ]
    nvimg61 = image_select(
        "Auswahl:",
        nvtmp61,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 1", 0),
        key=f"nvfrage61_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg61} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 1"] = nvimg61
    st.image(nvtmp61[st.session_state.auswahl.get("nv Seite 6 Thema 1", 0)])

    st.text('Topic 2: Overview of Great Apes\n- Discusses four types of great apes: orangutans, gorillas, chimpanzees, and bonobos, including evolutionary history, characteristics, and unique features.\n\n')

    tmp62 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/z8gvb34u3rqh46kp790af/Section2_Bild8.png?rlkey=l7ub2feuvqtwu50061lffozym&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img62 = image_select(
        "Auswahl:",
        tmp62,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 2", 0),
        key=f"frage62_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img62} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 2"] = img62
    st.image(tmp62[st.session_state.auswahl.get("Seite 6 Thema 2", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp62 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/lwd31wumizn3ver4uek7u/Section2_Bild1.png?rlkey=cln4r4ltkwzz0i60qgrfjoja8&dl=1",
        "https://www.dropbox.com/scl/fi/70cu9007cpfrkbgzzqhn0/Section2_Bild3.png?rlkey=0pd7m1eqdame1dadl7piala7k&dl=1",
        "https://www.dropbox.com/scl/fi/pm433k702d6q88pfbh32o/Section2_Bild0.png?rlkey=qdcbznzblnqzmijpfi7hhoavv&dl=1",
        "https://www.dropbox.com/scl/fi/cvkyu9usci18fibs84mh9/Section2_Bild2.png?rlkey=u7djhfk249ntw516dt1zprig4&dl=1",
        "https://www.dropbox.com/scl/fi/1g4rgajkajup737qut8i2/Section2_Bild6.png?rlkey=r516dgjrnkgbe900tyo9kxqp3&dl=1",
        "https://www.dropbox.com/scl/fi/oples2ko4ctf6bbznt4iy/Section2_Bild4.png?rlkey=lwjeb5p2juet5gwe1gdit4x51&dl=1",
        "https://www.dropbox.com/scl/fi/7cg45ymaz88qzmtthypuc/Section2_Bild5.png?rlkey=iirwn5s3bqc3h0xuixhyts2v7&dl=1",
        "https://www.dropbox.com/scl/fi/qyaan8g67rfgn3avevedv/Section2_Bild7.png?rlkey=tiw41o9eqkoscuoplzbb5hua3&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg62 = image_select(
        "Auswahl:",
        nvtmp62,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 2", 0),
        key=f"nvfrage62_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg62} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 2"] = nvimg62
    st.image(nvtmp62[st.session_state.auswahl.get("nv Seite 6 Thema 2", 0)])

    st.text('Topic 3: Living Conditions of Great Apes\n- Details how these primates inhabit various regions across Africa and Southeast Asia, discussing their habitats, diet, social structures, and behaviors.\n\n')

    tmp63 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/80aaz4j61t8tweu8seack/Section3_Bild0.png?rlkey=5164llg2i7xal9qirqy1fl381&dl=1",
        "https://www.dropbox.com/scl/fi/xlfl391ghl2bpnwlc8p1u/Section3_Bild4.png?rlkey=9xm1inm3z9d2ectdbqrsizm4l&dl=1",
        "https://www.dropbox.com/scl/fi/gwi0a1dsia5xafw43s488/Section3_Bild6.png?rlkey=mqi7tuebdtan6tr5oxcer3v18&dl=1",
        "https://www.dropbox.com/scl/fi/vcrlc0eotrh1pzn5qxmz9/Section3_Bild3.png?rlkey=ysxop35cin0hmln36n8p6czva&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img63 = image_select(
        "Auswahl:",
        tmp63,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 3", 0),
        key=f"frage63_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img63} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 3"] = img63
    st.image(tmp63[st.session_state.auswahl.get("Seite 6 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp63 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/l4pedoje4ttcxntv7vue8/Section3_Bild5.png?rlkey=ct56b0com903uj1nr01bykqz4&dl=1",
        "https://www.dropbox.com/scl/fi/iu2i1lr2b8kvmc09bxkag/Section3_Bild1.png?rlkey=bg1a37d5e5yatmptoxnm8ilil&dl=1",
        "https://www.dropbox.com/scl/fi/oqw8zp8myfu0nfsfmh864/Section3_Bild2.png?rlkey=fwndefnk37k98pcsmlnhvhr81&dl=1",
    ]
    nvimg63 = image_select(
        "Auswahl:",
        nvtmp63,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 3", 0),
        key=f"nvfrage63_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg63} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 3"] = nvimg63
    st.image(nvtmp63[st.session_state.auswahl.get("nv Seite 6 Thema 3", 0)])

    st.text('Topic 4: Challenges Facing Great Apes\n- Addresses threats like habitat destruction, hunting, and diseases transmitted from humans, explaining why they are critical issues for these animals.\n\n')

    tmp64 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/e0zomnebi6nyw68dcdtli/Section4_Bild0.png?rlkey=h92nmv07l48zwuir8139ul5xl&dl=1",
        "https://www.dropbox.com/scl/fi/c6pjjaghbqvz7rflillzb/Section4_Bild4.png?rlkey=e5hyjfyqv4sbqsiwsjq7aoifw&dl=1",
        "https://www.dropbox.com/scl/fi/95z3euv5crdew2zwndt76/Section4_Bild7.png?rlkey=6309hdlddbcp472a6lvbac5j4&dl=1",
        "https://www.dropbox.com/scl/fi/prpeyeyvpe7jnyt40b9pq/Section4_Bild5.png?rlkey=7oc82tyoi83rx4w5ez93ybndj&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img64 = image_select(
        "Auswahl:",
        tmp64,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 4", 0),
        key=f"frage64_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img64} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 4"] = img64
    st.image(tmp64[st.session_state.auswahl.get("Seite 6 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp64 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/zpfy7j4qaarux9q5y2swh/Section4_Bild3.png?rlkey=gg4rl940h714q2pezamuvaocy&dl=1",
        "https://www.dropbox.com/scl/fi/chaz4fstiebrmf1yrmlqs/Section4_Bild6.png?rlkey=rmsjiulqj1gma22oi4rt5p1mg&dl=1",
        "https://www.dropbox.com/scl/fi/f3a3kd4kbghf8v2h7gipz/Section4_Bild2.png?rlkey=kskaa2rrrwl4whqt2uqi3f6iu&dl=1",
        "https://www.dropbox.com/scl/fi/315so60dlpnffmiqvh3de/Section4_Bild8.png?rlkey=5dhqjudwse3y55ocsh1jc4k81&dl=1",
        "https://www.dropbox.com/scl/fi/ipjsb094zzkuycpctclaw/Section4_Bild1.png?rlkey=9xkcnsof29eoesduuyhkfipz6&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg64 = image_select(
        "Auswahl:",
        nvtmp64,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 4", 0),
        key=f"nvfrage64_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg64} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 4"] = nvimg64
    st.image(nvtmp64[st.session_state.auswahl.get("nv Seite 6 Thema 4", 0)])

    st.text('Topic 5: Helping Great Apes Survive\n- Outlines ways people can support conservation projects aimed at preserving great ape populations through sustainable practices, education, and advocacy.\n\n')

    tmp65 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/o8552wpddexeg9x18fu7f/Section5_Bild5.png?rlkey=uvd2tj2zl8b2vn5jm0c5fxvij&dl=1",
        "https://www.dropbox.com/scl/fi/kopj1o3am2awbp8w6d605/Section5_Bild0.png?rlkey=1yepooeoqz58bkkvzp873ztke&dl=1",
        "https://www.dropbox.com/scl/fi/o2183witx6p8tgxu7uwh9/Section5_Bild6.png?rlkey=3giraqwqn7jt258pcctl7nf1v&dl=1",
        "https://www.dropbox.com/scl/fi/tu79u871urf1v9mpji3on/Section5_Bild10.png?rlkey=t6kqkrbhod2chnitdyeplklox&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img65 = image_select(
        "Auswahl:",
        tmp65,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 5", 0),
        key=f"frage65_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img65} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 5"] = img65
    st.image(tmp65[st.session_state.auswahl.get("Seite 6 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp65 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/c9pipy0smdpssn1hhxba4/Section5_Bild11.png?rlkey=6njed18zzjkq3tvlikkst1xrm&dl=1",
        "https://www.dropbox.com/scl/fi/b3q6cs1mij12w3t388ur4/Section5_Bild9.png?rlkey=akzgidja86fsqasmm1yyp0pmd&dl=1",
        "https://www.dropbox.com/scl/fi/xlr9hgebpm4xyit1oeebx/Section5_Bild8.png?rlkey=h3e1xl7qhoshqjxhs6ket38tj&dl=1",
        "https://www.dropbox.com/scl/fi/oztrg1sd2fuss1yu1tcrd/Section5_Bild1.png?rlkey=w9mz0v2cmloqbjw889jjwkqtq&dl=1",
        "https://www.dropbox.com/scl/fi/grwyqi3ajnw5tpco2q3hx/Section5_Bild2.png?rlkey=balzpkporxjdswv4dciil99o3&dl=1",
        "https://www.dropbox.com/scl/fi/3scmcphc662f9wxn418gb/Section5_Bild7.png?rlkey=k76ifuccmlimvixvtl96vb3fc&dl=1",
        "https://www.dropbox.com/scl/fi/jb9twj6abk76c5ga5llgu/Section5_Bild4.png?rlkey=dgcwmchdu4j7r8xmcbt65oufg&dl=1",
        "https://www.dropbox.com/scl/fi/v0vcdv86cfiu47ih3uvrg/Section5_Bild3.png?rlkey=rajyn2hd92rj5bewkn6ar2rof&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg65 = image_select(
        "Auswahl:",
        nvtmp65,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 5", 0),
        key=f"nvfrage65_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg65} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 5"] = nvimg65
    st.image(nvtmp65[st.session_state.auswahl.get("nv Seite 6 Thema 5", 0)])

    st.text('Topic 6: Activities for Students\n- Offers suggestions for classroom activities related to each theme covered in the guide, encouraging active engagement among children aged 8-14 years old.\n\n')

    tmp66 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/yiua21x2lqpwkbiw4xqid/Section6_Bild0.png?rlkey=hi8bskxxdjytlrc6i2dxd6mna&dl=1",
        "https://www.dropbox.com/scl/fi/5x5k1i075y620uslnwb6f/Section6_Bild5.png?rlkey=h6s2lwnp4gv91it860yqk0ixo&dl=1",
        "https://www.dropbox.com/scl/fi/qlpcg2p82iyez5xv1mtqz/Section6_Bild6.png?rlkey=soyrqfyru13ra4wq513sgiuwd&dl=1",
        "https://www.dropbox.com/scl/fi/7thk9t03r21fsei5opoxk/Section6_Bild3.png?rlkey=k6qij1q97dqj5zwprk8ejnwl3&dl=1",
        "https://www.dropbox.com/scl/fi/lvbqop8dq4jnxv1lmu445/Section6_Bild4.png?rlkey=pi3v9mbvnpnj8naeet7hgyhit&dl=1",
        "https://www.dropbox.com/scl/fi/54xk4po3xb4d5j58ip4w8/Section6_Bild9.png?rlkey=0ck69o1acho41kvkf9tywmws8&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img66 = image_select(
        "Auswahl:",
        tmp66,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 6", 0),
        key=f"frage66_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img66} ausgewählt.")
    st.session_state.auswahl["Seite 6 Thema 6"] = img66
    st.image(tmp66[st.session_state.auswahl.get("Seite 6 Thema 6", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp66 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/fuxsjwp01v8ubqew3lnm5/Section6_Bild8.png?rlkey=s2nzlretenjktao5ck08ugfph&dl=1",
        "https://www.dropbox.com/scl/fi/lc7w3q3jf7bxa64rkxa4l/Section6_Bild10.png?rlkey=tgcpvhd97giltsvs8eecig4ab&dl=1",
        "https://www.dropbox.com/scl/fi/oizad7wf741o26xc4tr03/Section6_Bild2.png?rlkey=v433r5kcrlcvnmf5w0mw9x9ju&dl=1",
        "https://www.dropbox.com/scl/fi/nqqo66nutlyfiocx4wini/Section6_Bild7.png?rlkey=956ycau4ul0i26s4yn431acbg&dl=1",
        "https://www.dropbox.com/scl/fi/98bbyvg93kb1lnbo12buu/Section6_Bild1.png?rlkey=7z47k8b33kf1g2cepfqlb1844&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg66 = image_select(
        "Auswahl:",
        nvtmp66,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 6", 0),
        key=f"nvfrage66_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg66} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 6"] = nvimg66
    st.image(nvtmp66[st.session_state.auswahl.get("nv Seite 6 Thema 6", 0)])

    st.button("(Nachfolgende) Seite 7", on_click=lambda: wechsel_zu("page7"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page7":
    st.title("Seite 7")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/m9trtyj31813xiv3r4r9r/O1A1-GE.pdf?rlkey=vb8b0zyql60uzb38wvcbz6dgr&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Equip educators with extensive knowledge on suitable 3D print technologies and materials for effective implementation in classroom settings.')

    st.text('Topic 1: Understanding Additive Manufacturing and Its Benefits\n- Presents an overview of Additive Manufacturing, explaining its differences from Rapid Prototyping and conventional manufacturing techniques.')

    tmp71 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/7b0iuxkp4fac6b8aj1srk/Section1_Bild6.png?rlkey=3c8ym5rilluh068sn4uy33uz7&dl=1",
        "https://www.dropbox.com/scl/fi/jxs5nfpkkf7z8sehti7t0/Section1_Bild5.png?rlkey=m5dehhbr1hiob6eefdjrb8qip&dl=1",
        "https://www.dropbox.com/scl/fi/w2zwa1nkez1qq9sko5jis/Section1_Bild7.png?rlkey=3oge5s5plqlun7scc719c5b2t&dl=1",
        "https://www.dropbox.com/scl/fi/wf236avdhn62bzb6e70xd/Section1_Bild10.png?rlkey=vf9b81w6eb1pqtjnmjmilaj3e&dl=1",
        "https://www.dropbox.com/scl/fi/epjah2h49vvf7map9tlry/Section1_Bild8.png?rlkey=kuhdlzlsliiehoeu8v5gdc4lh&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img71 = image_select(
        "Auswahl:",
        tmp71,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 1", 0),
        key=f"frage71_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img71} ausgewählt.")
    st.session_state.auswahl["Seite 7 Thema 1"] = img71
    st.image(tmp71[st.session_state.auswahl.get("Seite 7 Thema 1", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp71 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/40on6omklutmen9m161ey/Section1_Bild0.png?rlkey=cn1cd7m5k3l41nqx0vgoivdnp&dl=1",
        "https://www.dropbox.com/scl/fi/paro2hxdh3fj0q4vbkext/Section1_Bild2.png?rlkey=3sutxzl9lolbgkyydozz036if&dl=1",
        "https://www.dropbox.com/scl/fi/0i9mdro4z6r3urkxvmbee/Section1_Bild9.png?rlkey=6f2dtc85nk4yj4ebulj4andx4&dl=1",
        "https://www.dropbox.com/scl/fi/pawdevi83ohm1f449ztv0/Section1_Bild11.png?rlkey=oapakszdr4pbanyg4q0garw0d&dl=1",
        "https://www.dropbox.com/scl/fi/ft572ro88upjhnqnwxmf9/Section1_Bild4.png?rlkey=8nq5kkzmtjx0zh7fv8ri9y24n&dl=1",
        "https://www.dropbox.com/scl/fi/it8zb4s0zz976fg4r1yhq/Section1_Bild1.png?rlkey=yd0ytki5n7yl2qcxq8395uq3r&dl=1",
        "https://www.dropbox.com/scl/fi/ral40ohkqhk8j21tqfsad/Section1_Bild3.png?rlkey=h3fq0yxeh9d0rjidtfvk6m6xu&dl=1",
    ]
    nvimg71 = image_select(
        "Auswahl:",
        nvtmp71,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 1", 0),
        key=f"nvfrage71_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg71} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 1"] = nvimg71
    st.image(nvtmp71[st.session_state.auswahl.get("nv Seite 7 Thema 1", 0)])

    st.text('Topic 2: Comparative Analysis of Common 3D Print Technologies\n- Evaluates seven widely utilized 3D print technologies according to criteria like speed, material compatibility, complexity level, cost, precision, and support structure needs.')

    tmp72 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/m6oa2jwag4wujxwtbtkxp/Section2_Bild7.png?rlkey=za6l2m3itprqjssd9ga2zhg5i&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img72 = image_select(
        "Auswahl:",
        tmp72,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 2", 0),
        key=f"frage72_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img72} ausgewählt.")
    st.session_state.auswahl["Seite 7 Thema 2"] = img72
    st.image(tmp72[st.session_state.auswahl.get("Seite 7 Thema 2", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp72 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/gecjqtvp2kzykptyir7d8/Section2_Bild1.png?rlkey=0c4ztvkflrhbp84528xrlfo5w&dl=1",
        "https://www.dropbox.com/scl/fi/a2pxvdot40tvg0renafuc/Section2_Bild3.png?rlkey=34in13jj519swb9rvityne23d&dl=1",
        "https://www.dropbox.com/scl/fi/0rr9x0r324jx7uvy6vfhf/Section2_Bild0.png?rlkey=kttxxwoex1fwiuyzpo3jm6ipb&dl=1",
        "https://www.dropbox.com/scl/fi/p7tqtkcq09pgoa9vmonbj/Section2_Bild11.png?rlkey=w6hkcgl1osg40zy6xuatnkw0n&dl=1",
        "https://www.dropbox.com/scl/fi/30yfx6bbp6u3rewpomt5j/Section2_Bild2.png?rlkey=wwn5lbommav3zuoi05on6jecs&dl=1",
        "https://www.dropbox.com/scl/fi/tui8g51jaetq610wxwgci/Section2_Bild8.png?rlkey=7z1jabk3jc05q03w9e0flqvks&dl=1",
        "https://www.dropbox.com/scl/fi/r7nt8p773a2by36xbhivl/Section2_Bild6.png?rlkey=dttf4hcczq52glr9irrmkw15n&dl=1",
        "https://www.dropbox.com/scl/fi/mhvx6zpeamu1eiciak453/Section2_Bild4.png?rlkey=36fqvb7tm3js6phe4a6yr6t38&dl=1",
        "https://www.dropbox.com/scl/fi/zuxtmw7puovvgfnsv79jb/Section2_Bild10.png?rlkey=1wh224gvgo3dysptt24jo58n8&dl=1",
        "https://www.dropbox.com/scl/fi/fuxep9h59j1yzr3d0ep3u/Section2_Bild5.png?rlkey=8ql8r54fbtysir58sgu3ag462&dl=1",
        "https://www.dropbox.com/scl/fi/1wj2t06leavdimz44yez0/Section2_Bild9.png?rlkey=vs9se5gh4jliygzupj2wpcipj&dl=1",
    ]
    nvimg72 = image_select(
        "Auswahl:",
        nvtmp72,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 2", 0),
        key=f"nvfrage72_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg72} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 2"] = nvimg72
    st.image(nvtmp72[st.session_state.auswahl.get("nv Seite 7 Thema 2", 0)])

    st.text('Topic 3: Recommended Education-Focused 3D Print Technologies\n- Detailed exploration of three preferred 3D print technologies - Fused Deposition Modeling (FDM), Selective Laser Sintering (SLS), and Stereolithography (SLA). This includes discussions on processes, materials, applications, pros, and cons for each method.\n\n')

    tmp73 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/hj0tfclvbsjsww12kjaln/Section3_Bild5.png?rlkey=x8mmcqdzwica8nnakeup19mz6&dl=1",
        "https://www.dropbox.com/scl/fi/0likokj4b40uat9i2raod/Section3_Bild0.png?rlkey=j0xg2p1t1zv4gbeo5qpt2enus&dl=1",
        "https://www.dropbox.com/scl/fi/7u1ukcg2o73gd4xve4asg/Section3_Bild6.png?rlkey=j15gl384oq2jthqc5sy9uf329&dl=1",
        "https://www.dropbox.com/scl/fi/kp9qwr4ptxcepxscptlus/Section3_Bild7.png?rlkey=ifbvp897besy0bs63497zgp4i&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img73 = image_select(
        "Auswahl:",
        tmp73,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 3", 0),
        key=f"frage73_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img73} ausgewählt.")
    st.session_state.auswahl["Seite 7 Thema 3"] = img73
    st.image(tmp73[st.session_state.auswahl.get("Seite 7 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp73 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/2ly1zqyt7bsz4aa9znqmh/Section3_Bild9.png?rlkey=8b3n2lmg8181kbecq8o1fll4t&dl=1",
        "https://www.dropbox.com/scl/fi/2s65br6y0wgtdgf8fesh3/Section3_Bild1.png?rlkey=t5os5k3kx3v8yqb1kkt9j0ni3&dl=1",
        "https://www.dropbox.com/scl/fi/d6zcrx8fjot9k5v9of43m/Section3_Bild4.png?rlkey=ympnior35wkueqpu43nanv2ph&dl=1",
        "https://www.dropbox.com/scl/fi/hmfibq5o6gmr3thb35l1i/Section3_Bild2.png?rlkey=2774xh2ie2ky9jwx7lmlveqa0&dl=1",
        "https://www.dropbox.com/scl/fi/cvzg4nwvoup0b65mj4of2/Section3_Bild8.png?rlkey=u59vg50m8lqi40xqthqqkhyym&dl=1",
        "https://www.dropbox.com/scl/fi/7jjnn34x22vpw8caidrhv/Section3_Bild3.png?rlkey=9eo1gjpbg29hx3zlci2ofw22v&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg73 = image_select(
        "Auswahl:",
        nvtmp73,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 3", 0),
        key=f"nvfrage73_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg73} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 3"] = nvimg73
    st.image(nvtmp73[st.session_state.auswahl.get("nv Seite 7 Thema 3", 0)])

    st.text('Topic 4: Creating a 3D Print Object Workflow\n- Outlines stages involved in developing a 3D printed item, encompassing acquiring the digital model, repairing/preparing the STL file, slicing the model, orientating and adding supports, generating G-Code, and ultimately printing the component.\n\n')

    tmp74 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/ig0rpkz2zv8ll48i4ob0y/Section4_Bild7.png?rlkey=o8wp7pe78fsfgvx6h9dp54sb5&dl=1",
        "https://www.dropbox.com/scl/fi/9ik9ira6bvipel4h4d727/Section4_Bild5.png?rlkey=vpyoedu6u6376kfoly4y3508d&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img74 = image_select(
        "Auswahl:",
        tmp74,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 4", 0),
        key=f"frage74_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img74} ausgewählt.")
    st.session_state.auswahl["Seite 7 Thema 4"] = img74
    st.image(tmp74[st.session_state.auswahl.get("Seite 7 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp74 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/rsx35fnmjl99mm5954rbx/Section4_Bild3.png?rlkey=b8pv5iw40jh797n78cuv0nqqr&dl=1",
        "https://www.dropbox.com/scl/fi/7d0wqf7j78s9qs5dg5mcs/Section4_Bild6.png?rlkey=7ow2y2n7vpmtxmsg8eiguxqhe&dl=1",
        "https://www.dropbox.com/scl/fi/bfm0xgij81jad78tsoh1q/Section4_Bild2.png?rlkey=cllbp1qfejooo0sehd7svimku&dl=1",
        "https://www.dropbox.com/scl/fi/d96ln50csinhoa4f1h0wm/Section4_Bild9.png?rlkey=1ac2dlyfi0edfz04tb3xdy7cv&dl=1",
        "https://www.dropbox.com/scl/fi/3e1yggwhy9fvhmdr1euge/Section4_Bild8.png?rlkey=ey2ltziqc9cryer5e2h7w64pi&dl=1",
        "https://www.dropbox.com/scl/fi/fswy0tutrqzdif0kqts7x/Section4_Bild0.png?rlkey=fbj6pgoxezimfb1ga8d7b8ddi&dl=1",
        "https://www.dropbox.com/scl/fi/8lqkc10ac7j152zpnj0jd/Section4_Bild4.png?rlkey=s9fy6jisoktzopvaj2q8p4ykt&dl=1",
        "https://www.dropbox.com/scl/fi/xlvwdnpq3qxhpyflu7lrt/Section4_Bild1.png?rlkey=j0v0hwuszwlo2x5ts2uguz97k&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg74 = image_select(
        "Auswahl:",
        nvtmp74,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 4", 0),
        key=f"nvfrage74_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg74} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 4"] = nvimg74
    st.image(nvtmp74[st.session_state.auswahl.get("nv Seite 7 Thema 4", 0)])

    st.text('Topic 5: Essential Software Tools for 3D Printing\n- Introduces necessary software solutions throughout the production process ranging from design tools, test & prep programs, slicing software, and overall workflow management systems.\n\n')

    tmp75 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/xr65fq9iabrjiljnf8on4/Section5_Bild6.png?rlkey=b0lqfw02slte6qxrde52198t1&dl=1",
        "https://www.dropbox.com/scl/fi/hvxucsfpofgqvilajkdvz/Section5_Bild3.png?rlkey=obu33kimjx50vnb8gtuu1yn7v&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img75 = image_select(
        "Auswahl:",
        tmp75,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 5", 0),
        key=f"frage75_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img75} ausgewählt.")
    st.session_state.auswahl["Seite 7 Thema 5"] = img75
    st.image(tmp75[st.session_state.auswahl.get("Seite 7 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp75 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/9hbgzqygru8w80fq4kdxo/Section5_Bild9.png?rlkey=muiwtf5jomkonm96wrtmx71uq&dl=1",
        "https://www.dropbox.com/scl/fi/34huttoht3jpbrj67razw/Section5_Bild5.png?rlkey=a8w9ejjqqf8ow7i0wtakb0pie&dl=1",
        "https://www.dropbox.com/scl/fi/i2cs7bulkpl0ov2h0is26/Section5_Bild8.png?rlkey=u841myi5ih7lzbqeovtmb0cj2&dl=1",
        "https://www.dropbox.com/scl/fi/555npfzfn3ijqvdc1qcjm/Section5_Bild0.png?rlkey=hegb91esay7x7z5a7cs2w1ecq&dl=1",
        "https://www.dropbox.com/scl/fi/do8gapddnwiudx2zuk5w9/Section5_Bild1.png?rlkey=7feb1f6f2op3giu6lc69dhv0k&dl=1",
        "https://www.dropbox.com/scl/fi/yvyu0wlq48pymx05tp5sd/Section5_Bild2.png?rlkey=zicweoxkmba1vcwb5kiva25a6&dl=1",
        "https://www.dropbox.com/scl/fi/m73x6ytxsnwl1hasn2j3e/Section5_Bild7.png?rlkey=0km75d0dkq40ccfp83w6io2om&dl=1",
        "https://www.dropbox.com/scl/fi/ybtccmn935jcfcbai8y1k/Section5_Bild4.png?rlkey=lzcu5be27g2ychkz8yfhj4xf9&dl=1",
        "https://www.dropbox.com/scl/fi/trjgtjarad2zrhxfhz500/Section5_Bild10.png?rlkey=l1j2i2w0xioxhyyhhrlcu34ad&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg75 = image_select(
        "Auswahl:",
        nvtmp75,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 5", 0),
        key=f"nvfrage75_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg75} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 5"] = nvimg75
    st.image(nvtmp75[st.session_state.auswahl.get("nv Seite 7 Thema 5", 0)])

    st.button("(Nachfolgende) Seite 8", on_click=lambda: wechsel_zu("page8"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [9, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page8":
    st.title("Seite 8")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/pxspouxwh962pf6yyq4zt/MuM_Band_14.pdf?rlkey=kmcf2d7sbkqutu9lshuts75ga&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Investigate the interplay between coral symbiosis, bioerosion, and human activities in shaping coral reef ecosystems, emphasizing historical research in the Red Sea and practical considerations for managing coral reef exhibits.')

    st.text('Topic 1: Coral Symbiosis and Photosynthetic Microalgae\n- Introduces the mutually beneficial relationship between corals and zooxanthellae, providing essential energy for efficient growth and reproduction.\n\n')

    tmp81 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/6kpcwy4903ncw2o06oauh/Section1_Bild6.png?rlkey=7x44f6zzds4ruxanvcanqsccl&dl=1",
        "https://www.dropbox.com/scl/fi/jau4gh8nkdbe6ckshwv4a/Section1_Bild11.png?rlkey=7wlcgexr21l5xw4ho38kogq80&dl=1",
        "https://www.dropbox.com/scl/fi/pos8q3m7poml778787lnf/Section1_Bild4.png?rlkey=ct0g04bkx4ssydfd37vglmsm0&dl=1",
        "https://www.dropbox.com/scl/fi/f2yd1xob18we1x7hruld2/Section1_Bild8.png?rlkey=hrsieujru772e3pmicsm0i80i&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img81 = image_select(
        "Auswahl:",
        tmp81,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 1", 0),
        key=f"frage81_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img81} ausgewählt.")
    st.session_state.auswahl["Seite 8 Thema 1"] = img81
    st.image(tmp81[st.session_state.auswahl.get("Seite 8 Thema 1", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp81 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/vr9a5e8tb61yvlylxresd/Section1_Bild0.png?rlkey=urxc86z7utc3s7t37lel76v1w&dl=1",
        "https://www.dropbox.com/scl/fi/07hqmc7ebiqafoso58f1w/Section1_Bild2.png?rlkey=yx3ugptfkpylqn40mqihaigl2&dl=1",
        "https://www.dropbox.com/scl/fi/8hljyqhqz8e0590rwobx2/Section1_Bild9.png?rlkey=cpxaecoky589bxzv7220c8g0f&dl=1",
        "https://www.dropbox.com/scl/fi/xhsggle6yohtwwavgky9h/Section1_Bild5.png?rlkey=7prfqex97opq33jlxrg5zrn7c&dl=1",
        "https://www.dropbox.com/scl/fi/4kgyq1g43tn2j6yn31ya9/Section1_Bild7.png?rlkey=gif76nj9d7wvi1m5krpi2pxim&dl=1",
        "https://www.dropbox.com/scl/fi/uya53rjihl7osb705au7u/Section1_Bild10.png?rlkey=i1ndh4x33b3do6ins490jt4dg&dl=1",
        "https://www.dropbox.com/scl/fi/oz6jaapvgi0s6juov46la/Section1_Bild1.png?rlkey=4mg13vo39m4drfu824tqbnmx7&dl=1",
        "https://www.dropbox.com/scl/fi/akrucgl6byjxj7bhtruqm/Section1_Bild3.png?rlkey=mx1kexw13d1w86yfdp5vgf30c&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg81 = image_select(
        "Auswahl:",
        nvtmp81,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 1", 0),
        key=f"nvfrage81_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg81} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 1"] = nvimg81
    st.image(nvtmp81[st.session_state.auswahl.get("nv Seite 8 Thema 1", 0)])

    st.text('Topic 2: Structure and Functionality of Weichkorallen Colonies\n- Discusses morphological features, competitive abilities, and interactions with other species in coral reef communities.')

    tmp82 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/1tdt8v2uq3c08xiiv78zs/Section2_Bild3.png?rlkey=kufzdvpcdkhncdu0z0zz3srj5&dl=1",
        "https://www.dropbox.com/scl/fi/uk785xny0ksr7ajz1nuul/Section2_Bild0.png?rlkey=d23o0f9egoxvj163zonmpvs0r&dl=1",
        "https://www.dropbox.com/scl/fi/9lzadlv1cnkbev59cq45n/Section2_Bild10.png?rlkey=nzn4ierx4ewiysgb9sscig3pw&dl=1",
        "https://www.dropbox.com/scl/fi/zlrg4p0gmgxn85wtnf7io/Section2_Bild7.png?rlkey=klehgftbwz36yxgsk11c84lu3&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img82 = image_select(
        "Auswahl:",
        tmp82,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 2", 0),
        key=f"frage82_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img82} ausgewählt.")
    st.session_state.auswahl["Seite 8 Thema 2"] = img82
    st.image(tmp82[st.session_state.auswahl.get("Seite 8 Thema 2", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp82 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/ev6l2m2m3r393fjyvstik/Section2_Bild1.png?rlkey=p3hdu6gpv7txkepnh1jhm5o9r&dl=1",
        "https://www.dropbox.com/scl/fi/bcfw7r3mwm1w1evhxgfbu/Section2_Bild2.png?rlkey=cz1y3afsegxftg9g2zmkpauwc&dl=1",
        "https://www.dropbox.com/scl/fi/33gay2fc35tivnh1r5p0d/Section2_Bild8.png?rlkey=iyehpxieoleqlcqr5e8whnmfh&dl=1",
        "https://www.dropbox.com/scl/fi/mrq79ihvxe5yid66dhyy5/Section2_Bild6.png?rlkey=dlirss00bd7cvzj93ub25d5f4&dl=1",
        "https://www.dropbox.com/scl/fi/bhrgz724y7rpvpvnazzso/Section2_Bild4.png?rlkey=9dw04i4jai4mwihvkcatnbww8&dl=1",
        "https://www.dropbox.com/scl/fi/zpuck36uhckvo03cyxjoj/Section2_Bild5.png?rlkey=f48ip8jdjpxotxvmktt9mwny4&dl=1",
        "https://www.dropbox.com/scl/fi/73dth3inow26tvrcbctt5/Section2_Bild9.png?rlkey=v1y1vkhsrsrfvit74olsev8oj&dl=1",
    ]
    nvimg82 = image_select(
        "Auswahl:",
        nvtmp82,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 2", 0),
        key=f"nvfrage82_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg82} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 2"] = nvimg82
    st.image(nvtmp82[st.session_state.auswahl.get("nv Seite 8 Thema 2", 0)])

    st.text('Topic 3: Impacts of Environmental Stressors and Bioerosion\n- Addresses threats posed by climate change, pollution, and bioerosion processes on coral reef structure and diversity.')

    tmp83 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/58v2burk61djztfmzjlqv/Section3_Bild9.png?rlkey=n7g0zqyrsxtraeb9kr0h5p46w&dl=1",
        "https://www.dropbox.com/scl/fi/9hq9rvspv73ftfppdhsez/Section3_Bild4.png?rlkey=7w9xpqs7cd582uwvheiwr5hpm&dl=1",
        "https://www.dropbox.com/scl/fi/fb65uselun9gvz8fya72k/Section3_Bild3.png?rlkey=mg1ocqfbe4hm0za6rvitva2ce&dl=1",
    ]
    img83 = image_select(
        "Auswahl:",
        tmp83,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 3", 0),
        key=f"frage83_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img83} ausgewählt.")
    st.session_state.auswahl["Seite 8 Thema 3"] = img83
    st.image(tmp83[st.session_state.auswahl.get("Seite 8 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp83 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/egb14t9c5ctuo9ap4rkki/Section3_Bild5.png?rlkey=2u8g30ndlic9sjuqqvtpcoz9m&dl=1",
        "https://www.dropbox.com/scl/fi/o6vmqwijejo4552mh1edo/Section3_Bild1.png?rlkey=dce53qst48zc5vjy5bpn72wby&dl=1",
        "https://www.dropbox.com/scl/fi/jxjxp0zrg6gubeojajexz/Section3_Bild0.png?rlkey=1x882xt5rkyzbzsfbycvckvd7&dl=1",
        "https://www.dropbox.com/scl/fi/0468y5wvshbpqncpzv0qc/Section3_Bild6.png?rlkey=2zg9x1ieonjma5b9i8jbh877w&dl=1",
        "https://www.dropbox.com/scl/fi/51ak0jewokf1jwoarlyyh/Section3_Bild7.png?rlkey=d1s9vm6knmngv5bnyxx5r91lf&dl=1",
        "https://www.dropbox.com/scl/fi/3jj29mctcla97dy84aivm/Section3_Bild2.png?rlkey=ylqu6yqa6eut16pp4z6yn15yi&dl=1",
        "https://www.dropbox.com/scl/fi/vanhjru4n63kljjihjb8f/Section3_Bild10.png?rlkey=21wue2z3kk2ygqsad27d5nrkp&dl=1",
        "https://www.dropbox.com/scl/fi/31zaawm26jzwbi64j2ydo/Section3_Bild8.png?rlkey=cbfdagye9vdhf1cz1btbej9f8&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg83 = image_select(
        "Auswahl:",
        nvtmp83,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 3", 0),
        key=f"nvfrage83_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg83} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 3"] = nvimg83
    st.image(nvtmp83[st.session_state.auswahl.get("nv Seite 8 Thema 3", 0)])

    st.text('Topic 4: Historical Research and Current Studies in the Red Sea\n- Overviews significant contributions by German scientists to our understanding of coral reef ecology in the region, alongside modern cooperative projects focused on conservation.\n\n')

    tmp84 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/dmsnyv3qpltgyyjz8vay8/Section4_Bild3.png?rlkey=usnbdk90ji81irct4vsqa63zd&dl=1",
        "https://www.dropbox.com/scl/fi/bxu2x6kgugg5yrskt24rd/Section4_Bild0.png?rlkey=oofeivivr19bbqewrfj6lryvs&dl=1",
        "https://www.dropbox.com/scl/fi/mvv0whejfns57l3tusbcv/Section4_Bild4.png?rlkey=szg5owo0rg0noavvhgij4w3jz&dl=1",
        "https://www.dropbox.com/scl/fi/q65evtyd5qp1ywbyt8pza/Section4_Bild5.png?rlkey=rki9mvwted9poluz3o6i6gq0e&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img84 = image_select(
        "Auswahl:",
        tmp84,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 4", 0),
        key=f"frage84_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img84} ausgewählt.")
    st.session_state.auswahl["Seite 8 Thema 4"] = img84
    st.image(tmp84[st.session_state.auswahl.get("Seite 8 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp84 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/xu2lumrczbgd12mt4ix16/Section4_Bild2.png?rlkey=lpr9bejlujoq70b6odo5yw4w4&dl=1",
        "https://www.dropbox.com/scl/fi/ftn5ikzhfiqq7pli01zq0/Section4_Bild1.png?rlkey=5h35gthv8nkf8swy9d0t1wt6h&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg84 = image_select(
        "Auswahl:",
        nvtmp84,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 4", 0),
        key=f"nvfrage84_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg84} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 4"] = nvimg84
    st.image(nvtmp84[st.session_state.auswahl.get("nv Seite 8 Thema 4", 0)])

    st.text('Topic 5: Creating Successful Aquarium Environments\n- Guidelines for designing suitable habitats, ensuring optimal water quality, choosing compatible species, regular maintenance practices, and balanced diets for coral reef displays.\n\n')

    tmp85 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/slacwtvz2py097d0snmdn/Section5_Bild5.png?rlkey=gfxa6bnazqwig9c81w92579zg&dl=1",
        "https://www.dropbox.com/scl/fi/fj8bw8p8r1f2l3pyywwt6/Section5_Bild8.png?rlkey=tce52z7ob0xk2k8686374umjd&dl=1",
        "https://www.dropbox.com/scl/fi/kwotpay3t6v0alxyi7vxm/Section5_Bild0.png?rlkey=veh1uyee39ijmeyesz7j8qjk8&dl=1",
        "https://www.dropbox.com/scl/fi/yi58k81m8wwfb8i9wzkcl/Section5_Bild7.png?rlkey=cvr9bvkl0ew7iqhks7mo3cf8q&dl=1",
        "https://www.dropbox.com/scl/fi/y18ege7qgkmzy79ium6q8/Section5_Bild4.png?rlkey=r2vp1fneegqo1blmwzt210uvs&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img85 = image_select(
        "Auswahl:",
        tmp85,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 5", 0),
        key=f"frage85_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img85} ausgewählt.")
    st.session_state.auswahl["Seite 8 Thema 5"] = img85
    st.image(tmp85[st.session_state.auswahl.get("Seite 8 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp85 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/0qbx0j7dbhd6u10n3ab0g/Section5_Bild9.png?rlkey=m8m332hxwb72fsa2fmsp7tuou&dl=1",
        "https://www.dropbox.com/scl/fi/5wjoqug325c0o7xxq3f6g/Section5_Bild1.png?rlkey=cv4qc250fnna5oupijwkp2xk6&dl=1",
        "https://www.dropbox.com/scl/fi/pa05wy9s1hnsf89yx9isw/Section5_Bild2.png?rlkey=96hskpq4o5dbu9v42e45y1m9f&dl=1",
        "https://www.dropbox.com/scl/fi/b45s17s3ldlkenw9bviih/Section5_Bild6.png?rlkey=e2nsgvfkxnxv96nopw2z8vyvb&dl=1",
        "https://www.dropbox.com/scl/fi/eyvmrnit637dq7ubr8rvr/Section5_Bild10.png?rlkey=tp329o4epqfuw4d02urzo64pr&dl=1",
        "https://www.dropbox.com/scl/fi/c6jmaq00wjo2fdgwp1ni5/Section5_Bild3.png?rlkey=5jgsf8us4dqq2hgynnx4lp1i6&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg85 = image_select(
        "Auswahl:",
        nvtmp85,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 5", 0),
        key=f"nvfrage85_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg85} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 5"] = nvimg85
    st.image(nvtmp85[st.session_state.auswahl.get("nv Seite 8 Thema 5", 0)])

    st.button("(Nachfolgende) Seite 9", on_click=lambda: wechsel_zu("page9"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 10]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page9":
    st.title("Seite 9")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/au048vay3mvxtzmnbbd3a/Probekapitel_Ernaehrungsberater_Ernaehrungslehre_ENB01-B.pdf?rlkey=0sgejv2f4ybw4u86mh3ew8xni&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: To provide foundational knowledge on general principles of nutrition science and energy requirements for human beings.\n\nTopics:\n\n1. General Groundwork of Nutrition Science\n   - Defining key terms related to nutrients, metabolism, digestion, absorption, excretion, and storage processes within the body.\n\n2. Energy Requirement and Production\n   - Understanding how our bodies generate energy through various biological oxidations occurring inside cells, resulting in both heat and chemical energy stored in ATP molecules.\n\n3. Importance of Balanced Diet\n   - Learning about essential macro-nutrients like carbohydrates, proteins, and fats along with micronutrients including vitamins, minerals, water, fiber, phytochemicals, and flavors which are vital components of a balanced diet.\n\n4. Calculating Daily Energy and Nutrient Needs\n   - Detailing methods used to calculate daily caloric intake based on factors such as age, sex, weight, height, activity level, and lifestyle choices. Additionally discussing recommended percentages of each macronutrient required per day according to current guidelines.\n\n5. Role of Water in Human Nutrition\n   - Emphasizing the importance of proper hydration levels for maintaining overall health and wellbeing while explaining potential consequences associated with chronic dehydration.')

    st.button("(Nachfolgende) Seite 10", on_click=lambda: wechsel_zu("page10"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 8]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page10":
    st.title("Seite 10")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/77k16ecyi6i1rh1hz2b4h/bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All.pdf?rlkey=7sobuajkuf6a68j5v2w8chhaf&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: To inform readers about recent discoveries made through the detection of gravitational waves emitted by colliding black holes.')

    st.text('Topic 1: First Direct Observation of Merged Black Holes\n- On May 21, 2019, scientists detected gravitational waves caused by two merging black holes, providing direct evidence of these cosmic phenomena.\n\n')

    tmp101 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/set2coktgzm7oajk1i82z/Section1_Bild0.png?rlkey=q0xmlsy8ygi9xh3kchiougtk9&dl=1",
        "https://www.dropbox.com/scl/fi/iitjxelfa96tc0ug5n43r/Section1_Bild2.png?rlkey=0hu8nnju3neiq8yg1lnxwpjnx&dl=1",
        "https://www.dropbox.com/scl/fi/c871u3vby1lu7z394eq61/Section1_Bild4.png?rlkey=av7tczv69tiehzafjvp2rsawx&dl=1",
        "https://www.dropbox.com/scl/fi/lw7r60b6kzjeatpl2pztk/Section1_Bild1.png?rlkey=cdw5ngrw6cl8i96tiuh59ebhs&dl=1",
        "https://www.dropbox.com/scl/fi/f2fg2ckgadxdwa1y70gdx/Section1_Bild3.png?rlkey=ndh3f9yowze68pre06z7vafps&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img101 = image_select(
        "Auswahl:",
        tmp101,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 1", 0),
        key=f"frage101_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img101} ausgewählt.")
    st.session_state.auswahl["Seite 10 Thema 1"] = img101
    st.image(tmp101[st.session_state.auswahl.get("Seite 10 Thema 1", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp101 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/zxgzjzoz3jmu690g2dlz1/Section1_Bild6.png?rlkey=qt7gjyllsbmfs977n0dxn5hfh&dl=1",
        "https://www.dropbox.com/scl/fi/o9h41bijqxujgq5rwkg0y/Section1_Bild9.png?rlkey=ef4ufqz19t8aryq4or40uud9m&dl=1",
        "https://www.dropbox.com/scl/fi/ssukwvz522sw62kjaj9iy/Section1_Bild5.png?rlkey=63riws60mgsze7herwamvo6wk&dl=1",
        "https://www.dropbox.com/scl/fi/kbfpya01d7z5y6orbfc6q/Section1_Bild7.png?rlkey=v6j57hl7cuchtx74nc9d45huw&dl=1",
        "https://www.dropbox.com/scl/fi/q9qkbvbctftteccmfq7b8/Section1_Bild8.png?rlkey=mcxsiswl29t1q2o0ut7qkw0ab&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg101 = image_select(
        "Auswahl:",
        nvtmp101,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 1", 0),
        key=f"nvfrage101_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg101} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 1"] = nvimg101
    st.image(nvtmp101[st.session_state.auswahl.get("nv Seite 10 Thema 1", 0)])

    st.text('Topic 2: Properties of Detected Black Holes\n- The merged black hole had approximately three times the mass of our sun, while its precursors were around five and eight solar masses each.\n\n')

    tmp102 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/fxbgqnvhy6ocb9l9iyk43/Section2_Bild1.png?rlkey=enntk6n52zs3n7ylvvwkntl43&dl=1",
        "https://www.dropbox.com/scl/fi/pard5x7lbt3ezekgeqhdf/Section2_Bild0.png?rlkey=0dqm2dk5ngalx4o2klecqghvy&dl=1",
        "https://www.dropbox.com/scl/fi/m0ikj0i8k20mqf0lci3ye/Section2_Bild8.png?rlkey=cw3ri4lsw008wtjkorif6c08t&dl=1",
        "https://www.dropbox.com/scl/fi/lurqyfwq72kav4f1gw98v/Section2_Bild9.png?rlkey=msv81jipi4xmmmionyc7jgrh8&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img102 = image_select(
        "Auswahl:",
        tmp102,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 2", 0),
        key=f"frage102_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img102} ausgewählt.")
    st.session_state.auswahl["Seite 10 Thema 2"] = img102
    st.image(tmp102[st.session_state.auswahl.get("Seite 10 Thema 2", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp102 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/x4s5crja1h9q9686ykejr/Section2_Bild3.png?rlkey=nzoarv0pqihrguaa4b4v33d0o&dl=1",
        "https://www.dropbox.com/scl/fi/fg44cgc307zs8x9uwvhx5/Section2_Bild2.png?rlkey=e95nsxy793tu0j8q2tyxcgwy1&dl=1",
        "https://www.dropbox.com/scl/fi/5dmjt4yqfkpj47ua2cdg2/Section2_Bild6.png?rlkey=pzlfdnbcusn1kbeqvzwjeb6mf&dl=1",
        "https://www.dropbox.com/scl/fi/si19a84a3tphfbq3ogaam/Section2_Bild4.png?rlkey=e8cpkm1ke0bs5s1g8t5cist9o&dl=1",
        "https://www.dropbox.com/scl/fi/tfd4u0a3pxq2t7zqhvet9/Section2_Bild5.png?rlkey=3n1v5n41p1rdiqrtcvm96nzed&dl=1",
        "https://www.dropbox.com/scl/fi/5es3lio2za3cholb67pgn/Section2_Bild7.png?rlkey=rl7w8b0d3xkmkx98g58toiikm&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg102 = image_select(
        "Auswahl:",
        nvtmp102,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 2", 0),
        key=f"nvfrage102_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg102} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 2"] = nvimg102
    st.image(nvtmp102[st.session_state.auswahl.get("nv Seite 10 Thema 2", 0)])

    st.text('Topic 3: Energy Emission During Mergers\n- Around 3% of the total energy released during the collision was transformed into gravitational waves, making it equivalent to the combined light emission of billions of stars at the same time.\n\n')

    tmp103 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/hijwddbj2680lyczakptr/Section3_Bild5.png?rlkey=n990n42c9td6q275gc2vh7opg&dl=1",
        "https://www.dropbox.com/scl/fi/wlztpjvvnqroleqjswun0/Section3_Bild0.png?rlkey=rl2jfo1c8lfmjfvgrz3lfncz7&dl=1",
        "https://www.dropbox.com/scl/fi/ruvasgivxwdlymfpdjoa1/Section3_Bild4.png?rlkey=kcy0jk2r7wun3m180f1t177m1&dl=1",
        "https://www.dropbox.com/scl/fi/0t7mn81kbp94bai8dlbs5/Section3_Bild2.png?rlkey=ub27ir68s64kniah0wgt33bd0&dl=1",
        "https://www.dropbox.com/scl/fi/nnpbpxk9sq4hu8hjxwkwx/Section3_Bild3.png?rlkey=kbjqhfjppjo52bf38pyiyar67&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img103 = image_select(
        "Auswahl:",
        tmp103,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 3", 0),
        key=f"frage103_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img103} ausgewählt.")
    st.session_state.auswahl["Seite 10 Thema 3"] = img103
    st.image(tmp103[st.session_state.auswahl.get("Seite 10 Thema 3", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp103 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/ud4oteyddcq2nkbolfsgb/Section3_Bild1.png?rlkey=8y3zf2mszsubo4p7x28oeo9sb&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg103 = image_select(
        "Auswahl:",
        nvtmp103,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 3", 0),
        key=f"nvfrage103_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg103} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 3"] = nvimg103
    st.image(nvtmp103[st.session_state.auswahl.get("nv Seite 10 Thema 3", 0)])

    st.text('Topic 4: Importance of Gravitational Waves\n- These observations offer insights into various aspects of physics, including general relativity and the nature of dark matter. They can help astronomers understand how galaxies formed and evolve over time.\n\n')

    tmp104 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/xisc0tyzyy007n7hd2ti6/Section4_Bild2.png?rlkey=ukpnkr22d6mitabt5ngja4k73&dl=1",
        "https://www.dropbox.com/scl/fi/zfg2fpn3a61v12xucktp8/Section4_Bild8.png?rlkey=vi4e0svewffba2jo47bp1kk1j&dl=1",
        "https://www.dropbox.com/scl/fi/kdaj80yg38e4izyrren0g/Section4_Bild0.png?rlkey=p03dr5zfoaw5o5jsh5yqwc34n&dl=1",
        "https://www.dropbox.com/scl/fi/muqt4g5vg6f1rtdmndff2/Section4_Bild1.png?rlkey=gvy887lvncy4enl3ujdarb6v5&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img104 = image_select(
        "Auswahl:",
        tmp104,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 4", 0),
        key=f"frage104_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img104} ausgewählt.")
    st.session_state.auswahl["Seite 10 Thema 4"] = img104
    st.image(tmp104[st.session_state.auswahl.get("Seite 10 Thema 4", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp104 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/82wccpgdnumxrq39ujwah/Section4_Bild3.png?rlkey=3yhtrsdk5ij14mg9mzmarrz2n&dl=1",
        "https://www.dropbox.com/scl/fi/kqtp6dwuuh2rzge6d4atl/Section4_Bild6.png?rlkey=gr11nvjn0j3123meo68068fwt&dl=1",
        "https://www.dropbox.com/scl/fi/76p5iklxxyri4rgnyzv1d/Section4_Bild9.png?rlkey=mgxttxz5082uyqye266mrk1cq&dl=1",
        "https://www.dropbox.com/scl/fi/cpco8j2jf32pljn1qiuck/Section4_Bild4.png?rlkey=34uptbebnrhc1w57epmybzcoo&dl=1",
        "https://www.dropbox.com/scl/fi/jyyobu2u7a5q1lzwzr4qx/Section4_Bild7.png?rlkey=gnwinkbk2dfjwrd0qm74wd21a&dl=1",
        "https://www.dropbox.com/scl/fi/frco7ctepdicpfrndas53/Section4_Bild5.png?rlkey=29xryaisyf24jisanu84lgk63&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg104 = image_select(
        "Auswahl:",
        nvtmp104,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 4", 0),
        key=f"nvfrage104_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg104} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 4"] = nvimg104
    st.image(nvtmp104[st.session_state.auswahl.get("nv Seite 10 Thema 4", 0)])

    st.text('Topic 5: Future Research Plans\n- Scientists are preparing for further observation campaigns with improved sensitivity levels, aiming to detect more events and deepen understanding of this fascinating phenomenon.\n\n')

    tmp105 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/lwzk8a0h3h1d8kqfje3iz/Section5_Bild9.png?rlkey=kxaik7dger84g4bdo69sxdvyy&dl=1",
        "https://www.dropbox.com/scl/fi/4yyh22gghm12xlfcwe7z5/Section5_Bild5.png?rlkey=fcm54e92h6z465ty7yktx25sy&dl=1",
        "https://www.dropbox.com/scl/fi/vxvffp8pe3guc7ohzm9vi/Section5_Bild8.png?rlkey=ha2rwmecgpbxt24vtcauzw9xd&dl=1",
        "https://www.dropbox.com/scl/fi/2xj7lb7qzejw5yf9dhr24/Section5_Bild7.png?rlkey=gf9fzemtzbm4jelxu9ya8yyoz&dl=1",
        "https://www.dropbox.com/scl/fi/p2xbrs379ht39ik7ik7hv/Section5_Bild6.png?rlkey=7uriyaospj7sb7ai0jvdr1bcj&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    img105 = image_select(
        "Auswahl:",
        tmp105,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 5", 0),
        key=f"frage105_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {img105} ausgewählt.")
    st.session_state.auswahl["Seite 10 Thema 5"] = img105
    st.image(tmp105[st.session_state.auswahl.get("Seite 10 Thema 5", 0)])

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp105 = [
        "https://www.dropbox.com/scl/fi/9rhcgpm4a3lgepo42dtcp/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ic9spx70pyhf0vi6v3fsjvrlp&dl=1",
        "https://www.dropbox.com/scl/fi/7f8mbiy3p6jm22973aszi/Section5_Bild0.png?rlkey=41slhmcfwpfw4nb5fz9mi6ffa&dl=1",
        "https://www.dropbox.com/scl/fi/ic4fel4ea58gx48l747v7/Section5_Bild1.png?rlkey=uq34b9ymg9aozeys46xjnosx7&dl=1",
        "https://www.dropbox.com/scl/fi/35cms9lsa3uv3jmxsh0mh/Section5_Bild2.png?rlkey=e8i7focmbfw910cyrdyg6hy66&dl=1",
        "https://www.dropbox.com/scl/fi/9slxbs47yxgt2eud85vz4/Section5_Bild4.png?rlkey=0ils9y6wht8byqbmbj8dj5cng&dl=1",
        "https://www.dropbox.com/scl/fi/dp8evvrqlhub5jgy7ecdf/Section5_Bild3.png?rlkey=hqf122vefkpnoaj70wt3lyash&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
        "https://www.dropbox.com/scl/fi/583bjkljoalljqqp4vh4f/Platzhalter.png?rlkey=ylvmob8rsszsjo9tmi1bjllh2&dl=1",
    ]
    nvimg105 = image_select(
        "Auswahl:",
        nvtmp105,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 5", 0),
        key=f"nvfrage105_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg105} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 5"] = nvimg105
    st.image(nvtmp105[st.session_state.auswahl.get("nv Seite 10 Thema 5", 0)])

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [7, 8, 9]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

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

    st.text("Falls sich nach dem Klick auf den Button kein E-Mail-Fenster öffnet, aktivieren Sie bitte Pop-ups für diese Seite in Ihrem Browser. Alternativ können Sie die Ergebnisse kopieren oder einen Screenshot erstellen und per E-Mail an jstrauch@pagemachine.de senden. Vielen Dank!")

    st.button("Ändern", on_click=lambda: wechsel_zu("start"))
