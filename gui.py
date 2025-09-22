import cv2
import json

class VirtualKeyboardGUI:
    def __init__(self, layout_file):
        # Load keyboard layout
        with open(layout_file, "r") as f:
            layout = json.load(f)

        self.rows = layout["rows"]
        self.key_positions = []  # stores key + position (x1, y1, x2, y2)

        # Keyboard settings
        self.key_width = 60
        self.key_height = 60
        self.start_x = 50
        self.start_y = 350
        self.spacing = 10

    def draw(self, frame):
        """
        Draws the entire keyboard on the frame.
        Stores key positions in self.key_positions.
        """
        self.key_positions = []  # reset each frame
        y = self.start_y

        for row in self.rows:
            x = self.start_x
            for key in row:
                # Draw key rectangle
                x1, y1 = x, y
                x2, y2 = x + self.key_width, y + self.key_height
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), -1)

                # Add key text
                font_scale = 0.8 if len(key) > 2 else 1
                cv2.putText(frame, key, (x1 + 15, y1 + 40),
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                            (255, 255, 255), 2)

                # Save position for controller
                self.key_positions.append({"key": key, "pos": (x1, y1, x2, y2)})

                x += self.key_width + self.spacing
            y += self.key_height + self.spacing

        return frame
