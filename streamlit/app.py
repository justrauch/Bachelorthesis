import streamlit as st
import pandas as pd
from streamlit_image_select import image_select

if "seite" not in st.session_state:
    st.session_state.seite = "page1"

def wechsel_zu(seite):
    st.session_state.seite = seite

if st.session_state.seite == "page1":
    st.title("Frage 1")

    st.text("Nachfolgend werden verschiedene beschreibungen von Pdfs angezeigt jede beschreibung besteht aus mehreren themen zu jedem thema werden verschiedene bilder ausgewählt gib hier an welches der bilder am besten zum jeweiligen thema passt in dem du auf dieses bild klickst falls keins der bilder passt wähle einfach die option keins passt.")

    st.text("Ziel: Eine Übersicht über die Entstehung, Struktur und bewegtes Leben im Sonnensystem sowie die Sammlung astronomischer Bilder und Daten bieten.")
    st.text("Thema 1: Entstehung des Universums und Sonnensystems\n- Erläutert die Entstehung des Urknalls und dessen Auswirkungen auf die Entstehung des Sonnensystems.")
    img = image_select(
        "Label", 
            [
                "https://www.dropbox.com/scl/fi/86dbzicfc4l6geixozny0/bad-sets-komponenten-keine-auswahl.jpg?rlkey=94py7cb4rho3ekpnx900n1zey&st=gp3i0mjv&dl=1",
                "https://www.dropbox.com/scl/fi/40yyg0pn60aqchts1enez/bild.png?rlkey=aeaymdsip9h9w7tn1acl32wya&e=1&st=80fysykr&dl=1", 
                "https://www.dropbox.com/scl/fi/wae1tzeks97bcwvsomt6r/Screenshot-2025-05-20-142258.png?rlkey=vjj5hic482xxuy6gozk3lt9ew&st=v43zqxsd&dl=1",
                "https://www.dropbox.com/scl/fi/50rclb268fd23zphoem93/flugzeug1.png?rlkey=32x1t1v7cve2ta5udwcjpga47&st=dshc7r5f&dl=1",
                "https://www.dropbox.com/scl/fi/c002p8dw2zgj6antyn421/affe1.png?rlkey=hwlaiiew7d3dyhz9mjthw8ux6&st=fguch6dn&dl=1",
                "https://www.dropbox.com/scl/fi/liwobvie562gr5lsrq8he/affe2.png?rlkey=1qnt9c5jhm4rghcilkl27pu73&st=eblbq82p&dl=1",
                "https://www.dropbox.com/scl/fi/heqrvnpeng74xaefz4het/affe3.png?rlkey=5ls7h70cii5dd3jn52jzp02f9&st=rob2y38g&dl=1",
                "https://www.dropbox.com/scl/fi/h0xvnzf4wifwdwmyur7li/Apfel-scaled.jpeg?rlkey=6o7gq1ztx29rm24jwborc9mnt&st=iunduxbi&dl=1",
                "https://www.dropbox.com/scl/fi/rvlrevp5uainih3b02td2/innenstadt1.png?rlkey=esh4ngkp6puaxozm3kvqg4sx7&st=14l3y2kk&dl=1",
            ],
        return_value="index",
        index=0,
        key="frage1"
    )

    st.write(f"Du hast Bild Nr. {img} ausgewählt.")

    st.session_state.auswahl1 = img

    st.button("Weiter zu Frage 2", on_click=lambda: wechsel_zu("page2"))

