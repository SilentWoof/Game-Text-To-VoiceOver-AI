# Architecture Overview

## 🧠 Design Philosophy

- **Modular isolation**: Each step (capture, crop, OCR, voice) is independently testable and traceable  
- **Visual calibration**: Red-box overlay confirms OCR region alignment via `calibrate_region.py`  
- **Privacy-first**: All processing is local; no cloud dependencies or external voice APIs  
- **Resolution-aware**: Region coordinates scale with screen size and are stored in `capture_config.py`  
- **Configurable output**: Voice saving is controlled via `voice_config.py` toggle  

## 🧩 Pipeline Flow

1. `game_narrate.py` → Orchestrates full pipeline: capture → OCR → voice → save  
2. `capture.py` → `capture_window()` isolates active window region  
3. `ocr.py` → Crops using `capture_config.py`, preprocesses, runs OCR  
4. `voice.py` → Narrates text aloud and optionally saves `.wav` file  
5. `utils.py` → Logs events and preprocesses images for OCR accuracy  

## 🔄 Extensibility

- Region presets per game  
- Dynamic scaling based on resolution  
- Hotkey triggers or background loop  
- Voice synthesis and subtitle overlay  
- Game-specific voice presets via `voice_presets.py` (planned)  
- Session-based folder organization for voice artifacts  
- CLI flags for toggling voice saving and verbosity  