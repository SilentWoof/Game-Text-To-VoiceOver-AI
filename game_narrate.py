# game_narrate.py

import os
import sys
import datetime
from src.capture import capture_window
from src.ocr import extract_text
from src.voice import narrate_text
from src.utils import log_event
from src.config import CONFIG
from src.gui import launch_gui, update_status

def log_text_to_file(title_text, body_text):
    date_str = datetime.datetime.now().strftime("%y%m%d")
    log_path = os.path.join("assets", "scripts")
    os.makedirs(log_path, exist_ok=True)
    file_path = os.path.join(log_path, f"{date_str}.txt")

    entry = (
        "______________________\n"
        f"{title_text.strip()}\n\n"
        f"{body_text.strip()}\n"
        "------------------------------\n"
    )

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry)

def run_narration():
    log_event("Starting game narration pipeline")

    image = capture_window()
    if image is None:
        log_event("No active window detected. Skipping OCR.")
        update_status("No active window detected.", "")
        return

    title_text = extract_text(image, region_name="Title")
    main_text = extract_text(image, region_name="Main")

    if CONFIG.settings["transcription"]["save_transcription_to_file"]:
        log_text_to_file(title_text, main_text)

    if not main_text.strip():
        log_event("No text extracted from 'Main' region. Skipping narration.")
        update_status("No text found in Main region.", "")
        return

    combined_text = f"{title_text.strip()}\n\n{main_text.strip()}"
    update_status("Text captured.", combined_text)

    filename = None
    if CONFIG.settings["voice"]["save_voice_to_file"]:
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        title_clean = "".join(c for c in title_text.strip() if c.isalnum() or c in (" ", "_")).strip().replace(" ", "_")
        if not title_clean:
            title_clean = "Untitled"
        output_dir = os.path.join("assets", "VOs")
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"{timestamp}_{title_clean}.wav")

    if CONFIG.settings["voice"]["enable_narration"] or CONFIG.settings["voice"]["save_voice_to_file"]:
        log_event(f"Calling narrate_text with save_to_file={CONFIG.settings['voice']['save_voice_to_file']} and filename={filename}")
        narrate_text(
            main_text,
            save_to_file=CONFIG.settings["voice"]["save_voice_to_file"],
            filename=filename if filename else "output.wav"
        )
    else:
        log_event("Narration and voice saving both disabled by config.")

    update_status("Narration complete.", combined_text)

if __name__ == "__main__":
    if "-calibrate" in sys.argv:
        from src.gui import calibrate_regions
        calibrate_regions()
    else:
        launch_gui(run_narration)