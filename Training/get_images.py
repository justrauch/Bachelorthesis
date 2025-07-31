# Extrahiere alle Bilder aus allen PDFs der Testmenge und speichere sie im Ordner 'sample'
# zur späteren Weiterverarbeitung (z. B. durch ein Klassifizierungsmodell).

import zipfile
import pymupdf
import io
import os
from PIL import Image

# Pfad zur ZIP-Datei mit den PDF-Testdaten
zip_path = "../Bsp.zip"

# Zielverzeichnis, in das die extrahierten Bilder gespeichert werden
output_dir = "./sample"
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    pdf_files = [f for f in zip_ref.namelist() if f.endswith('.pdf')]

    for idx, pdf_file in enumerate(pdf_files):
        with zip_ref.open(pdf_file) as file:
            pdf_bytes = file.read()

            # Öffne die PDF direkt aus dem Speicher
            doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")

            # Gehe Seite für Seite durch das PDF-Dokument
            for page_index in range(len(doc)):
                page = doc[page_index]

                # Hole alle eingebetteten Bilder auf der Seite
                images = page.get_images(full=True)

                # Extrahiere jedes Bild
                for img_index, img in enumerate(images):
                    xref = img[0]  # Bildreferenz-ID
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]

                    # Erzeuge ein PIL-Image-Objekt aus dem Byte-Inhalt
                    image = Image.open(io.BytesIO(image_bytes))

                    # Speichere das Bild mit eindeutiger Benennung
                    filename = f"file{idx}_page{page_index + 1}_image{img_index + 1}.{image_ext}"
                    image.save(os.path.join(output_dir, filename))
