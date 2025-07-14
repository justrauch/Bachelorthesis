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
    st.session_state.scroll_to_top = True
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
        "Thema 4: Lebensraum von Zebras\n"
        "Zebras leben typischerweise in offenen Savannen und Graslandschaften Afrikas. Ein wichtiger Bestandteil\n"
        "ihres Lebensraums sind Wasserstellen, die sie regelmäßig in Gruppen aufsuchen. Dabei ist zu beobachten\n"
        "dass Zebras oft gemeinsam trinken, um sich gegenseitig vor möglichen Raubtieren zu schützen."    )

    img63 = image_select(
        "Auswahl:",
        [
            "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
            "https://www.dropbox.com/scl/fi/ty14z8nmr5mojx2kb7bs1/WahrZebradpa0109-1.jpeg?rlkey=0pny0fwpaj4v99nwh2xxm34ih&dl=1",
            "https://www.dropbox.com/scl/fi/ldwbtg1ncry13p5schtin/image3.jpg?rlkey=h922dml3kw584vqop2le71yo9&dl=1",
            "https://www.dropbox.com/scl/fi/yiz4ycibua9rb2naitgjw/Bsp1_Wahl.png?rlkey=fheswjjy98aajg6zboroqublo&dl=1",
            "https://www.dropbox.com/scl/fi/rssx5yyin12xfo3slban1/file5_page6_image2.jpeg?rlkey=f72gr05cpt82kgiz64c1do7w4&dl=1",
            "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
        ],
        return_value="index",
        index=0,
        key=f"bsp_1_{st.session_state.reload_counter}"
    )

    st.text("Gute Wahl:")
    bsp1_arr = [
        "https://www.dropbox.com/scl/fi/yiz4ycibua9rb2naitgjw/Bsp1_Wahl.png?rlkey=fheswjjy98aajg6zboroqublo&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    bsp1_tmp = st.session_state.reload_counter % 2
    if bsp1_tmp == 0:
        st.image(bsp1_arr[0 if bsp1_tmp == 0 else 1])
    else:
        st.image(bsp1_arr[0 if bsp1_tmp == 1 else 1])

    st.text(       "Auswahl Nr. 4 ist sinnvoll, da das Bild die im Text beschriebene Szene, in der mehrere Zebras gemeinsam\n"
       "an einer Wasserstelle trinken, sehr gut visualisiert. Es unterstützt die Darstellung des typischen\n"
       "Lebensraums der Zebras und verdeutlicht ihr Sozialverhalten beim Trinken.\n"
       "Bild Nr. 3 passt weniger gut zur beschriebenen Szene, da es Zebras in Bewegung zeigt und nicht beim Trinken.\n"
       "Wäre Auswahl Nr. 4 nicht vorhanden, wäre die beste Wahl hier, keines der gezeigten Bilder auszuwählen.\n"
    )

    st.button(f"Frage 1", on_click=lambda s=f"page1": wechsel_zu(s))
    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))
    st.button("Nach oben scrollen", on_click=scroll())
