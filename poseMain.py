import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)

i=0

while True:
    succuss, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    myList = []
    text=None

    if results.pose_landmarks:

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            myList.append([id, cx, cy])

            cv2.circle(img, (cx, cy), 7, (0, 0, 0), cv2.FILLED)

        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    if len(myList) != 0:
        # print(myList[16][1],"x")
        # print(myList[16][2],"y")
        # print(myList[12][1],"x")
        # print(myList[12][2],"y")
        # cv2.circle(img, (myList[12][1], myList[12][2]), 15, (255, 0, 0), cv2.FILLED)
        # cv2.circle(img, (myList[16][1], myList[16][2]), 15, (255, 0, 0), cv2.FILLED)

        if abs(myList[16][1] - myList[15][1]) <= 80 and abs(myList[16][2] - myList[15][2]) <= 40 and abs(myList[12][1] - myList[16][1]) <= 70 and abs(myList[12][2] - myList[16][2]) <= 40:
            print("สวัสดีชาวโลก")
            text="Hello!"
        elif abs(myList[19][1] - myList[20][1]) <= 120 and abs(myList[19][2] - myList[20][2]) <= 110 and abs(myList[19][1] - myList[12][1]) >= 80 and abs(myList[19][2] - myList[12][2]) >= 140:
            print("ขอโทษ")
            text="Sorry"
    
    cv2.putText(img, text, (300,100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    print(i)
    i +=1
    cv2.imshow("image", img)

    time.sleep(.1)

    if cv2.waitKey(1) == ord("q"):
        break
