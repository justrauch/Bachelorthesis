# Mit diesem Skript kann man für eine Liste von Bildern jeweils eine Kantenbild-Version erzeugen,
# in der nur die Kanten des Bildes sichtbar sind:
# - Weiße Pixel = erkannte Kanten
# - Schwarze Pixel = keine Kanten

import cv2
import numpy as np

# Liste mit Pfaden zu den zu analysierenden Bildern
image_paths = [
    "../Training/sample_sorted/realistic/file3_page15_image1.png"
]

# Durchlaufe alle Bilder in der Liste
for idx, input_path in enumerate(image_paths):
    image = cv2.imread(input_path)

    if image is None:
        print(f"Bild konnte nicht geladen werden: {input_path}")
        continue

    # Umwandlung in Graustufen für die Kantenerkennung
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny-Algorithmus zur Kantenerkennung
    edges = cv2.Canny(gray, 25, 125)  # 25 = unterer Schwellenwert, 125 = oberer Schwellenwert

    # Zählt Anzahl weißer Pixel (Kanten)
    edge_count = np.sum(edges > 0)
    print(f"Kanten-Anzahl für {input_path}: {edge_count}")

    # Speichert das erzeugte Kantenbild unter dem folgenden Pfad
    output_path = f'canny_ergebnis_{idx + 1}.jpg'
    cv2.imwrite(output_path, edges)

    print(f'Canny-Bild wurde erfolgreich unter {output_path} gespeichert.')
