import cvzone
import cv2


cap=cv2.VideoCapture(0)
dedector=cvzone.HandDetector(maxHands=1,detectionCom=0.7)

while True:
    _,frame=cap.read()
    frame=dedector.findHands(frame)
    lmlist,bbox=dedector.findPosition(frame)
    if lmlist:
        fingers=dedector.fingersUp()
        print(fingers)
    cv2.imshow('armrobot',frame)
    cv2.waitKey(1)
