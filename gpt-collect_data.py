import cv2,numpy,pandas,glob,mediapipe

print("Starting....")

main = "data/gpt_maindata_max.csv"
pose_number = 4

data_class = "Backto"
images_path = glob.glob(f"TestPose/{data_class}/*.jpg")

pose = mediapipe.solutions.pose.Pose()
hands = mediapipe.solutions.hands.Hands()

data = []

for path in images_path:
    img = cv2.imread(path)
    img = cv2.flip(img, 1)

    results_pose = pose.process(img)
    results_hand = hands.process(img)
    
    LeftHand=[]
    RightHand = []
    row=[]
    start=0
    if results_hand.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results_hand.multi_hand_landmarks):
            handedness = results_hand.multi_handedness[idx].classification[0].label
            for id, lm in enumerate(hand_landmarks.landmark):
                if handedness:                        
                    if handedness == "Left" and len(LeftHand) < 42:
                        LeftHand.extend([lm.x,lm.y])
                    elif handedness == "Right" and len(RightHand) < 42:
                        RightHand.extend([lm.x,lm.y])
    if len(LeftHand) == 0:
        LeftHand=[0 for n in range(42)]     
    if len(RightHand) == 0:
        RightHand=[0 for n in range(42)]     
    row.extend(LeftHand)
    row.extend(RightHand)
    
    if results_pose.pose_landmarks:
        landmarks = results_pose.pose_landmarks.landmark
        for lm in landmarks:
            row.extend([lm.x, lm.y, lm.z])
    row.append(pose_number)
    
    data.append(row)

# บันทึกข้อมูลลงในไฟล์ CSV
df = pandas.DataFrame(data)
# df['label'] = labels
df.to_csv(main, mode='a', index=False, header=False)
# df.to_csv(main, index=False)
print("Process succussfully")