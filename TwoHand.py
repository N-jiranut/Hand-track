import cv2
import mediapipe as mp
import time

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
i=0
lol=0
# OpenCV Video Capture
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        lmList = []
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        # Convert to RGB (MediaPipe uses RGB format)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame
        results = hands.process(rgb_frame)

        print('Handedness:', results.multi_handedness)
        
        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # print(lol,"<---")
                # lol+=1
                handedness = results.multi_handedness[idx].classification[0].label
                # print(f"Detected {handedness} Hand")
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                h, w, _ = frame.shape
                x, y = int(hand_landmarks.landmark[0].x * w), int(hand_landmarks.landmark[0].y * h)
                # lmList.append([idx, x, y])
                cv2.putText(frame, f"{handedness} Hand", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # if len(lmList) != 0:
            #     print(lmList)

        # Show the Frame
        cv2.imshow("Hand Tracking", frame)
        
        time.sleep(.25)
        print(i)
        i+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()