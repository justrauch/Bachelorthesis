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
        "Thema 4: Lebensraum von Zebras\n"
        "Zebras leben typischerweise in offenen Savannen und Graslandschaften Afrikas. Ein wichtiger Bestandteil\n"
        "ihres Lebensraums sind Wasserstellen, die sie regelmäßig in Gruppen aufsuchen. Dabei ist zu beobachten\n"
        "dass Zebras oft gemeinsam trinken, um sich gegenseitig vor möglichen Raubtieren zu schützen."    )

    img63 = image_select(
        "Auswahl:",
        [
            "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
            "https://www.dropbox.com/scl/fi/gnrywvdllfedzqez5wn0j/WahrZebradpa0109-1.jpeg?rlkey=dp1lqmivqju68nxpdi15pwhv5&dl=1",
            "https://www.dropbox.com/scl/fi/dv00ehp04mgyx1ohlnfb3/image3.jpg?rlkey=bb8dyqbxrxtj0tmgpirgdmltr&dl=1",
            "https://www.dropbox.com/scl/fi/i04s5qrna96bln329otx6/Bsp1_Wahl.png?rlkey=ubintxzsj28w7bbeje2pegaof&dl=1",
            "https://www.dropbox.com/scl/fi/jifip30fr6kfwllt8yhi5/file5_page6_image2.jpeg?rlkey=kouzj5k7zdfa4l9pas20k22sr&dl=1",
            "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        ],
        return_value="index",
        index=0,
        key=f"bsp_1_{st.session_state.reload_counter}"
    )

    st.text("Gute Wahl:")
    bsp1_arr = [
        "https://www.dropbox.com/scl/fi/i04s5qrna96bln329otx6/Bsp1_Wahl.png?rlkey=ubintxzsj28w7bbeje2pegaof&dl=1",
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
    ]
    bsp1_tmp = st.session_state.reload_counter % 2
    if bsp1_tmp == 0:
        st.image(bsp1_arr[0 if bsp1_tmp == 0 else 1])
    else:
        st.image(bsp1_arr[0 if bsp1_tmp == 1 else 1])

    st.text(       
        "Auswahl Nr. 4 ist sinnvoll, da das Bild die im Text beschriebene Szene, in der mehrere Zebras gemeinsam"
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

    pdf_url = "https://www.dropbox.com/scl/fi/z93335bjzo7rm551y2vwd/40410000.pdf?rlkey=3kbzwf7limofb2vg15wuqeitd&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide detailed information on the German Federal Parliament (Bundestag) during its 20th term, including its roles, structures, buildings, members, and election process.')

    st.text("Topic 1: Functions of the Bundestag\n- Outlines the role of the Bundestag as Germany's sole directly elected constitutional organ responsible for making federal laws, electing the chancellor, controlling the government, and participating in appointing various officials.\n\n")

    tmp11 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/m0351svtaaasburfeqk9i/Section1_Bild0.png?rlkey=lmnmrip5xsjrad6p7ezc0szgh&dl=1",
        "https://www.dropbox.com/scl/fi/1qe5m4vv31zfhx1iw6n9m/Section1_Bild2.png?rlkey=0i5qy7bv9swk2tqm5ar0btbd2&dl=1",
        "https://www.dropbox.com/scl/fi/iqzkg3zycu5l0ephq8emh/Section1_Bild1.png?rlkey=g1a07qbj67mxq28v7bwejyn41&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/t6x2ohvd35xr04sutun1a/Section2_Bild1.png?rlkey=guczg5yk4bp06idh5bgkg9n0s&dl=1",
        "https://www.dropbox.com/scl/fi/e4zwr7137cms65xqd2o7o/Section2_Bild3.png?rlkey=ng1a8auz5yb4wmzouk6csb4do&dl=1",
        "https://www.dropbox.com/scl/fi/fr4f03ozbm3cj0msns2ee/Section2_Bild0.png?rlkey=okv4di8gkpctpcfjut2zcwejs&dl=1",
        "https://www.dropbox.com/scl/fi/o3waiuvbm7fewf5r1lixj/Section2_Bild2.png?rlkey=zexmh1d7tr655btg060a2di8e&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/1y6oixavvxrgr6obscvos/Section3_Bild1.png?rlkey=ullygffwo2frreefpwhzs45ng&dl=1",
        "https://www.dropbox.com/scl/fi/29d6xuwhnizz42mfefkj9/Section3_Bild0.png?rlkey=3lwv01lo08kupsmt5579x8b9z&dl=1",
        "https://www.dropbox.com/scl/fi/emq8z05e08evbgiqxuxo3/Section3_Bild2.png?rlkey=a08ctq9pw217qzskvs125e5lm&dl=1",
        "https://www.dropbox.com/scl/fi/2ykjvmfemsfwoc1343bun/Section3_Bild3.png?rlkey=rb1fw8z382zkc82pnpkm65aw9&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/ui8eukzyzpcfxuemy7fmv/Section4_Bild3.png?rlkey=7l1ytw5o2j4votrq9n1b7a0do&dl=1",
        "https://www.dropbox.com/scl/fi/yv3yexhmlsfy3dwao76cu/Section4_Bild2.png?rlkey=w3s7d78fb46q2w87gp2ekl2to&dl=1",
        "https://www.dropbox.com/scl/fi/o1juy4tfnhm2sh1kddhus/Section4_Bild0.png?rlkey=6qfnyzhjoyv4op9r5253x7leq&dl=1",
        "https://www.dropbox.com/scl/fi/iindmhappmyc566spdbz5/Section4_Bild1.png?rlkey=q20l3vn229c5e4k2esfxgnjsr&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/8pz9q0senogpg5uoz1ff5/Section5_Bild0.png?rlkey=sp50yagai2fq97fbxk6jtbhf6&dl=1",
        "https://www.dropbox.com/scl/fi/erwd24m015hgfids1njb1/Section5_Bild1.png?rlkey=k7ljevark1qraqceqlfvy8rlm&dl=1",
        "https://www.dropbox.com/scl/fi/fswoipcgrv9uzijeuqlxn/Section5_Bild2.png?rlkey=5jb579cjaw5vb08sfhnsld6hq&dl=1",
        "https://www.dropbox.com/scl/fi/ip57qcispln8mp2f8552h/Section5_Bild3.png?rlkey=m9pmlky2xh0jleh0nnbhbtemp&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/uk3rrejhj1ayneahq46z1/potenzial_der_windenergie.pdf?rlkey=itcvbluhbbwf724y69kn2wuob&dl=0"
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/esjpt9kwiad4jau7zszox/Section5_Bild0.png?rlkey=egq4xgqm46pf0772qdy1l59hc&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/bi8w9sl7qnq9h18j39715/Probe345Bd93.pdf?rlkey=j4omzxee0cohz3gdzmghixbrz&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Investigate the history, characteristics, distribution, threats, conservation efforts, and educational programs regarding dinosaurs.')

    st.text("Topic 1: History and Origin\n- Discusses when dinosaurs first emerged during Earth's history and how they evolved into various groups like sauropods, theropods, ceratopsians, and others.\n\n")

    tmp31 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/1admsp4990d1r371o9o3p/Section1_Bild0.png?rlkey=gkozvzpe09cnefgu3t0o519eq&dl=1",
        "https://www.dropbox.com/scl/fi/r649wlyp1wyq82azm2bxw/Section1_Bild6.png?rlkey=6mjjdq2uw3zru2tqbp72g3l3r&dl=1",
        "https://www.dropbox.com/scl/fi/jbx93gbix90o7xstxlm4h/Section1_Bild2.png?rlkey=hdult7105pxx89k3kmcinsg7o&dl=1",
        "https://www.dropbox.com/scl/fi/05xkuttgroai0k5r8v48j/Section1_Bild5.png?rlkey=0e2cu4pyh9s0qdveykwmxr3pd&dl=1",
        "https://www.dropbox.com/scl/fi/4v6jz0qr1cngqbmw8qqkq/Section1_Bild7.png?rlkey=kznod4rcyi6tvqf5p8rdppdje&dl=1",
        "https://www.dropbox.com/scl/fi/iz10yoqg1p7vfuzvhfhld/Section1_Bild8.png?rlkey=4iec51u5k11hw8vji8zcbw3xd&dl=1",
        "https://www.dropbox.com/scl/fi/pdno8e36b6hcpjguld2qj/Section1_Bild1.png?rlkey=az6m16f33zebwwezrquokme1o&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/us9bz480prgpvzimwidp3/Section1_Bild4.png?rlkey=5mzuswlol5db8ty6u42pb7n55&dl=1",
        "https://www.dropbox.com/scl/fi/t6u8g4d7841j298v6niz6/Section1_Bild3.png?rlkey=fjzt5q2cxe26iqk8lr2l2x1ul&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/sj5n3jhftd25anpm0nlhc/Section2_Bild1.png?rlkey=dave8tdvwdnh96t3fsqt53ek9&dl=1",
        "https://www.dropbox.com/scl/fi/918rlrwy4e8eszbr949nf/Section2_Bild3.png?rlkey=qb8im6idifghvcvk0vy2j68j8&dl=1",
        "https://www.dropbox.com/scl/fi/v5dpcwfalxbbo6b4ofuap/Section2_Bild0.png?rlkey=8fq3fek233u88d0uyb6xvi7j5&dl=1",
        "https://www.dropbox.com/scl/fi/xthpxikwojv026mo1cmy4/Section2_Bild2.png?rlkey=1d5gl1t7sx84qld0dp1guevdm&dl=1",
        "https://www.dropbox.com/scl/fi/idymx53khg3rpb6bei8ty/Section2_Bild8.png?rlkey=nkgh7nje12vclcc3yovr3kslo&dl=1",
        "https://www.dropbox.com/scl/fi/c038787tgerajblh1olwk/Section2_Bild6.png?rlkey=eflhxaafk0kxxf1lc5r8qmekd&dl=1",
        "https://www.dropbox.com/scl/fi/w679tlk8v8f1r56v7qytd/Section2_Bild4.png?rlkey=mbz2phukdzu8embrbxol182vz&dl=1",
        "https://www.dropbox.com/scl/fi/kgwxzcc9gcnzq6fubch28/Section2_Bild5.png?rlkey=e31jwl3kklbgmf72fz5t7nb8g&dl=1",
        "https://www.dropbox.com/scl/fi/9auj8f9bfiod953ntw3sj/Section2_Bild7.png?rlkey=dpj6imu2sp3p7bmo2xvzr6bul&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/dfia1fkzew81rrzcnn9cl/Section2_Bild10.png?rlkey=qfpfs3pfqyhg3lmzmnyay15wz&dl=1",
        "https://www.dropbox.com/scl/fi/lj15hl34yrm7kukeir0at/Section2_Bild9.png?rlkey=51tgc140nqzrd2voelfl2zgfx&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/iq7djpgp0bu76yet0o057/Section3_Bild5.png?rlkey=3qsym2xl6jo9pehbks9xs0p8n&dl=1",
        "https://www.dropbox.com/scl/fi/0o5nchf96g9fq3fjwcxn8/Section3_Bild1.png?rlkey=ww1y3pzzdjxe89u0csaxd953q&dl=1",
        "https://www.dropbox.com/scl/fi/i4y4gnh79kf4rwszser7y/Section3_Bild0.png?rlkey=y0ypoeakv48owlwcpkptnlfn2&dl=1",
        "https://www.dropbox.com/scl/fi/2n9wk8kiecj1fllzihm38/Section3_Bild4.png?rlkey=ysnp4o2lsmhfz691bim0vx8mu&dl=1",
        "https://www.dropbox.com/scl/fi/88itz34vsc9e66rwkobvd/Section3_Bild2.png?rlkey=r4z124zlo7jiwcqv4bb6pubmz&dl=1",
        "https://www.dropbox.com/scl/fi/irujxcm4niux9x9toayu4/Section3_Bild3.png?rlkey=j5mxgyaryx0ktrwuacxw8mxoe&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/ahwu80v5pin9hgxifv50g/Section4_Bild3.png?rlkey=nppxm3fxjpbpins9ys8t1xcya&dl=1",
        "https://www.dropbox.com/scl/fi/cxne01rezgrqr7jh786qg/Section4_Bild2.png?rlkey=ki48ijor7zpf9r59d07rlfco6&dl=1",
        "https://www.dropbox.com/scl/fi/mywqxnnl87zzncs8siln4/Section4_Bild0.png?rlkey=50vwgq658lnsk1gd2f9hfm6zy&dl=1",
        "https://www.dropbox.com/scl/fi/6oh72xedq4qpv06oqhvlx/Section4_Bild4.png?rlkey=0a03e021sxtauy8pehwahtp2k&dl=1",
        "https://www.dropbox.com/scl/fi/6wufcyqzn1ifqidlidf9i/Section4_Bild1.png?rlkey=ctulqh7u0n5v4wm82l4hva98m&dl=1",
        "https://www.dropbox.com/scl/fi/5i3hc2bqykjzesiboltz7/Section4_Bild5.png?rlkey=mbatthp4td0h1y2jjx5hfmwg9&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/211ri032f9jiv405uy2hj/Section5_Bild5.png?rlkey=d8gav5f1zca63a66mm45414hk&dl=1",
        "https://www.dropbox.com/scl/fi/43lwoxdwpl5huhzowsfwj/Section5_Bild8.png?rlkey=nos979x8xlq4caicpenfvgpv4&dl=1",
        "https://www.dropbox.com/scl/fi/r5onun8jz68fu0rfntkjd/Section5_Bild0.png?rlkey=4i0hitx2qu4ioi55ju0b6z5kq&dl=1",
        "https://www.dropbox.com/scl/fi/jc405yotq9x5gax6xjqph/Section5_Bild1.png?rlkey=nilquhsrhum0taquuaxlm9uwn&dl=1",
        "https://www.dropbox.com/scl/fi/pfco4tn995y6tr0h2sose/Section5_Bild2.png?rlkey=slawea6yo96fclhm4om2dvwdy&dl=1",
        "https://www.dropbox.com/scl/fi/qh74c3xs75g5gl3d93275/Section5_Bild7.png?rlkey=lmehtduriw92kf9kr43neyi5i&dl=1",
        "https://www.dropbox.com/scl/fi/rt6jts1yde7ld6avb6u36/Section5_Bild4.png?rlkey=rqc9fo8p1pcc2hlep84rceijw&dl=1",
        "https://www.dropbox.com/scl/fi/0h6x0iyoxmp39yp0440qr/Section5_Bild6.png?rlkey=w5z2j8piqiu6hyb4n3owys16r&dl=1",
        "https://www.dropbox.com/scl/fi/7g3m2jxddfdgt1cfna41o/Section5_Bild3.png?rlkey=hxtyel14nja94hs4wzppvymva&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/qbkzfdlu6d4y3k9t27iaw/Zweiter_Weltkrieg_01.pdf?rlkey=2kuwugtc1jclup8m1nfljgow4&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text("Goal: To provide historical context on the causes, events, and consequences of World War II, particularly focusing on Austria's role during this period.")

    st.text('Topic 1: Pre-World War II Era\n- Details the dissolution of the monarchy in Austria-Hungary after World War I, establishment of the First Republic, Treaties of Versailles and Saint Germain assigning blame for World War I to Germany and Austria, economic struggles faced by the new republic in the 1920s.\n\n')

    tmp41 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/t5gjjica77iraiocj6ptk/Section1_Bild0.png?rlkey=n1ssw0gu9iqgc7fvujx43kkh0&dl=1",
        "https://www.dropbox.com/scl/fi/y9l4zs7yxt4z2p2k73cmv/Section1_Bild2.png?rlkey=n7sasywlo00tscdi8rj75tt0s&dl=1",
        "https://www.dropbox.com/scl/fi/9xoaai7qctn5bwsjie9dd/Section1_Bild1.png?rlkey=g2bba4s39vmbjaabwiqamgrz7&dl=1",
        "https://www.dropbox.com/scl/fi/sbgc05comdcvbmptqhgey/Section1_Bild3.png?rlkey=3mhp12oqysvhej96knrn234eh&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/amcozivxpm7cu5stpihxg/Section2_Bild1.png?rlkey=qhf3o1p1jd92pt033s22wy4r4&dl=1",
        "https://www.dropbox.com/scl/fi/xs7xt0j8vf9pksl8r753v/Section2_Bild3.png?rlkey=wap51cxsvkfdwzjlq4ig54qxt&dl=1",
        "https://www.dropbox.com/scl/fi/zc22xknucmfnb4p2yxf4k/Section2_Bild0.png?rlkey=q0xq9puiw2ma011ctbmk3s7qq&dl=1",
        "https://www.dropbox.com/scl/fi/ikdc6rqt80120z50dhg0k/Section2_Bild2.png?rlkey=71tjf5ng34zm92mo2h8cyim6s&dl=1",
        "https://www.dropbox.com/scl/fi/net3h3opfnlgev17mq6hs/Section2_Bild4.png?rlkey=9jhd9v7q50yfuascy2yseayrk&dl=1",
        "https://www.dropbox.com/scl/fi/dl26hnnye0imzrlimboh7/Section2_Bild5.png?rlkey=havm56gp9uul6sbq8e7h6aqzx&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/z1uhfq8i4xs1u2oywu5di/Section3_Bild5.png?rlkey=1f1ymyfqce16qq3hub4w17o74&dl=1",
        "https://www.dropbox.com/scl/fi/3zffxhkz1bisgfi58mtid/Section3_Bild1.png?rlkey=wou772rxgk2xmj84to0h0f3w3&dl=1",
        "https://www.dropbox.com/scl/fi/s290k0rtvu89np7wovn40/Section3_Bild4.png?rlkey=dtoqf7ho1ekjtspw8ofocwcru&dl=1",
        "https://www.dropbox.com/scl/fi/chqxvo9ljktf2w1zdyz7u/Section3_Bild2.png?rlkey=ue6bcvhdg0ae75q00bjzt6jad&dl=1",
        "https://www.dropbox.com/scl/fi/nazohzkamfknrb6bbl6gv/Section3_Bild3.png?rlkey=36wisbvupuzskuuap7os99476&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/h3zxqh0d0zp2ecqvsmc5x/Section3_Bild0.png?rlkey=y0m2nybp9jgpm34epqg6x0cli&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/s48jh2pmc0jtzrpmqjgh4/Section4_Bild3.png?rlkey=6hc5jg0vuyfgks44cjqxhcpc0&dl=1",
        "https://www.dropbox.com/scl/fi/kajhsnj68wapsdk7kkhk0/Section4_Bild2.png?rlkey=bnsmcgvbomd0q032e26zjoufr&dl=1",
        "https://www.dropbox.com/scl/fi/prlr9yg1g3ji7ggdgz2ko/Section4_Bild0.png?rlkey=cidlrq9bomyh3ijz6m37g8ok7&dl=1",
        "https://www.dropbox.com/scl/fi/vjw6y1bsud27g7bssi154/Section4_Bild4.png?rlkey=up617rp4sns5vu07jjg8pc5lp&dl=1",
        "https://www.dropbox.com/scl/fi/y0uh5l1zjaccsi7502ymj/Section4_Bild5.png?rlkey=gdmtrnza9o72j82gyi1tmw4bq&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/3gjfiiaac5wiuqveo5vgj/Section4_Bild1.png?rlkey=hmlu5x43q3c70p3q16nq7v674&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/0hljhenkp3hbzmelkzi6q/Section5_Bild0.png?rlkey=mp5a868nkdgn4qq8g6hvuezd9&dl=1",
        "https://www.dropbox.com/scl/fi/2ig3dtse07wphxeacf0rd/Section5_Bild2.png?rlkey=g3st5vm7vhx5yz7ont1zhfo95&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/u8t3j7fe3ltht4db1f3h0/Section5_Bild1.png?rlkey=i2rzhj6aod0dpyf61mhizqduu&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/bujlwfirh477yme1m7to7/Broschuere_2013_hires.pdf?rlkey=6qzae3tv8yea335bavyun66tc&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Understand the structure, key components, and ongoing exploration of our solar system, with a focus on Mars and accessible image data repositories.')

    st.text('Topic 1: Our Solar System Overview\n- Presents basic facts about each planet, moon, asteroid, comet, and dwarf planet, including size, composition, distances from the Sun, rotations, and orbits.')

    tmp51 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/60b3q58cbxvlfwv3lidz7/Section1_Bild0.png?rlkey=m6wgoxw4pnzrhjifq7d34thcs&dl=1",
        "https://www.dropbox.com/scl/fi/fjq37pb9mf2sam50umrvd/Section1_Bild2.png?rlkey=fe5070u4xncf66abm7babuuwt&dl=1",
        "https://www.dropbox.com/scl/fi/a6eex0vjaerj9vv0phygd/Section1_Bild1.png?rlkey=6bxyunefqcinzevhqcqu5szzv&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/i5qssjw2aio69kjrhv2pg/Section2_Bild1.png?rlkey=qt23ackca865iyp5ye76j3lrz&dl=1",
        "https://www.dropbox.com/scl/fi/pron02mxpk6f4qewvf32h/Section2_Bild0.png?rlkey=k0y5qcoaz5m1rsiiltklawzxr&dl=1",
        "https://www.dropbox.com/scl/fi/d5bozc9dnbgrf8lg94x11/Section2_Bild2.png?rlkey=hxzaych20jzmqel2e5pi25bnd&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/q8x3mqj1gthgkukxrerh7/Section3_Bild1.png?rlkey=vzyryg9ccuvns8wibco3idpfx&dl=1",
        "https://www.dropbox.com/scl/fi/gt2t7auo8q67nwq6gj3v1/Section3_Bild2.png?rlkey=4tray16o22vjlzld95204ebk6&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/ygpfpu3ozbtk1totkklu8/Section3_Bild0.png?rlkey=wvefw4cxcf7jei34v0lid0yv8&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/k9g4l6gavi4l38m5cg2qe/Section4_Bild2.png?rlkey=94jqe9rwnw9jjfwd2q15571et&dl=1",
        "https://www.dropbox.com/scl/fi/4q1shl98fvzv79tge267f/Section4_Bild1.png?rlkey=1uquobhxg3miz7dicrjghewa2&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/rg4kkqxkq48csc833y1fe/Section4_Bild3.png?rlkey=20yavikixjxfs3dfsec0hpvl8&dl=1",
        "https://www.dropbox.com/scl/fi/z7bt98cx9w00glz32zrib/Section4_Bild0.png?rlkey=ogyy0aal119pjesgy0veo45qs&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/nwii81fh924inmyxxfkmw/Section5_Bild0.png?rlkey=sb0ycywmin960yt4he3ycf9c9&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/yzu8xx2uvt6z6r53ssxp3/Section5_Bild1.png?rlkey=pu8zliwnwowmnccfuc533wcwh&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/rn4pxirkg2j35bk4g9u8g/Menschenaffen_Unterrichtsmaterial.pdf?rlkey=gb67me3de18g4uylvnzd8yq78&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Providing educational resources for teachers to facilitate learning about great apes and conservation efforts led by WWF Germany\'s "Young Panda" project.')

    st.text('Topic 1: Introduction\n- Presents background information about the WWF organization and its focus on protecting endangered wildlife.\n\n')

    tmp61 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/nkvgrkaq8ihjq6umc2297/Section1_Bild6.png?rlkey=b393qstgtxmr5ajbkcnbwiavz&dl=1",
        "https://www.dropbox.com/scl/fi/rg3nopfzd4rha38ofq5wz/Section1_Bild2.png?rlkey=if6xmt43biyav9zmi7fvca92v&dl=1",
        "https://www.dropbox.com/scl/fi/54fzap1uwxtqw9j8oqwv4/Section1_Bild4.png?rlkey=m12czlbqfjfs2u7mufukq35kg&dl=1",
        "https://www.dropbox.com/scl/fi/lzzivzrwr6oyy4g71ges5/Section1_Bild10.png?rlkey=duw87akgu11srtrzermn1d2cp&dl=1",
        "https://www.dropbox.com/scl/fi/31jx71vr9064hpsoc683v/Section1_Bild8.png?rlkey=iwisclk91mmgzhfg451kmgu0m&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/6xm30wutbpdhp1ous0soe/Section1_Bild0.png?rlkey=7rc087li7dfnj3mrw8l5162ux&dl=1",
        "https://www.dropbox.com/scl/fi/cugmz5ucj8jcxz7wvjkfa/Section1_Bild9.png?rlkey=ydyj75gsivd8ennusfi8lricm&dl=1",
        "https://www.dropbox.com/scl/fi/q1lzc5d0prtnkfo95ztck/Section1_Bild5.png?rlkey=l8ev7hna4s4zbp5plq9384ah5&dl=1",
        "https://www.dropbox.com/scl/fi/vljm3kqum5g86xc8q0n5f/Section1_Bild7.png?rlkey=6a4e0d2ajk9mnq985zhlnuux1&dl=1",
        "https://www.dropbox.com/scl/fi/a09hprzbaiiualffogae1/Section1_Bild11.png?rlkey=eh13m7iweghx9pn5erqn15zw1&dl=1",
        "https://www.dropbox.com/scl/fi/gsk2td1bnrpdwquflhoo1/Section1_Bild1.png?rlkey=amc2api7gfrwj08o9pz0f4r62&dl=1",
        "https://www.dropbox.com/scl/fi/v8rbg578blp77ogv24itw/Section1_Bild3.png?rlkey=jymsz69dtljr012ux4c7jctgs&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/v6z3yfjg48q5ptiqep11j/Section2_Bild8.png?rlkey=4re8rsbukl1tcv7nusklne6tb&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/nvagfqmoqrdlrujyyugxg/Section2_Bild1.png?rlkey=pscm41nl6vklxl2s5yg929p40&dl=1",
        "https://www.dropbox.com/scl/fi/z1pacwbkpe00cym004bex/Section2_Bild3.png?rlkey=8m2ryocpit6ec8mfhcz8afys7&dl=1",
        "https://www.dropbox.com/scl/fi/k6l4m4j1e73agd7f9hi8w/Section2_Bild0.png?rlkey=0c447ukxqirg9t8523db4snym&dl=1",
        "https://www.dropbox.com/scl/fi/zeboajkuxxdxwv3gjfidp/Section2_Bild2.png?rlkey=u35lqj4nt8xz7yitlk6f79b4y&dl=1",
        "https://www.dropbox.com/scl/fi/0g6xchkjk8vq3l9m3ifm7/Section2_Bild6.png?rlkey=59j9qrup30m6z0b1aqtuhxjv1&dl=1",
        "https://www.dropbox.com/scl/fi/6a5e80173hkbe7dyleskh/Section2_Bild4.png?rlkey=ihltun01tbxecxhlxld9lo09h&dl=1",
        "https://www.dropbox.com/scl/fi/26mi17mun6u2fl7sshxms/Section2_Bild5.png?rlkey=i7jb860o78heta3ur2yr7h6gc&dl=1",
        "https://www.dropbox.com/scl/fi/t6iyrq2dxc3fn3l5jchao/Section2_Bild7.png?rlkey=a9xun28o0gt6yqsemx26knfrw&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/15gx1joxhyl1qjggvcvaj/Section3_Bild0.png?rlkey=q3pitqjuwwypbqs3wi4hbi7r4&dl=1",
        "https://www.dropbox.com/scl/fi/xfh9k6yzfa05u98pbgdae/Section3_Bild4.png?rlkey=2fybkbofzzyvoyx8l1m4h0urk&dl=1",
        "https://www.dropbox.com/scl/fi/n010q3s8e7exsl3nmrijc/Section3_Bild6.png?rlkey=xnj2izmmh61ripsdh1he1dyu0&dl=1",
        "https://www.dropbox.com/scl/fi/ra6abks5vswhfmxv1v0er/Section3_Bild3.png?rlkey=0nykbtvhw2eq0mrjqvfy05yqx&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/s15cd5shfunbqpf3xelmp/Section3_Bild5.png?rlkey=j8f4n7bgsm1z2ec99rafsxt96&dl=1",
        "https://www.dropbox.com/scl/fi/uzfnam5k4w6a7imxgrggu/Section3_Bild1.png?rlkey=abucknln19yn27aah9sdmkrrx&dl=1",
        "https://www.dropbox.com/scl/fi/xac5xtgohdexwwx0jux70/Section3_Bild2.png?rlkey=cgv1x69s1e8z1y57ccix2e10r&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/xra6v86r22ulmtkx4lll7/Section4_Bild0.png?rlkey=3fm19hn8l3jra9majv0bxkccc&dl=1",
        "https://www.dropbox.com/scl/fi/3ed6ty4v5o42h7mlpj27m/Section4_Bild4.png?rlkey=i6r3crosx7rq4ry4t2v6o7i7z&dl=1",
        "https://www.dropbox.com/scl/fi/xwh9f9hozwqjqp1jj8g6h/Section4_Bild7.png?rlkey=7g5t38vj5z2fd3bw5oks17td6&dl=1",
        "https://www.dropbox.com/scl/fi/up6tt8k9jnc4ebuqgi2pu/Section4_Bild5.png?rlkey=wd3942hmgv67ltgiie1zg6b6s&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/nqtagq2sq3hywa2hvims9/Section4_Bild3.png?rlkey=ze3fjk4hezw4n3zhf12h0yq96&dl=1",
        "https://www.dropbox.com/scl/fi/zye8ewzf8i8sinbw1r3bl/Section4_Bild6.png?rlkey=lxul6k9li4neriqgj22m4f9y1&dl=1",
        "https://www.dropbox.com/scl/fi/t64oh7u45ebgbsksm4r95/Section4_Bild2.png?rlkey=pe79jmlxnmy6gcmixzrauh93w&dl=1",
        "https://www.dropbox.com/scl/fi/6nul8p5uk1xdii3qkb6wq/Section4_Bild8.png?rlkey=c1rey418601zka6teohugunyj&dl=1",
        "https://www.dropbox.com/scl/fi/tvpv1x3vyr3lzps8pfne7/Section4_Bild1.png?rlkey=x3pu2nm1yhdv2al8n9lg6xwhb&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/txe3sww2bavnby7kcgljx/Section5_Bild5.png?rlkey=2hjfgrtw8i36g2a1amp6ct43p&dl=1",
        "https://www.dropbox.com/scl/fi/yfhyhwc7nhu818l4brxp2/Section5_Bild0.png?rlkey=5w2slaf5n4bz16e4w9q36z3hp&dl=1",
        "https://www.dropbox.com/scl/fi/fql2hfx2rpe2awnlxcpqn/Section5_Bild6.png?rlkey=0jrodq33jurtvxbcp59nwr7cj&dl=1",
        "https://www.dropbox.com/scl/fi/qq9qe35kxwvzqq7jira57/Section5_Bild10.png?rlkey=qzkaekaef9h8mrf8425gzr1dy&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/eih4gba5vjfczu93p2ubc/Section5_Bild11.png?rlkey=1vdquny84lbj7th3rxtr0aend&dl=1",
        "https://www.dropbox.com/scl/fi/gzmi8imox3xknnphcv8rh/Section5_Bild9.png?rlkey=o6tu8fh8qbzlnlg2z4urz8lrl&dl=1",
        "https://www.dropbox.com/scl/fi/zhx6wzlqcqo41iqjhv8ai/Section5_Bild8.png?rlkey=cwjqpzloh1onk2o66fkbibipg&dl=1",
        "https://www.dropbox.com/scl/fi/2lfjcqsiqbz6b424ecrv5/Section5_Bild1.png?rlkey=8g4unxo8azus539oyt05dv3y1&dl=1",
        "https://www.dropbox.com/scl/fi/n9b907s5hh3i7bqetir0b/Section5_Bild2.png?rlkey=rrb87k2bnggqcufgy23tzpl4m&dl=1",
        "https://www.dropbox.com/scl/fi/w21tb8g2mht0sutepygqz/Section5_Bild7.png?rlkey=vz6rfih7yx5um4exlyz8e61v0&dl=1",
        "https://www.dropbox.com/scl/fi/tj775zywxg6bzp9ymauzd/Section5_Bild4.png?rlkey=phvqvezjkfe1q7guvbyz8luhp&dl=1",
        "https://www.dropbox.com/scl/fi/mc9jrsayv9el6te0sp0xs/Section5_Bild3.png?rlkey=42kcx7zwqrzdza4rdlunck1mg&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/vged1rxrx8dgp9rt5v7us/Section6_Bild0.png?rlkey=k2k28gwzl1gs9ixh1qww5tatm&dl=1",
        "https://www.dropbox.com/scl/fi/wp6kub1495djcrxg4mvcn/Section6_Bild5.png?rlkey=duy491ms7alhb8brdclv8yjaw&dl=1",
        "https://www.dropbox.com/scl/fi/6kh9sqy1erm0mo3src9kg/Section6_Bild6.png?rlkey=oxsjofp1cib8wmncpz0bbxih0&dl=1",
        "https://www.dropbox.com/scl/fi/85pq6cm0wcussx9otrbm8/Section6_Bild3.png?rlkey=tp5k2qnhdkgbu293lb5rljan9&dl=1",
        "https://www.dropbox.com/scl/fi/ccdimk2606ytf8oeraqmw/Section6_Bild4.png?rlkey=re2m0oqjim0n8eewpgifin52v&dl=1",
        "https://www.dropbox.com/scl/fi/bngtwmpp1p2pqj5dmsas4/Section6_Bild9.png?rlkey=j691u9k6n1qcjcvv7pe70e539&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/pzuscqygtjoubgevaxbc4/Section6_Bild8.png?rlkey=9j3m9z0zv000xiywuw52idixr&dl=1",
        "https://www.dropbox.com/scl/fi/w1id53xo1huaklji42v4l/Section6_Bild10.png?rlkey=70ie0a6ye1ove99q21xlqdjae&dl=1",
        "https://www.dropbox.com/scl/fi/gkjcd4p9x9ds4llfit7sk/Section6_Bild2.png?rlkey=g3qhetmvvuv8961n9go221vm7&dl=1",
        "https://www.dropbox.com/scl/fi/dsyx0xx1q3spe2xj1c1ji/Section6_Bild7.png?rlkey=ftbeb99r9e99wt3yvhro73yhp&dl=1",
        "https://www.dropbox.com/scl/fi/y76acvvc4zeuzod2jhixi/Section6_Bild1.png?rlkey=mhhu1qtrivih6cr437ao6uirv&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/c9nmp5ntxu0ervlkdijx2/O1A1-GE.pdf?rlkey=v7zsg0cq4icvm5jilmjd12t23&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Equip educators with extensive knowledge on suitable 3D print technologies and materials for effective implementation in classroom settings.')

    st.text('Topic 1: Understanding Additive Manufacturing and Its Benefits\n- Presents an overview of Additive Manufacturing, explaining its differences from Rapid Prototyping and conventional manufacturing techniques.')

    tmp71 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/kmhbojex27bxy4af1vs9l/Section1_Bild6.png?rlkey=fc8bcx9i56tv96verlesr1vbv&dl=1",
        "https://www.dropbox.com/scl/fi/q6h6ynr6brkjimafj1o5f/Section1_Bild5.png?rlkey=z09ropze2jojezfef54ggknaq&dl=1",
        "https://www.dropbox.com/scl/fi/33jmqeupyogm4pxj2k0qr/Section1_Bild7.png?rlkey=l1pk7gtvp2iixkyowoi8dfka8&dl=1",
        "https://www.dropbox.com/scl/fi/gf75chu9m014o6ul25arn/Section1_Bild10.png?rlkey=3vgdbmvq9xkjptdu0vkwn8q1c&dl=1",
        "https://www.dropbox.com/scl/fi/qdovgcrcja0eql2wnetwk/Section1_Bild8.png?rlkey=a4g6ttcs1u9opixzsbebes6kj&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/4y8533m4nel9dnih9eucu/Section1_Bild0.png?rlkey=cx2i5vnh6oxwkukyanb9sdlx5&dl=1",
        "https://www.dropbox.com/scl/fi/pfgvgc4wx1ztxjyeyvy7s/Section1_Bild2.png?rlkey=xnsjkieqrekarg3itl9vnykim&dl=1",
        "https://www.dropbox.com/scl/fi/ke0fvj9tvc5mvkb1iaubj/Section1_Bild9.png?rlkey=8bhod0jvd75zkjmaa9ehk9vsc&dl=1",
        "https://www.dropbox.com/scl/fi/ukqjanl0zjf4jxvfdri8t/Section1_Bild11.png?rlkey=uayyayty2w12yo6z6j6cxuldg&dl=1",
        "https://www.dropbox.com/scl/fi/96jlt8rbjqj684zcgozch/Section1_Bild4.png?rlkey=jehyb46um5vcpjpessadveqxe&dl=1",
        "https://www.dropbox.com/scl/fi/tvzj6fovmhyxjdony5nc2/Section1_Bild1.png?rlkey=8ygrl68fm4sxwhdb4rhl671w5&dl=1",
        "https://www.dropbox.com/scl/fi/rqtmwv6xq8ct6kytjlltx/Section1_Bild3.png?rlkey=ei8rmwjmi93i3jygazgrs6ju2&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/3xmd0pmciqis98kcl5gb1/Section2_Bild7.png?rlkey=gpwhsrtazylkereq5p4b7m7ov&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/44tfporwb08pi5e3pqtma/Section2_Bild1.png?rlkey=uix5nlrwgzl0c3rk2yup78v9r&dl=1",
        "https://www.dropbox.com/scl/fi/q9ig6oj1rn79r76zjp6mf/Section2_Bild3.png?rlkey=wem06siaw4tgyittukgzapcje&dl=1",
        "https://www.dropbox.com/scl/fi/w2hpx79455zcbxkr28jyw/Section2_Bild0.png?rlkey=qus8ipe21laur76z2wfmjkgo5&dl=1",
        "https://www.dropbox.com/scl/fi/8cxuqtmz2gdc7v6zgae7e/Section2_Bild11.png?rlkey=a0w03hqp0x7pnr20v5vwbs44f&dl=1",
        "https://www.dropbox.com/scl/fi/rxymrjputliy45mxhm47p/Section2_Bild2.png?rlkey=9bsukb086lapqgrhxdbsp653u&dl=1",
        "https://www.dropbox.com/scl/fi/liykcsroqindntd2tkm6a/Section2_Bild8.png?rlkey=p8jpxgu17nqxkad3eswlfzk1p&dl=1",
        "https://www.dropbox.com/scl/fi/03afokc6yp9prmv9eatib/Section2_Bild6.png?rlkey=w5eu8dpl0td8okusu3fnaliu2&dl=1",
        "https://www.dropbox.com/scl/fi/ia8di26bjqq3n0xpabc3x/Section2_Bild4.png?rlkey=eaagj1iwgxeq1wi1om9uxoju5&dl=1",
        "https://www.dropbox.com/scl/fi/tz3klu5bsgw43ke2bkgdq/Section2_Bild10.png?rlkey=lyg27m40m9exs5tvqw8qdsfk5&dl=1",
        "https://www.dropbox.com/scl/fi/do0omtyl9we0q5yc61acq/Section2_Bild5.png?rlkey=e1rfyppi6fxae35hzfxp42a9m&dl=1",
        "https://www.dropbox.com/scl/fi/cgnsf64rn1l7vzayowol7/Section2_Bild9.png?rlkey=jsc3aovqlffwiz3grtybmmml6&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/dw5kfxkhbob0phsaqoc7b/Section3_Bild5.png?rlkey=ljhlu9p7ynhc0wgzpl9zdyn4k&dl=1",
        "https://www.dropbox.com/scl/fi/kmexzn2oda1ql8o1g4g19/Section3_Bild0.png?rlkey=ab6l94atxzevhbxts30j8e5yq&dl=1",
        "https://www.dropbox.com/scl/fi/tgsy954hxcchml2tevfkl/Section3_Bild6.png?rlkey=4x07pi1gnhlkczts8vhblvjtx&dl=1",
        "https://www.dropbox.com/scl/fi/gf4kosgd8xx2w3ql0kznu/Section3_Bild7.png?rlkey=a6venkk4prmgld48ns3smj53c&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/dlb7jah6yvjm0j4araigr/Section3_Bild9.png?rlkey=l41dfqnu9wioc8wyyl2iu0jcl&dl=1",
        "https://www.dropbox.com/scl/fi/b2dngsbml4tunwjuhl9zi/Section3_Bild1.png?rlkey=o2d2ute1s56v6z6cu3008rk4o&dl=1",
        "https://www.dropbox.com/scl/fi/3hn0ztrkvd7xmzmerd3kp/Section3_Bild4.png?rlkey=hkrresap2lqabsm8mh9imzcub&dl=1",
        "https://www.dropbox.com/scl/fi/jj0zpau6ac0b4b0jdmw4f/Section3_Bild2.png?rlkey=ia98yfqhs8g0yu26relg1zoyg&dl=1",
        "https://www.dropbox.com/scl/fi/aou5e8tonso7242o39doe/Section3_Bild8.png?rlkey=r0pud4x4cfu8smmhdaleh33l9&dl=1",
        "https://www.dropbox.com/scl/fi/1vtbo6vypgepgnf5dk7as/Section3_Bild3.png?rlkey=1aiqo0bdgfp94fdvh6o118wlb&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/o93e7kqb4rgl4452exr5k/Section4_Bild7.png?rlkey=o50yzwuik0b28agyur53ggwmu&dl=1",
        "https://www.dropbox.com/scl/fi/w2x3bxhimmqpz3gok1r0c/Section4_Bild5.png?rlkey=ectaxep7ohy42r4s7glp5h2y1&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/jqub3zhes18z51m3ur9gb/Section4_Bild3.png?rlkey=t6myq8yygmvjqsz6eja8c12o5&dl=1",
        "https://www.dropbox.com/scl/fi/2laopmh5m5q4pnvy0gc8l/Section4_Bild6.png?rlkey=4xbdhjyg8rjj6k6y4q27s8emd&dl=1",
        "https://www.dropbox.com/scl/fi/kz08gs1w9nrjy8p1q3d6y/Section4_Bild2.png?rlkey=fbz1jdg6vp5tl4ju27x9rsmv9&dl=1",
        "https://www.dropbox.com/scl/fi/hmr85ihztn4jc8kmcdxvl/Section4_Bild9.png?rlkey=t1mupqne0z85vh6ndciqbnne7&dl=1",
        "https://www.dropbox.com/scl/fi/2jgaogzcur1y9h3yqu4ho/Section4_Bild8.png?rlkey=1manslnwpmupm384vr7kvas86&dl=1",
        "https://www.dropbox.com/scl/fi/cwdwoigb39zgbkfozjtg8/Section4_Bild0.png?rlkey=nxi4ta33hs8qm1ujsojjwcvkn&dl=1",
        "https://www.dropbox.com/scl/fi/8071ta2nihz33rxufbfse/Section4_Bild4.png?rlkey=ee5prahdzi6gy29dnr2qdv83o&dl=1",
        "https://www.dropbox.com/scl/fi/8n3fpffdgehro15wrugrh/Section4_Bild1.png?rlkey=16fqd4396a7jxc0fldme2e4yr&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/9x6e0uivkp5tszbrjednh/Section5_Bild6.png?rlkey=nscg90xy6w3knu2jdczqafpkh&dl=1",
        "https://www.dropbox.com/scl/fi/vb2unncpb00fslt1xeq76/Section5_Bild3.png?rlkey=1q51otf40n2zgitifz7qwdty7&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/jwr4p2fz2m9xhwtvl6cv0/Section5_Bild9.png?rlkey=0s0h6kkfecbnch49h5h6z8c7o&dl=1",
        "https://www.dropbox.com/scl/fi/5yu0m13r4gadufmxjng9a/Section5_Bild5.png?rlkey=mapvsapc58kotd0fzlc4cx5so&dl=1",
        "https://www.dropbox.com/scl/fi/jr4fdetggvuser942ywr0/Section5_Bild8.png?rlkey=nj6dnsx18291y84ag9nw0i6a0&dl=1",
        "https://www.dropbox.com/scl/fi/o1p5uzcbp1hvi2s6sgtz2/Section5_Bild0.png?rlkey=8l6utirjlyca62q01krhmfnzf&dl=1",
        "https://www.dropbox.com/scl/fi/ysjnro422c6ssvgefmi6v/Section5_Bild1.png?rlkey=gdfoiri968zvth4uvtgve0okb&dl=1",
        "https://www.dropbox.com/scl/fi/3427c7le9yk4rjwzgry6b/Section5_Bild2.png?rlkey=vmfqhullh2d7h2pqj57j2zay5&dl=1",
        "https://www.dropbox.com/scl/fi/34lkzv56u9q1dxxgf069z/Section5_Bild7.png?rlkey=hd6oujz4ozveeykdz0tcp1w89&dl=1",
        "https://www.dropbox.com/scl/fi/itxibkjfznvw5nc6qygvk/Section5_Bild4.png?rlkey=6z38mg5m8mrp1r444dnjko6yk&dl=1",
        "https://www.dropbox.com/scl/fi/snqh209q8x3kfv0wuumt6/Section5_Bild10.png?rlkey=rtdy629ed8hucjdzq6lbjltp9&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/aw6ufwe4q61pnllaffliq/MuM_Band_14.pdf?rlkey=rldbcgwiix86auyasjnsxfqww&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Investigate the interplay between coral symbiosis, bioerosion, and human activities in shaping coral reef ecosystems, emphasizing historical research in the Red Sea and practical considerations for managing coral reef exhibits.')

    st.text('Topic 1: Coral Symbiosis and Photosynthetic Microalgae\n- Introduces the mutually beneficial relationship between corals and zooxanthellae, providing essential energy for efficient growth and reproduction.\n\n')

    tmp81 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/5l2knd76fmcewzqfin9qg/Section1_Bild6.png?rlkey=0i5q3x6ozikbxu2aroi8wb0y5&dl=1",
        "https://www.dropbox.com/scl/fi/1py870gja76sfn42r0kwr/Section1_Bild11.png?rlkey=i3qkzw5h0u3kfsj95fzgt89da&dl=1",
        "https://www.dropbox.com/scl/fi/kh2lno7pydhr0wzbqdt1y/Section1_Bild4.png?rlkey=gtlxolakq2vu9gfq5h6s1qy6k&dl=1",
        "https://www.dropbox.com/scl/fi/klcy54j9sn3xtxcs7wt83/Section1_Bild8.png?rlkey=648av2umywf0obnmf431lsx5c&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/5xgdjus09g67izz5rr7yc/Section1_Bild0.png?rlkey=ethjuwzqxf59c9zt6lwsg6aa3&dl=1",
        "https://www.dropbox.com/scl/fi/lqu2yki7x40c7tgjtnzei/Section1_Bild2.png?rlkey=sajcb6mqnm4nxcrvjyawk8t4z&dl=1",
        "https://www.dropbox.com/scl/fi/memj33fevivascwuciels/Section1_Bild9.png?rlkey=3858hrj31hrhn7ofmep28a9bp&dl=1",
        "https://www.dropbox.com/scl/fi/7jqin7v3iur05ug8mwnb9/Section1_Bild5.png?rlkey=3tk8z2p2oi6ft5qbsi2vbxeyr&dl=1",
        "https://www.dropbox.com/scl/fi/d51xep710kav0vnxgwqwy/Section1_Bild7.png?rlkey=y30mfg12jms7bqf8rt0ebgxr4&dl=1",
        "https://www.dropbox.com/scl/fi/pz6t9ak14c3gb3c040x2z/Section1_Bild10.png?rlkey=zfexlspe6sfdx5x80nyvlwn8g&dl=1",
        "https://www.dropbox.com/scl/fi/df2ipc86qo0qu1lbz1xwx/Section1_Bild1.png?rlkey=xybe8hprlf37psq9247f46c3u&dl=1",
        "https://www.dropbox.com/scl/fi/5osanc4qcc2sl4ql03vhx/Section1_Bild3.png?rlkey=vtaz46131rc9phiwdul7cpsru&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/kl4qxsuscw858sqnv1f6e/Section2_Bild3.png?rlkey=exiuwfjtut6ykl4fwvszt2m2a&dl=1",
        "https://www.dropbox.com/scl/fi/68uhj2pvoy2q61x82nru4/Section2_Bild0.png?rlkey=qi47g4cse2wbyh0amngsws1k4&dl=1",
        "https://www.dropbox.com/scl/fi/bd0hvvlb1wegli4en71qj/Section2_Bild10.png?rlkey=d6u6nmobgp39a591lfj8p8ot1&dl=1",
        "https://www.dropbox.com/scl/fi/vacohs0hpfoncszhlzfoz/Section2_Bild7.png?rlkey=9otkozmf61aggvkzg4ulnx2fo&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/06e0redg8eho7t1hjlflc/Section2_Bild1.png?rlkey=s1d74s1uve8cqt4atbv2vl9gt&dl=1",
        "https://www.dropbox.com/scl/fi/nl1d5txdsxvd0hnvth8z7/Section2_Bild2.png?rlkey=slmj134ns1cqwynd7ondjge33&dl=1",
        "https://www.dropbox.com/scl/fi/wq8wb10ha1idis7agrzx6/Section2_Bild8.png?rlkey=6x20q7mr02h6efmzn7q6c7ywh&dl=1",
        "https://www.dropbox.com/scl/fi/fr2a4a7dohpqs1uqvb70w/Section2_Bild6.png?rlkey=xgd1a3l5zhj9izekimske8mho&dl=1",
        "https://www.dropbox.com/scl/fi/kzdg6x444z28dzo84j3xd/Section2_Bild4.png?rlkey=epzpg7t4ovchuws8rkzj7qlue&dl=1",
        "https://www.dropbox.com/scl/fi/395wm7qq0vqw34so6p4wr/Section2_Bild5.png?rlkey=0tx4g2x8qgn1koaeknwcdw4k9&dl=1",
        "https://www.dropbox.com/scl/fi/ktgcyv0bfcoqosqu9p41s/Section2_Bild9.png?rlkey=bnswtp3b9lrtv78u7y711ka2p&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/wac57v414o8tcny4wg7z2/Section3_Bild9.png?rlkey=xv5vmpg91vg8xp1rhxo2640pl&dl=1",
        "https://www.dropbox.com/scl/fi/3tsqwz8us6c82ks8x20z9/Section3_Bild4.png?rlkey=kqbkbdijvzsz79n2utc1eyfdf&dl=1",
        "https://www.dropbox.com/scl/fi/ta23fips2voe1ra3mdydl/Section3_Bild3.png?rlkey=fhqmm3zvleolt83i509rmek1m&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/bzimdqifv74meu1h8pjwh/Section3_Bild5.png?rlkey=7rxc460udv5n7ivskey3rxfzw&dl=1",
        "https://www.dropbox.com/scl/fi/8lq5wso7oatrfm6qixnya/Section3_Bild1.png?rlkey=1arieqogcfsu9t9ezs37morfv&dl=1",
        "https://www.dropbox.com/scl/fi/hyvjvif0wphjpem8bflur/Section3_Bild0.png?rlkey=x16lbednxvdgb0yaq62oe5txl&dl=1",
        "https://www.dropbox.com/scl/fi/sw8ajlp2xnxutb7ll50ng/Section3_Bild6.png?rlkey=azbkkgh64p4e11pyod55njlbf&dl=1",
        "https://www.dropbox.com/scl/fi/qrc9gbejw7u33xjszcy5m/Section3_Bild7.png?rlkey=6vajv6lw8dlhobtj1ttmvrr7b&dl=1",
        "https://www.dropbox.com/scl/fi/5y0q2xam7eei10jq0usn9/Section3_Bild2.png?rlkey=s504yqfnf2pz9km5bwnbwqwyq&dl=1",
        "https://www.dropbox.com/scl/fi/vfrgdli62knfcrpsyp7qd/Section3_Bild10.png?rlkey=eliif79xn37rqv3bwv4ymd33n&dl=1",
        "https://www.dropbox.com/scl/fi/xalhsio7no3rifp5k3xcn/Section3_Bild8.png?rlkey=7y92ix3g39shf7vcyaprbea5n&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/nkupaq62vrpisavn4tfmk/Section4_Bild3.png?rlkey=2oaxb7vvxt9xe43ut0h9yvc7l&dl=1",
        "https://www.dropbox.com/scl/fi/dqurc7cm91vwddlvg41yx/Section4_Bild0.png?rlkey=vgcdk20yb5uld3x2bowzpitig&dl=1",
        "https://www.dropbox.com/scl/fi/c9c0vcthpau5qvvjbil1w/Section4_Bild4.png?rlkey=dc8uzmplga6r3uykmlyodtkf0&dl=1",
        "https://www.dropbox.com/scl/fi/gff5t8hrdtxh35jj5vfh7/Section4_Bild5.png?rlkey=7wifd435bc1zyf3ryh4x5ew2f&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/txcem2a6czjttgcch7y88/Section4_Bild2.png?rlkey=fikfc4xmpmui9j22b3aey56ol&dl=1",
        "https://www.dropbox.com/scl/fi/beud6o8ctcxh0xkv84vaz/Section4_Bild1.png?rlkey=ddjsyzry8b3orxge58xkd7ns6&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/6cb67y0kdm6xx2r90vgr8/Section5_Bild5.png?rlkey=k1ae278ga4mbks37rktrzbc1t&dl=1",
        "https://www.dropbox.com/scl/fi/4iwf0k584gxmz1vq3k3nl/Section5_Bild8.png?rlkey=pzuhn535q2oyijrppyt92jh5d&dl=1",
        "https://www.dropbox.com/scl/fi/d3yas06wsiv98r0hxo5kr/Section5_Bild0.png?rlkey=8cnkm6q2uah4itz5fpzq0fybm&dl=1",
        "https://www.dropbox.com/scl/fi/5oedn42qezu6vdb0r1asn/Section5_Bild7.png?rlkey=4fegkpgk2qb5awb93xxvc7nyo&dl=1",
        "https://www.dropbox.com/scl/fi/qxoq32y1dh1pl280gvr5y/Section5_Bild4.png?rlkey=6ps7eglnngpuor0beaihkbgd5&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/0xdygky60sb6vl3zjak5t/Section5_Bild9.png?rlkey=9s17u778etj7srkmw4kru12ld&dl=1",
        "https://www.dropbox.com/scl/fi/ypfkhedjn39qhtay7spco/Section5_Bild1.png?rlkey=odpurbuocfc6590y8orz7haip&dl=1",
        "https://www.dropbox.com/scl/fi/kd6mojiio7ek5m5au351n/Section5_Bild2.png?rlkey=33wsqrcos541taakbg20lk0tg&dl=1",
        "https://www.dropbox.com/scl/fi/hr95lxd1dpnai0oy9ps4n/Section5_Bild6.png?rlkey=y70rzqebugixz62dxebbitqly&dl=1",
        "https://www.dropbox.com/scl/fi/ha70zgrr9c1qgmkxayp9q/Section5_Bild10.png?rlkey=obhw4x4d95y26aj8kju8o8wrv&dl=1",
        "https://www.dropbox.com/scl/fi/9zdbyln68yx1nkftr7nce/Section5_Bild3.png?rlkey=y889g4nruwfph813gmuyheiws&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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

    pdf_url = "https://www.dropbox.com/scl/fi/436abwselhdjaoxrgt4w9/Probekapitel_Ernaehrungsberater_Ernaehrungslehre_ENB01-B.pdf?rlkey=05ep0wrigk54tpr2l82suv2wj&dl=0"
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

    pdf_url = "https://www.dropbox.com/scl/fi/up25uozr8ky9j0ld4pv7h/bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All.pdf?rlkey=a435ir79i3fu7jcaj6l2zez18&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: To inform readers about recent discoveries made through the detection of gravitational waves emitted by colliding black holes.')

    st.text('Topic 1: First Direct Observation of Merged Black Holes\n- On May 21, 2019, scientists detected gravitational waves caused by two merging black holes, providing direct evidence of these cosmic phenomena.\n\n')

    tmp101 = [
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/y9um4ofe7bxxu0gexupkg/Section1_Bild0.png?rlkey=19tyhb1e42b6dm4ion2wp6x79&dl=1",
        "https://www.dropbox.com/scl/fi/6eqnohmymb7r80q07ehpq/Section1_Bild2.png?rlkey=9sltn3pppzjsmz1yq1vbcmlzt&dl=1",
        "https://www.dropbox.com/scl/fi/8gi4ctzx4p9jdud00fj2x/Section1_Bild4.png?rlkey=t05e0fmf0jgz4evyfkn62hibo&dl=1",
        "https://www.dropbox.com/scl/fi/e8rt6409zlmo8yv84v71n/Section1_Bild1.png?rlkey=on2xrhmczgio4gcwz717vmwl9&dl=1",
        "https://www.dropbox.com/scl/fi/p94k3zwhbi0h5j6x2fz4i/Section1_Bild3.png?rlkey=w45t9ylqecjk9f6x3apkn1720&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/bc3ucjclhr6aronkgm5ue/Section1_Bild6.png?rlkey=4uyjd3rjsy0fga7tqydsjst75&dl=1",
        "https://www.dropbox.com/scl/fi/8picl2eeqigne232u48m4/Section1_Bild9.png?rlkey=bd8xrz8w67w9g0e4efsmrncno&dl=1",
        "https://www.dropbox.com/scl/fi/jhqzadj3dvfp5e6s7n2et/Section1_Bild5.png?rlkey=pgvtvc5aood4qojp0u54zc9a4&dl=1",
        "https://www.dropbox.com/scl/fi/4hzuqpl9ebshcblv9z1e2/Section1_Bild7.png?rlkey=9nmklw7201qjekezc0skql8kw&dl=1",
        "https://www.dropbox.com/scl/fi/38z8pxdrgtydfn6a4xdvw/Section1_Bild8.png?rlkey=li4qd6aajqya2ayejc2swwtk0&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/8jywykmuqmhab4ie6yfzr/Section2_Bild1.png?rlkey=zdo17wpdmb6sv1jg633aoucyn&dl=1",
        "https://www.dropbox.com/scl/fi/b1rmt4jnexx1t8u3iig7s/Section2_Bild0.png?rlkey=s7t67hm22b4ixu2qebch2vh1c&dl=1",
        "https://www.dropbox.com/scl/fi/v4uvj28wgrcricyvjodm1/Section2_Bild8.png?rlkey=fpql3eei7zvkmfravrvg7qij8&dl=1",
        "https://www.dropbox.com/scl/fi/a7b6r6nra274yizqc63vj/Section2_Bild9.png?rlkey=lce7jn5yjj50qmqjszzed83ub&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/mrcvyqicexmx2ob312bg8/Section2_Bild3.png?rlkey=pe0o5j9ggjy3z6c5usbpmrjfg&dl=1",
        "https://www.dropbox.com/scl/fi/pxgyf62w9da1z1qggvh3e/Section2_Bild2.png?rlkey=ioxdoncgsgfbwkzp2ajpql4jk&dl=1",
        "https://www.dropbox.com/scl/fi/y8pvnyutfbt7kxetg47e1/Section2_Bild6.png?rlkey=7v9x2bubobx35pfl10mmdrpiq&dl=1",
        "https://www.dropbox.com/scl/fi/y0f7cehpu8maik4x6t56r/Section2_Bild4.png?rlkey=xua840dulvvywgtkt50tiiygu&dl=1",
        "https://www.dropbox.com/scl/fi/1qax9ry3tjia7l81ocrbe/Section2_Bild5.png?rlkey=va251yug9gf50gfyfplb7b0ta&dl=1",
        "https://www.dropbox.com/scl/fi/6fbsvly3n9vq15tc9laf1/Section2_Bild7.png?rlkey=sx2nhpbdofhooy936piyvwd5x&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/snqv8b035ayv73b5fv9d6/Section3_Bild5.png?rlkey=o90ymv9hrs5e5r5vx2fz4x7cw&dl=1",
        "https://www.dropbox.com/scl/fi/6t1onzfw1pvysspycp211/Section3_Bild0.png?rlkey=ww3kokjkpi2hy5nfnnlqmlejy&dl=1",
        "https://www.dropbox.com/scl/fi/l5klahqadsite2e6tnumi/Section3_Bild4.png?rlkey=vvaxil6cf68qa1n66ncurfi9v&dl=1",
        "https://www.dropbox.com/scl/fi/e0fs655me8iziakqv14fh/Section3_Bild2.png?rlkey=l0gxihcc16ouaiabfg9w0lv4v&dl=1",
        "https://www.dropbox.com/scl/fi/1jbp9f78bf1p0gv9klqwl/Section3_Bild3.png?rlkey=ty520h2tccjqkk3d7n1gvmgea&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/lpjllop47dclaq5ivla96/Section3_Bild1.png?rlkey=mjykplsngry7npct80ouv0cx9&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/0t2yy3kh11svz9z766vys/Section4_Bild2.png?rlkey=3bsoq9lw58iu2rcsr856suwpd&dl=1",
        "https://www.dropbox.com/scl/fi/i1xxdejnq65x6q7hkvv6v/Section4_Bild8.png?rlkey=qkrqgk0s52hku5htsqyl4txpl&dl=1",
        "https://www.dropbox.com/scl/fi/at4a2g6t7wim2xelqyo58/Section4_Bild0.png?rlkey=cfjhuq62xywc88dlyw3djrlex&dl=1",
        "https://www.dropbox.com/scl/fi/jujumazlufnxw93hna1sr/Section4_Bild1.png?rlkey=cjim9st5nyb72y9ms8pzdz632&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/f65whu13m6y4lpfdcqfp3/Section4_Bild3.png?rlkey=dljtikddktsrhsq8t3cs20wx9&dl=1",
        "https://www.dropbox.com/scl/fi/t1q8uyxv0ulrzt8bwnc47/Section4_Bild6.png?rlkey=pa5qdh7ykvjp05y17uibxk2z0&dl=1",
        "https://www.dropbox.com/scl/fi/241j684156blb5qoh5fv9/Section4_Bild9.png?rlkey=b3pfzalpg6blof83ul1vt4g93&dl=1",
        "https://www.dropbox.com/scl/fi/dnzqo0gz9g6uczdthzxsp/Section4_Bild4.png?rlkey=quddhs0rx5c9ub4ey7axohomj&dl=1",
        "https://www.dropbox.com/scl/fi/vb73ul3xutrhwnzelmqbt/Section4_Bild7.png?rlkey=edu4pmoks7oxko49b0k7t6a93&dl=1",
        "https://www.dropbox.com/scl/fi/bz719ssds2n8tmf6d9nyb/Section4_Bild5.png?rlkey=yko0f0rhz6jui8aivx1ekgr10&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/tlhm5u31ja9hjydfab1gy/Section5_Bild9.png?rlkey=wih1ji7v1ysvc6nastw0xscel&dl=1",
        "https://www.dropbox.com/scl/fi/hiccj1o2l8r9y86l8jznu/Section5_Bild5.png?rlkey=7v7zrwfryxz28jsh401dlkvpl&dl=1",
        "https://www.dropbox.com/scl/fi/nsapzxklg7ov3v033x4az/Section5_Bild8.png?rlkey=n1v320cjhxxvvhlzpb4shay4l&dl=1",
        "https://www.dropbox.com/scl/fi/gibcjuzu5w824nxcu6dyu/Section5_Bild7.png?rlkey=vl25e2kebepz4gkn029cj8hmj&dl=1",
        "https://www.dropbox.com/scl/fi/0xq6ly9dxavymft3twxag/Section5_Bild6.png?rlkey=c4k3z47e1osvlmkfd7zxu79wu&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
        "https://www.dropbox.com/scl/fi/mhaq9cw64rckpm3tcap8v/bad-sets-komponenten-keine-auswahl.jpg?rlkey=er4xk4dn0fyshgqw1odcn817t&dl=1",
        "https://www.dropbox.com/scl/fi/07lfmz4ue7b1zgo18i1sk/Section5_Bild0.png?rlkey=bhs9jnbft5qao4jqbhpvjtn34&dl=1",
        "https://www.dropbox.com/scl/fi/7s2vn8556zgta6kdwkhvx/Section5_Bild1.png?rlkey=ifjauue3f6d83jm6dsgkpyhz6&dl=1",
        "https://www.dropbox.com/scl/fi/5nbdkqp1ky7pp858mlvck/Section5_Bild2.png?rlkey=cqjaqefv7rlnca8723ig45jxx&dl=1",
        "https://www.dropbox.com/scl/fi/zo0xkj9dcb76eiqaf4a3l/Section5_Bild4.png?rlkey=nvilis6pi827nhmyok7zrj1pj&dl=1",
        "https://www.dropbox.com/scl/fi/k3ps196f2jku83kiulg50/Section5_Bild3.png?rlkey=g1yw4klazflbnf93ph56kiw67&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
        "https://www.dropbox.com/scl/fi/77lk9ww5sncuow1pd9c8u/Platzhalter.png?rlkey=nd3fl19x1wj4w6ip4pc43fidk&dl=1",
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
