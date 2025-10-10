# src/ocr.py

import pytesseract
from src.utils import preprocess_image, log_event
from src.params import ocr_region

def extract_text(image):
    """
    Extracts text from a defined region of the image using OCR.
    Args:
        image (PIL.Image): The full captured image
    Returns:
        str: Extracted text from the cropped region
    """
    # Load region coordinates from params
    x1 = ocr_region["upper_left"]["x"]
    y1 = ocr_region["upper_left"]["y"]
    x2 = ocr_region["lower_right"]["x"]
    y2 = ocr_region["lower_right"]["y"]

    # Crop image to defined region
    cropped = image.crop((x1, y1, x2, y2))
    log_event(f"Cropped image to region: ({x1}, {y1}) → ({x2}, {y2})")

    # Preprocess and run OCR
    preprocessed = preprocess_image(cropped)
    text = pytesseract.image_to_string(preprocessed)
    return text