# src/voice.py

import os
import re
import pyttsx3
from src.utils import log_event
from src.config import SETTINGS  # unified config import

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
    Optionally saves narration to a .wav file in assets/VOs/.

    Args:
        text (str): The text to narrate.
        save_to_file (bool): If True, saves narration to file instead of speaking aloud.
        filename (str): Name of the output .wav file.
    """
    log_event("Starting voice narration")

    # Normalize and reflow text for smoother delivery
    text = normalize_text(text)
    sentences = re.split(r'(?<=[.!?]) +', text)
    reflowed_text = ' '.join(sentence.strip() for sentence in sentences)

    engine = pyttsx3.init()
    voice_settings = SETTINGS["voice"]

    engine.setProperty("rate", voice_settings["rate"])
    engine.setProperty("volume", voice_settings["volume"])

    if voice_settings["voice_id"]:
        engine.setProperty("voice", voice_settings["voice_id"])

    # Respect config override
    should_save = save_to_file and voice_settings.get("save_voice_to_file", True)

    if should_save:
        output_path = os.path.join("assets", "VOs", filename)
        engine.save_to_file(reflowed_text, output_path)
        engine.runAndWait()  # Required to flush and write the file
        log_event(f"Voice saved to {output_path}")
    else:
        engine.say(reflowed_text)
        engine.runAndWait()

    log_event("Voice narration complete")