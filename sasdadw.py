import cv2
import mediapipe as mp
mpHands = mp.solutions.hands
hands = mpHands.Hands(2)
row=[]
img = cv2.imread("TestPose/Home/captured_image20.jpg")
img = cv2.flip(img, 1)
results_hand = hands.process(img)
if results_hand.multi_hand_landmarks:
    landmarks = results_hand.multi_hand_landmarks
    for lm in landmarks:
        row.extend([lm.x, lm.y, lm.z])
        # for idx, hand_landmarks in enumerate(results_hand.multi_hand_landmarks):
        #     handedness = results_hand.multi_handedness[idx].classification[0].label
        #     for id, lm in enumerate(hand_landmarks.landmark):
        #         h, w, c = img.shape
        #         cx, cy = int(lm.x * w), int(lm.y * h)
        #         if handedness:                        
        #             print(handedness)
print(row)