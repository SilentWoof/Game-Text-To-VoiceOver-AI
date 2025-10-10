# src/voice.py

import os
import pyttsx3
from src.utils import log_event
from src.voice_config import VOICE_SETTINGS

def narrate_text(text: str, save_to_file: bool = False, filename: str = "output.wav"):
    """
    Narrates the given text using pyttsx3 TTS engine.
    Applies settings from voice_config.py.
    Optionally saves narration to a .wav file in assets/VOs/.

    Args:
        text (str): The text to narrate.
        save_to_file (bool): If True, saves narration to file instead of speaking aloud.
        filename (str): Name of the output .wav file.
    """
    log_event("Starting voice narration")

    # Normalize line breaks to avoid unnatural pauses
    text = text.replace('\n', ' ').strip()

    engine = pyttsx3.init()
    engine.setProperty("rate", VOICE_SETTINGS["rate"])
    engine.setProperty("volume", VOICE_SETTINGS["volume"])

    if VOICE_SETTINGS["voice_id"]:
        engine.setProperty("voice", VOICE_SETTINGS["voice_id"])

    # Respect config override
    should_save = save_to_file and VOICE_SETTINGS.get("save_voice_to_file", True)

    if should_save:
        output_path = os.path.join("assets", "VOs", filename)
        engine.save_to_file(text, output_path)
        engine.runAndWait()  # Required to flush and write the file
        log_event(f"Voice saved to {output_path}")
    else:
        engine.say(text)
        engine.runAndWait()

    log_event("Voice narration complete")