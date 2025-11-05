# src/ocr.py

import pytesseract
from src.utils import preprocess_image, log_event
from src.config import CONFIG

def extract_text(image, region_name="Main"):
    """
    Extracts text from a named region of the image using OCR.
    Args:
        image (PIL.Image): The full captured image
        region_name (str): The key name of the region to extract ("Main", "Title", etc.)
    Returns:
        str: Extracted text from the cropped region
    """
    if region_name not in CONFIG.ocr_regions:
        log_event(f"Region '{region_name}' not found in config.")
        return ""

    region = CONFIG.ocr_regions[region_name]
    x1 = region["upper_left"]["x"]
    y1 = region["upper_left"]["y"]
    x2 = region["lower_right"]["x"]
    y2 = region["lower_right"]["y"]

    cropped = image.crop((x1, y1, x2, y2))
    log_event(f"Cropped image to '{region_name}' region: ({x1}, {y1}) → ({x2}, {y2})")

    preprocessed = preprocess_image(cropped)
    text = pytesseract.image_to_string(preprocessed)
    return text