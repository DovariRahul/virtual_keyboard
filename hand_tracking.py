import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def get_index_fingertip(self, frame, draw=True):
        """
        Detects the hand in the given frame and returns index fingertip coordinates (x, y).
        :param frame: input image (BGR from OpenCV)
        :param draw: whether to draw landmarks
        :return: (x, y) coordinates of fingertip or None if not found
        """
        h, w, c = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Index fingertip landmark (8)
                x_tip = int(hand_landmarks.landmark[8].x * w)
                y_tip = int(hand_landmarks.landmark[8].y * h)

                # Draw fingertip point
                cv2.circle(frame, (x_tip, y_tip), 10, (0, 255, 0), -1)

                return (x_tip, y_tip)

        return None
