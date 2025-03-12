import cv2
import mediapipe as mp
import time
# import HandTrackingModule as htm
# from cvzone.HandTrackingModule import HandDetector

class handDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectioncon=0.5, trackcon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectioncon, self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):
        lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)

                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 0), cv2FILLED)
        
        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw = True)
        lmList = detector.findPosition(img, draw = False)

        if len(lmList) != 0:
            cv2.circle(img, (lmList[1][1], lmList[1][2]), 15, (255, 0, 0), cv2.FILLED)
            print(lmList[1])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()
