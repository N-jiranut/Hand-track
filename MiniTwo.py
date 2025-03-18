import mediapipe as mp
import cv2

def get_label(index, hand, results):
    output = None
    for idx, classification in enumerate(results.multi_handedness):
        if classification.classification[0].index == index:
            
            label = classification.classification[0].label
            score = classification.classification[0].score
            text = '{} {}'.format(label, round(score, 2))
            
            coords = tuple(mp.multiply(
                mp.array((hand.landmark[mp_hands.HandLandmark.WRIST].x, hand.landmark[mp_hands.HandLandmark.WRIST].y)),
            [640,480]).astype(int))
            
            output = text, coords
            
    return output

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while True:
    succus, frame = cap.read()
    frame = cv2.flip(frame, 1)

    results = hands.process(frame)

    if results.multi_hand_landmarks:
        for num, hand in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            mp_hands.HandLandmark.WRIST
            results.multi_hand_landmarks[0]
            results.multi_handedness[0].classification[0].index == num
            round(results.multi_handedness[0].classification[0].score, 2)
    
            if get_label(num, hand, results):
                text, coord = get_label(num, hand, results)
                cv2.putText(frame, text, coord, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) == ord("q"):
        break