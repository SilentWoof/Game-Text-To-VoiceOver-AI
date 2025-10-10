# Setup Guide

## 🧰 Requirements

- Python 3.10 or higher  
- Tesseract OCR installed and added to system PATH  
- Required Python packages: Pillow, pytesseract, pyttsx3, pywin32, pyautogui  

## 📦 Installation

1. Clone the repository  
2. Run: pip install -r requirements.txt  
3. Verify Tesseract is installed by running: tesseract --version  
4. Configure OCR region in src/capture_config.py  
   - Use tests/calibrate_region.py to preview and align the red-box overlay  
   - Coordinates will auto-scale based on screen resolution  
5. Configure voice settings in src/voice_config.py  
   - Adjust rate, volume, and optional voice_id  
   - Toggle .wav file saving via save_voice_to_file: True or False  

## 🧪 Testing

Visual Calibration  
Start-Sleep -Seconds 5; py -3.10 tests/calibrate_region.py  
Displays red-box overlay to confirm OCR region alignment.

OCR Extraction  
Start-Sleep -Seconds 5; py -3.10 tests/ocr_test.py  
Captures active window, extracts text, and prints to console.

Voice Synthesis  
py -3.10 tests/voice_test.py  
Narrates sample text aloud and optionally saves .wav file.

## 🚀 Run Full Pipeline

py -3.10 game_narrate.py  
Captures active window → extracts text → narrates aloud → saves voice file (if enabled).