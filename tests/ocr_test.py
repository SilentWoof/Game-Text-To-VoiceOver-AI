# tests/ocr_test.py

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.capture import capture_screen, get_active_window_region
from src.ocr import extract_text
from src.utils import log_event

if __name__ == "__main__":
    log_event("Starting OCR test")

    region = get_active_window_region()
    log_event(f"Active window region: {region}")

    image = capture_screen(region=region)
    text = extract_text(image)

    log_event("OCR result:")
    print("🧠 OCR Result:\n", text)