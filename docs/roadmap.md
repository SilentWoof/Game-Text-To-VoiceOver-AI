# Roadmap

## ✅ Current Capabilities

- **Local-only processing**: All capture, OCR, voice synthesis, and file saving occur entirely on the user's machine  
- **No cloud dependencies**: No external APIs, cloud services, or online voice engines are used  
- **No telemetry or tracking**: The system does not collect, transmit, or log user data beyond local console output  
- **Voice synthesis is offline**: Narration is powered by `pyttsx3`, a local TTS engine with no network calls  
- **Configurable voice saving**: `.wav` file generation is controlled via `VOICE_SETTINGS["save_voice_to_file"]` in `voice_config.py`  
- **Calibration artifacts are local**: Region previews are stored in `output/` and excluded via `.gitignore`  
- **Modular auditability**: Each module (capture, OCR, voice) is isolated and testable, enabling forensic-grade rollback and inspection  
- **No background capture**: Only the active window is targeted, and OCR is restricted to a user-defined region  
- **Line-break normalization**: Narration flow is driven by punctuation, not OCR formatting  

---

## 🛠️ Planned Enhancements

- **Voice customization per game**: Scaffold `voice_presets.py` to load narration styles based on game title or context  
- **Naturalized speech flow**: Add sentence smoothing, pause tuning, and optional SSML support for expressive delivery  
- **Session-based voice folders**: Auto-organize `.wav` files by game or timestamped session  
- **OCR region snapshots**: Save cropped image alongside voice file for traceability and debugging  
- **CLI flags for runtime control**: Toggle voice saving, verbosity, and region override from command line  
- **Subtitle overlay (optional)**: Display extracted text in real-time for accessibility or streaming  
- **Hotkey triggers**: Enable background loop or manual capture via keyboard shortcut  
- **Game-specific OCR presets**: Load region coordinates dynamically based on active window title  