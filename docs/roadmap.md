# Roadmap

## ✅ Current Capabilities

- **Local-only processing**: All capture, OCR, voice synthesis, and file saving occur entirely on the user's machine  
- **No cloud dependencies**: No external APIs, cloud services, or online voice engines are used  
- **No telemetry or tracking**: The system does not collect, transmit, or log user data beyond local console output  
- **Voice synthesis is offline**: Narration is powered by `pyttsx3`, a local TTS engine with no network calls  
- **Unified configuration**: All settings (resolution, OCR regions, voice, transcription) are stored in `config.py`  
- **CLI calibration**: OCR zone overlays are triggered via `-calibrate` flag in `game_narrate.py`  
- **Modular auditability**: Each module (capture, OCR, voice) is isolated and testable, enabling forensic-grade rollback and inspection  
- **No background capture**: Only the active window is targeted, and OCR is restricted to defined regions  
- **Line-break normalization**: Narration flow is driven by punctuation, not OCR formatting  
- **Optional voice saving**: `.wav` file generation is controlled via `SETTINGS["voice"]["save_voice_to_file"]`  
- **Optional transcription logging**: Daily `.txt` logs are stored in `assets/scripts/` when enabled  
- **Visual calibration artifacts**: OCR zone previews are saved to `assets/calibration/` and excluded via `.gitignore`  

---

## 🛠️ Planned Enhancements

- **Naturalized speech flow**: Add sentence smoothing, pause tuning, and optional SSML support for expressive delivery  
- **Voice preview utility**: Add CLI tool to test voice settings before narration  
- **Config export/import**: Save and load config profiles for different games or setups  
- **Hotkey triggers**: Enable background loop or manual capture via keyboard shortcut  