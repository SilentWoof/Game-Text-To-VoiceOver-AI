import pyautogui
import pytesseract
import cv2
import numpy as np

# Optional: Set path to tesseract.exe if not on PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1: Capture screenshot
screenshot = pyautogui.screenshot()

# Step 2: Convert to OpenCV format
image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Step 3: Run OCR
text = pytesseract.image_to_string(image)

# Step 4: Print result
print("🧠 OCR Result:")
print(text)