if st.session_state.seite == "page1":
    st.title("Seite 1")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/c4ot3ris4xkgrz4vbgbow/40410000.pdf?rlkey=v7ex77n54ie5bix99rxpgk5id&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide detailed information on the German Federal Parliament (Bundestag) during its 20th term, including its roles, structures, buildings, members, and election process.')

    st.text('Topic 4: Buildings housing the Bundestag\n- Overviews the history and architecture of several parliamentary buildings located in Berlin, including the iconic glass dome atop the Reichstag building.\n- Describes additional facilities built recently to accommodate increased membership due to changes in voting regulations.\n\n')
    choice14_arr = [
        "https://www.dropbox.com/scl/fi/vuwjs4ykjb471unkmeqbt/Section4_choice.png?rlkey=8qg3vzh374evc5rqidaz05m4h&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice14_tmp = st.session_state.reload_counter % 2
    if choice14_tmp == 0:
        st.image(choice14_arr[0 if choice14_tmp == 0 else 1])
    else:
        st.image(choice14_arr[0 if choice14_tmp == 1 else 1])
    st.text(' An aerial view showcases a large, ornate building with a glass dome, surrounded by a park and a cityscape under a partly cloudy sky.')
    antwort14 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort14")
    st.session_state.auswahl["Seite 1 Frage"] = antwort14

    tmp14 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/by8bhno9vrpw4muuhnldq/Section4_Bild2.png?rlkey=vgofwjggqzaunkwhe1f8oohrx&dl=1",
        "https://www.dropbox.com/scl/fi/71r3l8fmblmidfert71r2/Section4_Bild0.png?rlkey=o1n8pcotadjr6kss85t8bkagw&dl=1",
        "https://www.dropbox.com/scl/fi/waj29s71quim2c7qox7ci/Section4_Bild1.png?rlkey=ety1m1rikukc5f3dus0ycxd3e&dl=1",
    ]
    img14 = image_select(
        "Mögliche Valide Bilder:",
        tmp14,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Valides Bild", 0),
        key=f"frage14_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Valides Bild"] = img14
    valid14_tmp = st.session_state.reload_counter % 2
    if valid14_tmp == 0:
        st.image(tmp14[st.session_state.auswahl.get("Seite 1 Valides Bild", 0)] if valid14_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp14[st.session_state.auswahl.get("Seite 1 Valides Bild", 0)] if valid14_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 1 Valides Bild"], key="wv14", disabled=True)
    st.button("(Nachfolgende) Seite 2", on_click=lambda: wechsel_zu("page2"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [3, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page2":
    st.title("Seite 2")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/mqg9sdpiykcvbye7ohjdv/Probe345Bd93.pdf?rlkey=72qar9s8kggg9pkvjx2laurth&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Discuss the history, characteristics, distribution, threats, conservation efforts, and educational programs regarding dinosaurs.')

    st.text('Topic 1: Origin and Dominance of Dinosaurs\n- Details how dinosaurs evolved around 225 million years ago during the Triassic Period; explains why they dominated land ecosystems until their extinction approximately 65 million years ago.\n\n')
    choice21_arr = [
        "https://www.dropbox.com/scl/fi/rrt8u8qw3ylaos4d3rehr/Section1_choice.png?rlkey=5uxlb2kquf4uczxwo8o7j2zof&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice21_tmp = st.session_state.reload_counter % 2
    if choice21_tmp == 0:
        st.image(choice21_arr[0 if choice21_tmp == 0 else 1])
    else:
        st.image(choice21_arr[0 if choice21_tmp == 1 else 1])
    st.text(' A colorful illustration depicts a map of Earth approximately 225 million years ago, showing the arrangement of continents like Asia, Africa, South America, India, Australia, and Antartica surrounded by oceans and labeled with geological features.')
    antwort21 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort21")
    st.session_state.auswahl["Seite 2 Frage"] = antwort21

    tmp21 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/kouvvc8o0wpikpmag5hsa/Section1_Bild0.png?rlkey=f8sc7vrcnjo5m3pbhilbwnpvi&dl=1",
        "https://www.dropbox.com/scl/fi/d8m5kz02kbflrm2285kj2/Section1_Bild6.png?rlkey=pml89r7lpczla3dauu20s7pwm&dl=1",
        "https://www.dropbox.com/scl/fi/v3vi2xp8ds4idoj5n0kyt/Section1_Bild2.png?rlkey=c5205waa41msaabfbf5stfmkg&dl=1",
        "https://www.dropbox.com/scl/fi/4b2rs338wcksqg35cbva6/Section1_Bild5.png?rlkey=w5c9ol53h35da0jjrs53sm0ci&dl=1",
        "https://www.dropbox.com/scl/fi/lhgxw39vbrm4zrlno1wrl/Section1_Bild4.png?rlkey=cuihdo31wuh8uzgp5ygq37ixy&dl=1",
        "https://www.dropbox.com/scl/fi/d0qeb7l4o9a06vt780ya9/Section1_Bild1.png?rlkey=p170cm8oj3ef187rqpitjgrke&dl=1",
        "https://www.dropbox.com/scl/fi/tb6bacqzkj0dej3389ar8/Section1_Bild3.png?rlkey=4kmo9kqwfpby1r1lp3ng4jw4x&dl=1",
    ]
    img21 = image_select(
        "Mögliche Valide Bilder:",
        tmp21,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 2 Valides Bild", 0),
        key=f"frage21_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 2 Valides Bild"] = img21
    valid21_tmp = st.session_state.reload_counter % 2
    if valid21_tmp == 0:
        st.image(tmp21[st.session_state.auswahl.get("Seite 2 Valides Bild", 0)] if valid21_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp21[st.session_state.auswahl.get("Seite 2 Valides Bild", 0)] if valid21_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 2 Valides Bild"], key="wv21", disabled=True)
    st.button("(Nachfolgende) Seite 3", on_click=lambda: wechsel_zu("page3"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 4, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page3":
    st.title("Seite 3")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/mqg9sdpiykcvbye7ohjdv/Probe345Bd93.pdf?rlkey=72qar9s8kggg9pkvjx2laurth&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Discuss the history, characteristics, distribution, threats, conservation efforts, and educational programs regarding dinosaurs.')

    st.text('Topic 3: Climate Changes and Global Catastrophe\n- Elaborates on changes in climate throughout the Mesozoic Era leading up to the End-Cretaceous Event; discusses theories suggesting a meteorite collision and volcanic activity contributed to the mass extinction of dinosaurs.\n\n')
    choice33_arr = [
        "https://www.dropbox.com/scl/fi/l5w6xl6ln1l8h50r25si0/Section3_choice.png?rlkey=wfr2wmqkiybxg5wyy9kj2dcj2&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice33_tmp = st.session_state.reload_counter % 2
    if choice33_tmp == 0:
        st.image(choice33_arr[0 if choice33_tmp == 0 else 1])
    else:
        st.image(choice33_arr[0 if choice33_tmp == 1 else 1])
    st.text(' The image shows a depiction of an asteroid impacting Earth on the left, alongside a map of the Yucatan Peninsula in Mexico and Belize highlighting the Chicxulub crater and the location of San Antonio on the right.')
    antwort33 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort33")
    st.session_state.auswahl["Seite 3 Frage"] = antwort33

    tmp33 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/u16x688q6y09khzbyi7yl/Section3_Bild5.png?rlkey=as5y0wufq1erx2z68tccpr35p&dl=1",
        "https://www.dropbox.com/scl/fi/bkyhddqxn48bin3nxjbxm/Section3_Bild9.png?rlkey=7h0npxrruxkc767fj3des0tms&dl=1",
        "https://www.dropbox.com/scl/fi/m3su5pfvzjsamwyytsoaw/Section3_Bild1.png?rlkey=jb0spl7y2mr36ryq9m1c6qnmw&dl=1",
        "https://www.dropbox.com/scl/fi/9wcs3f9h4r011e7vzmg08/Section3_Bild0.png?rlkey=46amdhwj5nbefs8s7jf47p7vb&dl=1",
        "https://www.dropbox.com/scl/fi/u2bbhm0g2qlt23bbzysu0/Section3_Bild4.png?rlkey=d42lm6rm0e65fo2h2uxkq8i1k&dl=1",
        "https://www.dropbox.com/scl/fi/z8524hjo5eftmngy2n1xs/Section3_Bild6.png?rlkey=dga2ncu0v5mfdkd0ym9uizxfv&dl=1",
        "https://www.dropbox.com/scl/fi/o8cjdavgaxfwgmsc95419/Section3_Bild7.png?rlkey=hgmb7a0z61iuuxjyvj42urocz&dl=1",
        "https://www.dropbox.com/scl/fi/foau6fur198pzvvhwkzly/Section3_Bild2.png?rlkey=a8btaxbimi4tcduz838g0emnd&dl=1",
        "https://www.dropbox.com/scl/fi/op0neayma64d3l07jj6xk/Section3_Bild8.png?rlkey=toy8dgwavfd7u85mhdga0t2vl&dl=1",
        "https://www.dropbox.com/scl/fi/3ikivxkzwdq7juzn9x0li/Section3_Bild3.png?rlkey=80x5hjichr680jjsab8oyfkzl&dl=1",
        "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
    ]
    img33 = image_select(
        "Mögliche Valide Bilder:",
        tmp33,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Valides Bild", 0),
        key=f"frage33_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Valides Bild"] = img33
    valid33_tmp = st.session_state.reload_counter % 2
    if valid33_tmp == 0:
        st.image(tmp33[st.session_state.auswahl.get("Seite 3 Valides Bild", 0)] if valid33_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp33[st.session_state.auswahl.get("Seite 3 Valides Bild", 0)] if valid33_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 3 Valides Bild"], key="wv33", disabled=True)
    st.button("(Nachfolgende) Seite 4", on_click=lambda: wechsel_zu("page4"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 5, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page4":
    st.title("Seite 4")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/wqkfgzdig35g0yo9neupf/Broschuere_2013_hires.pdf?rlkey=ewrhf2r8xtgke9ux3in0l3p95&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Understand the exploration of our solar system, focusing on significant findings related to planets, moons, asteroids, comets, and dwarf planets.')

    st.text('Topic 1: Key Findings About Inner & Outer Planets\n- Presents fundamental facts about terrestrial and gas giants, emphasizing their size, compositions, rotations, distances from the sun, and distinctive features like the Great Red Spot and Hexagon storm on Jupiter.\n\n')
    choice41_arr = [
        "https://www.dropbox.com/scl/fi/bxsl0059xbo6puplv4pic/Section1_choice.png?rlkey=bqdxmso4bpvzg0gl4n7hw7co1&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice41_tmp = st.session_state.reload_counter % 2
    if choice41_tmp == 0:
        st.image(choice41_arr[0 if choice41_tmp == 0 else 1])
    else:
        st.image(choice41_arr[0 if choice41_tmp == 1 else 1])
    st.text(' The image depicts a vibrant illustration of the solar system with planets orbiting a bright sun, set against a backdrop of a swirling galaxy and distant stars.')
    antwort41 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort41")
    st.session_state.auswahl["Seite 4 Frage"] = antwort41

    tmp41 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/r1s9w46sc84fd7xcdxqbx/Section1_Bild0.png?rlkey=u0fikgjx2zp1fuhysg7gom9mi&dl=1",
        "https://www.dropbox.com/scl/fi/aeubhasa0ktv9faf4gay0/Section1_Bild2.png?rlkey=tplpy5br06l26b5mip2edgb55&dl=1",
        "https://www.dropbox.com/scl/fi/1uyexuh3f8f9vp23j7g0w/Section1_Bild1.png?rlkey=wj6vdwgm60iguuapb0si25p5w&dl=1",
    ]
    img41 = image_select(
        "Mögliche Valide Bilder:",
        tmp41,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Valides Bild", 0),
        key=f"frage41_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Valides Bild"] = img41
    valid41_tmp = st.session_state.reload_counter % 2
    if valid41_tmp == 0:
        st.image(tmp41[st.session_state.auswahl.get("Seite 4 Valides Bild", 0)] if valid41_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp41[st.session_state.auswahl.get("Seite 4 Valides Bild", 0)] if valid41_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 4 Valides Bild"], key="wv41", disabled=True)
    st.button("(Nachfolgende) Seite 5", on_click=lambda: wechsel_zu("page5"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 6]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page5":
    st.title("Seite 5")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/dl7xr4edcjqye3xdx0nux/Menschenaffen_Unterrichtsmaterial.pdf?rlkey=lzkwispw171pcc5bpwtovn8ne&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide educational resources for teachers to facilitate learning about great apes through various subjects like German language, Biology, Social Studies, Geography, and Arts.')

    st.text('Topic 2: About WWF\'s Youth Education Program "Young Panda"\n- Details the goals and objectives of the youth education initiative aimed at children aged 8-14 years old.\n\n')
    choice52_arr = [
        "https://www.dropbox.com/scl/fi/24c6c3q5816z4m7c2gytf/Section2_choice.png?rlkey=ksp2wbdlxhcrq1gthaqgply7r&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice52_tmp = st.session_state.reload_counter % 2
    if choice52_tmp == 0:
        st.image(choice52_arr[0 if choice52_tmp == 0 else 1])
    else:
        st.image(choice52_arr[0 if choice52_tmp == 1 else 1])
    st.text(' A man in a blue jacket and black hat is pointing at a moss-covered log while a group of children wearing backpacks look on in a wooded area.')
    antwort52 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort52")
    st.session_state.auswahl["Seite 5 Frage"] = antwort52

    tmp52 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/xiaky9xm71j0ykzsfi6ej/Section2_Bild3.png?rlkey=il35b5uk54wgu5egmcutz7rbe&dl=1",
        "https://www.dropbox.com/scl/fi/9r397roisca37gvgx3rcx/Section2_Bild2.png?rlkey=3rcdl9wxmnxao4agzcriq0yeo&dl=1",
        "https://www.dropbox.com/scl/fi/hs32a89h00g4lcas626um/Section2_Bild6.png?rlkey=zjbtpzgnd1qc2ssezeyo3g0ht&dl=1",
        "https://www.dropbox.com/scl/fi/y5nke1j5fkh2qvc8evlal/Section2_Bild4.png?rlkey=5klt1kn39b20sinh4agfvbt6r&dl=1",
        "https://www.dropbox.com/scl/fi/t55pqpz6sg95mufrdwdv2/Section2_Bild5.png?rlkey=ac881etgr7zxaluo92k98lceo&dl=1",
        "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
        "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
    ]
    img52 = image_select(
        "Mögliche Valide Bilder:",
        tmp52,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Valides Bild", 0),
        key=f"frage52_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Valides Bild"] = img52
    valid52_tmp = st.session_state.reload_counter % 2
    if valid52_tmp == 0:
        st.image(tmp52[st.session_state.auswahl.get("Seite 5 Valides Bild", 0)] if valid52_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp52[st.session_state.auswahl.get("Seite 5 Valides Bild", 0)] if valid52_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 5 Valides Bild"], key="wv52", disabled=True)

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp52 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/s5ltf9jcelp2633ub7426/Section2_Bild1.png?rlkey=7lgdvh97gbqq8c45s56upngpk&dl=1",
        "https://www.dropbox.com/scl/fi/5xgwwydqnuhkqyuq0opgt/Section2_Bild0.png?rlkey=ejvw2qjh5i0bg33zrenq758gn&dl=1",
        "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
    ]
    nvimg52 = image_select(
        "Nicht Valide Bilder:",
        nvtmp52,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Nicht Valides Bild", 0),
        key=f"nvfrage52_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg52} ausgewählt.")
    st.session_state.auswahl["Seite 5 Nicht Valides Bild"] = nvimg52
    nvalid52_tmp = st.session_state.reload_counter % 2
    if nvalid52_tmp == 0:
        st.image(nvtmp52[st.session_state.auswahl.get("Seite 5 Nicht Valides Bild", 0)] if nvalid52_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp52[st.session_state.auswahl.get("Seite 5 Nicht Valides Bild", 0)] if nvalid52_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild: ", value=st.session_state.auswahl["Seite 5 Nicht Valides Bild"], key="nvw52", disabled=True)

    st.button("(Nachfolgende) Seite 6", on_click=lambda: wechsel_zu("page6"))

    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page6":
    st.title("Seite 6")
    st.text(text)

    pdf_url = "https://www.dropbox.com/scl/fi/x0ug7u457t0agaoh9gz2d/bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All.pdf?rlkey=ln77357z0hins7bialfdpbbfb&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Describe recent discoveries made through the detection of gravitational waves caused by colliding black holes.')

    st.text('Topic 1: First Direct Observation of Merged Black Holes\n- On May 21, 2019, scientists detected gravitational waves originating from the merger of two massive black holes approximately 8 billion light years away. This marked the first direct observation of this phenomenon.\n\n')
    choice61_arr = [
        "https://www.dropbox.com/scl/fi/73i9its0wtcfbj2nodtlv/Section1_choice.png?rlkey=ald5l08fkx9td24a12i6ept6r&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice61_tmp = st.session_state.reload_counter % 2
    if choice61_tmp == 0:
        st.image(choice61_arr[0 if choice61_tmp == 0 else 1])
    else:
        st.image(choice61_arr[0 if choice61_tmp == 1 else 1])
    st.text(' The image depicts two black holes surrounded by swirling blue light and a grid-like pattern against a backdrop of numerous stars.')
    antwort61 = st.radio("Unterstützt diese Beschreibung das Thema?", ["Ja", "Nein"], key="antwort61")
    st.session_state.auswahl["Seite 6 Frage"] = antwort61

    tmp61 = [
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
        "https://www.dropbox.com/scl/fi/ivnnerv0b665kjym04zoc/Section1_Bild0.png?rlkey=etow49rztsgo0b4n0o8w6nbwn&dl=1",
        "https://www.dropbox.com/scl/fi/yzon7j8ms8yxxv4fmsn0k/Section1_Bild2.png?rlkey=svs5cue54jf42rw35lsgtbdac&dl=1",
        "https://www.dropbox.com/scl/fi/8o95xn80i8ts2t6ltl2c2/Section1_Bild5.png?rlkey=p0kd5fnrlvy4xq964ol1sjgs4&dl=1",
        "https://www.dropbox.com/scl/fi/fvvigaz594fr57ttmsl0e/Section1_Bild4.png?rlkey=4gefa4f3kk34rk1onp248gcsj&dl=1",
        "https://www.dropbox.com/scl/fi/ypf2bqvwab4ymncrqq5wt/Section1_Bild1.png?rlkey=d1ra0cbzz7h0jxeho2drm72mq&dl=1",
        "https://www.dropbox.com/scl/fi/tgkl0wi5ri1ic0gcc6w9t/Section1_Bild3.png?rlkey=yie6nb51qaiwrokrq8rbyktdn&dl=1",
        "https://www.dropbox.com/scl/fi/ffn7bp3vcuwcehe7af48x/Platzhalter.png?rlkey=jwud0umcxbw973lfjkchu1c6d&dl=1",
    ]
    img61 = image_select(
        "Mögliche Valide Bilder:",
        tmp61,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Valides Bild", 0),
        key=f"frage61_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Valides Bild"] = img61
    valid61_tmp = st.session_state.reload_counter % 2
    if valid61_tmp == 0:
        st.image(tmp61[st.session_state.auswahl.get("Seite 6 Valides Bild", 0)] if valid61_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp61[st.session_state.auswahl.get("Seite 6 Valides Bild", 0)] if valid61_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text_input("Gewähltes Bild", value=st.session_state.auswahl["Seite 6 Valides Bild"], key="wv61", disabled=True)
    with st.container():
        cols = st.columns([2] * 6)
        fragen = [1, 2, 3, 4, 5]
        for i, frage in enumerate(fragen):
            cols[i].button(f"Seite {frage}", on_click=lambda s=f"page{frage}": wechsel_zu(s))

    st.button("Auswertung", on_click=lambda: wechsel_zu("auswertung"))

    st.button("Erklärung", on_click=lambda: wechsel_zu("start"))

    st.button("Nach oben scrollen", on_click=scroll)

elif st.session_state.seite == "auswertung":
    st.title("Auswertung")
    st.write("Du hast diese Bilder gewählt:")

    auswertung_text = ""

    for key, value in sorted(st.session_state.auswahl.items()):
        auswertung_text += f"{key} → {value}\n"

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
