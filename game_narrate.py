import os
import sys
import datetime
import threading
import tkinter as tk
from PIL import ImageDraw

import keyboard

from src.capture import capture_window, capture_screen, get_active_window_region
from src.ocr import extract_text
from src.voice import narrate_text
from src.utils import log_event
from src.config import SETTINGS, ocr_regions

# Global reference to the status label
status_label = None

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

def calibrate_regions():
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

def update_status(message):
    if status_label:
        status_label.config(text=message)

def run_narration():
    log_event("Starting game narration pipeline")

    image = capture_window()
    if image is None:
        log_event("No active window detected. Skipping OCR.")
        update_status("No active window detected.")
        return

    title_text = extract_text(image, region_name="Title")
    main_text = extract_text(image, region_name="Main")

    if SETTINGS["transcription"]["save_transcription_to_file"]:
        log_text_to_file(title_text, main_text)

    if not main_text.strip():
        log_event("No text extracted from 'Main' region. Skipping narration.")
        update_status("No text found in Main region.")
        return

    narrate_text(main_text)

    if SETTINGS["voice"]["save_voice_to_file"]:
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = f"{timestamp}.wav"
        narrate_text(main_text, save_to_file=True, filename=filename)
        log_event(f"Narration saved as {filename}")

    update_status("Narration complete.")

def start_hotkey_listener():
    keyboard.add_hotkey("ctrl+alt+n", run_narration)
    keyboard.wait()

def launch_gui():
    global status_label

    root = tk.Tk()
    root.title("Game Narrate")
    root.geometry("320x140")
    root.resizable(False, False)

    tk.Label(root, text="Hotkey Enabled: Ctrl + Alt + N", font=("Segoe UI", 11)).pack(pady=10)

    status_label = tk.Label(root, text="Waiting for input...", font=("Segoe UI", 10), fg="gray")
    status_label.pack(pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.quit, width=10)
    quit_button.pack(pady=10)

    threading.Thread(target=start_hotkey_listener, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    if "-calibrate" in sys.argv:
        calibrate_regions()
    else:
        launch_gui()