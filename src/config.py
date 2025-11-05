# src/config.py

# Base resolution reference
resolution = {
    "width": 1920,
    "height": 1080
}

# OCR target regions
ocr_regions = {
    "Title": {
        "upper_left": {"x": 1035, "y": 110},
        "lower_right": {"x": 1700, "y": 168}
    },
    "Main": {
        "upper_left": {"x": 1035, "y": 170},
        "lower_right": {"x": 1700, "y": 900}
    },
}

# Global settings
SETTINGS = {
    "voice": {
        "enable_narration": False,
        "save_voice_to_file": False,
        "rate": 155,
        "volume": 1.0,
        "voice_id": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
    },
    "transcription": {
        "save_transcription_to_file": True
    }
}