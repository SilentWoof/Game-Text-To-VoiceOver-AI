# docs/setup.md

# Setup Guide

## 🧰 Requirements

- Python 3.10+  
- Tesseract OCR installed and in PATH  
- Pillow, pytesseract, pywin32  

## 📦 Installation

1. Clone the repo  
2. Run `pip install -r requirements.txt`  
3. Edit `params.py` to match your resolution and region  

## 🧪 Testing

Visual Calibration:  
Start-Sleep -Seconds 5; py -3.10 tests/calibrate_region.py

OCR Extraction:  
Start-Sleep -Seconds 5; py -3.10 tests/ocr_test.py