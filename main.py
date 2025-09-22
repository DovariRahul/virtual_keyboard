import cv2
import time

# Our modules
from hand_tracking import HandTracker
from gui import VirtualKeyboardGUI
from controller import KeyController
from voice_input import VoiceInput
from search import handle_search

def main():
    # Initialize components
    hand_tracker = HandTracker()
    keyboard_gui = VirtualKeyboardGUI("keyboard_layout.json")
    controller = KeyController()
    voice = VoiceInput()

    # Start webcam
    cap = cv2.VideoCapture(0)

    last_key = None
    last_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # mirror view

        # Detect hand & fingertip
        fingertip = hand_tracker.get_index_fingertip(frame)

        # Draw keyboard layout
        frame = keyboard_gui.draw(frame)

        # If fingertip detected → check key pressed
        if fingertip:
            key = controller.get_key_pressed(fingertip, keyboard_gui.key_positions)

            if key:
                # Debounce (avoid multiple presses too fast)
                if last_key != key:
                    last_key = key
                    last_time = time.time()
                elif time.time() - last_time > 0.5:
                    print("Pressed:", key)

                    if key == "Mic":
                        text = voice.listen()
                        if text:
                            controller.type_text(text)
                    elif key == "Enter":
                        handle_search()
                    else:
                        controller.handle_key(key)

                    last_key = None

        # Show frame
        cv2.imshow("Virtual Keyboard", frame)

        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
