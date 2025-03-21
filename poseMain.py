import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

i=0

while True:
    succuss, img = cap.read()
    
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    # imgRGB1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results1 = hands.process(imgRGB)

    myList = []
    RightH = []
    LeftH=[]
    text=None

    if results.pose_landmarks:

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            myList.append([id, cx, cy])

            cv2.circle(img, (cx, cy), 7, (0, 0, 0), cv2.FILLED)

        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
    if results1.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results1.multi_hand_landmarks):
            handedness = results1.multi_handedness[idx].classification[0].label
            for handLms in results1.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 7, (240, 255, 85), cv2.FILLED)
                    if handedness == "Left":
                        LeftH.append(['left',id,cx,cy])
                    elif handedness == "Right":
                        RightH.append(['right',id,cx,cy])

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if len(myList) != 0:
        print(myList)
    # #     # print(myList[16][1],"x")
    # #     # print(myList[16][2],"y")
    # #     # print(myList[12][1],"x")
    # #     # print(myList[12][2],"y")
    # #     # cv2.circle(img, (myList[12][1], myList[12][2]), 15, (255, 0, 0), cv2.FILLED)
    # #     # cv2.circle(img, (myList[16][1], myList[16][2]), 15, (255, 0, 0), cv2.FILLED)

    #     if abs(myList[16][1] - myList[15][1]) <= 80 and abs(myList[16][2] - myList[15][2]) <= 40 and abs(myList[12][1] - myList[16][1]) <= 90 and abs(myList[12][2] - myList[16][2]) <= 40:
    #         print("สวัสดีชาวโลก")
    #         text="Hello!"
    #     elif abs(myList[19][1] - myList[20][1]) <= 120 and abs(myList[19][2] - myList[20][2]) <= 110 and abs(myList[19][1] - myList[12][1]) >= 80 and abs(myList[19][2] - myList[12][2]) >= 100:
    #         print("ขอโทษ")
    #         text="Sorry"
    
    if len(RightH)!=0:
        print(RightH)
    if len(LeftH)!=0:
        print(LeftH)

    
    cv2.putText(img, text, (300,100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    print(i)
    i +=1
    
    cv2.imshow("image", img)

    time.sleep(.1)

    if cv2.waitKey(1) == ord("q"):
        break
