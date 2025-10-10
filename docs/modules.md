# Module Breakdown

## src/

- `capture.py`: Captures active window or full screen; includes `capture_window()` and `get_active_window_region()` for region isolation  
- `ocr.py`: Crops image using config-defined zones, preprocesses, and runs OCR via Tesseract  
- `voice.py`: Narrates extracted text aloud using pyttsx3; optionally saves `.wav` file based on config  
- `config.py`: Unified configuration for resolution, OCR regions, voice settings, and transcription toggles  
- `utils.py`: Logging (`log_event`) and image preprocessing (`preprocess_image`) utilities  

## root/

- `game_narrate.py`: Orchestrates full pipeline—capture → OCR → voice → save; supports `-calibrate` flag for visual zone overlay  
- `requirements.txt`: Lists dependencies (e.g. `pyttsx3`, `pytesseract`, `Pillow`, `pyautogui`, `pygetwindow`)  

## tests/

- `ocr_test.py`: Runs OCR pipeline on active window and prints extracted text from `"Main"` region  
- `voice_test.py`: Narrates sample text aloud; file saving disabled by default  

## assets/

- `VOs/`: Stores timestamped voice narration files (`.wav`)  
- `scripts/`: Stores daily transcription logs (`YYMMDD.txt`)  
- `calibration/`: Stores OCR zone overlay previews (`zone_calibration.png`)  

## docs/

- `architecture.md`: Pipeline flow, design philosophy, and extensibility  
- `setup.md`: Installation, configuration, and usage instructions  
- `privacy.md`: Local-only processing and voice file handling  
- `roadmap.md`: Planned features and future enhancements  
- `changelog.md`: Version history and module-level changes  
- `modules.md`: This file—module breakdown and structure overview  