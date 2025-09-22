import time
import cv2

# -----------------------------
# Debounce helper function
# -----------------------------
def debounce(last_time, debounce_time=0.5):
    """
    Returns True if enough time has passed since last_time
    to register a new action. Otherwise returns False.
    """
    current_time = time.time()
    if current_time - last_time > debounce_time:
        return True
    return False

# -----------------------------
# Draw highlighted key
# -----------------------------
def highlight_key(frame, key_pos, color=(0, 255, 0)):
    """
    Highlights a key rectangle on the frame.
    :param frame: OpenCV image
    :param key_pos: (x1, y1, x2, y2)
    :param color: RGB color tuple
    """
    x1, y1, x2, y2 = key_pos
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)

# -----------------------------
# Normalize text
# -----------------------------
def normalize_text(text):
    """
    Converts text to lowercase and removes leading/trailing spaces.
    """
    if text:
        return text.strip().lower()
    return ""
