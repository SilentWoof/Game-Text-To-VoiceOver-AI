# src/config.py

import json
import os

class Config:
    def __init__(self):
        self.resolution = self.load_json("assets/resolution_config.json", {
            "width": 1920,
            "height": 1080
        })

        self.ocr_regions = self.load_json("assets/ocr_config.json", {
            "Title": {
                "upper_left": {"x": 1035, "y": 110},
                "lower_right": {"x": 1700, "y": 168}
            },
            "Main": {
                "upper_left": {"x": 1035, "y": 170},
                "lower_right": {"x": 1700, "y": 900}
            }
        })

        self.settings = {
            "voice": {
                "enable_narration": False,
                "save_voice_to_file": False,
                "rate": 155,
                "volume": 1.0,
                "voice_id": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0"
            },
            "transcription": {
                "save_transcription_to_file": True
            }
        }

    def load_json(self, path, fallback):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return fallback

CONFIG = Config()