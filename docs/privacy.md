# Privacy Principles

This project is built with privacy-first design:

- **Local-only processing**: All capture, OCR, voice synthesis, and file saving occur entirely on the user's machine  
- **No cloud dependencies**: No external APIs, cloud services, or online voice engines are used  
- **No telemetry or tracking**: The system does not collect, transmit, or log user data beyond local console output  
- **Voice synthesis is offline**: Narration is powered by `pyttsx3`, a local TTS engine with no network calls  
- **Configurable voice saving**: `.wav` file generation is controlled via `VOICE_SETTINGS["save_voice_to_file"]` in `voice_config.py`  
- **Calibration artifacts are local**: Region previews are stored in `output/` and excluded via `.gitignore`  
- **Modular auditability**: Each module (capture, OCR, voice) is isolated and testable, enabling forensic-grade rollback and inspection  
- **No background capture**: Only the active window is targeted, and OCR is restricted to a user-defined region  