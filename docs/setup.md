# Setup Guide

## 🧰 Requirements

- Python 3.10 or higher  
- Tesseract OCR installed and added to system PATH  
- Required Python packages:
  - pyttsx3
  - pillow
  - pyautogui
  - pygetwindow
  - pytesseract

## 📦 Installation

1. Clone the repository  
2. Run: pip install -r requirements.txt  
3. Verify Tesseract is installed by running: tesseract --version  
4. Configure resolution and OCR regions in src/config.py  
   - Use `python game_narrate.py -calibrate` to preview and align the red/blue overlay  
   - Coordinates are resolution-aware and editable in `ocr_regions`  
5. Configure voice and transcription settings in src/config.py  
   - Adjust rate, volume, and optional voice_id  
   - Toggle .wav file saving via `save_voice_to_file: True` or `False`  
   - Enable daily text logging via `save_transcription_to_file: True`  

## 🧪 Testing

OCR Extraction  
- Start-Sleep -Seconds 5; py -3.10 tests/ocr_test.py  
- Captures active window, extracts text from "Main" region, and prints to console  

Voice Synthesis  
- py -3.10 tests/voice_test.py  
- Narrates sample text aloud (file saving disabled by default)  

## 🖼️ Visual Calibration

- py -3.10 game_narrate.py -calibrate  
- Displays red and blue overlays for "Main" and "Title" OCR zones  
- Saves preview to assets/calibration/zone_calibration.png  

## 🚀 Run Full Pipeline

- py -3.10 game_narrate.py  
- Captures active window → extracts "Title" and "Main" text → narrates "Main"  
- Optionally logs transcription and saves voice file based on config settings  