# Module Breakdown

## src/

- `capture.py`: Captures active window or full screen; includes `capture_window()` for region isolation  
- `ocr.py`: Crops image using `capture_config.py`, preprocesses, and runs OCR  
- `voice.py`: Narrates extracted text aloud; optionally saves `.wav` file based on config  
- `voice_config.py`: Stores voice rate, volume, voice ID, and save toggle (`save_voice_to_file`)  
- `capture_config.py`: Stores resolution and OCR region coordinates for cropping  
- `utils.py`: Logging (`log_event`) and image preprocessing (`preprocess_image`) utilities  

## root/

- `game_narrate.py`: Orchestrates full pipeline—capture → OCR → voice → save  
- `requirements.txt`: Lists dependencies (e.g. `pyttsx3`, `pytesseract`, `Pillow`, `pyautogui`)  

## tests/

- `calibrate_region.py`: Draws red box over OCR region for visual alignment  
- `voice_test.py`: Narrates sample text with optional `.wav` output for voice validation  
- `ocr_test.py`: Runs full OCR pipeline and prints extracted text  
- `output/`: Stores calibration preview images and test artifacts  

## assets/

- `VOs/`: Stores timestamped voice narration files (`.wav`)  

## docs/

- `architecture.md`: Pipeline flow, design philosophy, and extensibility  
- `setup.md`: Installation, configuration, and usage instructions  
- `privacy.md`: Local-only processing and voice file handling  
- `roadmap.md`: Planned features and future enhancements  
- `changelog.md`: Version history and module-level changes  
- `modules.md`: This file—module breakdown and structure overview  