# src/voice.py

import os
import re
import time
import pyttsx3
from src.utils import log_event
from src.config import CONFIG

def normalize_text(text: str) -> str:
    """
    Cleans up OCR output for smoother narration.
    - Removes line breaks and extra spaces
    - Adds spacing after punctuation for natural pauses
    """
    text = text.replace('\n', ' ').replace('  ', ' ')
    text = re.sub(r'([.!?])', r'\1 ', text)
    return text.strip()

def narrate_text(text: str, save_to_file: bool = False, filename: str = "output.wav"):
    """
    Narrates the given text using pyttsx3 TTS engine.
    Applies settings from config.py.
    Optionally saves narration to a .wav file.

    Args:
        text (str): The text to narrate.
        save_to_file (bool): If True, saves narration to file.
        filename (str): Full path to the output .wav file.
    """
    log_event("Starting voice narration")

    # Normalize and reflow text for smoother delivery
    text = normalize_text(text)
    sentences = re.split(r'(?<=[.!?]) +', text)
    reflowed_text = ' '.join(sentence.strip() for sentence in sentences)

    engine = pyttsx3.init()
    voice_settings = CONFIG.settings["voice"]

    engine.setProperty("rate", voice_settings["rate"])
    engine.setProperty("volume", voice_settings["volume"])

    if voice_settings["voice_id"]:
        engine.setProperty("voice", voice_settings["voice_id"])

    # Speak aloud if narration is enabled
    if voice_settings.get("enable_narration", False):
        engine.say(reflowed_text)

    # Save to file if requested
    if save_to_file:
        output_path = filename
        engine.save_to_file(reflowed_text, output_path)

    engine.runAndWait()
    time.sleep(0.5)  # Give time for file to flush

    if save_to_file:
        if os.path.exists(output_path):
            log_event(f"Voice saved to {output_path}")
        else:
            log_event(f"⚠️ Failed to save voice file at {output_path}")

    log_event("Voice narration complete")