if st.session_state.seite == "page2":
    st.title("Frage 2")

    st.text("Nachfolgend werden verschiedene beschreibungen von Pdfs angezeigt jede beschreibung besteht aus mehreren themen zu jedem thema werden verschiedene bilder ausgewählt gib hier an welches der bilder am besten zum jeweiligen thema passt in dem du auf dieses bild klickst falls keins der bilder passt wähle einfach die option keins passt.")

    st.text("Ziel: Eine Übersicht über die Entstehung, Struktur und bewegtes Leben im Sonnensystem sowie die Sammlung astronomischer Bilder und Daten bieten.")
    st.text("Thema 1: Entstehung des Universums und Sonnensystems\n- Erläutert die Entstehung des Urknalls und dessen Auswirkungen auf die Entstehung des Sonnensystems.")
    img21 = image_select(
        "Label", 
            [
                "https://www.dropbox.com/scl/fi/86dbzicfc4l6geixozny0/bad-sets-komponenten-keine-auswahl.jpg?rlkey=94py7cb4rho3ekpnx900n1zey&st=gp3i0mjv&dl=1",
                "https://www.dropbox.com/scl/fi/40yyg0pn60aqchts1enez/bild.png?rlkey=aeaymdsip9h9w7tn1acl32wya&e=1&st=80fysykr&dl=1", 
                "https://www.dropbox.com/scl/fi/wae1tzeks97bcwvsomt6r/Screenshot-2025-05-20-142258.png?rlkey=vjj5hic482xxuy6gozk3lt9ew&st=v43zqxsd&dl=1",
                "https://www.dropbox.com/scl/fi/50rclb268fd23zphoem93/flugzeug1.png?rlkey=32x1t1v7cve2ta5udwcjpga47&st=dshc7r5f&dl=1",
                "https://www.dropbox.com/scl/fi/c002p8dw2zgj6antyn421/affe1.png?rlkey=hwlaiiew7d3dyhz9mjthw8ux6&st=fguch6dn&dl=1",
                "https://www.dropbox.com/scl/fi/liwobvie562gr5lsrq8he/affe2.png?rlkey=1qnt9c5jhm4rghcilkl27pu73&st=eblbq82p&dl=1",
                "https://www.dropbox.com/scl/fi/heqrvnpeng74xaefz4het/affe3.png?rlkey=5ls7h70cii5dd3jn52jzp02f9&st=rob2y38g&dl=1",
                "https://www.dropbox.com/scl/fi/h0xvnzf4wifwdwmyur7li/Apfel-scaled.jpeg?rlkey=6o7gq1ztx29rm24jwborc9mnt&st=iunduxbi&dl=1",
                "https://www.dropbox.com/scl/fi/rvlrevp5uainih3b02td2/innenstadt1.png?rlkey=esh4ngkp6puaxozm3kvqg4sx7&st=14l3y2kk&dl=1",
            ],
        return_value="index",
        index=0,
        key="frage21"
    )

    st.write(f"Du hast Bild Nr. {img21} ausgewählt.")

    st.text("Thema 2: Entstehung des Universums und Sonnensystems\n- Erläutert die Entstehung des Urknalls und dessen Auswirkungen auf die Entstehung des Sonnensystems.")
    img22 = image_select(
        "Label", 
            [
                "https://www.dropbox.com/scl/fi/86dbzicfc4l6geixozny0/bad-sets-komponenten-keine-auswahl.jpg?rlkey=94py7cb4rho3ekpnx900n1zey&st=gp3i0mjv&dl=1",
                "https://www.dropbox.com/scl/fi/40yyg0pn60aqchts1enez/bild.png?rlkey=aeaymdsip9h9w7tn1acl32wya&e=1&st=80fysykr&dl=1", 
                "https://www.dropbox.com/scl/fi/wae1tzeks97bcwvsomt6r/Screenshot-2025-05-20-142258.png?rlkey=vjj5hic482xxuy6gozk3lt9ew&st=v43zqxsd&dl=1",
                "https://www.dropbox.com/scl/fi/50rclb268fd23zphoem93/flugzeug1.png?rlkey=32x1t1v7cve2ta5udwcjpga47&st=dshc7r5f&dl=1",
                "https://www.dropbox.com/scl/fi/c002p8dw2zgj6antyn421/affe1.png?rlkey=hwlaiiew7d3dyhz9mjthw8ux6&st=fguch6dn&dl=1",
                "https://www.dropbox.com/scl/fi/liwobvie562gr5lsrq8he/affe2.png?rlkey=1qnt9c5jhm4rghcilkl27pu73&st=eblbq82p&dl=1",
                "https://www.dropbox.com/scl/fi/heqrvnpeng74xaefz4het/affe3.png?rlkey=5ls7h70cii5dd3jn52jzp02f9&st=rob2y38g&dl=1",
                "https://www.dropbox.com/scl/fi/h0xvnzf4wifwdwmyur7li/Apfel-scaled.jpeg?rlkey=6o7gq1ztx29rm24jwborc9mnt&st=iunduxbi&dl=1",
                "https://www.dropbox.com/scl/fi/rvlrevp5uainih3b02td2/innenstadt1.png?rlkey=esh4ngkp6puaxozm3kvqg4sx7&st=14l3y2kk&dl=1",
            ],
        return_value="index",
        index=0,
        key="frage22"
    )

    st.write(f"Du hast Bild Nr. {img22} ausgewählt.")

    st.session_state.auswahl2 = f"Frage 21: {img21} Frage 22: {img22}"

    st.button("Weiter zu Auswertung", on_click=lambda: wechsel_zu("auswertung"))

# === AUSWERTUNG ===
elif st.session_state.seite == "auswertung":
    st.title("🔍 Auswertung")
    st.write("Du hast dieses Bild gewählt:")

    st.write(f"Deine Auswahl für Frage 1: {st.session_state.auswahl1}.")
    st.write(f"Deine Auswahl für Frage 2: {st.session_state.auswahl2}.")
    st.button("Änderen", on_click=lambda: wechsel_zu("page1"))
