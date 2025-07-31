# Dieses Skript lädt PDF-Dateien aus dem Common Crawl herunter, um sie für die Evaluation des Text-Zusammenfassungsmodells zu verwenden.

import os
from warcio.archiveiterator import ArchiveIterator
from langdetect import detect
import fitz
import io

# Optional: Vorbereitungsschritte (Kommentiert für spätere Ausführung in z. B. Colab)
"""
# 1. Lade Liste mit WARC-Pfaden herunter (enthält Speicherorte der WARC-Dateien):
!wget https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-13/warc.paths.gz
!gunzip -f warc.paths.gz

# 2. Lade den ersten verfügbaren WARC-Pfad:
!head -n 1 warc.paths
with open("warc.paths", "r") as f:
    first_path = f.readline().strip()

# 3. Lade die eigentliche WARC-Datei:
!wget https://data.commoncrawl.org/{first_path}
filename = first_path.split("/")[-1]
print(filename)

# 4. Installiere benötigte Python-Bibliotheken:
!pip install warcio
!pip install langdetect
!pip install PyMuPDF
"""

filename = "CC-MAIN-20250315031626-20250315061626-00000.warc.gz"  # Beispiel-WARC-Datei
pdf_counter = 0  # Zähler für gefundene PDF-Dateien
max_pdfs = 25  # Maximal zu speichernde PDFs

output_folder = "/content/test"  # Zielordner für gefundene PDFs
os.makedirs(output_folder, exist_ok=True)  # Ordner ggf. erstellen

def pdf_is_english_and_has_images(binary_pdf_data):
    """
    Prüft, ob die gegebene PDF-Datei (als Binärdaten) englischen oder deutschen Text enthält
    und mindestens ein eingebettetes Bild hat.
    """
    try:
        # Temporäre Speicherung des PDF zur Analyse mit PyMuPDF
        with open("temp.pdf", "wb") as temp_file:
            temp_file.write(binary_pdf_data)

        doc = fitz.open("temp.pdf")
        
        # Alle Texte der Seiten zusammenfügen und Sprache erkennen
        full_text = "".join(page.get_text() for page in doc)
        is_english = detect(full_text) in ["en", "de"]

        # (optional) Prüfe, ob irgendeine Seite Bilder enthält
        has_images = any(len(page.get_images(full=True)) > 0 for page in doc)

        return is_english and has_images

    except Exception as e:
        print("Fehler bei Analyse:", e)
        return False

# Hauptlogik zum Durchsuchen der WARC-Datei
with open(filename, "rb") as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type != "response":
            continue  # Nur HTTP-Antworten sind interessant

        # Extrahiere URL und Content-Type (Dateityp)
        url = record.rec_headers.get_header("WARC-Target-URI")
        content_type = record.http_headers.get_header("Content-Type") if record.http_headers else None

        if content_type and "application/pdf" in content_type:
            binary_pdf = record.content_stream().read()

            # PDF wird nur gespeichert, wenn sie Text enthält und englisch/deutsch ist
            if pdf_is_english_and_has_images(binary_pdf):
                pdf_counter += 1
                save_path = os.path.join(output_folder, f"Pdf_nr_{pdf_counter}.pdf")
                print(f"PDF erfüllt Kriterien: {url} → {save_path}")

                with open(save_path, "wb") as f:
                    f.write(binary_pdf)

                # Maximalanzahl erreicht → Schleife abbrechen
                if pdf_counter >= max_pdfs:
                    break
