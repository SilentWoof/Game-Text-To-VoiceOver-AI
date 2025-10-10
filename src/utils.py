# src/utils.py

from datetime import datetime
from PIL import Image, ImageOps, ImageEnhance

def log_event(message):
    """
    Logs a timestamped message to the console.
    Args:
        message (str): The message to log
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def preprocess_image(image):
    """
    Applies preprocessing to improve OCR accuracy.
    Args:
        image (PIL.Image): The image to preprocess
    Returns:
        PIL.Image: Preprocessed image
    """
    # Convert to grayscale
    gray = ImageOps.grayscale(image)

    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(gray)
    enhanced = enhancer.enhance(1.5)

    # Apply binary thresholding
    thresholded = enhanced.point(lambda p: 255 if p > 180 else 0)

    return thresholded