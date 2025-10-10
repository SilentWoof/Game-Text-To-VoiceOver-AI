# Architecture Overview

## 🧠 Design Philosophy

- **Modular isolation**: Each step (capture, OCR, voice) is independently testable and traceable  
- **Visual calibration**: OCR zone overlay triggered via `-calibrate` flag in `game_narrate.py`  
- **Privacy-first**: All processing is local; no cloud dependencies or external voice APIs  
- **Unified configuration**: Resolution, regions, voice, and logging settings stored in `config.py`  
- **Configurable output**: Voice saving and transcription toggles controlled via `SETTINGS` in `config.py`  

## 🧩 Pipeline Flow

1. `game_narrate.py` → Orchestrates full pipeline: capture → OCR → voice → save  
2. `capture.py` → `capture_window()` isolates active window region  
3. `ocr.py` → Crops using config-defined zones, preprocesses, and runs OCR  
4. `voice.py` → Narrates text aloud and optionally saves `.wav` file  
5. `utils.py` → Logs events and preprocesses images for OCR accuracy  
6. `config.py` → Stores resolution, OCR regions, voice settings, and transcription toggles  

## 🔄 Extensibility

- Region presets per game  
- Dynamic scaling based on resolution  
- Hotkey triggers or background loop  
- Voice synthesis and subtitle overlay  
- Game-specific voice presets via `voice_presets.py` (planned)  
- Session-based folder organization for voice artifacts  
- CLI flags for toggling voice saving, calibration, and verbosity  

## 🗺️ Pipeline Diagram

🎮 game_narrate.py  
├── 🖼️ capture.py  
│   └── capture_window() → grabs active game window  
│   └── get_active_window_region() → defines crop zone  
├── 🧠 ocr.py  
│   └── extract_text(image, region_name) → runs OCR on cropped region  
├── 🗣️ voice.py  
│   └── narrate_text(text, save_to_file=False) → speaks aloud or saves .wav  
├── 📋 utils.py  
│   └── log_event(msg) → timestamped logging  
│   └── preprocess_image(image) → grayscale + sharpening  
├── ⚙️ config.py  
│   └── ocr_regions → defines "Title" and "Main" zones  
│   └── SETTINGS → toggles for voice and transcription  
└── 🧪 CLI flag: `-calibrate`  
    └── overlays OCR zones and saves preview to assets/calibration/