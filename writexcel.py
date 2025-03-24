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
main=pd.read_excel('data/Runout.xlsx')
main=pd.DataFrame(main)
count = 2
for i in range(count-1):
    # print(count)
    count-=1
    time.sleep(1)
print("<Start capture>")

cap = cv2.VideoCapture(0)
    
for i in range(1):
    # print(i+1)
    succus, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("image", img)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # results = pose.process(imgRGB)
    results1 = hands.process(imgRGB)
    data=[]
    # for i in range(21):
    #    data.append("LHx"+str(i):[0])
    #    data.update("LHy"+str(i):[0])
    # for i in range(21):
    #    data.update({"RHx"+str(i):[0]})
    #    data.update({"RHy"+str(i):[0]})
    # for i in range(33):
    #    data.update({"Bx"+str(i):[0]})
    #    data.update({"By"+str(i):[0]})
    hmm = 1  
    if results1.multi_hand_landmarks:
        LeftHand=[]
        RightHand = []
        for idx, hand_landmarks in enumerate(results1.multi_hand_landmarks):
            # print(hand_landmarks)
        #     hmm+=1
            handedness = results1.multi_handedness[idx].classification[0].label
            if handedness:
                # print(handedness,"<---",idx)
                # for handLms in results1.multi_hand_landmarks:
                #     print(handLms)
                    # print(hmm)
                    # hmm+=1
                    for id, lm in enumerate(hand_landmarks.landmark):
                        # print(lm.x)
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if handedness:                        
                            if handedness == "Left":
                                LeftHand.append(cx)
                                LeftHand.append(cy)
                                # LeftHand.append(idx)
                            elif handedness == "Right":
                                RightHand.append(cx)
                                RightHand.append(cy)
                                # RightHand.append(idx)
                                
        if len(LeftHand) == 0:
            for i in range(42):
                LeftHand.append(0)
        if len(RightHand) == 0:
            for i in range(42):
                RightHand.append(0)
        data.extend(LeftHand)
        data.extend(RightHand)
        print(data)
        print(len(data))

    # if results.pose_landmarks:
    #     for id, lm in enumerate(results.pose_landmarks.landmark):
    #         h, w, c = img.shape
    #         cx, cy = int(lm.x*w), int(lm.y*h)

            # data["Bx"+str(id)] = [str(cx)]
            # data["By"+str(id)] = [str(cy)]



    # data=pd.DataFrame(data)
    # main = pd.concat([main, data], ignore_index=True)
    time.sleep(2)
    cv2.waitKey(1)

# main.to_excel('data/Runout.xlsx')
print("Cupture complete")



