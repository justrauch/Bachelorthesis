import streamlit as st
from streamlit_image_select import image_select
from streamlit_scroll_to_top import scroll_to_here
import urllib.parse
import uuid

if "email_count" not in st.session_state:
    st.session_state.email_count = 0

if "seite" not in st.session_state:
    st.session_state.seite = "page1"

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

if st.session_state.seite == "page1":
    st.title("Seite 1")

    pdf_url = "https://www.dropbox.com/scl/fi/c4ot3ris4xkgrz4vbgbow/40410000.pdf?rlkey=v7ex77n54ie5bix99rxpgk5id&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide detailed information on the German Federal Parliament (Bundestag) during its 20th term, including its roles, structures, buildings, members, and election process.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Functions of the Bundestag\n- Outlines the legislative role of the Bundestag in making federal laws binding throughout Germany.\n- Details how the Bundestag elects the chancellor, exercises control over the government, and participates in appointing key officials like judges and data privacy commissioners.\n\n')
    choice11_arr = [
        "https://www.dropbox.com/scl/fi/s7yb6h5xf5ez5cz9qm1l0/Section1_choice.png?rlkey=ykin1zsegnusw0h4jzyif229i&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice11_tmp = st.session_state.reload_counter % 2
    if choice11_tmp == 0:
        st.image(choice11_arr[0 if choice11_tmp == 0 else 1])
    else:
        st.image(choice11_arr[0 if choice11_tmp == 1 else 1])
    st.text(' A high-angle view of a large, circular parliamentary chamber with rows of blue seats facing a central podium, featuring a large eagle emblem visible through the glass ceiling.')

    tmp11 = [
        "https://www.dropbox.com/scl/fi/9h5k5o3ssjsnzt4q6zvov/Section1_Bild0.png?rlkey=8uly4670ifgo6pkddttorn881&dl=1",
        "https://www.dropbox.com/scl/fi/xjegf7j8ywtv9yjovspft/Section1_Bild2.png?rlkey=ao48kodtibfdw9lkhg31eitiq&dl=1",
        "https://www.dropbox.com/scl/fi/2az9q10djayvnax7wl77h/Section1_Bild1.png?rlkey=cj4eospddzq9jd9wmev0katkr&dl=1",
    ]
    img11 = image_select(
        "Mögliche Valide Bilder:",
        tmp11,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 1", 0),
        key=f"frage11_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Thema 1"] = img11
    valid11_tmp = st.session_state.reload_counter % 2
    if valid11_tmp == 0:
        st.image(tmp11[st.session_state.auswahl.get("Seite 1 Thema 1", 0)] if valid11_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp11[st.session_state.auswahl.get("Seite 1 Thema 1", 0)] if valid11_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Composition of the Bundestag\n- States that the Bundestag consists of 734 representatives directly elected every four years.\n- Describes the distribution of seats among parties based on proportional representation and explains the concept of "overhang" and "compensatory mandates."\n\n')
    choice12_arr = [
        "https://www.dropbox.com/scl/fi/ebyxq4pmh0gb79z4clxz1/Section2_choice.png?rlkey=2irgs9mkk490bximru2pbpm2n&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice12_tmp = st.session_state.reload_counter % 2
    if choice12_tmp == 0:
        st.image(choice12_arr[0 if choice12_tmp == 0 else 1])
    else:
        st.image(choice12_arr[0 if choice12_tmp == 1 else 1])
    st.text(' A large, modern building with rows of blue seats arranged in a circular pattern, filled with people, and featuring a large eagle emblem hanging from the ceiling.')

    tmp12 = [
        "https://www.dropbox.com/scl/fi/kp97a439u5pbejkl3jeqf/Section2_Bild1.png?rlkey=0lotqdl97lnjb6dxoxyr9p4mq&dl=1",
        "https://www.dropbox.com/scl/fi/m077unympbtpdh5n1rjnq/Section2_Bild3.png?rlkey=dskg3b1v1tse8rv5np5ub721v&dl=1",
        "https://www.dropbox.com/scl/fi/vj8hcyhc4ykhkspwhwpxl/Section2_Bild0.png?rlkey=lxmk818pu7ykgfm9x6y11zr4o&dl=1",
        "https://www.dropbox.com/scl/fi/qr5luc2riv4qhujezw1l9/Section2_Bild2.png?rlkey=1ib5f9c2d11v4nchebxi6ln5y&dl=1",
    ]
    img12 = image_select(
        "Mögliche Valide Bilder:",
        tmp12,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 2", 0),
        key=f"frage12_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Thema 2"] = img12
    valid12_tmp = st.session_state.reload_counter % 2
    if valid12_tmp == 0:
        st.image(tmp12[st.session_state.auswahl.get("Seite 1 Thema 2", 0)] if valid12_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp12[st.session_state.auswahl.get("Seite 1 Thema 2", 0)] if valid12_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Important Institutions within the Bundestag\n- Introduces various committees, commissions, and offices responsible for specific tasks related to legislation, oversight, and administration.\n- Names important figures such as the president, vice presidents, and committee chairs who lead these institutions.\n\n')
    choice13_arr = [
        "https://www.dropbox.com/scl/fi/xr0hign05qg3uzuw4ratx/Section3_choice.png?rlkey=plmu80oxfiootonj1i47x5ql8&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice13_tmp = st.session_state.reload_counter % 2
    if choice13_tmp == 0:
        st.image(choice13_arr[0 if choice13_tmp == 0 else 1])
    else:
        st.image(choice13_arr[0 if choice13_tmp == 1 else 1])
    st.text(' A high-angle view of a large, circular parliamentary chamber with rows of blue seats facing a central podium, featuring a large eagle emblem visible through the glass ceiling.')

    tmp13 = [
        "https://www.dropbox.com/scl/fi/r8jp0hxos1jtl35n2dhdg/Section3_Bild1.png?rlkey=6uh8j3khhcpg5zb00vpiarycn&dl=1",
        "https://www.dropbox.com/scl/fi/p363r22mqlr2tihchyfen/Section3_Bild0.png?rlkey=qoh1qxo0bq8biz9628mqubiag&dl=1",
        "https://www.dropbox.com/scl/fi/zdgpcnvd26ou683m2auud/Section3_Bild2.png?rlkey=n7h6ba3i6lz0zzkhlud9wnimu&dl=1",
        "https://www.dropbox.com/scl/fi/1uy43zo1oeht4mq5wysxk/Section3_Bild3.png?rlkey=bb3wic3yj5s0vqrfp7z6rlw86&dl=1",
    ]
    img13 = image_select(
        "Mögliche Valide Bilder:",
        tmp13,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 3", 0),
        key=f"frage13_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Thema 3"] = img13
    valid13_tmp = st.session_state.reload_counter % 2
    if valid13_tmp == 0:
        st.image(tmp13[st.session_state.auswahl.get("Seite 1 Thema 3", 0)] if valid13_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp13[st.session_state.auswahl.get("Seite 1 Thema 3", 0)] if valid13_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
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

    tmp14 = [
        "https://www.dropbox.com/scl/fi/by8bhno9vrpw4muuhnldq/Section4_Bild2.png?rlkey=vgofwjggqzaunkwhe1f8oohrx&dl=1",
        "https://www.dropbox.com/scl/fi/71r3l8fmblmidfert71r2/Section4_Bild0.png?rlkey=o1n8pcotadjr6kss85t8bkagw&dl=1",
        "https://www.dropbox.com/scl/fi/waj29s71quim2c7qox7ci/Section4_Bild1.png?rlkey=ety1m1rikukc5f3dus0ycxd3e&dl=1",
    ]
    img14 = image_select(
        "Mögliche Valide Bilder:",
        tmp14,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 4", 0),
        key=f"frage14_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Thema 4"] = img14
    valid14_tmp = st.session_state.reload_counter % 2
    if valid14_tmp == 0:
        st.image(tmp14[st.session_state.auswahl.get("Seite 1 Thema 4", 0)] if valid14_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp14[st.session_state.auswahl.get("Seite 1 Thema 4", 0)] if valid14_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Process of Electing Members to the Bundestag\n- Breaks down the two votes cast by citizens—direct vote for district candidates and party lists—required to determine which individuals represent them in the Bundestag.\n- Addresses qualifications needed for candidacy, campaign financing restrictions, and the five percent threshold required for smaller political parties to gain representation.')

    tmp15 = [
        "https://www.dropbox.com/scl/fi/7kqeo74ye9jj1s2oe4gc2/Section5_Bild0.png?rlkey=wgighmziahtvmwi4yzx70ci9l&dl=1",
        "https://www.dropbox.com/scl/fi/yy9csuf9ga19hy7n3xcp4/Section5_Bild1.png?rlkey=s0vzrdv20olmcldx6x8t0jkaq&dl=1",
        "https://www.dropbox.com/scl/fi/ziac66j7l06lnawlvil3n/Section5_Bild2.png?rlkey=n1ejvnpqij6ekshbzvibw1kvv&dl=1",
    ]
    img15 = image_select(
        "Mögliche Valide Bilder:",
        tmp15,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 1 Thema 5", 0),
        key=f"frage15_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 1 Thema 5"] = img15
    valid15_tmp = st.session_state.reload_counter % 2
    if valid15_tmp == 0:
        st.image(tmp15[st.session_state.auswahl.get("Seite 1 Thema 5", 0)] if valid15_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp15[st.session_state.auswahl.get("Seite 1 Thema 5", 0)] if valid15_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page2":
    st.title("Seite 2")

    pdf_url = "https://www.dropbox.com/scl/fi/xf0pfas91xqjaal3q8qzh/potenzial_der_windenergie.pdf?rlkey=f898fzwxeth4kvg7gdnngy3xl&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Maximize renewable energy production while protecting valuable natural resources in Germany.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Onshore Wind Energy Potential\n- Calculates the feasible area for wind energy utilization considering suitable sites free from protected zones, urban settlements, water bodies, and military facilities. Two types of reference wind turbines are analyzed - strong and weak ones.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text("Topic 2: Natural Area Protection Regulations\n- Introduces measures taken to safeguard various German ecosystems, encompassing Lärmschutzwald (woodlands designed to mitigate noise), Nationalparks (large, stricter protected territories), Natura 2000-Gebiete (designated habitats under EU's conservation network), Naturdenkmäler (individually preserved natural wonders), and Naturparke (extensive cultural landscapes).")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Factors Affecting Realized Wind Energy Potential\n- Addresses obstacles hindering complete harnessing of wind energy potential, comprising spatial development objectives, public resistance, location-based financing issues, and clashes related to civilian and military infrastructure demands.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Sensitivity Analysis & Optimizing Wind Energy Production\n- Investigates variations in wind energy potential when adjusting critical parameters like minimum distances required near residential structures and typical yearly wind speeds across regions.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Implications and Future Steps\n- Emphasizes the need for addressing practical hurdles and making informed societal choices at diverse decision-making levels to fully capitalize on Germany’s onshore wind energy prospects.\n\n')
    choice25_arr = [
        "https://www.dropbox.com/scl/fi/wsuemxxeku6puszj6gpcg/Section5_choice.png?rlkey=h8wimis03z2j1v5xiugnkw59i&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice25_tmp = st.session_state.reload_counter % 2
    if choice25_tmp == 0:
        st.image(choice25_arr[0 if choice25_tmp == 0 else 1])
    else:
        st.image(choice25_arr[0 if choice25_tmp == 1 else 1])
    st.text(' A row of white wind turbines stands against a backdrop of rolling green hills and a cloudy sky.')

    tmp25 = [
        "https://www.dropbox.com/scl/fi/634t87z27vajv6x47y6iw/Section5_Bild0.png?rlkey=piagjdfo6p1tbno4c7g9ma54k&dl=1",
    ]
    img25 = image_select(
        "Mögliche Valide Bilder:",
        tmp25,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 2 Thema 5", 0),
        key=f"frage25_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 2 Thema 5"] = img25
    valid25_tmp = st.session_state.reload_counter % 2
    if valid25_tmp == 0:
        st.image(tmp25[st.session_state.auswahl.get("Seite 2 Thema 5", 0)] if valid25_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp25[st.session_state.auswahl.get("Seite 2 Thema 5", 0)] if valid25_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page3":
    st.title("Seite 3")

    pdf_url = "https://www.dropbox.com/scl/fi/mqg9sdpiykcvbye7ohjdv/Probe345Bd93.pdf?rlkey=72qar9s8kggg9pkvjx2laurth&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Discuss the history, characteristics, distribution, threats, conservation efforts, and educational programs regarding dinosaurs.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Origin and Dominance of Dinosaurs\n- Details how dinosaurs evolved around 225 million years ago during the Triassic Period; explains why they dominated land ecosystems until their extinction approximately 65 million years ago.\n\n')
    choice31_arr = [
        "https://www.dropbox.com/scl/fi/rrt8u8qw3ylaos4d3rehr/Section1_choice.png?rlkey=5uxlb2kquf4uczxwo8o7j2zof&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice31_tmp = st.session_state.reload_counter % 2
    if choice31_tmp == 0:
        st.image(choice31_arr[0 if choice31_tmp == 0 else 1])
    else:
        st.image(choice31_arr[0 if choice31_tmp == 1 else 1])
    st.text(' A colorful illustration depicts a map of Earth approximately 225 million years ago, showing the arrangement of continents like Asia, Africa, South America, India, Australia, and Antartica surrounded by oceans and labeled with geological features.')

    tmp31 = [
        "https://www.dropbox.com/scl/fi/kouvvc8o0wpikpmag5hsa/Section1_Bild0.png?rlkey=f8sc7vrcnjo5m3pbhilbwnpvi&dl=1",
        "https://www.dropbox.com/scl/fi/d8m5kz02kbflrm2285kj2/Section1_Bild6.png?rlkey=pml89r7lpczla3dauu20s7pwm&dl=1",
        "https://www.dropbox.com/scl/fi/v3vi2xp8ds4idoj5n0kyt/Section1_Bild2.png?rlkey=c5205waa41msaabfbf5stfmkg&dl=1",
        "https://www.dropbox.com/scl/fi/4b2rs338wcksqg35cbva6/Section1_Bild5.png?rlkey=w5c9ol53h35da0jjrs53sm0ci&dl=1",
        "https://www.dropbox.com/scl/fi/lhgxw39vbrm4zrlno1wrl/Section1_Bild4.png?rlkey=cuihdo31wuh8uzgp5ygq37ixy&dl=1",
        "https://www.dropbox.com/scl/fi/d0qeb7l4o9a06vt780ya9/Section1_Bild1.png?rlkey=p170cm8oj3ef187rqpitjgrke&dl=1",
        "https://www.dropbox.com/scl/fi/tb6bacqzkj0dej3389ar8/Section1_Bild3.png?rlkey=4kmo9kqwfpby1r1lp3ng4jw4x&dl=1",
    ]
    img31 = image_select(
        "Mögliche Valide Bilder:",
        tmp31,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 1", 0),
        key=f"frage31_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Thema 1"] = img31
    valid31_tmp = st.session_state.reload_counter % 2
    if valid31_tmp == 0:
        st.image(tmp31[st.session_state.auswahl.get("Seite 3 Thema 1", 0)] if valid31_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp31[st.session_state.auswahl.get("Seite 3 Thema 1", 0)] if valid31_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Physical Features and Classifications\n- Outlines various types of dinosaurs based on their body structure, locomotive abilities, and food sources; describes differences between saurischians and ornithischians.\n\n')
    choice32_arr = [
        "https://www.dropbox.com/scl/fi/9ngqcl7t89yl5flmtgekh/Section2_choice.png?rlkey=xwikbtbgrb8koevwcyvdyfajr&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice32_tmp = st.session_state.reload_counter % 2
    if choice32_tmp == 0:
        st.image(choice32_arr[0 if choice32_tmp == 0 else 1])
    else:
        st.image(choice32_arr[0 if choice32_tmp == 1 else 1])
    st.text(" The image shows a phylogenetic tree of dinosaurs labeled with various classifications and illustrations of Plateosaurus, Diplodocus, and Brachiosaurus, alongside a skeletal diagram of a dinosaur's skull and spine.")

    tmp32 = [
        "https://www.dropbox.com/scl/fi/pfknk8qqzmnnib6x68fol/Section2_Bild1.png?rlkey=tn1z1ce2n99woh14w83rsfia2&dl=1",
        "https://www.dropbox.com/scl/fi/fasuthq2rcjy115t3cdrh/Section2_Bild0.png?rlkey=ij5j0a20sghshio8kz6pbqnmd&dl=1",
        "https://www.dropbox.com/scl/fi/vqyr7kfaim2dr6jofhr6i/Section2_Bild2.png?rlkey=5ds8jvd47v9adjry5fywtmd9g&dl=1",
        "https://www.dropbox.com/scl/fi/r3awfvd9sr75x0xsty359/Section2_Bild8.png?rlkey=cenq1f0gmc5j07w1lf02e9mvp&dl=1",
        "https://www.dropbox.com/scl/fi/oh1zucmhh5glax2l6ydal/Section2_Bild6.png?rlkey=uygm3rg2gixiholqjb6agp47t&dl=1",
        "https://www.dropbox.com/scl/fi/4pqwjjilrojhdok90cj3b/Section2_Bild5.png?rlkey=q5ja9erslvjuw6thgxc88tsjp&dl=1",
        "https://www.dropbox.com/scl/fi/zktmkkmpqornrbobo22ny/Section2_Bild7.png?rlkey=8kdxb8p1r9he3rg4cu13q901v&dl=1",
    ]
    img32 = image_select(
        "Mögliche Valide Bilder:",
        tmp32,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 2", 0),
        key=f"frage32_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Thema 2"] = img32
    valid32_tmp = st.session_state.reload_counter % 2
    if valid32_tmp == 0:
        st.image(tmp32[st.session_state.auswahl.get("Seite 3 Thema 2", 0)] if valid32_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp32[st.session_state.auswahl.get("Seite 3 Thema 2", 0)] if valid32_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp32 = [
        "https://www.dropbox.com/scl/fi/2w9a8eog5l94ibschhah0/Section2_Bild3.png?rlkey=4z9niuwdzwx88r3fjc191syle&dl=1",
        "https://www.dropbox.com/scl/fi/o9x00eznqxes8htnmeh5s/Section2_Bild4.png?rlkey=r6t028gdzqc48m6t17ijwizeq&dl=1",
    ]
    nvimg32 = image_select(
        "Nicht Valide Bilder:",
        nvtmp32,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 3 Thema 2", 0),
        key=f"nvfrage32_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg32} ausgewählt.")
    st.session_state.auswahl["nv Seite 3 Thema 2"] = nvimg32
    nvalid32_tmp = st.session_state.reload_counter % 2
    if nvalid32_tmp == 0:
        st.image(nvtmp32[st.session_state.auswahl.get("nv Seite 3 Thema 2", 0)] if nvalid32_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp32[st.session_state.auswahl.get("nv Seite 3 Thema 2", 0)] if nvalid32_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
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

    tmp33 = [
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
    ]
    img33 = image_select(
        "Mögliche Valide Bilder:",
        tmp33,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 3", 0),
        key=f"frage33_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Thema 3"] = img33
    valid33_tmp = st.session_state.reload_counter % 2
    if valid33_tmp == 0:
        st.image(tmp33[st.session_state.auswahl.get("Seite 3 Thema 3", 0)] if valid33_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp33[st.session_state.auswahl.get("Seite 3 Thema 3", 0)] if valid33_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Remaining Mysteries and Debated Issues\n- Addresses ongoing questions surrounding dinosaur behavior, intelligence, and potential warmth-bloodedness due to discoveries of fossilized remains showing evidence of feathers.\n\n')
    choice34_arr = [
        "https://www.dropbox.com/scl/fi/sl5pju0ne4cp9sbf6bge0/Section4_choice.png?rlkey=ejo58ng2kx3623vupsxb2mejo&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice34_tmp = st.session_state.reload_counter % 2
    if choice34_tmp == 0:
        st.image(choice34_arr[0 if choice34_tmp == 0 else 1])
    else:
        st.image(choice34_arr[0 if choice34_tmp == 1 else 1])
    st.text(' The image shows a close-up of a dinosaur skull and partial neck vertebrae, with a bluish-purple hue and sharp teeth.')

    tmp34 = [
        "https://www.dropbox.com/scl/fi/ylckz0dcf3nt18qfld63r/Section4_Bild3.png?rlkey=h7ftq6oafigb4mqzvhnjzftl1&dl=1",
        "https://www.dropbox.com/scl/fi/hvchmi745pn74x0p3d9uh/Section4_Bild2.png?rlkey=oyzey4rxws51w297rrdjclgl2&dl=1",
        "https://www.dropbox.com/scl/fi/4puh583foz9q41tf4tnf1/Section4_Bild0.png?rlkey=dav0aberprs73zvnuvv8jzqnf&dl=1",
        "https://www.dropbox.com/scl/fi/ft2012mp54cfnomb0efcz/Section4_Bild4.png?rlkey=jew4fy1qx1bjt22y5ybs8jy4m&dl=1",
        "https://www.dropbox.com/scl/fi/jvn9xl7n2uk13wpg62y6z/Section4_Bild1.png?rlkey=ygw44otzurk85p1xzvfztserb&dl=1",
        "https://www.dropbox.com/scl/fi/ymkr487vf1lwsc01anlgp/Section4_Bild5.png?rlkey=zrrdy7yfsfmxwtd6sl44smivu&dl=1",
    ]
    img34 = image_select(
        "Mögliche Valide Bilder:",
        tmp34,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 4", 0),
        key=f"frage34_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Thema 4"] = img34
    valid34_tmp = st.session_state.reload_counter % 2
    if valid34_tmp == 0:
        st.image(tmp34[st.session_state.auswahl.get("Seite 3 Thema 4", 0)] if valid34_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp34[st.session_state.auswahl.get("Seite 3 Thema 4", 0)] if valid34_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text("Topic 5: Legacy and Impact of Dinosaurs Today\n- Emphasizes the importance of studying dinosaurs for understanding Earth's past environments and biological diversity; highlights popular culture references depicting dinosaurs in movies, books, and toys.")

    tmp35 = [
        "https://www.dropbox.com/scl/fi/te9jiwvabyikq6h8xmenu/Section5_Bild0.png?rlkey=c7hvtneajnhl7znq5r9685ori&dl=1",
        "https://www.dropbox.com/scl/fi/1mhgg20c188mkj9l9pfea/Section5_Bild1.png?rlkey=qlri2w7d0z2smbq19hxzqdgls&dl=1",
        "https://www.dropbox.com/scl/fi/sps1btcs1nuxsam9tq3ky/Section5_Bild2.png?rlkey=7s87351j1setjxqv6o6n8r40i&dl=1",
        "https://www.dropbox.com/scl/fi/4o1wl1w7282kjjzgq91tj/Section5_Bild3.png?rlkey=ivtr27lkoqpx0a4hrsso7hnq7&dl=1",
    ]
    img35 = image_select(
        "Mögliche Valide Bilder:",
        tmp35,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 3 Thema 5", 0),
        key=f"frage35_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 3 Thema 5"] = img35
    valid35_tmp = st.session_state.reload_counter % 2
    if valid35_tmp == 0:
        st.image(tmp35[st.session_state.auswahl.get("Seite 3 Thema 5", 0)] if valid35_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp35[st.session_state.auswahl.get("Seite 3 Thema 5", 0)] if valid35_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page4":
    st.title("Seite 4")

    pdf_url = "https://www.dropbox.com/scl/fi/qt595erzzaye36pspwz8g/Zweiter_Weltkrieg_01.pdf?rlkey=dn85y8w9ze6fa91vyt3npmu44&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: To provide historical context on World War II, focusing specifically on events leading up to it, its course, effects away from battlefields, consequences after its conclusion, and political situation post-conflict.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text("Topic 1: Leadup to World War II\n- Details the dissolution of Austria-Hungary at the end of World War I, Treaties of Versailles and Saint Germain assigning blame for World War I to Germany and Austria, economic struggles faced by both countries during the 1920's due to these treaties, rise of authoritarian rule under Chancellor Engelbert Dollfüss in Austria, Nazi takeover in Germany led by Adolf Hitler, and his subsequent consolidation of power through various means including propaganda and violence against opponents.\n\n")
    choice41_arr = [
        "https://www.dropbox.com/scl/fi/l5npvyrwi3nwqdnt14mfw/Section1_choice.png?rlkey=iv08z0lzh9thc6c2jf6d04ccz&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice41_tmp = st.session_state.reload_counter % 2
    if choice41_tmp == 0:
        st.image(choice41_arr[0 if choice41_tmp == 0 else 1])
    else:
        st.image(choice41_arr[0 if choice41_tmp == 1 else 1])
    st.text(' A black and white photograph shows a procession of open-top cars driving down a cobblestone street lined with a large crowd of people raising their arms in salute.')

    tmp41 = [
        "https://www.dropbox.com/scl/fi/wmokpt2b1ge9rmz9ugkex/Section1_Bild0.png?rlkey=wo44ivjnxp93ufl2affyousv9&dl=1",
        "https://www.dropbox.com/scl/fi/ofuutdgqt0aj8wfm7grvv/Section1_Bild2.png?rlkey=dhjmc8rlycuvpcdgh7ij3jh84&dl=1",
        "https://www.dropbox.com/scl/fi/sdql0fj43byqlrj7fnviw/Section1_Bild5.png?rlkey=6b7y38adojz8df45eigeaguef&dl=1",
        "https://www.dropbox.com/scl/fi/f7a984nwdnpchdh8t770y/Section1_Bild4.png?rlkey=ri0y6q45apnn1yik7ztzx4325&dl=1",
        "https://www.dropbox.com/scl/fi/4fbfwd3boqhp5ustz86co/Section1_Bild1.png?rlkey=kx3mzusgmieo72dpw4euqh7ak&dl=1",
        "https://www.dropbox.com/scl/fi/i5fi8h7zmxvio79bjrxx9/Section1_Bild3.png?rlkey=fxbtp5qs24dcvlf0tm8log38r&dl=1",
    ]
    img41 = image_select(
        "Mögliche Valide Bilder:",
        tmp41,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 1", 0),
        key=f"frage41_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Thema 1"] = img41
    valid41_tmp = st.session_state.reload_counter % 2
    if valid41_tmp == 0:
        st.image(tmp41[st.session_state.auswahl.get("Seite 4 Thema 1", 0)] if valid41_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp41[st.session_state.auswahl.get("Seite 4 Thema 1", 0)] if valid41_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Start of World War II\n- Outlines how Hitler declared himself German Fuhrer and President upon Hindenburg’s death, persecution of Jews and minorities escalating, invasion of Poland initiating World War II, Britain and France declaring war on Germany two days later, beginning of "Blitzkrieg" strategy used by Germany resulting in quick victories over several European nations within months.\n\n')
    choice42_arr = [
        "https://www.dropbox.com/scl/fi/6yw2ipxt9emiieqc3vju9/Section2_choice.png?rlkey=aqbb2p6e3auvw26up2366ylfn&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice42_tmp = st.session_state.reload_counter % 2
    if choice42_tmp == 0:
        st.image(choice42_arr[0 if choice42_tmp == 0 else 1])
    else:
        st.image(choice42_arr[0 if choice42_tmp == 1 else 1])
    st.text(' Two figures stand amidst debris and rubble next to a fire truck in front of a damaged building with smoke rising in the background.')

    tmp42 = [
        "https://www.dropbox.com/scl/fi/8p873bnoev7mc4bjpjkjr/Section2_Bild0.png?rlkey=7zhg26rg9qwtg95bff4odqewf&dl=1",
    ]
    img42 = image_select(
        "Mögliche Valide Bilder:",
        tmp42,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 2", 0),
        key=f"frage42_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Thema 2"] = img42
    valid42_tmp = st.session_state.reload_counter % 2
    if valid42_tmp == 0:
        st.image(tmp42[st.session_state.auswahl.get("Seite 4 Thema 2", 0)] if valid42_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp42[st.session_state.auswahl.get("Seite 4 Thema 2", 0)] if valid42_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Course of World War II\n- Provides overview of key battles, invasions, and turning points throughout the six year conflict, including Battle of Britain, Operation Barbarossa (invasion of Soviet Union), D-Day landing in Normandy, Yalta Conference, atomic bomb attacks on Hiroshima and Nagasaki, and eventual surrender of Germany and Japan.\n\n')
    choice43_arr = [
        "https://www.dropbox.com/scl/fi/8vqgz92q25da9nnbc3bce/Section3_choice.png?rlkey=5l89hihpjman25xf1zf8uuntw&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice43_tmp = st.session_state.reload_counter % 2
    if choice43_tmp == 0:
        st.image(choice43_arr[0 if choice43_tmp == 0 else 1])
    else:
        st.image(choice43_arr[0 if choice43_tmp == 1 else 1])
    st.text(' A black and white photograph shows a car with flags of Finland, the Soviet Union, the United Kingdom, and the United States waving from its roof against a blurred background of a building and a statue.')

    tmp43 = [
        "https://www.dropbox.com/scl/fi/gs2a9hwa5rw05mocbwzx9/Section3_Bild1.png?rlkey=5us8mfw4w2ru7xsaetwk9ucrk&dl=1",
        "https://www.dropbox.com/scl/fi/8aqpwuuih1alowpavogzj/Section3_Bild0.png?rlkey=ac3fvgju2es6w7lyb5mco3oeo&dl=1",
        "https://www.dropbox.com/scl/fi/9uuzcqc6ejq4bvf3yudd5/Section3_Bild2.png?rlkey=evs66da2q55w7wodrtoy8lt8c&dl=1",
    ]
    img43 = image_select(
        "Mögliche Valide Bilder:",
        tmp43,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 3", 0),
        key=f"frage43_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Thema 3"] = img43
    valid43_tmp = st.session_state.reload_counter % 2
    if valid43_tmp == 0:
        st.image(tmp43[st.session_state.auswahl.get("Seite 4 Thema 3", 0)] if valid43_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp43[st.session_state.auswahl.get("Seite 4 Thema 3", 0)] if valid43_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Life During World War II Outside Battlegrounds\n- Describes impact of war on civilian populations across Europe, North Africa, Asia, and Pacific regions; details food scarcity, evacuation efforts, air raids, resistance movements, and experiences of women, children, and forced laborers during this time period.\n\n')
    choice44_arr = [
        "https://www.dropbox.com/scl/fi/geguukoiw7i3psrjgk64k/Section4_choice.png?rlkey=xxz4phblmedhxdo4qsskuhkff&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice44_tmp = st.session_state.reload_counter % 2
    if choice44_tmp == 0:
        st.image(choice44_arr[0 if choice44_tmp == 0 else 1])
    else:
        st.image(choice44_arr[0 if choice44_tmp == 1 else 1])
    st.text(' A black and white image shows a group of thin, distressed children huddled together in a trench or tunnel, looking upwards with expressions of fear and desperation.')

    tmp44 = [
        "https://www.dropbox.com/scl/fi/hyxpa8mf73h0l3bwevvik/Section4_Bild0.png?rlkey=0qy95f9c2yk6nb798iqmubfj4&dl=1",
        "https://www.dropbox.com/scl/fi/1uaq89x3nje4fsqp6ddhg/Section4_Bild1.png?rlkey=ynyhfymc4lwcuplwhied85uq6&dl=1",
    ]
    img44 = image_select(
        "Mögliche Valide Bilder:",
        tmp44,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 4", 0),
        key=f"frage44_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Thema 4"] = img44
    valid44_tmp = st.session_state.reload_counter % 2
    if valid44_tmp == 0:
        st.image(tmp44[st.session_state.auswahl.get("Seite 4 Thema 4", 0)] if valid44_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp44[st.session_state.auswahl.get("Seite 4 Thema 4", 0)] if valid44_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Aftermath of World War II\n- Addresses changes in global politics caused by the war, establishment of United Nations, start of Cold War, division of Germany into four occupation zones controlled by Allied powers, reconstruction process in defeated nations, ongoing debate regarding responsibility for war crimes committed during the conflict, and lasting impacts on societies worldwide.\n\n')
    choice45_arr = [
        "https://www.dropbox.com/scl/fi/tsj4jn2mrlzvzb557tgv7/Section5_choice.png?rlkey=fkpwkbbht3kpohu8xqq4g0et4&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice45_tmp = st.session_state.reload_counter % 2
    if choice45_tmp == 0:
        st.image(choice45_arr[0 if choice45_tmp == 0 else 1])
    else:
        st.image(choice45_arr[0 if choice45_tmp == 1 else 1])
    st.text(' The image is a map of Berlin divided into four sectors: French (blue), British (green), American (yellow), and Soviet (red), all surrounded by a Soviet zone.')

    tmp45 = [
        "https://www.dropbox.com/scl/fi/ywa66vd1dii6q1hb9zb1j/Section5_Bild0.png?rlkey=3yaf0i6pqbqd94xfv8atru8gm&dl=1",
        "https://www.dropbox.com/scl/fi/g925kzm7t0y6uh10s91et/Section5_Bild1.png?rlkey=sl76vedpdle9rlodz0jlhpyg5&dl=1",
        "https://www.dropbox.com/scl/fi/vnc2fv35svrwfymtwyh6l/Section5_Bild2.png?rlkey=vkfy043nec7dsz85dfd5h41pl&dl=1",
        "https://www.dropbox.com/scl/fi/6vxcaqeq0xzmo9xx13sjg/Section5_Bild3.png?rlkey=beox79l6hxwx88tiq86nrsiul&dl=1",
    ]
    img45 = image_select(
        "Mögliche Valide Bilder:",
        tmp45,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 4 Thema 5", 0),
        key=f"frage45_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 4 Thema 5"] = img45
    valid45_tmp = st.session_state.reload_counter % 2
    if valid45_tmp == 0:
        st.image(tmp45[st.session_state.auswahl.get("Seite 4 Thema 5", 0)] if valid45_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp45[st.session_state.auswahl.get("Seite 4 Thema 5", 0)] if valid45_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page5":
    st.title("Seite 5")

    pdf_url = "https://www.dropbox.com/scl/fi/wqkfgzdig35g0yo9neupf/Broschuere_2013_hires.pdf?rlkey=ewrhf2r8xtgke9ux3in0l3p95&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Understand the exploration of our solar system, focusing on significant findings related to planets, moons, asteroids, comets, and dwarf planets.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Key Findings About Inner & Outer Planets\n- Presents fundamental facts about terrestrial and gas giants, emphasizing their size, compositions, rotations, distances from the sun, and distinctive features like the Great Red Spot and Hexagon storm on Jupiter.\n\n')
    choice51_arr = [
        "https://www.dropbox.com/scl/fi/bxsl0059xbo6puplv4pic/Section1_choice.png?rlkey=bqdxmso4bpvzg0gl4n7hw7co1&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice51_tmp = st.session_state.reload_counter % 2
    if choice51_tmp == 0:
        st.image(choice51_arr[0 if choice51_tmp == 0 else 1])
    else:
        st.image(choice51_arr[0 if choice51_tmp == 1 else 1])
    st.text(' The image depicts a vibrant illustration of the solar system with planets orbiting a bright sun, set against a backdrop of a swirling galaxy and distant stars.')

    tmp51 = [
        "https://www.dropbox.com/scl/fi/r1s9w46sc84fd7xcdxqbx/Section1_Bild0.png?rlkey=u0fikgjx2zp1fuhysg7gom9mi&dl=1",
        "https://www.dropbox.com/scl/fi/aeubhasa0ktv9faf4gay0/Section1_Bild2.png?rlkey=tplpy5br06l26b5mip2edgb55&dl=1",
        "https://www.dropbox.com/scl/fi/1uyexuh3f8f9vp23j7g0w/Section1_Bild1.png?rlkey=wj6vdwgm60iguuapb0si25p5w&dl=1",
    ]
    img51 = image_select(
        "Mögliche Valide Bilder:",
        tmp51,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 1", 0),
        key=f"frage51_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Thema 1"] = img51
    valid51_tmp = st.session_state.reload_counter % 2
    if valid51_tmp == 0:
        st.image(tmp51[st.session_state.auswahl.get("Seite 5 Thema 1", 0)] if valid51_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp51[st.session_state.auswahl.get("Seite 5 Thema 1", 0)] if valid51_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Celestial Bodies Beyond Planets\n- Outlines various types of smaller celestial bodies found in the solar system, including asteroids, comets, dwarf planets, and natural satellites (moons).\n\n')
    choice52_arr = [
        "https://www.dropbox.com/scl/fi/scesvva3lqde8ezbx8i6x/Section2_choice.png?rlkey=hjr9qchan7cd7q18renjalzdw&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice52_tmp = st.session_state.reload_counter % 2
    if choice52_tmp == 0:
        st.image(choice52_arr[0 if choice52_tmp == 0 else 1])
    else:
        st.image(choice52_arr[0 if choice52_tmp == 1 else 1])
    st.text(' A series of planets, varying in size and color, are arranged in a line against a dark, starry background.')

    tmp52 = [
        "https://www.dropbox.com/scl/fi/3d9pkfls24ui4bgl57zya/Section2_Bild1.png?rlkey=q65wlmvewqw6hnonhgkuwv5m9&dl=1",
        "https://www.dropbox.com/scl/fi/4bp2q105mfpsb7ekg71ee/Section2_Bild0.png?rlkey=83re1settv0kn9gxybtgyg871&dl=1",
        "https://www.dropbox.com/scl/fi/e68hn36urvthuuvjrir67/Section2_Bild2.png?rlkey=i1k07s3c416byhf7zuozo4r1m&dl=1",
    ]
    img52 = image_select(
        "Mögliche Valide Bilder:",
        tmp52,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 2", 0),
        key=f"frage52_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Thema 2"] = img52
    valid52_tmp = st.session_state.reload_counter % 2
    if valid52_tmp == 0:
        st.image(tmp52[st.session_state.auswahl.get("Seite 5 Thema 2", 0)] if valid52_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp52[st.session_state.auswahl.get("Seite 5 Thema 2", 0)] if valid52_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Milestones in Space Exploration History\n- Recounts important events in the journey of human knowledge acquisition concerning the solar system, starting with Sputnik 1 in 1957 until present day, showcasing accomplishments achieved by numerous international space agencies.\n\n')
    choice53_arr = [
        "https://www.dropbox.com/scl/fi/neq4gtsra02f7iorypej8/Section3_choice.png?rlkey=t9wwyg4ziraj4lg9mwbfh8knv&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice53_tmp = st.session_state.reload_counter % 2
    if choice53_tmp == 0:
        st.image(choice53_arr[0 if choice53_tmp == 0 else 1])
    else:
        st.image(choice53_arr[0 if choice53_tmp == 1 else 1])
    st.text(' The image depicts a vibrant illustration of the solar system with planets orbiting a bright sun, set against a backdrop of a swirling galaxy and distant stars.')

    tmp53 = [
        "https://www.dropbox.com/scl/fi/mthuajerz5o717xaad7na/Section3_Bild0.png?rlkey=fqmgro2zmju8bhozlkg0ty9yw&dl=1",
    ]
    img53 = image_select(
        "Mögliche Valide Bilder:",
        tmp53,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 3", 0),
        key=f"frage53_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Thema 3"] = img53
    valid53_tmp = st.session_state.reload_counter % 2
    if valid53_tmp == 0:
        st.image(tmp53[st.session_state.auswahl.get("Seite 5 Thema 3", 0)] if valid53_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp53[st.session_state.auswahl.get("Seite 5 Thema 3", 0)] if valid53_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp53 = [
        "https://www.dropbox.com/scl/fi/7rfvlcah504ejc1crv4jt/Section3_Bild1.png?rlkey=lf7aakl2jibqgmklfpypr5036&dl=1",
    ]
    nvimg53 = image_select(
        "Nicht Valide Bilder:",
        nvtmp53,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 5 Thema 3", 0),
        key=f"nvfrage53_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg53} ausgewählt.")
    st.session_state.auswahl["nv Seite 5 Thema 3"] = nvimg53
    nvalid53_tmp = st.session_state.reload_counter % 2
    if nvalid53_tmp == 0:
        st.image(nvtmp53[st.session_state.auswahl.get("nv Seite 5 Thema 3", 0)] if nvalid53_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp53[st.session_state.auswahl.get("nv Seite 5 Thema 3", 0)] if nvalid53_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Asteroid Belts, Belt-Inhabitants, and Near Earth Objects\n- Investigates the origin, distribution, and threat levels associated with asteroids located in the asteroid belts and those approaching Earth (Near Earth Objects - NEOs).\n\n')
    choice54_arr = [
        "https://www.dropbox.com/scl/fi/c75ympeo766k3wr4pud27/Section4_choice.png?rlkey=hhfwx57tq7i6ukiz88thw4o38&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice54_tmp = st.session_state.reload_counter % 2
    if choice54_tmp == 0:
        st.image(choice54_arr[0 if choice54_tmp == 0 else 1])
    else:
        st.image(choice54_arr[0 if choice54_tmp == 1 else 1])
    st.text(' The image depicts a vibrant illustration of the solar system with planets orbiting a bright sun, set against a backdrop of a swirling galaxy and distant stars.')

    tmp54 = [
        "https://www.dropbox.com/scl/fi/f3x2jaxg167w097d3t6u3/Section4_Bild3.png?rlkey=0ip8c1zcwrbg5kaw1bc03r139&dl=1",
        "https://www.dropbox.com/scl/fi/tvu0ofcihg4wzu15r4j8g/Section4_Bild2.png?rlkey=uhmufnz2aa36nhsmv1eeazckf&dl=1",
        "https://www.dropbox.com/scl/fi/ihwhggdk87mo34uo8ftgw/Section4_Bild0.png?rlkey=qhre64supqkrzjs3fniavd74k&dl=1",
        "https://www.dropbox.com/scl/fi/7bhw4cjcu2pbgu0pdzjom/Section4_Bild1.png?rlkey=o4wvx8udm57loqqqirc8n9s0p&dl=1",
    ]
    img54 = image_select(
        "Mögliche Valide Bilder:",
        tmp54,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 4", 0),
        key=f"frage54_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Thema 4"] = img54
    valid54_tmp = st.session_state.reload_counter % 2
    if valid54_tmp == 0:
        st.image(tmp54[st.session_state.auswahl.get("Seite 5 Thema 4", 0)] if valid54_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp54[st.session_state.auswahl.get("Seite 5 Thema 4", 0)] if valid54_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text("Topic 5: Significance of Comets in Early Planet Formation and Life Development\n- Elucidates the roles played by comets during the formation of our solar system, particularly their contribution towards creating Earth's atmosphere and potentially influencing the rise of biology.\n\n")
    choice55_arr = [
        "https://www.dropbox.com/scl/fi/guvyjf8fywg4qj1oztes2/Section5_choice.png?rlkey=ft4sk0hl1jlka69q9350a3g2j&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice55_tmp = st.session_state.reload_counter % 2
    if choice55_tmp == 0:
        st.image(choice55_arr[0 if choice55_tmp == 0 else 1])
    else:
        st.image(choice55_arr[0 if choice55_tmp == 1 else 1])
    st.text(' The image depicts a vibrant illustration of the solar system with planets orbiting a bright sun, set against a backdrop of a swirling galaxy and distant stars.')

    tmp55 = [
        "https://www.dropbox.com/scl/fi/sjh0ctbyud9nonqe2mvsg/Section5_Bild0.png?rlkey=1od2htrcks59yo2crq5ui9k2a&dl=1",
        "https://www.dropbox.com/scl/fi/nq5v49ffwfy04b7qdjfpg/Section5_Bild1.png?rlkey=4zgt9ne8sxlif8dmr9o7wcxt8&dl=1",
        "https://www.dropbox.com/scl/fi/ijgxg2d7oa9i2gg3zzdxk/Section5_Bild2.png?rlkey=0a85fpzv84rcpt7o97a0iv8s7&dl=1",
        "https://www.dropbox.com/scl/fi/rtapfgfhzq9ti0pxbi90b/Section5_Bild4.png?rlkey=9sdw7zreigomhyy8ikqk54ovs&dl=1",
    ]
    img55 = image_select(
        "Mögliche Valide Bilder:",
        tmp55,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 5 Thema 5", 0),
        key=f"frage55_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 5 Thema 5"] = img55
    valid55_tmp = st.session_state.reload_counter % 2
    if valid55_tmp == 0:
        st.image(tmp55[st.session_state.auswahl.get("Seite 5 Thema 5", 0)] if valid55_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp55[st.session_state.auswahl.get("Seite 5 Thema 5", 0)] if valid55_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp55 = [
        "https://www.dropbox.com/scl/fi/qav539unuoie3pwgjrmwf/Section5_Bild3.png?rlkey=79rixpps0z8yau42z5olkyzhp&dl=1",
    ]
    nvimg55 = image_select(
        "Nicht Valide Bilder:",
        nvtmp55,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 5 Thema 5", 0),
        key=f"nvfrage55_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg55} ausgewählt.")
    st.session_state.auswahl["nv Seite 5 Thema 5"] = nvimg55
    nvalid55_tmp = st.session_state.reload_counter % 2
    if nvalid55_tmp == 0:
        st.image(nvtmp55[st.session_state.auswahl.get("nv Seite 5 Thema 5", 0)] if nvalid55_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp55[st.session_state.auswahl.get("nv Seite 5 Thema 5", 0)] if nvalid55_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page6":
    st.title("Seite 6")

    pdf_url = "https://www.dropbox.com/scl/fi/dl7xr4edcjqye3xdx0nux/Menschenaffen_Unterrichtsmaterial.pdf?rlkey=lzkwispw171pcc5bpwtovn8ne&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Provide educational resources for teachers to facilitate learning about great apes through various subjects like German language, Biology, Social Studies, Geography, and Arts.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Introduction\n- Presents background information about the World Wide Fund for Nature (WWF) and its focus on protecting endangered animals.\n\n')
    choice61_arr = [
        "https://www.dropbox.com/scl/fi/t5ecgbjl7a6oh3hexsxjq/Section1_choice.png?rlkey=d8gzmuq68isaqfbw7w71tvnwd&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice61_tmp = st.session_state.reload_counter % 2
    if choice61_tmp == 0:
        st.image(choice61_arr[0 if choice61_tmp == 0 else 1])
    else:
        st.image(choice61_arr[0 if choice61_tmp == 1 else 1])
    st.text(' An orangutan with long reddish-brown fur is clinging to a tree branch surrounded by lush green foliage.')

    tmp61 = [
        "https://www.dropbox.com/scl/fi/6m3w4jz4eo9edd0n3jvpm/Section1_Bild0.png?rlkey=yujuisuay1c3wng7hcpwsr9o2&dl=1",
        "https://www.dropbox.com/scl/fi/1rb3b3q0e54a2b1m4qohe/Section1_Bild7.png?rlkey=j40o84b26fmi5fk76fy84tz3q&dl=1",
        "https://www.dropbox.com/scl/fi/mcfjx7kyrwp4ldv8rvoro/Section1_Bild3.png?rlkey=n82vntwm4vxct1a8cmddjb9vs&dl=1",
    ]
    img61 = image_select(
        "Mögliche Valide Bilder:",
        tmp61,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 1", 0),
        key=f"frage61_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 1"] = img61
    valid61_tmp = st.session_state.reload_counter % 2
    if valid61_tmp == 0:
        st.image(tmp61[st.session_state.auswahl.get("Seite 6 Thema 1", 0)] if valid61_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp61[st.session_state.auswahl.get("Seite 6 Thema 1", 0)] if valid61_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp61 = [
        "https://www.dropbox.com/scl/fi/bl4ad6yj1ts8b8vadhz7o/Section1_Bild6.png?rlkey=1x9dqca34nedrspuzhs4zdkor&dl=1",
        "https://www.dropbox.com/scl/fi/9cjug4tl5zpnw3g1yis1e/Section1_Bild2.png?rlkey=19k72jfdvzebcvij7i1lcce8o&dl=1",
        "https://www.dropbox.com/scl/fi/3w9l5vapp8ig2okzt2f68/Section1_Bild5.png?rlkey=c74vq383skcwnw2cvie5jioou&dl=1",
        "https://www.dropbox.com/scl/fi/l1k4u15kx0szqozi597zf/Section1_Bild4.png?rlkey=klo23zf6656bxfjgezand6pku&dl=1",
        "https://www.dropbox.com/scl/fi/7tq1p3crtzd3mh5zlosna/Section1_Bild8.png?rlkey=mmz1cq1ftye5s3emtxoa1i95e&dl=1",
        "https://www.dropbox.com/scl/fi/44oc61s33u978firxq5yx/Section1_Bild1.png?rlkey=kw8cnkerpl2dhw0q0ww5532j3&dl=1",
    ]
    nvimg61 = image_select(
        "Nicht Valide Bilder:",
        nvtmp61,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 1", 0),
        key=f"nvfrage61_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg61} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 1"] = nvimg61
    nvalid61_tmp = st.session_state.reload_counter % 2
    if nvalid61_tmp == 0:
        st.image(nvtmp61[st.session_state.auswahl.get("nv Seite 6 Thema 1", 0)] if nvalid61_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp61[st.session_state.auswahl.get("nv Seite 6 Thema 1", 0)] if nvalid61_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: About WWF\'s Youth Education Program "Young Panda"\n- Details the goals and objectives of the youth education initiative aimed at children aged 8-14 years old.\n\n')
    choice62_arr = [
        "https://www.dropbox.com/scl/fi/24c6c3q5816z4m7c2gytf/Section2_choice.png?rlkey=ksp2wbdlxhcrq1gthaqgply7r&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice62_tmp = st.session_state.reload_counter % 2
    if choice62_tmp == 0:
        st.image(choice62_arr[0 if choice62_tmp == 0 else 1])
    else:
        st.image(choice62_arr[0 if choice62_tmp == 1 else 1])
    st.text(' A man in a blue jacket and black hat is pointing at a moss-covered log while a group of children wearing backpacks look on in a wooded area.')

    tmp62 = [
        "https://www.dropbox.com/scl/fi/xiaky9xm71j0ykzsfi6ej/Section2_Bild3.png?rlkey=il35b5uk54wgu5egmcutz7rbe&dl=1",
        "https://www.dropbox.com/scl/fi/9r397roisca37gvgx3rcx/Section2_Bild2.png?rlkey=3rcdl9wxmnxao4agzcriq0yeo&dl=1",
        "https://www.dropbox.com/scl/fi/hs32a89h00g4lcas626um/Section2_Bild6.png?rlkey=zjbtpzgnd1qc2ssezeyo3g0ht&dl=1",
        "https://www.dropbox.com/scl/fi/y5nke1j5fkh2qvc8evlal/Section2_Bild4.png?rlkey=5klt1kn39b20sinh4agfvbt6r&dl=1",
        "https://www.dropbox.com/scl/fi/t55pqpz6sg95mufrdwdv2/Section2_Bild5.png?rlkey=ac881etgr7zxaluo92k98lceo&dl=1",
    ]
    img62 = image_select(
        "Mögliche Valide Bilder:",
        tmp62,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 2", 0),
        key=f"frage62_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 2"] = img62
    valid62_tmp = st.session_state.reload_counter % 2
    if valid62_tmp == 0:
        st.image(tmp62[st.session_state.auswahl.get("Seite 6 Thema 2", 0)] if valid62_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp62[st.session_state.auswahl.get("Seite 6 Thema 2", 0)] if valid62_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp62 = [
        "https://www.dropbox.com/scl/fi/s5ltf9jcelp2633ub7426/Section2_Bild1.png?rlkey=7lgdvh97gbqq8c45s56upngpk&dl=1",
        "https://www.dropbox.com/scl/fi/5xgwwydqnuhkqyuq0opgt/Section2_Bild0.png?rlkey=ejvw2qjh5i0bg33zrenq758gn&dl=1",
    ]
    nvimg62 = image_select(
        "Nicht Valide Bilder:",
        nvtmp62,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 2", 0),
        key=f"nvfrage62_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg62} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 2"] = nvimg62
    nvalid62_tmp = st.session_state.reload_counter % 2
    if nvalid62_tmp == 0:
        st.image(nvtmp62[st.session_state.auswahl.get("nv Seite 6 Thema 2", 0)] if nvalid62_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp62[st.session_state.auswahl.get("nv Seite 6 Thema 2", 0)] if nvalid62_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Overview of Great Apes\n- Discusses four types of great apes: Orangutans, Gorillas, Chimpanzees, and Bonobos, including evolutionary history, characteristics, and unique features.')


    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp63 = [
        "https://www.dropbox.com/scl/fi/2fkku469s6l3rd5uxn966/Section3_Bild5.png?rlkey=8j581h9xdm6ycbar7c28pzf6s&dl=1",
        "https://www.dropbox.com/scl/fi/oy4d1xsobvw3z9qik66mz/Section3_Bild1.png?rlkey=xjrfklww228u624z4jynf7auf&dl=1",
        "https://www.dropbox.com/scl/fi/qldkn1uy6i2j022eos0lt/Section3_Bild0.png?rlkey=7tyd6qe2urnj58r6enyidjxr0&dl=1",
        "https://www.dropbox.com/scl/fi/5jjcba9ojmkheedli2eyp/Section3_Bild4.png?rlkey=aea529fviklpnllwifp4fsyam&dl=1",
        "https://www.dropbox.com/scl/fi/69rpnkgmdszdaj44m279p/Section3_Bild6.png?rlkey=4rqqaq9volis83clmlhl1lijx&dl=1",
        "https://www.dropbox.com/scl/fi/j2rl7f53ds4hgvro7tdaj/Section3_Bild7.png?rlkey=jp3nez4bsfoc3lbrqv6yqj85b&dl=1",
        "https://www.dropbox.com/scl/fi/06exmancl2j19f4k1cg3q/Section3_Bild2.png?rlkey=65r7lqc1xnpo3s6v59jch47x0&dl=1",
        "https://www.dropbox.com/scl/fi/k63zqqw464p4tacrfxc66/Section3_Bild3.png?rlkey=sih4wojvioeccv33fm7r6z30p&dl=1",
    ]
    nvimg63 = image_select(
        "Nicht Valide Bilder:",
        nvtmp63,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 3", 0),
        key=f"nvfrage63_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg63} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 3"] = nvimg63
    nvalid63_tmp = st.session_state.reload_counter % 2
    if nvalid63_tmp == 0:
        st.image(nvtmp63[st.session_state.auswahl.get("nv Seite 6 Thema 3", 0)] if nvalid63_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp63[st.session_state.auswahl.get("nv Seite 6 Thema 3", 0)] if nvalid63_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Living Conditions of Great Apes\n- Addresses how and where these primates reside across continents, specifically focusing on tropical rainforests and savanna regions.\n\n')
    choice64_arr = [
        "https://www.dropbox.com/scl/fi/iaztgpeyfexx8efduob32/Section4_choice.png?rlkey=z9tv5nvmjrp01hj44l5mffs37&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice64_tmp = st.session_state.reload_counter % 2
    if choice64_tmp == 0:
        st.image(choice64_arr[0 if choice64_tmp == 0 else 1])
    else:
        st.image(choice64_arr[0 if choice64_tmp == 1 else 1])
    st.text(' An orange-haired orangutan is centered in the image, peering over a lush green jungle backdrop with German text and logos at the bottom.')

    tmp64 = [
        "https://www.dropbox.com/scl/fi/m6z0wiu5bunt2hqxpwpge/Section4_Bild0.png?rlkey=o9y5b6u74c7ige2puuui4bg5j&dl=1",
    ]
    img64 = image_select(
        "Mögliche Valide Bilder:",
        tmp64,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 4", 0),
        key=f"frage64_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 4"] = img64
    valid64_tmp = st.session_state.reload_counter % 2
    if valid64_tmp == 0:
        st.image(tmp64[st.session_state.auswahl.get("Seite 6 Thema 4", 0)] if valid64_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp64[st.session_state.auswahl.get("Seite 6 Thema 4", 0)] if valid64_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp64 = [
        "https://www.dropbox.com/scl/fi/4ckf0s8uipr1mclcp40gq/Section4_Bild3.png?rlkey=gw9p17vev7peu1bcg17nnu33d&dl=1",
        "https://www.dropbox.com/scl/fi/lt2atim74xsr0pyo1d1jl/Section4_Bild6.png?rlkey=d0o1swy30gicy0g6ttecjlota&dl=1",
        "https://www.dropbox.com/scl/fi/2dc8po2lg64h09lkys5do/Section4_Bild2.png?rlkey=btljtwln7etclehvz2pczpwww&dl=1",
        "https://www.dropbox.com/scl/fi/a764kd9wawz7sotcat03q/Section4_Bild8.png?rlkey=wffof0d77wowgd9iu8vo1co11&dl=1",
        "https://www.dropbox.com/scl/fi/c4pnlxoc0u722qjgityz1/Section4_Bild4.png?rlkey=vax50uqy1lrqgvi6jucpmtt3p&dl=1",
        "https://www.dropbox.com/scl/fi/ysd7o3rwturt013g16q21/Section4_Bild7.png?rlkey=efamnx7ichbk3qiuq69xog8z3&dl=1",
        "https://www.dropbox.com/scl/fi/8b4rvreiz6millgmvdwkp/Section4_Bild1.png?rlkey=8kx5vi7qr6mdvytinmt5yxs00&dl=1",
        "https://www.dropbox.com/scl/fi/bzgv0boqolvyppvuohp0s/Section4_Bild5.png?rlkey=ihsvp2b0etkpwrf7qeo4po47k&dl=1",
    ]
    nvimg64 = image_select(
        "Nicht Valide Bilder:",
        nvtmp64,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 4", 0),
        key=f"nvfrage64_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg64} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 4"] = nvimg64
    nvalid64_tmp = st.session_state.reload_counter % 2
    if nvalid64_tmp == 0:
        st.image(nvtmp64[st.session_state.auswahl.get("nv Seite 6 Thema 4", 0)] if nvalid64_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp64[st.session_state.auswahl.get("nv Seite 6 Thema 4", 0)] if nvalid64_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Threats to Great Apes\n- Identifies factors contributing to the decline of great ape populations, such as hunting, deforestation, and human encroachment into habitats.\n\n')
    choice65_arr = [
        "https://www.dropbox.com/scl/fi/h1q8azmybyldxik76nrvr/Section5_choice.png?rlkey=t06941zvusncj5a9hrv1dlzb7&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice65_tmp = st.session_state.reload_counter % 2
    if choice65_tmp == 0:
        st.image(choice65_arr[0 if choice65_tmp == 0 else 1])
    else:
        st.image(choice65_arr[0 if choice65_tmp == 1 else 1])
    st.text(' An orange-haired orangutan is centered in the image, peering over a lush green jungle backdrop with German text and logos at the bottom.')

    tmp65 = [
        "https://www.dropbox.com/scl/fi/pwcgj9si2x6kpqcet0q0e/Section5_Bild0.png?rlkey=p9ng91miqc8x53vya7ol9qirf&dl=1",
    ]
    img65 = image_select(
        "Mögliche Valide Bilder:",
        tmp65,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 5", 0),
        key=f"frage65_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 5"] = img65
    valid65_tmp = st.session_state.reload_counter % 2
    if valid65_tmp == 0:
        st.image(tmp65[st.session_state.auswahl.get("Seite 6 Thema 5", 0)] if valid65_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp65[st.session_state.auswahl.get("Seite 6 Thema 5", 0)] if valid65_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp65 = [
        "https://www.dropbox.com/scl/fi/dztsqwaby6b674nl7tgqh/Section5_Bild5.png?rlkey=148xv1d8m98rogv7n5q16hiw0&dl=1",
        "https://www.dropbox.com/scl/fi/ja1po14nexljuhi6ufmkz/Section5_Bild8.png?rlkey=b8y00804ial3air1ctun8wn4z&dl=1",
        "https://www.dropbox.com/scl/fi/thifblavbk9h0crizf5kt/Section5_Bild1.png?rlkey=evz97u6vp0ba4xz2rpitbo68n&dl=1",
        "https://www.dropbox.com/scl/fi/se9vcrwl3wd9tnzqy4kff/Section5_Bild2.png?rlkey=ho9pnreigo1gfktqba01ds8o9&dl=1",
        "https://www.dropbox.com/scl/fi/erbtxipw4ncy350fbfmsh/Section5_Bild7.png?rlkey=jp6daifddwgppwebmf9i2c0no&dl=1",
        "https://www.dropbox.com/scl/fi/slk9szat7c94j5gv49vc6/Section5_Bild4.png?rlkey=5mfgry8494n3afcjr9tnlrp5w&dl=1",
        "https://www.dropbox.com/scl/fi/v2uwdeo5expmrimfvg665/Section5_Bild6.png?rlkey=j3t1blar4vjlp8p6pbfc8lzqn&dl=1",
        "https://www.dropbox.com/scl/fi/0ceam7tb1ggv4wrs6q9me/Section5_Bild3.png?rlkey=7pb5ir5gpxk0u4gskm0fojvb4&dl=1",
    ]
    nvimg65 = image_select(
        "Nicht Valide Bilder:",
        nvtmp65,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 5", 0),
        key=f"nvfrage65_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg65} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 5"] = nvimg65
    nvalid65_tmp = st.session_state.reload_counter % 2
    if nvalid65_tmp == 0:
        st.image(nvtmp65[st.session_state.auswahl.get("nv Seite 6 Thema 5", 0)] if nvalid65_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp65[st.session_state.auswahl.get("nv Seite 6 Thema 5", 0)] if nvalid65_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 6: Solutions and Protection Efforts\n- Outlines conservation strategies employed by WWF and others to preserve great ape habitats, combat wildlife trafficking, and promote sustainable development.\n\n')
    choice66_arr = [
        "https://www.dropbox.com/scl/fi/7liib7mxjj9q2yjwaem2o/Section6_choice.png?rlkey=cfuqovpisc97x7z0aiyi4rjd5&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice66_tmp = st.session_state.reload_counter % 2
    if choice66_tmp == 0:
        st.image(choice66_arr[0 if choice66_tmp == 0 else 1])
    else:
        st.image(choice66_arr[0 if choice66_tmp == 1 else 1])
    st.text(' An orange-haired orangutan is centered in the image, peering over a lush green jungle backdrop with German text and logos at the bottom.')

    tmp66 = [
        "https://www.dropbox.com/scl/fi/sh3eepw9yth2kt8t8m2xt/Section6_Bild10.png?rlkey=kzku3asl68a958i9desjhx40j&dl=1",
        "https://www.dropbox.com/scl/fi/zoz1icyi1nrvunb4efheb/Section6_Bild4.png?rlkey=qjhnygsz0htntflagdipa4ini&dl=1",
        "https://www.dropbox.com/scl/fi/mxo01dkyg2ldj649ks325/Section6_Bild2.png?rlkey=gves3lcnlnrcp6aniavo2i83e&dl=1",
        "https://www.dropbox.com/scl/fi/yhzp16meqtaxlf82zz7cp/Section6_Bild9.png?rlkey=o91dn0pfrmjn4gfzesq6yddhq&dl=1",
    ]
    img66 = image_select(
        "Mögliche Valide Bilder:",
        tmp66,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 6", 0),
        key=f"frage66_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 6"] = img66
    valid66_tmp = st.session_state.reload_counter % 2
    if valid66_tmp == 0:
        st.image(tmp66[st.session_state.auswahl.get("Seite 6 Thema 6", 0)] if valid66_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp66[st.session_state.auswahl.get("Seite 6 Thema 6", 0)] if valid66_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp66 = [
        "https://www.dropbox.com/scl/fi/r9dk4aj1ed4aqs3n90po5/Section6_Bild8.png?rlkey=9jug4yuslqjc7u6me1qz5cwhi&dl=1",
        "https://www.dropbox.com/scl/fi/yg320emk0z84wikp99oc2/Section6_Bild0.png?rlkey=k5j9dcpq9cca45eedg10i8n89&dl=1",
        "https://www.dropbox.com/scl/fi/kwmxmbur74b48gwv6lkjn/Section6_Bild5.png?rlkey=r7psiqr7egyc7dk1yu6vs75n4&dl=1",
        "https://www.dropbox.com/scl/fi/hubh7ynan9br4xc3a1nvf/Section6_Bild6.png?rlkey=e711rl0otbc82ufd68xhueqjq&dl=1",
        "https://www.dropbox.com/scl/fi/xhdpjmq6b2eo8j92p3nny/Section6_Bild3.png?rlkey=g5flqulealw0fo492x2esoq7z&dl=1",
        "https://www.dropbox.com/scl/fi/mgfuir49yuk5no221m2kj/Section6_Bild11.png?rlkey=qy4c1iwbhwe2fwkee5oyi67bo&dl=1",
        "https://www.dropbox.com/scl/fi/z2e97hnj0pl54ibzmy9uc/Section6_Bild7.png?rlkey=tsjsy26lsg13u99ikcf1pol4j&dl=1",
        "https://www.dropbox.com/scl/fi/hvvaywnb66pgjxmdp3v0t/Section6_Bild1.png?rlkey=io17ta9u3luh7ge399d9cxdm8&dl=1",
    ]
    nvimg66 = image_select(
        "Nicht Valide Bilder:",
        nvtmp66,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 6", 0),
        key=f"nvfrage66_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg66} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 6"] = nvimg66
    nvalid66_tmp = st.session_state.reload_counter % 2
    if nvalid66_tmp == 0:
        st.image(nvtmp66[st.session_state.auswahl.get("nv Seite 6 Thema 6", 0)] if nvalid66_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp66[st.session_state.auswahl.get("nv Seite 6 Thema 6", 0)] if nvalid66_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 7: Human-Apes Relationships\n- Investigates interactions between humans and great apes, discussing both conflicts and instances of cooperation.')

    tmp67 = [
        "https://www.dropbox.com/scl/fi/qwarnc4cso7o1ybgqy086/Section7_Bild5.png?rlkey=d6fd4cm7r7tn8kq82n9h6rnb1&dl=1",
        "https://www.dropbox.com/scl/fi/yk2pex0gfgqzsajsigxiq/Section7_Bild3.png?rlkey=a344ece2gs6z3zpxrxhhntfsr&dl=1",
        "https://www.dropbox.com/scl/fi/jd1e7obc1vk6rtf7mp1w7/Section7_Bild8.png?rlkey=a26h1e3izorqjd5bz5k17froj&dl=1",
        "https://www.dropbox.com/scl/fi/d0ldfgttlvujwrt2y8nqr/Section7_Bild4.png?rlkey=smlsg8kyba4g1ounr3enuw4i6&dl=1",
        "https://www.dropbox.com/scl/fi/hdcjyziljw84xvgp2b6n5/Section7_Bild0.png?rlkey=zw78rfu885br4qccgt6jr6ple&dl=1",
    ]
    img67 = image_select(
        "Mögliche Valide Bilder:",
        tmp67,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 7", 0),
        key=f"frage67_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 7"] = img67
    valid67_tmp = st.session_state.reload_counter % 2
    if valid67_tmp == 0:
        st.image(tmp67[st.session_state.auswahl.get("Seite 6 Thema 7", 0)] if valid67_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp67[st.session_state.auswahl.get("Seite 6 Thema 7", 0)] if valid67_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp67 = [
        "https://www.dropbox.com/scl/fi/7fbxk4af8e2vmsysh6h7z/Section7_Bild7.png?rlkey=4r6w91gqyszph7hf8scrs0my6&dl=1",
        "https://www.dropbox.com/scl/fi/ku4yr9lg4blahhkwycly8/Section7_Bild9.png?rlkey=j3zc17s4zlop7ebqtthwc2nyv&dl=1",
        "https://www.dropbox.com/scl/fi/21s5ht9woh80macujz124/Section7_Bild10.png?rlkey=eskumi7zze77jjk752rzj65qa&dl=1",
        "https://www.dropbox.com/scl/fi/a7z1oeloiqqlaeqhvpi57/Section7_Bild6.png?rlkey=parahq7cm2lqsdno25jyhplro&dl=1",
        "https://www.dropbox.com/scl/fi/wxwuziovppeo8zpzgpl5x/Section7_Bild2.png?rlkey=t8pq5emo21pq6acx9bn3t31jc&dl=1",
        "https://www.dropbox.com/scl/fi/tt97txvmsgb6gne6rmy3i/Section7_Bild1.png?rlkey=nzaza6vg9gzvhduyvaamzqajw&dl=1",
    ]
    nvimg67 = image_select(
        "Nicht Valide Bilder:",
        nvtmp67,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 7", 0),
        key=f"nvfrage67_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg67} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 7"] = nvimg67
    nvalid67_tmp = st.session_state.reload_counter % 2
    if nvalid67_tmp == 0:
        st.image(nvtmp67[st.session_state.auswahl.get("nv Seite 6 Thema 7", 0)] if nvalid67_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp67[st.session_state.auswahl.get("nv Seite 6 Thema 7", 0)] if nvalid67_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 8: Activities for Students\n- Offers suggestions for classroom activities related to each theme covered throughout the guidebook, encouraging active engagement among students.\n\n')
    choice68_arr = [
        "https://www.dropbox.com/scl/fi/34co5uecuxyf4dovosxc3/Section8_choice.png?rlkey=eemcweex3pendj5fvbyjebtn0&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice68_tmp = st.session_state.reload_counter % 2
    if choice68_tmp == 0:
        st.image(choice68_arr[0 if choice68_tmp == 0 else 1])
    else:
        st.image(choice68_arr[0 if choice68_tmp == 1 else 1])
    st.text(' An orange-haired orangutan is centered in the image, peering over a lush green jungle backdrop with German text and logos at the bottom.')

    tmp68 = [
        "https://www.dropbox.com/scl/fi/3plhbk4pwzw74wshe1fd0/Section8_Bild0.png?rlkey=18gxkmntm0ni8sq4jy1mvvz7m&dl=1",
        "https://www.dropbox.com/scl/fi/erw7a6ch7kwszsdwsb29e/Section8_Bild3.png?rlkey=21uzlvzikqvo40wuz0mjl6a01&dl=1",
    ]
    img68 = image_select(
        "Mögliche Valide Bilder:",
        tmp68,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 6 Thema 8", 0),
        key=f"frage68_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 6 Thema 8"] = img68
    valid68_tmp = st.session_state.reload_counter % 2
    if valid68_tmp == 0:
        st.image(tmp68[st.session_state.auswahl.get("Seite 6 Thema 8", 0)] if valid68_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp68[st.session_state.auswahl.get("Seite 6 Thema 8", 0)] if valid68_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp68 = [
        "https://www.dropbox.com/scl/fi/ofrxqt5ofhm6ucdz7mmzz/Section8_Bild1.png?rlkey=mv8j3sevrkki4lklok92hhrci&dl=1",
        "https://www.dropbox.com/scl/fi/r3bkv4ynx6g9p7qfi8j13/Section8_Bild4.png?rlkey=rc2c69wpza4t94u69vsyblubj&dl=1",
        "https://www.dropbox.com/scl/fi/i78ogzysrxd5c6dwb6f9j/Section8_Bild2.png?rlkey=cfgydo29hsn7zvhjkml8a4pwt&dl=1",
    ]
    nvimg68 = image_select(
        "Nicht Valide Bilder:",
        nvtmp68,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 6 Thema 8", 0),
        key=f"nvfrage68_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg68} ausgewählt.")
    st.session_state.auswahl["nv Seite 6 Thema 8"] = nvimg68
    nvalid68_tmp = st.session_state.reload_counter % 2
    if nvalid68_tmp == 0:
        st.image(nvtmp68[st.session_state.auswahl.get("nv Seite 6 Thema 8", 0)] if nvalid68_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp68[st.session_state.auswahl.get("nv Seite 6 Thema 8", 0)] if nvalid68_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page7":
    st.title("Seite 7")

    pdf_url = "https://www.dropbox.com/scl/fi/mrrevzli8cfw2terg9wog/O1A1-GE.pdf?rlkey=d6wylmg2esc9ljvngsxkwwu7c&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Equip educators and enthusiasts with essential knowledge about diverse 3D print technologies and best practices for optimizing designs for Fused Deposition Modeling (FDM).')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Overview of 3D Printing Techniques\n- Defines key terminology associated with 3D printing, including additive manufacturing, rapid prototyping, and various 3D printing methods.')

    tmp71 = [
        "https://www.dropbox.com/scl/fi/wc3zvjrfulqrvtjubvlg3/Section1_Bild0.png?rlkey=n0iljtptzu2ha6f5417lbqz4d&dl=1",
        "https://www.dropbox.com/scl/fi/o03ihopuwp657gflr6kf7/Section1_Bild6.png?rlkey=ypq1vquq76lq0r4koai94p69s&dl=1",
        "https://www.dropbox.com/scl/fi/j0iwluowulc8h8v4uafr9/Section1_Bild5.png?rlkey=vg7v9um79auua6eq9et7plzib&dl=1",
        "https://www.dropbox.com/scl/fi/25lakun5ztlm346ckussg/Section1_Bild7.png?rlkey=ih13aozc5b5819w7xqpl03dfe&dl=1",
        "https://www.dropbox.com/scl/fi/75tvtkat4488nakavod9v/Section1_Bild10.png?rlkey=4dxn76ojc0yrl7t6ec3ulgb41&dl=1",
        "https://www.dropbox.com/scl/fi/p4wd9ryuybwkox4i39lev/Section1_Bild8.png?rlkey=axqzvdpoyk0esf2h8q6o9y1ak&dl=1",
    ]
    img71 = image_select(
        "Mögliche Valide Bilder:",
        tmp71,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 1", 0),
        key=f"frage71_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 7 Thema 1"] = img71
    valid71_tmp = st.session_state.reload_counter % 2
    if valid71_tmp == 0:
        st.image(tmp71[st.session_state.auswahl.get("Seite 7 Thema 1", 0)] if valid71_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp71[st.session_state.auswahl.get("Seite 7 Thema 1", 0)] if valid71_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp71 = [
        "https://www.dropbox.com/scl/fi/1480z9faad0eiqgocr32k/Section1_Bild2.png?rlkey=sl3r4u9zrw716tuujuik9dasg&dl=1",
        "https://www.dropbox.com/scl/fi/kuhjt15lom9goptorns1v/Section1_Bild9.png?rlkey=6wbxxg8xsdm8yrsjpe9pde2mg&dl=1",
        "https://www.dropbox.com/scl/fi/2zqyv0rr7fadc42qcdrex/Section1_Bild11.png?rlkey=vwjzu62ug9dlxal0123jgtqho&dl=1",
        "https://www.dropbox.com/scl/fi/oxk1eyeaetzbpuzbsb7zn/Section1_Bild4.png?rlkey=b84ghr4w3v4sjdbsucmkug2ss&dl=1",
        "https://www.dropbox.com/scl/fi/x4o8qkjzwevk3hy41xth8/Section1_Bild1.png?rlkey=578for6jgo1le0f6n80dwvfo4&dl=1",
        "https://www.dropbox.com/scl/fi/j21ds50vsywl3bjux4p5u/Section1_Bild3.png?rlkey=4nw1rakecc1lf96j5hb8q4dp3&dl=1",
    ]
    nvimg71 = image_select(
        "Nicht Valide Bilder:",
        nvtmp71,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 1", 0),
        key=f"nvfrage71_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg71} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 1"] = nvimg71
    nvalid71_tmp = st.session_state.reload_counter % 2
    if nvalid71_tmp == 0:
        st.image(nvtmp71[st.session_state.auswahl.get("nv Seite 7 Thema 1", 0)] if nvalid71_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp71[st.session_state.auswahl.get("nv Seite 7 Thema 1", 0)] if nvalid71_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Comparative Analysis of Popular 3D Print Technologies\n- Evaluates seven frequently utilized 3D print technologies across factors like speed, cost, material choices, accuracy, intricacy, support structure requirements, and post-production necessities.\n\n')
    choice72_arr = [
        "https://www.dropbox.com/scl/fi/6eofwfjh1ny68oxljp7uw/Section2_choice.png?rlkey=6nicmj04ocqm4cysltf5votbd&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice72_tmp = st.session_state.reload_counter % 2
    if choice72_tmp == 0:
        st.image(choice72_arr[0 if choice72_tmp == 0 else 1])
    else:
        st.image(choice72_arr[0 if choice72_tmp == 1 else 1])
    st.text(' The image is a table comparing various 3D printing technologies, detailing their process, materials, complexity, speed, size, accuracy, surface finish, strengths, weaknesses, pricing, and application examples.')

    tmp72 = [
        "https://www.dropbox.com/scl/fi/s4hq3bgfjmbm2xj6s9bgn/Section2_Bild0.png?rlkey=1a3jq2s58syr7p73hu1hhw0bg&dl=1",
        "https://www.dropbox.com/scl/fi/hn70dokhzofuj3eolfhak/Section2_Bild5.png?rlkey=ixf5un5elj9mk4zyh5366733c&dl=1",
    ]
    img72 = image_select(
        "Mögliche Valide Bilder:",
        tmp72,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 2", 0),
        key=f"frage72_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 7 Thema 2"] = img72
    valid72_tmp = st.session_state.reload_counter % 2
    if valid72_tmp == 0:
        st.image(tmp72[st.session_state.auswahl.get("Seite 7 Thema 2", 0)] if valid72_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp72[st.session_state.auswahl.get("Seite 7 Thema 2", 0)] if valid72_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp72 = [
        "https://www.dropbox.com/scl/fi/gbkzrxyjifg4ibcg11cvl/Section2_Bild1.png?rlkey=tptm57320px7uhy3qiwtcmsdn&dl=1",
        "https://www.dropbox.com/scl/fi/pihhd4an6zcdwfmjqcyjw/Section2_Bild3.png?rlkey=yssg12r5w4mqc90yujz5pqxir&dl=1",
        "https://www.dropbox.com/scl/fi/on3rao4xl5no52zv6eg6x/Section2_Bild11.png?rlkey=j8ei2j5a2lfdrd14vlgbomb4w&dl=1",
        "https://www.dropbox.com/scl/fi/dx6xat5cgwzqcilp2hvqp/Section2_Bild2.png?rlkey=8l8wc67chq42e99tt5f9kxrk8&dl=1",
        "https://www.dropbox.com/scl/fi/lv3rasduxjzwtwalr18xh/Section2_Bild8.png?rlkey=50fncbdju6b5r1eszjin1v88k&dl=1",
        "https://www.dropbox.com/scl/fi/g6n027pzxek4p79mdc1ny/Section2_Bild6.png?rlkey=39eztlru0yugty8qar0di2e1h&dl=1",
        "https://www.dropbox.com/scl/fi/hxqyyvn6fzs6lghx6u1la/Section2_Bild4.png?rlkey=13wgji1efe32ttx3fivemx3lo&dl=1",
        "https://www.dropbox.com/scl/fi/jerrt9jz343ahsfz01ggu/Section2_Bild10.png?rlkey=whj9kag15ln80kk5yviptztks&dl=1",
        "https://www.dropbox.com/scl/fi/ksc3cf99fvqopq3eobmg7/Section2_Bild7.png?rlkey=f9q03ov2u0r8uee3colc4l510&dl=1",
        "https://www.dropbox.com/scl/fi/1dgujc3udo7xo1pnqdu53/Section2_Bild9.png?rlkey=suhxu08umerlnvzj1vy73jgjf&dl=1",
    ]
    nvimg72 = image_select(
        "Nicht Valide Bilder:",
        nvtmp72,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 2", 0),
        key=f"nvfrage72_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg72} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 2"] = nvimg72
    nvalid72_tmp = st.session_state.reload_counter % 2
    if nvalid72_tmp == 0:
        st.image(nvtmp72[st.session_state.auswahl.get("nv Seite 7 Thema 2", 0)] if nvalid72_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp72[st.session_state.auswahl.get("nv Seite 7 Thema 2", 0)] if nvalid72_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Fundamentals of Fused Deposition Modeling (FDM) Technology\n- Details the operating principles, materials, applications, merits, demerits, and practicality of FDM technology, renowned for its accessibility and user-friendliness.\n\n')
    choice73_arr = [
        "https://www.dropbox.com/scl/fi/5m70p0z2el0fj8hiwcrwp/Section3_choice.png?rlkey=q5jca3hdf2v6ruiuci7zrkdc1&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice73_tmp = st.session_state.reload_counter % 2
    if choice73_tmp == 0:
        st.image(choice73_arr[0 if choice73_tmp == 0 else 1])
    else:
        st.image(choice73_arr[0 if choice73_tmp == 1 else 1])
    st.text(' The image is a diagram illustrating a 3D printing process, showing a feed mechanism, filament, print head with a nozzle, a partially printed object in the shape of a capital "H" with support structures, and a lowerable print table.')

    tmp73 = [
        "https://www.dropbox.com/scl/fi/veyb90istsn0qrucjh5hx/Section3_Bild5.png?rlkey=gxjtu8zcv0cxgny54rg1dubys&dl=1",
        "https://www.dropbox.com/scl/fi/8brjvzuu9679hzje8i91h/Section3_Bild0.png?rlkey=5feowpnokhcn0u90z2zrkt73v&dl=1",
    ]
    img73 = image_select(
        "Mögliche Valide Bilder:",
        tmp73,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 3", 0),
        key=f"frage73_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 7 Thema 3"] = img73
    valid73_tmp = st.session_state.reload_counter % 2
    if valid73_tmp == 0:
        st.image(tmp73[st.session_state.auswahl.get("Seite 7 Thema 3", 0)] if valid73_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp73[st.session_state.auswahl.get("Seite 7 Thema 3", 0)] if valid73_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp73 = [
        "https://www.dropbox.com/scl/fi/tlhmv2ttcunyg57stvyuh/Section3_Bild9.png?rlkey=3uft56j3skyf3exjxsxkdv94f&dl=1",
        "https://www.dropbox.com/scl/fi/512fezflgsezniixkjr2j/Section3_Bild1.png?rlkey=acgkx24so8wz5jha3qoixbsq0&dl=1",
        "https://www.dropbox.com/scl/fi/0yhmac2k9ccioit7tijr2/Section3_Bild4.png?rlkey=2l7oxgo4vs2o782oi4i1p8hdg&dl=1",
        "https://www.dropbox.com/scl/fi/p9pbbkh4k73ioxib7qz8j/Section3_Bild6.png?rlkey=0i9d0ds4sbmv2cepan17guaea&dl=1",
        "https://www.dropbox.com/scl/fi/xqn38j7a46r1ne0acj7sz/Section3_Bild7.png?rlkey=c6o1gycvxiqpbjfgh9vtak3o6&dl=1",
        "https://www.dropbox.com/scl/fi/9n2p9j1r5b5qv16xej5hs/Section3_Bild2.png?rlkey=06p58h08589qd5z8mcikam00x&dl=1",
        "https://www.dropbox.com/scl/fi/5kalyyt2urm6a7l9wbchp/Section3_Bild10.png?rlkey=msfx7gte43ylyvfzaimh9f32c&dl=1",
        "https://www.dropbox.com/scl/fi/4ogqrhfozobuxcbdrsxrr/Section3_Bild8.png?rlkey=1gl6ky7f91kbvt8y5rvm67w2a&dl=1",
        "https://www.dropbox.com/scl/fi/ienm28g8hengb9ewphn80/Section3_Bild11.png?rlkey=g6eserl2muy12ry9zq7z419fd&dl=1",
        "https://www.dropbox.com/scl/fi/f1oykei02s8ar042fhtmh/Section3_Bild3.png?rlkey=y5v6coiet4ozjigff60lbxeqz&dl=1",
    ]
    nvimg73 = image_select(
        "Nicht Valide Bilder:",
        nvtmp73,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 3", 0),
        key=f"nvfrage73_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg73} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 3"] = nvimg73
    nvalid73_tmp = st.session_state.reload_counter % 2
    if nvalid73_tmp == 0:
        st.image(nvtmp73[st.session_state.auswahl.get("nv Seite 7 Thema 3", 0)] if nvalid73_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp73[st.session_state.auswahl.get("nv Seite 7 Thema 3", 0)] if nvalid73_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Enhancing Quality & Minimizing Challenges in FDM 3D Printing\n- Addresses typical difficulties like warping effects, layer separation, vertical pin failures, and solutions for reducing these issues through strategic design modifications.\n\n')
    choice74_arr = [
        "https://www.dropbox.com/scl/fi/9rfzi8s7qgsvyy0hk1xqr/Section4_choice.png?rlkey=0pdametj4ngz8pd60ndaxufzf&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice74_tmp = st.session_state.reload_counter % 2
    if choice74_tmp == 0:
        st.image(choice74_arr[0 if choice74_tmp == 0 else 1])
    else:
        st.image(choice74_arr[0 if choice74_tmp == 1 else 1])
    st.text(' A small, white, 3D-printed model of a seashell with a spiraled top sits on a white surface.')

    tmp74 = [
        "https://www.dropbox.com/scl/fi/dlvfh0h0twoer1vcekrqf/Section4_Bild6.png?rlkey=aaib5aocyaxrfjftkgr41sihc&dl=1",
        "https://www.dropbox.com/scl/fi/6i4b3wetiev35jjiooe12/Section4_Bild0.png?rlkey=ve6yjrp0gegptfmrm92eblqz7&dl=1",
    ]
    img74 = image_select(
        "Mögliche Valide Bilder:",
        tmp74,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 4", 0),
        key=f"frage74_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 7 Thema 4"] = img74
    valid74_tmp = st.session_state.reload_counter % 2
    if valid74_tmp == 0:
        st.image(tmp74[st.session_state.auswahl.get("Seite 7 Thema 4", 0)] if valid74_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp74[st.session_state.auswahl.get("Seite 7 Thema 4", 0)] if valid74_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp74 = [
        "https://www.dropbox.com/scl/fi/ovbtohdxtm5c577j82uzg/Section4_Bild3.png?rlkey=8e90ljv6kxl414a71y9dyy0nv&dl=1",
        "https://www.dropbox.com/scl/fi/vsqeln0jh774zhobns4uy/Section4_Bild2.png?rlkey=6g4hiuehbvk9s2iaj33s9usdm&dl=1",
        "https://www.dropbox.com/scl/fi/sqywgltwx4knsyycvse1s/Section4_Bild9.png?rlkey=b1l3bvecl7awu7j92q4urwpu3&dl=1",
        "https://www.dropbox.com/scl/fi/ld5l4l6vunnt9ttmv9l9l/Section4_Bild8.png?rlkey=3tffa53bi5hdqiafai36btdng&dl=1",
        "https://www.dropbox.com/scl/fi/31mozqzi3f9gc6e5lrgb3/Section4_Bild4.png?rlkey=lrxonz0zlykagttxhj5dtexya&dl=1",
        "https://www.dropbox.com/scl/fi/0wrbyqig3drjn9va4tqax/Section4_Bild7.png?rlkey=tlm104ttetomimcr7i6w3odzf&dl=1",
        "https://www.dropbox.com/scl/fi/j9bsyn5r0m3128bpk5wq7/Section4_Bild1.png?rlkey=2ecblddgcsujff1u63cyc04g2&dl=1",
        "https://www.dropbox.com/scl/fi/dyvqxpw2uoxn5oaocmai2/Section4_Bild5.png?rlkey=1dpvz455qt0ygtzutz6dyk6wz&dl=1",
    ]
    nvimg74 = image_select(
        "Nicht Valide Bilder:",
        nvtmp74,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 4", 0),
        key=f"nvfrage74_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg74} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 4"] = nvimg74
    nvalid74_tmp = st.session_state.reload_counter % 2
    if nvalid74_tmp == 0:
        st.image(nvtmp74[st.session_state.auswahl.get("nv Seite 7 Thema 4", 0)] if nvalid74_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp74[st.session_state.auswahl.get("nv Seite 7 Thema 4", 0)] if nvalid74_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Optimized Design Approaches for FDM Production\n- Proposes advanced methodologies such as splitting models, altering orientations, defining manufacturing directions, and implementing specific design elements to streamline processes, boost efficiency, strengthen prints, and maintain superior quality.\n\n')
    choice75_arr = [
        "https://www.dropbox.com/scl/fi/86gtwyjc3z7knvjyvclv9/Section5_choice.png?rlkey=qo0s2jtnniybv03xe6rpp5qcj&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice75_tmp = st.session_state.reload_counter % 2
    if choice75_tmp == 0:
        st.image(choice75_arr[0 if choice75_tmp == 0 else 1])
    else:
        st.image(choice75_arr[0 if choice75_tmp == 1 else 1])
    st.text(' The image shows a diagram of multiple parallel, curved layers stacked on top of each other, with rounded edges and notches at the layer boundaries.')

    tmp75 = [
        "https://www.dropbox.com/scl/fi/rm12785m3ntllxmwmjn81/Section5_Bild9.png?rlkey=vum1rjqbethqv4cedxqy23f3u&dl=1",
        "https://www.dropbox.com/scl/fi/se6msqwrjgbkccylu03kz/Section5_Bild8.png?rlkey=o4y15lm0w66sluv8we7oom8yc&dl=1",
        "https://www.dropbox.com/scl/fi/xyz761uw7sfk05epg0uu4/Section5_Bild1.png?rlkey=pn9vilfbbqh7vri9qc01g77ww&dl=1",
        "https://www.dropbox.com/scl/fi/cso6xox4aei4zewaemrym/Section5_Bild3.png?rlkey=y3skowd6cyiakihn9tnfnigyf&dl=1",
    ]
    img75 = image_select(
        "Mögliche Valide Bilder:",
        tmp75,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 7 Thema 5", 0),
        key=f"frage75_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 7 Thema 5"] = img75
    valid75_tmp = st.session_state.reload_counter % 2
    if valid75_tmp == 0:
        st.image(tmp75[st.session_state.auswahl.get("Seite 7 Thema 5", 0)] if valid75_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp75[st.session_state.auswahl.get("Seite 7 Thema 5", 0)] if valid75_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp75 = [
        "https://www.dropbox.com/scl/fi/b1v9fd7mtjvhguco1ukib/Section5_Bild11.png?rlkey=bohnsnp2ea3j6lvukvdr1onyl&dl=1",
        "https://www.dropbox.com/scl/fi/3r6s7x7pfyxgifl3wai1n/Section5_Bild5.png?rlkey=nz1rq4r5wabhtwek0l5pcr0l6&dl=1",
        "https://www.dropbox.com/scl/fi/6wwz45uaxtk953r6ntz3y/Section5_Bild0.png?rlkey=683m0sjd0iduutoueh7t683yj&dl=1",
        "https://www.dropbox.com/scl/fi/e059njoefl4x0506h2vyr/Section5_Bild2.png?rlkey=agogfy4wr4iatzm6alk6lcsv1&dl=1",
        "https://www.dropbox.com/scl/fi/7h6cibbsift9wyxcvlbo3/Section5_Bild7.png?rlkey=i4fobcsv2o6qvnh7kqyifs6gg&dl=1",
        "https://www.dropbox.com/scl/fi/bux15022binwms2dk9s14/Section5_Bild4.png?rlkey=7sim12sr4y13joan3l2eug8xn&dl=1",
        "https://www.dropbox.com/scl/fi/499w7de691msd72mwau9x/Section5_Bild6.png?rlkey=bpam5yn335cil1h962t614bet&dl=1",
        "https://www.dropbox.com/scl/fi/7xvsq6xtyvroi8975oab0/Section5_Bild10.png?rlkey=pj1njn3pge6zxgkbc849ssw6z&dl=1",
    ]
    nvimg75 = image_select(
        "Nicht Valide Bilder:",
        nvtmp75,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 7 Thema 5", 0),
        key=f"nvfrage75_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg75} ausgewählt.")
    st.session_state.auswahl["nv Seite 7 Thema 5"] = nvimg75
    nvalid75_tmp = st.session_state.reload_counter % 2
    if nvalid75_tmp == 0:
        st.image(nvtmp75[st.session_state.auswahl.get("nv Seite 7 Thema 5", 0)] if nvalid75_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp75[st.session_state.auswahl.get("nv Seite 7 Thema 5", 0)] if nvalid75_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page8":
    st.title("Seite 8")

    pdf_url = "https://www.dropbox.com/scl/fi/rlhxra16921mb2h6h0jui/MuM_Band_14.pdf?rlkey=x2tv604tprsnysghlhuvgx714&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Understand the roles and interactions of symbiotic algae, Weichkorallen, and coral reefs, as well as factors impacting their health and global conservation efforts.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: Symbiosis Between Corals and Zooxanthellae\n- Overview of the beneficial partnership between certain corals and microscopic algae known as zooxanthellae.\n\n')
    choice81_arr = [
        "https://www.dropbox.com/scl/fi/yaxsx67yyr5hcxxqmbos8/Section1_choice.png?rlkey=trgp57skw58p7sv3qo97wp79x&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice81_tmp = st.session_state.reload_counter % 2
    if choice81_tmp == 0:
        st.image(choice81_arr[0 if choice81_tmp == 0 else 1])
    else:
        st.image(choice81_arr[0 if choice81_tmp == 1 else 1])
    st.text(' The image is a black and white diagram showing a scale from 0 to 1200 on the left and a scale from 0 to 40cm on the right, with various fungal names listed vertically along the right side.')

    tmp81 = [
        "https://www.dropbox.com/scl/fi/1d1dchqaug9cya8b4qfdv/Section1_Bild0.png?rlkey=2ym55cyx0o30wjb8yb0w0tle6&dl=1",
        "https://www.dropbox.com/scl/fi/lorm0ozszkrlhp64gcp0n/Section1_Bild6.png?rlkey=u8rtqnw3i8y21cm6odbng5did&dl=1",
        "https://www.dropbox.com/scl/fi/oydjeh239q3c1kr7b3wee/Section1_Bild9.png?rlkey=uwl2qlgg7y17anv21a7yu1yd7&dl=1",
        "https://www.dropbox.com/scl/fi/w6gb1o4oqrbwwm1fmrj6l/Section1_Bild11.png?rlkey=esaxchemg5hmi0jhbof0zxorl&dl=1",
        "https://www.dropbox.com/scl/fi/db7y27bjw9p8iqklskehi/Section1_Bild4.png?rlkey=e0mbm2bcigq484stnlierdq12&dl=1",
        "https://www.dropbox.com/scl/fi/3hu36tz6aos6d4nkl3pwy/Section1_Bild8.png?rlkey=cxpojyvvf9smylulw7i23tsbw&dl=1",
    ]
    img81 = image_select(
        "Mögliche Valide Bilder:",
        tmp81,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 1", 0),
        key=f"frage81_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 8 Thema 1"] = img81
    valid81_tmp = st.session_state.reload_counter % 2
    if valid81_tmp == 0:
        st.image(tmp81[st.session_state.auswahl.get("Seite 8 Thema 1", 0)] if valid81_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp81[st.session_state.auswahl.get("Seite 8 Thema 1", 0)] if valid81_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp81 = [
        "https://www.dropbox.com/scl/fi/zn7i9z7xg54x60ebp9as6/Section1_Bild2.png?rlkey=j4vfumuq97n1ttlgjh614v92z&dl=1",
        "https://www.dropbox.com/scl/fi/ei65zqd4xrcs98rmp6pnc/Section1_Bild5.png?rlkey=ud12rlaq7879jcf2hdehtmk1r&dl=1",
        "https://www.dropbox.com/scl/fi/pepnp1br8ih6nj3ghhgb3/Section1_Bild7.png?rlkey=a2vh23pv281l8u9egy5yv7tfv&dl=1",
        "https://www.dropbox.com/scl/fi/ez788i7l1ykxkx0m5dtpb/Section1_Bild10.png?rlkey=gpvaup4iltr7cg2o4906q0fqi&dl=1",
        "https://www.dropbox.com/scl/fi/8aw9m2i4zuh1t1p0lohb0/Section1_Bild1.png?rlkey=ysiq4xd8deobnkadbmyksp4so&dl=1",
        "https://www.dropbox.com/scl/fi/xbjvgqttlee5zhhmkanl8/Section1_Bild3.png?rlkey=ap7j6065ia8eogorejdkbgwz4&dl=1",
    ]
    nvimg81 = image_select(
        "Nicht Valide Bilder:",
        nvtmp81,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 1", 0),
        key=f"nvfrage81_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg81} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 1"] = nvimg81
    nvalid81_tmp = st.session_state.reload_counter % 2
    if nvalid81_tmp == 0:
        st.image(nvtmp81[st.session_state.auswahl.get("nv Seite 8 Thema 1", 0)] if nvalid81_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp81[st.session_state.auswahl.get("nv Seite 8 Thema 1", 0)] if nvalid81_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Functions and Niches of Weichkorallen Within Tropical Coral Communities\n- Description of diverse shapes, capabilities, light requirements, and locations occupied by Weichkorallen.\n\n')
    choice82_arr = [
        "https://www.dropbox.com/scl/fi/e16wya6cbzz0vrbhqigol/Section2_choice.png?rlkey=fo70mvsn1eu8eivxjm5bg0dmo&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice82_tmp = st.session_state.reload_counter % 2
    if choice82_tmp == 0:
        st.image(choice82_arr[0 if choice82_tmp == 0 else 1])
    else:
        st.image(choice82_arr[0 if choice82_tmp == 1 else 1])
    st.text(' The image shows three separate photographs: a close-up of a vibrant red coral structure, a black and white microscopic image of several elongated, textured objects, a grayscale image of a rounded cell-like structure, and a detailed illustration of a cross-section with red accents.')

    tmp82 = [
        "https://www.dropbox.com/scl/fi/lfdw2ztwkeses012doo9u/Section2_Bild1.png?rlkey=scgy4fpidkru7rwrczunoom0x&dl=1",
        "https://www.dropbox.com/scl/fi/5o38webvio917f9qcctxl/Section2_Bild0.png?rlkey=8nw6sh8mfm4g05kl6aarv0ho1&dl=1",
        "https://www.dropbox.com/scl/fi/wc32z47fj0zg8et6ge3ee/Section2_Bild6.png?rlkey=ddtt9boxzivwor4smhdq9mnas&dl=1",
        "https://www.dropbox.com/scl/fi/8faoqhst3f7n3wx1j9dj5/Section2_Bild4.png?rlkey=pvlhplbjo0zck2zil3imskt4u&dl=1",
        "https://www.dropbox.com/scl/fi/zu158x7pqlgvlxxv51a6l/Section2_Bild5.png?rlkey=f8hd855da4ywdzo7nbjob0w1i&dl=1",
        "https://www.dropbox.com/scl/fi/e9glswy3sis0ubs14cbt8/Section2_Bild7.png?rlkey=0n224w20c7iuin191urt6gr2g&dl=1",
        "https://www.dropbox.com/scl/fi/4zkl3ddepwwxbi43o96cy/Section2_Bild9.png?rlkey=kzkrjif5pmvnygjwr6pvbwavt&dl=1",
    ]
    img82 = image_select(
        "Mögliche Valide Bilder:",
        tmp82,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 2", 0),
        key=f"frage82_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 8 Thema 2"] = img82
    valid82_tmp = st.session_state.reload_counter % 2
    if valid82_tmp == 0:
        st.image(tmp82[st.session_state.auswahl.get("Seite 8 Thema 2", 0)] if valid82_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp82[st.session_state.auswahl.get("Seite 8 Thema 2", 0)] if valid82_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp82 = [
        "https://www.dropbox.com/scl/fi/11rmu1eulp2jr6x2s43dm/Section2_Bild3.png?rlkey=90n13f8uexvr7g4nototacvze&dl=1",
        "https://www.dropbox.com/scl/fi/s23eliwdwt2qzodq2rx6g/Section2_Bild2.png?rlkey=aiw5fmovwnh1to3it3tuv7q1j&dl=1",
        "https://www.dropbox.com/scl/fi/l101cp1v4z6bw42czlvpw/Section2_Bild8.png?rlkey=8vbeupkk2thfe5ryk1vag7pvw&dl=1",
        "https://www.dropbox.com/scl/fi/mz8un2vuqvduv05gs3per/Section2_Bild10.png?rlkey=1pnhjayvzf81qk4cunatj32aa&dl=1",
    ]
    nvimg82 = image_select(
        "Nicht Valide Bilder:",
        nvtmp82,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 2", 0),
        key=f"nvfrage82_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg82} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 2"] = nvimg82
    nvalid82_tmp = st.session_state.reload_counter % 2
    if nvalid82_tmp == 0:
        st.image(nvtmp82[st.session_state.auswahl.get("nv Seite 8 Thema 2", 0)] if nvalid82_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp82[st.session_state.auswahl.get("nv Seite 8 Thema 2", 0)] if nvalid82_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Influences on Relationships Amongst Corals, Zooxanthellae, and Other Organisms\n- Analysis of competition, predation, mutualism, and interdependencies amongst various inhabitants of coral reef systems.\n\n')
    choice83_arr = [
        "https://www.dropbox.com/scl/fi/gawb9gqyjuw2vwirvb8vw/Section3_choice.png?rlkey=86cn9p451nr2dpcp8h3n241vc&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice83_tmp = st.session_state.reload_counter % 2
    if choice83_tmp == 0:
        st.image(choice83_arr[0 if choice83_tmp == 0 else 1])
    else:
        st.image(choice83_arr[0 if choice83_tmp == 1 else 1])
    st.text(' The image shows two black and white electron micrographs labeled "a" and "b," depicting cellular structures with internal components and surrounding membranes.')

    tmp83 = [
        "https://www.dropbox.com/scl/fi/jtl6ohbzw05s3fh77kgww/Section3_Bild4.png?rlkey=fpwwosfolpu1hjwraymyf2uda&dl=1",
        "https://www.dropbox.com/scl/fi/6ikz4k64canka77a9cmkm/Section3_Bild7.png?rlkey=msluxrd48jz4952ao5su50pll&dl=1",
        "https://www.dropbox.com/scl/fi/ch3fvwoytyyzkl9x2gw5o/Section3_Bild8.png?rlkey=3iu24eaxc2id92q86oltb39yi&dl=1",
    ]
    img83 = image_select(
        "Mögliche Valide Bilder:",
        tmp83,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 3", 0),
        key=f"frage83_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 8 Thema 3"] = img83
    valid83_tmp = st.session_state.reload_counter % 2
    if valid83_tmp == 0:
        st.image(tmp83[st.session_state.auswahl.get("Seite 8 Thema 3", 0)] if valid83_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp83[st.session_state.auswahl.get("Seite 8 Thema 3", 0)] if valid83_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp83 = [
        "https://www.dropbox.com/scl/fi/7a027mcrsnckz32bpott5/Section3_Bild5.png?rlkey=r9lul39ybre6ifj3k3ou5m0bf&dl=1",
        "https://www.dropbox.com/scl/fi/45fnrothtdkmdmvb6skw4/Section3_Bild9.png?rlkey=j714md2ilcuf8pbjizpczajbj&dl=1",
        "https://www.dropbox.com/scl/fi/k9fcfgxnm42medevc708x/Section3_Bild1.png?rlkey=k3kg6w8kaei6hfamsr37mjgn8&dl=1",
        "https://www.dropbox.com/scl/fi/6eh9r8qquqzjlfigpmofd/Section3_Bild0.png?rlkey=padwbr1o6fvbvgo5tyoyl7it7&dl=1",
        "https://www.dropbox.com/scl/fi/finubgihzgujpc2fyeni3/Section3_Bild6.png?rlkey=vjnvvf993nwcbfkhcul7r1e7w&dl=1",
        "https://www.dropbox.com/scl/fi/dcfy8vifg9k5a0quc4mlu/Section3_Bild2.png?rlkey=ewt486d7620k0p8fdtvg7esn0&dl=1",
        "https://www.dropbox.com/scl/fi/57ny64mcgh3ih644zdzzk/Section3_Bild3.png?rlkey=omwgzi4mfful1d1c80mb93pib&dl=1",
    ]
    nvimg83 = image_select(
        "Nicht Valide Bilder:",
        nvtmp83,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 3", 0),
        key=f"nvfrage83_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg83} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 3"] = nvimg83
    nvalid83_tmp = st.session_state.reload_counter % 2
    if nvalid83_tmp == 0:
        st.image(nvtmp83[st.session_state.auswahl.get("nv Seite 8 Thema 3", 0)] if nvalid83_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp83[st.session_state.auswahl.get("nv Seite 8 Thema 3", 0)] if nvalid83_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Factors Affecting Health and Stability of Coral Reef Structures\n- Identifies key drivers behind changes in coral coverage, such as anthropogenic pressures and climactic shifts.')

    tmp84 = [
        "https://www.dropbox.com/scl/fi/pgzrqpffu8janok4wl04x/Section4_Bild3.png?rlkey=0o9rf1k68tv59phjfohu4csbh&dl=1",
        "https://www.dropbox.com/scl/fi/gnjd8017o1l5s3e76b1q3/Section4_Bild2.png?rlkey=kt0s2h95332d4vxvrcy4op07k&dl=1",
        "https://www.dropbox.com/scl/fi/rs68d6nevqz2z9jqk1pf6/Section4_Bild9.png?rlkey=6ok8rbv40rou5s26ive4brwpq&dl=1",
        "https://www.dropbox.com/scl/fi/3rzt2lfqojhip0iplranr/Section4_Bild1.png?rlkey=dqvf6c027cw43tjtt6wsvxusb&dl=1",
    ]
    img84 = image_select(
        "Mögliche Valide Bilder:",
        tmp84,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 4", 0),
        key=f"frage84_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 8 Thema 4"] = img84
    valid84_tmp = st.session_state.reload_counter % 2
    if valid84_tmp == 0:
        st.image(tmp84[st.session_state.auswahl.get("Seite 8 Thema 4", 0)] if valid84_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp84[st.session_state.auswahl.get("Seite 8 Thema 4", 0)] if valid84_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp84 = [
        "https://www.dropbox.com/scl/fi/q1607fbv4k2dc014nb73t/Section4_Bild6.png?rlkey=60rnbfpxxvw09rr8fi7wbqf1t&dl=1",
        "https://www.dropbox.com/scl/fi/nw5hcnifiaaz7pj322cdt/Section4_Bild10.png?rlkey=cluk4fqs76un6yn1n9zhq8u1m&dl=1",
        "https://www.dropbox.com/scl/fi/j1zg986adazp7gr3u354i/Section4_Bild8.png?rlkey=wsxic2zu6j79xz4tgl0g5vkr6&dl=1",
        "https://www.dropbox.com/scl/fi/61yu4g93ajr17quuigxyu/Section4_Bild0.png?rlkey=475v3i7wxyy0ccr0xz92bnkxh&dl=1",
        "https://www.dropbox.com/scl/fi/ylm0t2vwfp1hah9r85z82/Section4_Bild4.png?rlkey=gbbw7snvpirgkm62et8cux3sl&dl=1",
        "https://www.dropbox.com/scl/fi/uqzpjiko7emvuz7kz3ats/Section4_Bild7.png?rlkey=7d7zfyx9ydz23v99dv39gyale&dl=1",
        "https://www.dropbox.com/scl/fi/xj9bpc5s63zexrsga4iro/Section4_Bild5.png?rlkey=gturqgdxweedlm2qrps12ocnz&dl=1",
    ]
    nvimg84 = image_select(
        "Nicht Valide Bilder:",
        nvtmp84,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 4", 0),
        key=f"nvfrage84_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg84} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 4"] = nvimg84
    nvalid84_tmp = st.session_state.reload_counter % 2
    if nvalid84_tmp == 0:
        st.image(nvtmp84[st.session_state.auswahl.get("nv Seite 8 Thema 4", 0)] if nvalid84_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp84[st.session_state.auswahl.get("nv Seite 8 Thema 4", 0)] if nvalid84_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Strategies for Sustaining Coral Reef Ecosystems\n- Review of approaches aimed at mitigating damage caused by human activities and restoring degraded reefs using innovative techniques.')

    tmp85 = [
        "https://www.dropbox.com/scl/fi/m4l3x96yhkr2lq01fr7se/Section5_Bild8.png?rlkey=2q66kujlcnhp8e95guf10a590&dl=1",
        "https://www.dropbox.com/scl/fi/zwozvy8eu23cigm37b646/Section5_Bild1.png?rlkey=0uzpvfoy87w43bs70lvoueznx&dl=1",
        "https://www.dropbox.com/scl/fi/yatbezge9qqvs67o05hpo/Section5_Bild6.png?rlkey=auuw108okxjvuhc8j0ifsuk1e&dl=1",
    ]
    img85 = image_select(
        "Mögliche Valide Bilder:",
        tmp85,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 8 Thema 5", 0),
        key=f"frage85_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 8 Thema 5"] = img85
    valid85_tmp = st.session_state.reload_counter % 2
    if valid85_tmp == 0:
        st.image(tmp85[st.session_state.auswahl.get("Seite 8 Thema 5", 0)] if valid85_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp85[st.session_state.auswahl.get("Seite 8 Thema 5", 0)] if valid85_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp85 = [
        "https://www.dropbox.com/scl/fi/akhzsg387nr59bszhn5gr/Section5_Bild9.png?rlkey=pf4m8ws6cdsp7o4ui1f1fzwfq&dl=1",
        "https://www.dropbox.com/scl/fi/hyixl2a0qhodf0ro7sfot/Section5_Bild5.png?rlkey=yp2verxi9e9oxpcvumx8v5rkb&dl=1",
        "https://www.dropbox.com/scl/fi/jlinwkdmgbj82a41eu3cs/Section5_Bild0.png?rlkey=3zcmhn9g9hx3ealsceyquk35h&dl=1",
        "https://www.dropbox.com/scl/fi/9nqip6pkj7vsl36z4ln7k/Section5_Bild2.png?rlkey=1sc4vvtw9dcge7xz9ssfurdko&dl=1",
        "https://www.dropbox.com/scl/fi/lesoz1cjjrb1or218lhqk/Section5_Bild7.png?rlkey=7rfinv6mo6qeqmu9wsxri0ncq&dl=1",
        "https://www.dropbox.com/scl/fi/fidwav71uwvodwnlnld6f/Section5_Bild4.png?rlkey=oghr3u3mitkea8xd0rrk7nsju&dl=1",
        "https://www.dropbox.com/scl/fi/2gkuiqc7uqz8oj24f02t4/Section5_Bild10.png?rlkey=m2f9k8rs5ezvywkkw77iu8b3b&dl=1",
        "https://www.dropbox.com/scl/fi/1h7ix66vybiwimaojedfq/Section5_Bild3.png?rlkey=owzyv2s11nah7zt3mwc1rn1so&dl=1",
    ]
    nvimg85 = image_select(
        "Nicht Valide Bilder:",
        nvtmp85,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 8 Thema 5", 0),
        key=f"nvfrage85_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg85} ausgewählt.")
    st.session_state.auswahl["nv Seite 8 Thema 5"] = nvimg85
    nvalid85_tmp = st.session_state.reload_counter % 2
    if nvalid85_tmp == 0:
        st.image(nvtmp85[st.session_state.auswahl.get("nv Seite 8 Thema 5", 0)] if nvalid85_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp85[st.session_state.auswahl.get("nv Seite 8 Thema 5", 0)] if nvalid85_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page9":
    st.title("Seite 9")

    pdf_url = "https://www.dropbox.com/scl/fi/09h74sa2i3n4ubpbyngxq/Probekapitel_Ernaehrungsberater_Ernaehrungslehre_ENB01-B.pdf?rlkey=mohgoul8qrdgsri3jhy0lp123&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: To provide foundational knowledge on general principles of nutrition science, including energy requirements, nutrient recommendations, and calculation methods for food analysis.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: General Concepts of Nutrition Science\n- Defines key terms related to nutrition and explains the role of various substances in human body functions.\n\n')
    choice91_arr = [
        "https://www.dropbox.com/scl/fi/ueo4006ph1tn716x1581h/Section1_choice.png?rlkey=a292lkrv5x0obyf1o39xxmcxu&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice91_tmp = st.session_state.reload_counter % 2
    if choice91_tmp == 0:
        st.image(choice91_arr[0 if choice91_tmp == 0 else 1])
    else:
        st.image(choice91_arr[0 if choice91_tmp == 1 else 1])
    st.text(" A close-up shot shows a person's hands holding a pen and writing on a white surface.")

    tmp91 = [
        "https://www.dropbox.com/scl/fi/0t43fke0nkqufmbnkgpqj/Section1_Bild2.png?rlkey=dzgzatcay4augx7yb7fw8hqmd&dl=1",
        "https://www.dropbox.com/scl/fi/pkjb1ajtxyffculwj15m1/Section1_Bild1.png?rlkey=60vd9pvfwbtffj8ob33v5p5xe&dl=1",
    ]
    img91 = image_select(
        "Mögliche Valide Bilder:",
        tmp91,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 9 Thema 1", 0),
        key=f"frage91_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 9 Thema 1"] = img91
    valid91_tmp = st.session_state.reload_counter % 2
    if valid91_tmp == 0:
        st.image(tmp91[st.session_state.auswahl.get("Seite 9 Thema 1", 0)] if valid91_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp91[st.session_state.auswahl.get("Seite 9 Thema 1", 0)] if valid91_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp91 = [
        "https://www.dropbox.com/scl/fi/js7fhoj5pkl03q9qkxmof/Section1_Bild0.png?rlkey=16dok0gxio2lr40498bkgruto&dl=1",
        "https://www.dropbox.com/scl/fi/f23ewdgvrxq2uvv74jg45/Section1_Bild3.png?rlkey=yv2hceh0a764k1g7ujiu32ugf&dl=1",
    ]
    nvimg91 = image_select(
        "Nicht Valide Bilder:",
        nvtmp91,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 9 Thema 1", 0),
        key=f"nvfrage91_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg91} ausgewählt.")
    st.session_state.auswahl["nv Seite 9 Thema 1"] = nvimg91
    nvalid91_tmp = st.session_state.reload_counter % 2
    if nvalid91_tmp == 0:
        st.image(nvtmp91[st.session_state.auswahl.get("nv Seite 9 Thema 1", 0)] if nvalid91_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp91[st.session_state.auswahl.get("nv Seite 9 Thema 1", 0)] if nvalid91_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Energy Requirement and Calculations\n- Details how energy is produced within cells through biological oxidation process and introduces two units used to measure energy intake (kilocalories and kilojules).')

    tmp92 = [
        "https://www.dropbox.com/scl/fi/4focanycble1cntt597sg/Section2_Bild1.png?rlkey=c9lp3pww8z26wwb7szos632vg&dl=1",
        "https://www.dropbox.com/scl/fi/ge6vaxm5g8rjk204kaspr/Section2_Bild2.png?rlkey=rf2v8xoyjcqp68qcloni0xci8&dl=1",
    ]
    img92 = image_select(
        "Mögliche Valide Bilder:",
        tmp92,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 9 Thema 2", 0),
        key=f"frage92_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 9 Thema 2"] = img92
    valid92_tmp = st.session_state.reload_counter % 2
    if valid92_tmp == 0:
        st.image(tmp92[st.session_state.auswahl.get("Seite 9 Thema 2", 0)] if valid92_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp92[st.session_state.auswahl.get("Seite 9 Thema 2", 0)] if valid92_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp92 = [
        "https://www.dropbox.com/scl/fi/56fmrh3jikoqzd4w9xn9v/Section2_Bild3.png?rlkey=g8f0ikvlpvcxcx3k1lpyad5uf&dl=1",
        "https://www.dropbox.com/scl/fi/57sdvft7lefji2v6os5ot/Section2_Bild0.png?rlkey=o8c55mybmrr05q864czrshgkn&dl=1",
    ]
    nvimg92 = image_select(
        "Nicht Valide Bilder:",
        nvtmp92,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 9 Thema 2", 0),
        key=f"nvfrage92_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg92} ausgewählt.")
    st.session_state.auswahl["nv Seite 9 Thema 2"] = nvimg92
    nvalid92_tmp = st.session_state.reload_counter % 2
    if nvalid92_tmp == 0:
        st.image(nvtmp92[st.session_state.auswahl.get("nv Seite 9 Thema 2", 0)] if nvalid92_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp92[st.session_state.auswahl.get("nv Seite 9 Thema 2", 0)] if nvalid92_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Basic Composition of Foods\n- Outlines the three primary sources of dietary energy—carbohydrates, proteins, and lipids—with corresponding caloric values per gram.')

    tmp93 = [
        "https://www.dropbox.com/scl/fi/7yogbf45plm6nqowx3x08/Section3_Bild1.png?rlkey=w6bwqx013v5d571u1asaq23p5&dl=1",
        "https://www.dropbox.com/scl/fi/ko7u78t6hqmz1o4thvpl0/Section3_Bild2.png?rlkey=s4r83o9bqlhv1dsdivltbz13i&dl=1",
    ]
    img93 = image_select(
        "Mögliche Valide Bilder:",
        tmp93,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 9 Thema 3", 0),
        key=f"frage93_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 9 Thema 3"] = img93
    valid93_tmp = st.session_state.reload_counter % 2
    if valid93_tmp == 0:
        st.image(tmp93[st.session_state.auswahl.get("Seite 9 Thema 3", 0)] if valid93_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp93[st.session_state.auswahl.get("Seite 9 Thema 3", 0)] if valid93_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp93 = [
        "https://www.dropbox.com/scl/fi/p4kt8ruiany6dtwe1ni1o/Section3_Bild0.png?rlkey=d09s4i4x68zsm8ot74x7cwbyq&dl=1",
        "https://www.dropbox.com/scl/fi/q4w0pvjqndsx8cz0uuonf/Section3_Bild3.png?rlkey=o5knp92x2piry602cqc4qz234&dl=1",
    ]
    nvimg93 = image_select(
        "Nicht Valide Bilder:",
        nvtmp93,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 9 Thema 3", 0),
        key=f"nvfrage93_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg93} ausgewählt.")
    st.session_state.auswahl["nv Seite 9 Thema 3"] = nvimg93
    nvalid93_tmp = st.session_state.reload_counter % 2
    if nvalid93_tmp == 0:
        st.image(nvtmp93[st.session_state.auswahl.get("nv Seite 9 Thema 3", 0)] if nvalid93_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp93[st.session_state.auswahl.get("nv Seite 9 Thema 3", 0)] if nvalid93_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Determining Daily Energy and Nutrient Needs\n- Presents calculations for estimating daily energy needs based on basal metabolism rate and activity level, along with recommended percentages of calories derived from carbohydrates, protein, and fat.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Methodology for Assessing Food Content\n- Demonstrates techniques for determining the amount of essential nutrients present in foods via simple calculations utilizing known caloric and nutrient contents per unit weight.\n\n')
    choice95_arr = [
        "https://www.dropbox.com/scl/fi/xlyv8xo44rz9tda9l9yrs/Section5_choice.png?rlkey=b0wrysd651onio4buwdfjp3nx&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice95_tmp = st.session_state.reload_counter % 2
    if choice95_tmp == 0:
        st.image(choice95_arr[0 if choice95_tmp == 0 else 1])
    else:
        st.image(choice95_arr[0 if choice95_tmp == 1 else 1])
    st.text(" A close-up shot shows a person's hands holding a pen and writing on a white surface.")

    tmp95 = [
        "https://www.dropbox.com/scl/fi/wpm2ixk7ve5jtv6b3jwk1/Section5_Bild1.png?rlkey=25ybwfjnljejn6vdx363h7kou&dl=1",
        "https://www.dropbox.com/scl/fi/yx0wgv590qq028998tvqo/Section5_Bild2.png?rlkey=da3o9f38sfgi3sjrhoskq1s9a&dl=1",
    ]
    img95 = image_select(
        "Mögliche Valide Bilder:",
        tmp95,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 9 Thema 5", 0),
        key=f"frage95_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 9 Thema 5"] = img95
    valid95_tmp = st.session_state.reload_counter % 2
    if valid95_tmp == 0:
        st.image(tmp95[st.session_state.auswahl.get("Seite 9 Thema 5", 0)] if valid95_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp95[st.session_state.auswahl.get("Seite 9 Thema 5", 0)] if valid95_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp95 = [
        "https://www.dropbox.com/scl/fi/41g1c7a8ahiapldoeilc2/Section5_Bild0.png?rlkey=bdt7uj4xjl9tol7ylwjl7jc9z&dl=1",
        "https://www.dropbox.com/scl/fi/slgz427pry0qqq029t3p3/Section5_Bild3.png?rlkey=1qy06yospadqqwiysg6ut7a58&dl=1",
    ]
    nvimg95 = image_select(
        "Nicht Valide Bilder:",
        nvtmp95,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 9 Thema 5", 0),
        key=f"nvfrage95_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg95} ausgewählt.")
    st.session_state.auswahl["nv Seite 9 Thema 5"] = nvimg95
    nvalid95_tmp = st.session_state.reload_counter % 2
    if nvalid95_tmp == 0:
        st.image(nvtmp95[st.session_state.auswahl.get("nv Seite 9 Thema 5", 0)] if nvalid95_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp95[st.session_state.auswahl.get("nv Seite 9 Thema 5", 0)] if nvalid95_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

if st.session_state.seite == "page10":
    st.title("Seite 10")

    pdf_url = "https://www.dropbox.com/scl/fi/x0ug7u457t0agaoh9gz2d/bdw_2022-006_96_Schwarze-Loecher-erschuettern-das-All.pdf?rlkey=ln77357z0hins7bialfdpbbfb&dl=0"
    st.text("Wenn die Bilder nicht angezeigt werden, bitte ca. 10 Sekunden warten und anschließend auf den Button „Neuladen“ klicken."
        "Wichtig: Nicht den Browser neu laden, da sonst alle bisherigen Auswahlen verloren gehen!")
    if st.button("Neuladen"):
        st.session_state.reload_counter += 1
        st.rerun()
    st.markdown(f'<a href="{pdf_url}" target="_blank">PDF anzeigen</a>', unsafe_allow_html=True)
    st.text('Goal: Describe recent discoveries made through the detection of gravitational waves caused by colliding black holes.')

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 1: First Direct Observation of Merged Black Holes\n- On May 21, 2019, scientists detected gravitational waves originating from the merger of two massive black holes approximately 8 billion light years away. This marked the first direct observation of this phenomenon.\n\n')
    choice101_arr = [
        "https://www.dropbox.com/scl/fi/73i9its0wtcfbj2nodtlv/Section1_choice.png?rlkey=ald5l08fkx9td24a12i6ept6r&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice101_tmp = st.session_state.reload_counter % 2
    if choice101_tmp == 0:
        st.image(choice101_arr[0 if choice101_tmp == 0 else 1])
    else:
        st.image(choice101_arr[0 if choice101_tmp == 1 else 1])
    st.text(' The image depicts two black holes surrounded by swirling blue light and a grid-like pattern against a backdrop of numerous stars.')

    tmp101 = [
        "https://www.dropbox.com/scl/fi/ivnnerv0b665kjym04zoc/Section1_Bild0.png?rlkey=etow49rztsgo0b4n0o8w6nbwn&dl=1",
        "https://www.dropbox.com/scl/fi/yzon7j8ms8yxxv4fmsn0k/Section1_Bild2.png?rlkey=svs5cue54jf42rw35lsgtbdac&dl=1",
        "https://www.dropbox.com/scl/fi/8o95xn80i8ts2t6ltl2c2/Section1_Bild5.png?rlkey=p0kd5fnrlvy4xq964ol1sjgs4&dl=1",
        "https://www.dropbox.com/scl/fi/fvvigaz594fr57ttmsl0e/Section1_Bild4.png?rlkey=4gefa4f3kk34rk1onp248gcsj&dl=1",
        "https://www.dropbox.com/scl/fi/ypf2bqvwab4ymncrqq5wt/Section1_Bild1.png?rlkey=d1ra0cbzz7h0jxeho2drm72mq&dl=1",
        "https://www.dropbox.com/scl/fi/tgkl0wi5ri1ic0gcc6w9t/Section1_Bild3.png?rlkey=yie6nb51qaiwrokrq8rbyktdn&dl=1",
    ]
    img101 = image_select(
        "Mögliche Valide Bilder:",
        tmp101,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 1", 0),
        key=f"frage101_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 10 Thema 1"] = img101
    valid101_tmp = st.session_state.reload_counter % 2
    if valid101_tmp == 0:
        st.image(tmp101[st.session_state.auswahl.get("Seite 10 Thema 1", 0)] if valid101_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp101[st.session_state.auswahl.get("Seite 10 Thema 1", 0)] if valid101_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 2: Properties of Detected Black Holes\n- The merged black hole had a combined mass equivalent to around three times that of our sun. One of its components was slightly more massive than the other. Both were spinning rapidly along the same axis as their orbital motion.\n\n')
    choice102_arr = [
        "https://www.dropbox.com/scl/fi/s3xodamwlgdctbh42b5k5/Section2_choice.png?rlkey=geit2i2apbkrfox31ulvh49wo&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice102_tmp = st.session_state.reload_counter % 2
    if choice102_tmp == 0:
        st.image(choice102_arr[0 if choice102_tmp == 0 else 1])
    else:
        st.image(choice102_arr[0 if choice102_tmp == 1 else 1])
    st.text(' The image depicts two black holes surrounded by swirling blue light and a grid-like pattern against a backdrop of numerous stars.')

    tmp102 = [
        "https://www.dropbox.com/scl/fi/a43nyfby05vbeeyk7a3mf/Section2_Bild3.png?rlkey=ll9cov0ph0ykczbulnrmxz6mf&dl=1",
        "https://www.dropbox.com/scl/fi/z4ho0jlbrlt56se8nkurd/Section2_Bild0.png?rlkey=rbo694vpjlarjm5b7mk8raa8o&dl=1",
        "https://www.dropbox.com/scl/fi/uk6tywra5xit195snphqd/Section2_Bild2.png?rlkey=iv33422t5ylzcw1lcds5ssyai&dl=1",
        "https://www.dropbox.com/scl/fi/8345vsppzjvkylwufg2qn/Section2_Bild9.png?rlkey=wxy8rwr7cno8acm5sog4tyutw&dl=1",
    ]
    img102 = image_select(
        "Mögliche Valide Bilder:",
        tmp102,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 2", 0),
        key=f"frage102_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 10 Thema 2"] = img102
    valid102_tmp = st.session_state.reload_counter % 2
    if valid102_tmp == 0:
        st.image(tmp102[st.session_state.auswahl.get("Seite 10 Thema 2", 0)] if valid102_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp102[st.session_state.auswahl.get("Seite 10 Thema 2", 0)] if valid102_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp102 = [
        "https://www.dropbox.com/scl/fi/f7kgxajon06523zb1vk9p/Section2_Bild1.png?rlkey=2jvbnignretjzjptim9cbyqwe&dl=1",
        "https://www.dropbox.com/scl/fi/9xl9m8taxfuhhcdxflfb4/Section2_Bild8.png?rlkey=l0l04hp9qsq1xjyw9ysmk321k&dl=1",
        "https://www.dropbox.com/scl/fi/ztwapgq7qdgnsx6tvtwtj/Section2_Bild6.png?rlkey=emgsluoe34uhm1duvg30704yc&dl=1",
        "https://www.dropbox.com/scl/fi/hruhgbwfvnysaemcoe4fu/Section2_Bild4.png?rlkey=qe9ay9bpswg9ds5seuxbn7793&dl=1",
        "https://www.dropbox.com/scl/fi/3boxdko7540k3itut2foi/Section2_Bild5.png?rlkey=4wv6i5kzbjrevukb2307z9d87&dl=1",
        "https://www.dropbox.com/scl/fi/jm6andqwc5crnfb9c90jc/Section2_Bild7.png?rlkey=zzuocvavp9omta6lnlg86tl2k&dl=1",
    ]
    nvimg102 = image_select(
        "Nicht Valide Bilder:",
        nvtmp102,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 2", 0),
        key=f"nvfrage102_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg102} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 2"] = nvimg102
    nvalid102_tmp = st.session_state.reload_counter % 2
    if nvalid102_tmp == 0:
        st.image(nvtmp102[st.session_state.auswahl.get("nv Seite 10 Thema 2", 0)] if nvalid102_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp102[st.session_state.auswahl.get("nv Seite 10 Thema 2", 0)] if nvalid102_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 3: Energy Emitted During Mergers\n- When these black holes merge, they emit energy primarily in the form of gravitational waves but also some electromagnetic radiation. Approximately four solar masses worth of energy was emitted during this event.')

    tmp103 = [
        "https://www.dropbox.com/scl/fi/cfvumyncseiqbyycj7kb2/Section3_Bild0.png?rlkey=8olh0v3ja3gz9cqsinz72nbi2&dl=1",
        "https://www.dropbox.com/scl/fi/o5uonszvzl4mvg3xz6o6d/Section3_Bild4.png?rlkey=28k5ua9yl6mwrqh3r01x530yl&dl=1",
        "https://www.dropbox.com/scl/fi/0zajo8ro9m34qlykv7hgs/Section3_Bild2.png?rlkey=cug0vs40mpu2kyxutgfhoeqlq&dl=1",
        "https://www.dropbox.com/scl/fi/3hqbubglljjha43qp2dvm/Section3_Bild3.png?rlkey=nrw0bw4f6iene2y5a539ffuih&dl=1",
    ]
    img103 = image_select(
        "Mögliche Valide Bilder:",
        tmp103,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 3", 0),
        key=f"frage103_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 10 Thema 3"] = img103
    valid103_tmp = st.session_state.reload_counter % 2
    if valid103_tmp == 0:
        st.image(tmp103[st.session_state.auswahl.get("Seite 10 Thema 3", 0)] if valid103_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp103[st.session_state.auswahl.get("Seite 10 Thema 3", 0)] if valid103_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp103 = [
        "https://www.dropbox.com/scl/fi/18579piapln1lvlsy32yj/Section3_Bild5.png?rlkey=yt709qv5ah2sswx87ars4wahu&dl=1",
        "https://www.dropbox.com/scl/fi/chl1rufspd8us0t1hm4dq/Section3_Bild9.png?rlkey=qqyx4ai7dmynhjsxkwlt129wj&dl=1",
        "https://www.dropbox.com/scl/fi/2hwwpydf6cewyrvvbkmp7/Section3_Bild1.png?rlkey=vwk8ui1ddz6k3o7tnhw7n17sa&dl=1",
        "https://www.dropbox.com/scl/fi/s6d6kngaftyegk8gukuwx/Section3_Bild6.png?rlkey=jpryotn4cdn3yyjom729gsusf&dl=1",
        "https://www.dropbox.com/scl/fi/gxq7pnvstprpm2bpjxkih/Section3_Bild7.png?rlkey=gobtjac4g6meow5t56fr16aoy&dl=1",
        "https://www.dropbox.com/scl/fi/zlngjkdmncornq90tmhil/Section3_Bild8.png?rlkey=jzurzss9xmwbzrp5s33sf40q7&dl=1",
    ]
    nvimg103 = image_select(
        "Nicht Valide Bilder:",
        nvtmp103,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 3", 0),
        key=f"nvfrage103_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg103} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 3"] = nvimg103
    nvalid103_tmp = st.session_state.reload_counter % 2
    if nvalid103_tmp == 0:
        st.image(nvtmp103[st.session_state.auswahl.get("nv Seite 10 Thema 3", 0)] if nvalid103_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp103[st.session_state.auswahl.get("nv Seite 10 Thema 3", 0)] if nvalid103_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 4: Impact on Understanding Black Hole Mergers\n- These observations provide valuable insights into how binary black hole systems evolve over time before coalescing and help refine theories regarding the formation of heavy elements like gold and platinum within stars.\n\n')
    choice104_arr = [
        "https://www.dropbox.com/scl/fi/0qn6ckb3ch1tqsh2tfy1d/Section4_choice.png?rlkey=x3qb4fw2nssj7esftnu5jsfby&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice104_tmp = st.session_state.reload_counter % 2
    if choice104_tmp == 0:
        st.image(choice104_arr[0 if choice104_tmp == 0 else 1])
    else:
        st.image(choice104_arr[0 if choice104_tmp == 1 else 1])
    st.text(' The image shows a scatter plot with orange dots plotted on a grid, labeled "weight alongside in 00s" and "bodyweight in kilograms."')

    tmp104 = [
        "https://www.dropbox.com/scl/fi/0u9v50pbltjragzlta55h/Section4_Bild3.png?rlkey=z0romi5t1l4389r3k3s6rmqpb&dl=1",
        "https://www.dropbox.com/scl/fi/e88pvvml75ypckd79dxbt/Section4_Bild2.png?rlkey=qtgt61lmvww9ubbxqace1ub3g&dl=1",
        "https://www.dropbox.com/scl/fi/my3ial14v3c4ze5wamcc9/Section4_Bild0.png?rlkey=do637qgaykulhoym42qahrf9l&dl=1",
        "https://www.dropbox.com/scl/fi/03y4aeld5axmxih38gwzg/Section4_Bild4.png?rlkey=dwg4nbx8qneuqzh2bmqiy0fx8&dl=1",
    ]
    img104 = image_select(
        "Mögliche Valide Bilder:",
        tmp104,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 4", 0),
        key=f"frage104_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 10 Thema 4"] = img104
    valid104_tmp = st.session_state.reload_counter % 2
    if valid104_tmp == 0:
        st.image(tmp104[st.session_state.auswahl.get("Seite 10 Thema 4", 0)] if valid104_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp104[st.session_state.auswahl.get("Seite 10 Thema 4", 0)] if valid104_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp104 = [
        "https://www.dropbox.com/scl/fi/2gjxcui0gfsob41i3bxbs/Section4_Bild6.png?rlkey=ib592th2x9hlhelqxpx2qgo9i&dl=1",
        "https://www.dropbox.com/scl/fi/neop0fr4v5r4yykex1qen/Section4_Bild9.png?rlkey=q03sscndoqyejchm55y1r05ia&dl=1",
        "https://www.dropbox.com/scl/fi/81s2o9izzaz2hm6x4gee4/Section4_Bild8.png?rlkey=s2sicmp9ge0jjlg8eysw8oumr&dl=1",
        "https://www.dropbox.com/scl/fi/vn098od72bc1bcfa9a7p2/Section4_Bild7.png?rlkey=c67p9ibfepbzeqz7frkrfnz16&dl=1",
        "https://www.dropbox.com/scl/fi/xxbhi47igkfu1cir221co/Section4_Bild1.png?rlkey=7axc1dz0e5tcrkik1au8n19wm&dl=1",
        "https://www.dropbox.com/scl/fi/6xlirn8hwgt76jifh9rb5/Section4_Bild5.png?rlkey=yvyudus1ywy6goi04mk8u61fl&dl=1",
    ]
    nvimg104 = image_select(
        "Nicht Valide Bilder:",
        nvtmp104,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 4", 0),
        key=f"nvfrage104_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg104} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 4"] = nvimg104
    nvalid104_tmp = st.session_state.reload_counter % 2
    if nvalid104_tmp == 0:
        st.image(nvtmp104[st.session_state.auswahl.get("nv Seite 10 Thema 4", 0)] if nvalid104_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp104[st.session_state.auswahl.get("nv Seite 10 Thema 4", 0)] if nvalid104_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("--------------------------------------------------------------------------------------------------------")
    st.text('Topic 5: Future Research Plans\n- Scientists are preparing for future observing runs with improved sensitivity levels which could lead to detecting even more black hole mergers at higher rates.\n\n')
    choice105_arr = [
        "https://www.dropbox.com/scl/fi/js7cqj0xhty72iy7fvexg/Section5_choice.png?rlkey=n77qiw3sz3s4r9rdply4769lg&dl=1",
        "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1",
    ]
    choice105_tmp = st.session_state.reload_counter % 2
    if choice105_tmp == 0:
        st.image(choice105_arr[0 if choice105_tmp == 0 else 1])
    else:
        st.image(choice105_arr[0 if choice105_tmp == 1 else 1])
    st.text(' The image is a scatter plot graph with data points clustered in three distinct regions labeled "Weakening," "Steady," and "Increasing," and with axes labeled "Weightloss in pounds" and "Weeks."')

    tmp105 = [
        "https://www.dropbox.com/scl/fi/xf6rw9eevedjlltv66u3m/Section5_Bild9.png?rlkey=i4igr881btq4jjaw5o5dcwpu6&dl=1",
        "https://www.dropbox.com/scl/fi/35d7c2g7784fz9exh4oxc/Section5_Bild5.png?rlkey=x517q4o7hbndlvexhef6zslsi&dl=1",
        "https://www.dropbox.com/scl/fi/z3yi6uelne2ct3qlryrdo/Section5_Bild8.png?rlkey=fge9t3eqwskltx5j3a8csxn81&dl=1",
        "https://www.dropbox.com/scl/fi/a48qo0cjmug1iv1y6lbou/Section5_Bild7.png?rlkey=dkmsyrodvnftb6554akfs47va&dl=1",
        "https://www.dropbox.com/scl/fi/qkv3gr24ecq7hpj9yru1d/Section5_Bild6.png?rlkey=ehk5g7282g2fvffazydfssm2u&dl=1",
    ]
    img105 = image_select(
        "Mögliche Valide Bilder:",
        tmp105,
        return_value="index",
        index=st.session_state.auswahl.get("Seite 10 Thema 5", 0),
        key=f"frage105_{st.session_state.reload_counter}"
    )
    st.session_state.auswahl["Seite 10 Thema 5"] = img105
    valid105_tmp = st.session_state.reload_counter % 2
    if valid105_tmp == 0:
        st.image(tmp105[st.session_state.auswahl.get("Seite 10 Thema 5", 0)] if valid105_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(tmp105[st.session_state.auswahl.get("Seite 10 Thema 5", 0)] if valid105_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

    st.text("Die folgenden Bilder wurden aussortiert. Falls du der Meinung bist, dass eines davon thematisch relevant ist, wähle es bitte aus.")

    nvtmp105 = [
        "https://www.dropbox.com/scl/fi/sh9btx8iz8g3kkpv2ufdt/Section5_Bild0.png?rlkey=fqg93uibd2ywp3s6wiypbc7r0&dl=1",
        "https://www.dropbox.com/scl/fi/2e4j6o2ezfyanmze1bko3/Section5_Bild1.png?rlkey=wlbox5d25z5mw4n3zrf0tegqo&dl=1",
        "https://www.dropbox.com/scl/fi/9uq1wm9h7v71drntwjssi/Section5_Bild2.png?rlkey=gac6emd5gfootwyr2x9wq9xwd&dl=1",
        "https://www.dropbox.com/scl/fi/w1sow8k7em7m294csf8ej/Section5_Bild4.png?rlkey=wxcsk45b70epcw2th50a670yk&dl=1",
        "https://www.dropbox.com/scl/fi/e980en2sva90ruvqkwgti/Section5_Bild3.png?rlkey=g6bmjx07x8h2k7rgefh1jau7r&dl=1",
    ]
    nvimg105 = image_select(
        "Nicht Valide Bilder:",
        nvtmp105,
        return_value="index",
        index=st.session_state.auswahl.get("nv Seite 10 Thema 5", 0),
        key=f"nvfrage105_{st.session_state.reload_counter}"
    )
    st.write(f"Du hast Bild Nr. {nvimg105} ausgewählt.")
    st.session_state.auswahl["nv Seite 10 Thema 5"] = nvimg105
    nvalid105_tmp = st.session_state.reload_counter % 2
    if nvalid105_tmp == 0:
        st.image(nvtmp105[st.session_state.auswahl.get("nv Seite 10 Thema 5", 0)] if nvalid105_tmp == 0 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")
    else:
        st.image(nvtmp105[st.session_state.auswahl.get("nv Seite 10 Thema 5", 0)] if nvalid105_tmp == 1 else "https://www.dropbox.com/scl/fi/8zxrgtciju3a5s6g6re94/bad-sets-komponenten-keine-auswahl.jpg?rlkey=ij0j741l44g5o6p4wz2y8gy0l&dl=1")

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

    st.button("Nach oben scrollen", on_click=scroll)

