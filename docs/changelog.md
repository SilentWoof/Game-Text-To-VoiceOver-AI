# Changelog

## v0.1 — Initial Commit

- Active window capture  
- Basic OCR extraction  

## v0.2 — Region Isolation

- params.py for resolution and crop box  
- Modular cropping logic  

## v0.3 — Visual Calibration

- Red-box overlay script  
- Calibration preview saved to tests/output/  

## v0.4 — OCR Test Script

- Full pipeline test with logging  
- PowerShell delay for manual switching  

## v0.5 — Voice Synthesis Integration

- Added voice.py for local text-to-speech narration  
- Configurable voice settings via voice_config.py  
- Line-break normalization for natural speech flow  
- Optional .wav file saving with timestamped filenames  

## v0.6 — Full Pipeline Orchestration

- Created game_narrate.py to coordinate capture → OCR → voice  
- Prevented duplicate narration when saving is disabled  
- Added save_voice_to_file toggle to voice_config.py  
- Timestamped voice files stored in assets/VOs/  

## v0.7 — Voice and Calibration Testing

- Added voice_test.py for standalone narration validation  
- Updated calibrate_region.py for resolution-aware red-box overlay  
- Modular test harnesses for OCR and voice synthesis  

## v0.8 — Unified Config and CLI Calibration

- Replaced params.py and voice_config.py with unified config.py  
- Integrated calibration overlay into game_narrate.py via `-calibrate` flag  
- Removed calibrate_region.py and consolidated logic  
- Explicit region targeting in ocr_test.py  
- Disabled file saving in voice_test.py by default  
- Added top-level docstrings to all test scripts  
- Cleaned up redundant imports and clarified logging output  