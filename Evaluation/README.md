# Bachelorarbeit – Test-Skripte & Evaluation

Dieses Projekt enthält alle Python-Skripte zur Analyse und Optimierung der Module dieser Bachelorarbeit.

---

## Voraussetzungen

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Zusätzlich erforderlich (Linux/WSL):

```bash
sudo apt install tesseract-ocr tesseract-ocr-deu
sudo apt install tesseract-ocr tesseract-ocr-rus
```

---

## Übersicht der Skripte

### Strukturprüfung der Textzusammenfassung

Zuerst PDFs herunterladen mit:

```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\commoncrawl.py
```

Überprüft, ob ein generierter Text der geforderten Struktur folgt:
- Eine Zeile beginnend mit 'Goal:'
- Gefolgt von aufsteigend nummerierten 'Topic X:' Blöcken

Pfad:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\Section_test.py
```

---

### Textlängen-Analyse (OCR-basiert)

Analysiert die Textmenge in Bildern (z. B. Tabellen, Infografiken) mithilfe von OCR und erstellt ein Histogramm.

Pfad:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\graph.py
```

Einstellung in der Datei:
```python
diagramm = 1
```

---

### Test Bildauswahl mit Gemma

Testet, ob das Modell "Gemma" das passende Bild für ein gegebenes Thema auswählt.

Pfad:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\image_select_test.py
```

---

### Sigmoid-Optimierung für Kantenfilterung

Optimiert die Parameter der Funktion `custom_sigmoid()`, um valide Bilder besser von irrelevanten zu trennen (z. B. Logos, QR-Codes).

Optimierungsskript:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\sigmoid_opt.py
```

Visualisierung der Kurve mit:

```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\graph.py
```

In `graph.py`:
```python
diagramm = 0
```

---

### Canny-Methode (relativ/absolut) und Modelltests

Testet die Bildklassifikation basierend auf Kantenzählung (mit und ohne Normalisierung/Sigmoid) für beide Ansätze.

Pfad:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\canny_opt.py
```

---

### Visualisierung der Umfrageergebnisse

Zeigt Balkendiagramme für die Ergebnisse der Nutzerumfrage.

Pfad:
```
\\wsl.localhost\Ubuntu-22.04\home\jstrauch\bachelorthesis\Bachelorthesis\Testen\graph.py
```

Einstellung:
```python
diagramm = 2
```
