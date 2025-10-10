# Game-Text-To-VoiceOver-AI

A modular pipeline to automatically extract in-game text and narrate it using voice synthesis—designed for blind playthroughs, immersive commentary, and accessibility.

## 🔧 Features

- Screen capture using `pyautogui`
- OCR via `pytesseract` and Tesseract engine
- Modular design for future voice cloning integration
- Fully offline, privacy-respecting architecture

## 📦 Requirements

See [`requirements.txt`](requirements.txt) for dependencies.

## 🚀 Getting Started

1. Install Python 3.10+
2. Install Tesseract OCR engine (Windows: [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki))
3. Install dependencies:

    py -3.10 -m pip install -r requirements.txt

4. Run the OCR test script:

    py -3.10 tests/ocr_test.py

## 📁 Repo Structure

See [`docs/architecture.md`](docs/architecture.md) for module breakdown.

## 🛡️ Privacy

No cloud calls. No telemetry. See [`docs/privacy.md`](docs/privacy.md).

## 🗺️ Roadmap

Planned features and milestones are tracked in [`docs/roadmap.md`](docs/roadmap.md).