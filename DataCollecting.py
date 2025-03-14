import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture("PoseVideos/Hello1.jpg")

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
    cv2.circle(img, (myList[15][1], myList[15][2]), 15, (255, 0, 0), cv2.FILLED)
    cv2.circle(img, (myList[16][1], myList[16][2]), 15, (255, 0, 0), cv2.FILLED)
    print(myList[15])
    print(myList[16])

Nimg = cv2.resize(img, (850,700))

if myList[16][1] - myList[15][1] <= 600 and myList[16][2] - myList[15][2] <= 200:
    print("สวัสดีชาวโลก")

while True:
    cv2.imshow("image", Nimg)

    if cv2.waitKey(1) == ord("q"):
        break
