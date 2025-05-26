import cv2, glob, time, mediapipe, pandas

main = "data/Go_x.csv"
pose_number = 0

data_class = "Go"

total_data = []
images_path = glob.glob(f"TestPose/{data_class}/*.jpg")
pose = mediapipe.solutions.pose.Pose()
hands = mediapipe.solutions.hands.Hands()

for path in images_path:
    img = cv2.imread(path)
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("image", img)
    # cv2.waitKey(1)
    try:
        results_pose = pose.process(imgRGB)
        results_hand = hands.process(imgRGB)
    except:
        print("error occur!")
    else:
        data=[]
        LeftHand=[]
        RightHand = []
        Pose = []
        if results_hand.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results_hand.multi_hand_landmarks):
                handedness = results_hand.multi_handedness[idx].classification[0].label
                if handedness:
                        for id, lm in enumerate(hand_landmarks.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)                     
                            if handedness == "Left" and len(LeftHand) < 42:
                                LeftHand.append(cx)
                                LeftHand.append(cy)
                            elif handedness == "Right" and len(RightHand) < 42:
                                RightHand.append(cx)
                                RightHand.append(cy)
        if len(LeftHand) == 0:
            LeftHand.extend([0 for _ in range(42)])
        if len(RightHand) == 0:
            RightHand.extend([0 for _ in range(42)])
        data.extend(LeftHand)
        data.extend(RightHand)
        
        if results_pose.pose_landmarks:
            for id, lm in enumerate(results_pose.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                Pose.append(cx)
                Pose.append(cy)
        if len(Pose) == 0:
            Pose.extend([0 for _ in range(42)])
        data.extend(Pose)
        
        data.append(pose_number)
        
        total_data.extend([data])

df_data = pandas.DataFrame(total_data)
# df_data = df_data.drop(df_data.index[[0]])
df_data.to_csv(main, index=False)
print(f"Finish!")