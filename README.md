# README.md

# Game Text-to-VoiceOver AI

Modular pipeline for capturing, extracting, and narrating in-game note text—designed for immersive accessibility and blind playthroughs.

## 🎯 Purpose

This project enables blind or visually impaired players to experience narrative-driven games by extracting in-game note text and converting it to voice. Built with modular isolation, visual calibration, and privacy-first principles.

## 🧩 Features

- 🖼️ Visual Calibration: Red-box overlay confirms OCR region alignment  
- 📐 Region Isolation: Crops out UI controls using `params.py`  
- 🧠 OCR Extraction: Clean text from game notes using Tesseract  
- 🗂️ Modular Design: Each step is independently testable and documented  
- 🔒 Privacy-First: All processing is local; no cloud dependencies  
- 🧪 Test Scripts: Validate calibration and OCR with PowerShell delay  
- 📦 Configurable: Resolution and region stored in `params.py`  
- 🗣️ Voice Synthesis (coming soon): Narrate extracted text for immersion  

## 📁 Structure

Game-Text-To-VoiceOver-AI/  
├── src/  
│   ├── capture.py         → Active window capture  
│   ├── ocr.py             → Region crop + OCR  
│   ├── params.py          → Resolution + region config  
│   ├── utils.py           → Logging + preprocessing  
├── tests/  
│   ├── calibrate_region.py  → Visual overlay for OCR region  
│   ├── ocr_test.py          → Full OCR pipeline test  
│   └── output/              → Calibration images (ignored by Git)  
├── docs/  
│   ├── architecture.md  
│   ├── modules.md  
│   ├── setup.md  
│   ├── privacy.md  
│   ├── roadmap.md  
│   └── changelog.md  
├── .gitignore  
└── README.md  

## ⚙️ Configuration

params.py example:  
resolution = { "width": 1920, "height": 1080 }  
ocr_region = {  
 "upper_left": { "x": 100, "y": 100 },  
 "lower_right": { "x": 1820, "y": 900 }  
}

## 🧪 Testing

Visual Calibration:  
Start-Sleep -Seconds 5; py -3.10 tests/calibrate_region.py

OCR Extraction:  
Start-Sleep -Seconds 5; py -3.10 tests/ocr_test.py

## 📚 Documentation

- [Architecture](docs/architecture.md)  
- [Modules](docs/modules.md)  
- [Setup Guide](docs/setup.md)  
- [Privacy Principles](docs/privacy.md)  
- [Roadmap](docs/roadmap.md)  
- [Changelog](docs/changelog.md)