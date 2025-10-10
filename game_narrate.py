# game_narrate.py

import datetime
from src.capture import capture_window
from src.ocr import extract_text
from src.voice import narrate_text
from src.utils import log_event
from src.voice_config import VOICE_SETTINGS

def main():
    log_event("Starting game narration pipeline")

    # Step 1: Capture image from active window
    image = capture_window()
    if image is None:
        log_event("No active window detected. Skipping OCR.")
        return

    # Step 2: Extract text via OCR
    text = extract_text(image)
    if not text.strip():
        log_event("No text extracted. Skipping narration.")
        return

    # Step 3: Narrate aloud
    narrate_text(text)

    # Step 4: Save to timestamped voice file (if enabled)
    if VOICE_SETTINGS.get("save_voice_to_file", True):
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = f"{timestamp}.wav"
        narrate_text(text, save_to_file=True, filename=filename)
        log_event(f"Narration saved as {filename}")

if __name__ == "__main__":
    main()