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

    if results.pose_landmarks:

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            myList.append([id, cx, cy])

            cv2.circle(img, (cx, cy), 7, (0, 0, 0), cv2.FILLED)

        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    if len(myList) != 0:
        print(myList[1])

    print(i)
    i +=1
    cv2.imshow("image", img)

    time.sleep(.25)

    if cv2.waitKey(1) == ord("q"):
        break
