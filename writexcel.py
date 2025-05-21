import cv2
import mediapipe as mp
import time
import pandas as pd
from openpyxl import load_workbook

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpHands = mp.solutions.hands
hands = mpHands.Hands(2)
mpDraw = mp.solutions.drawing_utils

main='data/Runout4000.xlsx'
# output = 

cap = cv2.VideoCapture(0)

# load = load_workbook(main)
# loaded = load.active
count = 6

for i in range(count-1):
    print(count)
    count-=1
    time.sleep(1)
print("<Start capture>")
reminder=[]   
for i in range(4000):
    print(i+1)
    succus, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("image", img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    results1 = hands.process(imgRGB)
    data=[]
    LeftHand=[]
    RightHand = []
    Pose = []
    if results1.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results1.multi_hand_landmarks):
            handedness = results1.multi_handedness[idx].classification[0].label
            if handedness:
                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if handedness:                        
                            if handedness == "Left" and len(LeftHand) < 42:
                                LeftHand.append(cx)
                                LeftHand.append(cy)
                            elif handedness == "Right" and len(RightHand) < 42:
                                RightHand.append(cx)
                                RightHand.append(cy)
    if len(LeftHand) == 0:
        for i in range(42):
            LeftHand.append(0)
    if len(RightHand) == 0:
        for i in range(42):
            RightHand.append(0)
    data.extend(LeftHand)
    data.extend(RightHand)

    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            Pose.append(cx)
            Pose.append(cy)
            
    if len(Pose) == 0:
        for i in range(66):
            Pose.append(0)
    data.extend(Pose)    
    reminder.extend([data])
    # time.sleep(.001)
    cv2.waitKey(1)
# loaded.append(reminder)
# load.save(main)
reminder = pd.DataFrame(reminder)
reminder.to_excel(main)
print("Cupture complete")