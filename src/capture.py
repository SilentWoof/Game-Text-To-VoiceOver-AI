# src/capture.py

import pyautogui
from PIL import Image
import pygetwindow as gw

def get_active_window_region():
    """
    Returns the bounding box of the currently active window.
    Returns:
        tuple: (left, top, width, height) or None
    """
    win = gw.getActiveWindow()
    if win is None:
        return None
    return (win.left, win.top, win.width, win.height)

def capture_screen(region=None):
    """
    Captures a screenshot of the entire screen or a specified region.
    Args:
        region (tuple): Optional (left, top, width, height)
    Returns:
        PIL.Image: Screenshot image
    """
    screenshot = pyautogui.screenshot(region=region)
    return screenshot