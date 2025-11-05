# src/gui.py

import os
import json
import time
import threading
import tkinter as tk
from tkinter import font, messagebox
from PIL import ImageDraw

from src.capture import capture_screen, get_active_window_region
from src.config import CONFIG
from src.utils import log_event

status_label = None
text_display = None

def update_status(message, captured_text=""):
    if status_label:
        status_label.config(text=message)
    if text_display:
        text_display.config(state="normal")
        text_display.delete("1.0", tk.END)
        if captured_text.strip():
            text_display.insert(tk.END, captured_text.strip())
        text_display.config(state="disabled")

def calibrate_regions():
    log_event("Starting OCR zone calibration")
    response = messagebox.askokcancel(
        "Activate Game Window",
        "Please click OK, then switch to your game window within 5 seconds.\n\n"
        "Calibration will begin automatically."
    )
    if not response:
        log_event("Calibration cancelled by user.")
        return

    root = tk._default_root
    if root:
        root.iconify()
        log_event("Minimized Game Narrate window.")

    time.sleep(5)
    region = get_active_window_region()
    image = capture_screen(region=region)
    draw = ImageDraw.Draw(image)

    for region_name, coords in CONFIG.ocr_regions.items():
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

    if root:
        root.deiconify()
        log_event("Restored Game Narrate window.")

def edit_regions():
    editor = tk.Toplevel()
    editor.title("Edit Regions")
    editor.geometry("400x520")
    editor.resizable(False, False)

    entries = {}

    tk.Label(editor, text="Screen Resolution", font=("Segoe UI", 10, "bold")).pack(pady=(10, 0))
    tk.Label(editor, text="Set the base resolution used for OCR scaling.").pack()
    res_frame = tk.Frame(editor)
    res_frame.pack(pady=5)
    tk.Label(res_frame, text="Width:").grid(row=0, column=0)
    tk.Label(res_frame, text="Height:").grid(row=1, column=0)

    width_entry = tk.Entry(res_frame, width=10)
    width_entry.insert(0, str(CONFIG.resolution["width"]))
    width_entry.grid(row=0, column=1)

    height_entry = tk.Entry(res_frame, width=10)
    height_entry.insert(0, str(CONFIG.resolution["height"]))
    height_entry.grid(row=1, column=1)

    tk.Label(editor, text="OCR Regions", font=("Segoe UI", 10, "bold")).pack(pady=(15, 0))
    tk.Label(editor, text="Define the pixel zones for Title and Main text extraction.").pack()

    def create_region_fields(region_name):
        tk.Label(editor, text=f"{region_name} Region", font=("Segoe UI", 9, "bold")).pack(pady=(10, 0))
        frame = tk.Frame(editor)
        frame.pack()
        for i, corner in enumerate(["upper_left", "lower_right"]):
            for j, axis in enumerate(["x", "y"]):
                label = f"{corner} {axis}"
                tk.Label(frame, text=label).grid(row=i, column=j * 2)
                val = CONFIG.ocr_regions[region_name][corner][axis]
                entry = tk.Entry(frame, width=8)
                entry.insert(0, str(val))
                entry.grid(row=i, column=j * 2 + 1)
                entries[f"{region_name}_{corner}_{axis}"] = entry

    create_region_fields("Title")
    create_region_fields("Main")

    def save_all():
        try:
            CONFIG.resolution["width"] = int(width_entry.get())
            CONFIG.resolution["height"] = int(height_entry.get())
            with open("assets/resolution_config.json", "w", encoding="utf-8") as f:
                json.dump(CONFIG.resolution, f, indent=2)

            for region in ["Title", "Main"]:
                for corner in ["upper_left", "lower_right"]:
                    for axis in ["x", "y"]:
                        key = f"{region}_{corner}_{axis}"
                        val = int(entries[key].get())
                        CONFIG.ocr_regions[region][corner][axis] = val
            with open("assets/ocr_config.json", "w", encoding="utf-8") as f:
                json.dump(CONFIG.ocr_regions, f, indent=2)

            messagebox.showinfo("Saved", "Capture settings updated successfully.")
            editor.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "All fields must be integers.")

    tk.Button(editor, text="Save", command=save_all, width=12).pack(pady=20)

def launch_gui(run_narration_callback):
    global status_label, text_display

    root = tk.Tk()
    root.title("Game Narrate")
    root.geometry("400x550")
    root.resizable(False, False)

    title_font = font.Font(family="Segoe UI", size=12, weight="bold")
    italic_font = font.Font(family="Segoe UI", size=10, slant="italic")

    tk.Label(root, text="Game Narrate", font=title_font).pack(pady=(10, 5))
    tk.Label(root, text="Hotkey Enabled: Ctrl + Alt + N", font=("Segoe UI", 10)).pack()

    settings_frame = tk.LabelFrame(root, text="Settings", padx=10, pady=5)
    settings_frame.pack(padx=10, pady=(5, 10), fill="x")

    narration_var = tk.BooleanVar(value=CONFIG.settings["voice"]["enable_narration"])
    voice_save_var = tk.BooleanVar(value=CONFIG.settings["voice"]["save_voice_to_file"])
    transcript_var = tk.BooleanVar(value=CONFIG.settings["transcription"]["save_transcription_to_file"])

    def update_settings():
        CONFIG.settings["voice"]["enable_narration"] = narration_var.get()
        CONFIG.settings["voice"]["save_voice_to_file"] = voice_save_var.get()
        CONFIG.settings["transcription"]["save_transcription_to_file"] = transcript_var.get()
        log_event("SETTINGS updated from GUI")

    def run_with_settings():
        update_settings()
        run_narration_callback()

    tk.Checkbutton(settings_frame, text="Enable Narration", variable=narration_var, command=update_settings).pack(anchor="w")
    tk.Checkbutton(settings_frame, text="Save Voice to File", variable=voice_save_var, command=update_settings).pack(anchor="w")
    tk.Checkbutton(settings_frame, text="Save Transcription to File", variable=transcript_var, command=update_settings).pack(anchor="w")

    button_frame = tk.Frame(root)
    button_frame.pack(pady=(0, 10))

    tk.Button(button_frame, text="Calibrate", command=calibrate_regions, width=10).pack(side="left", padx=5)
    tk.Button(button_frame, text="Edit Regions", command=edit_regions, width=14).pack(side="left", padx=5)
    tk.Button(button_frame, text="Quit", command=root.quit, width=10).pack(side="left", padx=5)

    tk.Label(root, text="Last Text Captured:", font=("Segoe UI", 10)).pack()
    text_display = tk.Text(root, height=15, wrap="word", font=italic_font, state="disabled", bg="#f4f4f4", relief="sunken")
    text_display.pack(padx=10, pady=(0, 10), fill="both", expand=True)

    status_label = tk.Label(root, text="Waiting for input...", font=("Segoe UI", 9), fg="gray")
    status_label.pack(pady=(0, 5))

    threading.Thread(target=lambda: keyboard_listener(run_with_settings), daemon=True).start()
    root.mainloop()

def keyboard_listener(callback):
    import keyboard
    keyboard.add_hotkey("ctrl+alt+n", callback)
    keyboard.wait()