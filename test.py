import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
i=0
while True:
    succuss, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:

        myHand = results.multi_hand_landmarks[0]

        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append([id, cx, cy])

        #     for id, lm in enumerate(handLms.landmark):
        #         h, w, c = img.shape
        #         cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 7, (0, 0, 0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    
    # print(results.multi_hand_landmarks)

    if len(lmList) != 0:
        print(lmList[1])

    print(i)
    i +=1

    cv2.imshow("image", img)

    time.sleep(.25)    

    if cv2.waitKey(1) == ord("q"):
        break
    