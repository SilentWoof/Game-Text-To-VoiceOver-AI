# game_narrate.py

"""
Main entry point for game narration and OCR zone calibration.

Usage:
    python game_narrate.py           → Runs narration pipeline
    python game_narrate.py -calibrate → Captures active window and overlays OCR zones
"""

import datetime
import os
import sys
from PIL import ImageDraw

from src.capture import capture_window, capture_screen, get_active_window_region
from src.ocr import extract_text
from src.voice import narrate_text
from src.utils import log_event
from src.config import SETTINGS, ocr_regions

def log_text_to_file(title_text, body_text):
    """
    Appends the captured title and body text to a daily log file.
    Format: assets/scripts/YYMMDD.txt
    Each entry is separated by a divider.
    """
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

def calibrate_regions():
    """
    Captures the active window and overlays OCR zones for visual calibration.
    Saves the result to assets/calibration/zone_calibration.png
    """
    log_event("Starting OCR zone calibration")

    region = get_active_window_region()
    image = capture_screen(region=region)
    draw = ImageDraw.Draw(image)

    for region_name, coords in ocr_regions.items():
        x1 = coords["upper_left"]["x"]
        y1 = coords["upper_left"]["y"]
        x2 = coords["lower_right"]["x"]
        y2 = coords["lower_right"]["y"]

        color = "red" if region_name == "Main" else "blue"
        draw.rectangle([(x1, y1), (x2, y2)], outline=color, width=3)
        log_event(f"Drew {region_name} region: ({x1}, {y1}) → ({x2}, {y2}) in {color}")

    output_dir = os.path.join("assets", "calibration")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "zone_calibration.png")

    image.show()
    image.save(output_path)
    log_event(f"Calibration image saved as {output_path}")

def main():
    if "-calibrate" in sys.argv:
        calibrate_regions()
        return

    log_event("Starting game narration pipeline")

    image = capture_window()
    if image is None:
        log_event("No active window detected. Skipping OCR.")
        return

    title_text = extract_text(image, region_name="Title")
    main_text = extract_text(image, region_name="Main")

    if SETTINGS["transcription"]["save_transcription_to_file"]:
        log_text_to_file(title_text, main_text)

    if not main_text.strip():
        log_event("No text extracted from 'Main' region. Skipping narration.")
        return

    narrate_text(main_text)

    if SETTINGS["voice"]["save_voice_to_file"]:
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = f"{timestamp}.wav"
        narrate_text(main_text, save_to_file=True, filename=filename)
        log_event(f"Narration saved as {filename}")

if __name__ == "__main__":
    main()