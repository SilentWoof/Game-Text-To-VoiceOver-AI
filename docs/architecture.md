# Architecture Overview

## Modules

- `capture.py`: Captures screen using `pyautogui`, returns image buffer
- `ocr.py`: Converts image to text using `pytesseract`
- `voiceover.py`: (Planned) Converts extracted text to voice
- `utils.py`: Shared functions—logging, preprocessing, bounding boxes

## Flow

1. `capture.py` → screenshot
2. `ocr.py` → extract text
3. `voiceover.py` → narrate (future)