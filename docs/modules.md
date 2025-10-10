# Module Breakdown

## `capture.py`
- Captures screen using `pyautogui`
- Returns image buffer for OCR

## `ocr.py`
- Converts image to text using `pytesseract`
- Includes preprocessing hooks (e.g. grayscale, thresholding)

## `voiceover.py` *(planned)*
- Converts extracted text to voice
- Will support local TTS and voice cloning

## `utils.py`
- Shared helpers: logging, bounding boxes, config parsing