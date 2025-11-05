# Architecture Overview

## 🧠 Design Philosophy

- **Modular isolation**: Each step (capture, OCR, voice, GUI) is independently testable and traceable  
- **Visual calibration**: OCR zone overlay triggered via `-calibrate` flag in `game_narrate.py`  
- **Privacy-first**: All processing is local; no cloud dependencies or external voice APIs  
- **Unified configuration**: Resolution, regions, voice, transcription, and GUI settings stored in `config.py`  
- **Independent toggles**: Narration, voice saving, and transcript logging can be enabled separately via `SETTINGS`  
- **Responsive UX**: Captured text is displayed immediately in the GUI before narration begins  

## 🧩 Pipeline Flow

1. `game_narrate.py` → Orchestrates full pipeline: capture → OCR → GUI → voice → save  
2. `capture.py` → `capture_window()` isolates active window region  
3. `ocr.py` → Crops using config-defined zones, preprocesses, and runs OCR  
4. `voice.py` → Narrates text aloud and optionally saves `.wav` file  
5. `utils.py` → Logs events and preprocesses images for OCR accuracy  
6. `config.py` → Stores resolution, OCR regions, voice settings, and transcription toggles  
7. `gui.py` → Manages window layout, settings toggles, region editor, calibration overlay, and status updates  

## 🔄 Extensibility

- Region presets per game  
- Dynamic scaling based on resolution  
- Hotkey triggers or background loop  
- Voice synthesis and subtitle overlay  
- Game-specific voice presets via `voice_presets.py` (planned)  
- Session-based folder organization for voice artifacts  
- CLI flags for toggling voice saving, calibration, and verbosity  
- GUI enhancements: voice preview, playback controls, and real-time status updates  

## 🗺️ Pipeline Diagram

🎮 game_narrate.py  
├── 🖼️ capture.py  
│   └── capture_window() → grabs active game window  
│   └── get_active_window_region() → defines crop zone  
├── 🧠 ocr.py  
│   └── extract_text(image, region_name) → runs OCR on cropped region  
├── 🖥️ gui.py  
│   └── launch_gui(callback) → builds interface and binds hotkey  
│   └── update_status(message, text) → updates status and display  
│   └── calibrate_regions() → overlays OCR zones and saves preview  
│   └── edit_regions() → GUI editor for resolution and crop zones  
├── 🗣️ voice.py  
│   └── narrate_text(text, save_to_file=False, filename="...") → speaks aloud and/or saves .wav  
├── 📋 utils.py  
│   └── log_event(msg) → timestamped logging  
│   └── preprocess_image(image) → grayscale + sharpening  
├── ⚙️ config.py  
│   └── ocr_regions → defines "Title" and "Main" zones  
│   └── SETTINGS → toggles for voice, transcription, and GUI behavior  
└── 🧪 CLI flag: `-calibrate`  
    └── overlays OCR zones and saves preview to assets/calibration/