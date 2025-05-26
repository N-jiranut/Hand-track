import cv2
import mediapipe as mp
import numpy as np
import pickle
import joblib

model = joblib.load('ML-model/gpt-pose_model_max.pkl')

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
hands = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)
    results = pose.process(image)
    results_hand = hands.process(image)
    
    LeftHand=[]
    RightHand = []
    row=[]
    start=0
    if results_hand.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results_hand.multi_hand_landmarks):
            handedness = results_hand.multi_handedness[idx].classification[0].label
            for id, lm in enumerate(hand_landmarks.landmark):
                if handedness:                        
                    if handedness == "Left" and len(LeftHand) < 42:
                        LeftHand.extend([lm.x,lm.y])
                    elif handedness == "Right" and len(RightHand) < 42:
                        RightHand.extend([lm.x,lm.y])
    if len(LeftHand) == 0:
        LeftHand=[0 for n in range(42)]     
    if len(RightHand) == 0:
        RightHand=[0 for n in range(42)]     
    row.extend(LeftHand)
    row.extend(RightHand)
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        for lm in landmarks:
            row.extend([lm.x, lm.y, lm.z])
            
        X_input = np.array(row).reshape(1, -1)
        prediction = model.predict(X_input)
        cv2.putText(frame, f'Pose: {prediction[0]}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Pose Classification', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
