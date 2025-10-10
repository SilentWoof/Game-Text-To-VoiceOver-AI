# docs/architecture.md

# Architecture Overview

## 🧠 Design Philosophy

- Modular isolation: Each step (capture, crop, OCR) is independently testable  
- Visual calibration: Red-box overlay confirms region alignment  
- Privacy-first: All processing is local; no cloud dependencies  
- Resolution-aware: Region coordinates scale with screen size  

## 🧩 Pipeline Flow

1. `capture.py` → Captures active window  
2. `ocr.py` → Crops using `params.py`, preprocesses, runs OCR  
3. `voice.py` (coming soon) → Converts extracted text to speech  

## 🔄 Extensibility

- Region presets per game  
- Dynamic scaling based on resolution  
- Hotkey triggers or background loop  
- Voice synthesis and subtitle overlay  