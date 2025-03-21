import cv2

cap = cv2.VideoCapture(0)

while True:
    succuss, img = cap.read()
    cv2.imshow("image", img)