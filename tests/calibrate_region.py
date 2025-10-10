# tests/calibrate_region.py

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.capture import capture_screen, get_active_window_region
from src.params import ocr_region
from src.utils import log_event

from PIL import ImageDraw

if __name__ == "__main__":
    log_event("Starting calibration")

    # Capture active window
    region = get_active_window_region()
    image = capture_screen(region=region)

    # Get OCR region from params
    x1 = ocr_region["upper_left"]["x"]
    y1 = ocr_region["upper_left"]["y"]
    x2 = ocr_region["lower_right"]["x"]
    y2 = ocr_region["lower_right"]["y"]

    # Draw red rectangle on image
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=3)

    # Save or show image
    image.show()  # Opens in default viewer
    
    image.save("tests/output/calibration_preview.png")

    log_event("Calibration image saved as tests/output/calibration_preview.png")