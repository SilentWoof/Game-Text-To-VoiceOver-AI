# src/capture.py

import pyautogui
from PIL import Image
import pygetwindow as gw
from src.config import CONFIG

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

def capture_window():
    """
    Captures a screenshot of the currently active window.
    Returns:
        PIL.Image: Screenshot image or None if no window is active
    """
    region = get_active_window_region()
    if region is None:
        return None
    return capture_screen(region)