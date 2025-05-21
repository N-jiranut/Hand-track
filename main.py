import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
i=1

while True:
    # LeftH=[]
    # RightH=[]
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    
    
    # if results.multi_hand_landmarks:
    #     for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
    #         handedness = results.multi_handedness[idx].classification[0].label
    #         for handLms in results.multi_hand_landmarks:
    #             for id, lm in enumerate(handLms.landmark):
    #                 h, w, c = img.shape
    #                 if id == 8:
    #                     cx, cy = int(lm.x * w), int(lm.y * h)
    #                     cv2.circle(img, (cx, cy), 7, (240, 255, 85), cv2.FILLED)
                    # if handedness == "Left":
                        # LeftH.append(['left',id,cx,cy])
                    # elif handedness == "Right":
                    #     RightH.append(['right',id,cx,cy])

                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # if len(LeftH)!=0:
    #     print(LeftH)
    # if len(RightH)!=0:
    #     print(RightH)

    print(i)
    i+=1
    cv2.imshow("image", img)
    time.sleep(.1)
    if cv2.waitKey(1) == ord("q"):
        break