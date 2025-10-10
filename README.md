# 🎮 Game Text-to-VoiceOver AI

Modular, privacy-first pipeline for capturing, extracting, and narrating in-game note text—designed for immersive accessibility and blind playthroughs.

## 🎯 Purpose

This project enables blind or visually impaired players to experience narrative-driven games by extracting in-game note text and converting it to voice. Built for modular clarity, forensic traceability, and full local control—no cloud dependencies, no hidden steps.

## 🧩 Features

- 🖼️ Visual Calibration: Overlay OCR zones directly on the active game window with `-calibrate`
- 📐 Region Isolation: Crops only the narrative zones, excluding UI clutter
- 🧠 OCR Extraction: Uses Tesseract to extract clean, readable text from game notes
- 🗣️ Voice Synthesis: Narrates extracted text using pyttsx3 with configurable rate, volume, and voice
- 🗂️ Modular Design: Each step—capture, OCR, voice—is independently testable and traceable
- 🔒 Privacy-First: All processing is local; no cloud APIs or external data sharing
- ⚙️ Unified Configuration: All settings (resolution, regions, voice, transcription) live in `src/config.py`
- 🧪 Test Harnesses: Lightweight scripts for OCR and voice validation
- 🧾 Daily Logging: Optional transcription logging to timestamped `.txt` files

## 📦 Installation

Requirements:
- Python 3.10+
- Tesseract OCR installed and added to PATH
- pip packages:
  - pyttsx3
  - pillow
  - pyautogui
  - pygetwindow
  - pytesseract

Optional (Windows only):
- PowerShell for timed test execution
- Tesseract installer: https://github.com/tesseract-ocr/tesseract

## ⚙️ Configuration

All settings are stored in `src/config.py`:

Resolution:
- width: 1920
- height: 1080

OCR Regions:
- Title:
  - upper_left: x=1035, y=110
  - lower_right: x=1700, y=168
- Main:
  - upper_left: x=1035, y=170
  - lower_right: x=1700, y=900

Voice Settings:
- save_voice_to_file: False
- rate: 180
- volume: 1.0
- voice_id: None

Transcription Settings:
- save_transcription_to_file: False

You can adjust coordinates, voice settings, and logging behavior without touching any core logic.

## 🚀 Usage

Run narration pipeline:
- python game_narrate.py

Run calibration overlay:
- python game_narrate.py -calibrate

This will draw red and blue boxes over the `"Main"` and `"Title"` OCR zones and save a screenshot to `assets/calibration/zone_calibration.png`.

## 🧪 Testing

OCR Extraction:
- Start-Sleep -Seconds 5; py -3.10 tests/ocr_test.py

Voice Synthesis:
- Start-Sleep -Seconds 5; py -3.10 tests/voice_test.py

## 📁 Project Structure
```
Game-Text-To-VoiceOver-AI/
├── src/
│   ├── capture.py         → Active window capture
│   ├── ocr.py             → Region crop + OCR
│   ├── voice.py           → Voice synthesis
│   ├── utils.py           → Logging + preprocessing
│   ├── config.py          → Unified settings and regions
├── tests/
│   ├── ocr_test.py        → OCR pipeline test
│   └── voice_test.py      → Voice synthesis test
├── assets/
│   ├── scripts/           → Daily transcription logs
│   ├── VOs/               → Saved voice files
│   └── calibration/       → OCR zone overlays
├── docs/
│   ├── architecture.md
│   ├── modules.md
│   ├── setup.md
│   ├── privacy.md
│   ├── roadmap.md
│   └── changelog.md
├── .gitignore
└── README.md
```
## 📚 Documentation

- Architecture → docs/architecture.md
- Modules → docs/modules.md
- Setup Guide → docs/setup.md
- Privacy Principles → docs/privacy.md
- Roadmap → docs/roadmap.md
- Changelog → docs/changelog.md

## 🛡️ Privacy & Philosophy

This project is built for forensic-grade accessibility:
- No cloud APIs
- No telemetry
- No hidden dependencies
- Every step is modular, inspectable, and overrideable

Perfect for blind playthroughs, immersive narration, and traceable pipelines.