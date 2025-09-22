import pyautogui
import time

class KeyController:
    def __init__(self, debounce_time=0.5):
        self.last_key = None
        self.last_time = 0
        self.debounce_time = debounce_time  # seconds

    def get_key_pressed(self, fingertip, key_positions):
        """
        Checks if fingertip is inside a key bounding box.
        :param fingertip: (x, y) coordinates
        :param key_positions: list of {"key": str, "pos": (x1, y1, x2, y2)}
        :return: key name if pressed, else None
        """
        if fingertip is None:
            return None

        x, y = fingertip
        for kp in key_positions:
            x1, y1, x2, y2 = kp["pos"]
            if x1 < x < x2 and y1 < y < y2:
                return kp["key"]

        return None

    def handle_key(self, key):
        """
        Handles normal and special keys with PyAutoGUI.
        """
        if not self._debounce(key):
            return  # Skip if debounce active

        if key == "Space":
            pyautogui.typewrite(" ")
        elif key == "Back":
            pyautogui.press("backspace")
        elif key == "Enter":
            pyautogui.press("enter")
        elif key == "Mic":
            # Voice handled separately in main.py
            pass
        else:
            pyautogui.typewrite(key.lower())

    def type_text(self, text):
        """
        Types a full string (used by voice input).
        """
        pyautogui.typewrite(text)

    def _debounce(self, key):
        """
        Prevents multiple presses for the same key within debounce_time.
        """
        current_time = time.time()
        if self.last_key == key and (current_time - self.last_time) < self.debounce_time:
            return False
        self.last_key = key
        self.last_time = current_time
        return True
