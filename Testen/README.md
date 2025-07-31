# Bachelor Thesis – Test Scripts & Evaluation

This project contains all Python scripts for analyzing and optimizing the modules of this bachelor thesis.

---

## Requirements

### Install dependencies

pip install -r requirements.txt

Additionally required (Linux/WSL):

sudo apt install tesseract-ocr tesseract-ocr-deu
sudo apt install tesseract-ocr tesseract-ocr-rus

---

## Overview of Scripts

### Structure Check of the Text Summary

First download PDFs using:

\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\commoncrawl.py

Checks whether a generated text follows the required structure:
- A line starting with 'Goal:'
- Followed by ascendingly numbered 'Topic X:' blocks

Path:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\Section_test.py

---

### Text Length Analysis (OCR-based)

Analyzes the amount of text in images (e.g. tables, infographics) using OCR and creates a histogram.

Path:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\graph.py

Set in the file:
diagramm = 1

---

### Test Image Selection with Gemma

Tests whether the "Gemma" model selects the appropriate image for a given topic.

Path:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\image_select_test.py

---

### Sigmoid Optimization for Edge Filtering

Optimizes the parameters of the custom_sigmoid() function to better separate valid images from irrelevant ones (e.g. logos, QR codes).

Optimization script:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\sigmoid_opt.py

Visualize the curve with:

\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\graph.py

In graph.py:
diagramm = 0

---

### Canny Method (relative/absolute) and Model Testing

Tests image classification based on edge count (with and without normalization/sigmoid), for both approaches.

Path:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\canny_opt.py

---

### Visualization of Survey Results

Displays bar charts for the user survey results.

Path:
\\\\wsl.localhost\\Ubuntu-22.04\\home\\jstrauch\\bachelorthesis\\Bachelorthesis\\Testen\\graph.py

Setting:
diagramm = 2
