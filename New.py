import cv2
import time
ready=False
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
changed = "Question"
count=5
end=5
for i in range(count):

    print(count)
    count-=1
    time.sleep(1)
    if i+1==end:
        ready=True
print("Ready!!!")
if ready:
    for i in range(100):
        save_path = f"TestPose/{changed}/captured_image{i}.jpg" 
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if ret:
            cv2.imwrite(save_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 20])
        
cap.release()
cv2.destroyAllWindows()
print("Finish")