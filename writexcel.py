import cv2
import mediapipe as mp
import time
import pandas as pd
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
main=pd.read_excel('data/test.xlsx')
main=pd.DataFrame(main)
count = 4
for i in range(3):
    print(count)
    count-=1
    time.sleep(1)
print("<Start capture>")
cap = cv2.VideoCapture(0)
    
for i in range(100):
    print(i+1)
    succuss, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("image", img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    results1 = hands.process(imgRGB)
    data={}
    for i in range(21):
       data.update({"LHx"+str(i):[0]})
       data.update({"LHy"+str(i):[0]})
    for i in range(21):
       data.update({"RHx"+str(i):[0]})
       data.update({"RHy"+str(i):[0]})
    for i in range(33):
       data.update({"Bx"+str(i):[0]})
       data.update({"By"+str(i):[0]})

    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            data["Bx"+str(id)] = [str(cx)]
            data["By"+str(id)] = [str(cy)]

    if results1.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results1.multi_hand_landmarks):
            handedness = results1.multi_handedness[idx].classification[0].label
            for handLms in results1.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if handedness == "Left":
                        data["LHx"+str(id)] = [str(cx)]
                        data["LHy"+str(id)] = [str(cy)]
                    elif handedness == "Right":
                        data["RHx"+str(id)] = [str(cx)]
                        data["RHy"+str(id)] = [str(cy)]


    data=pd.DataFrame(data)
    main = pd.concat([main, data], ignore_index=True)
    time.sleep(.1)
    cv2.waitKey(1)

main.to_excel('data/No.xlsx')
print("Cupture complete")