import cv2
import time
import os
import HandDetector as htm
import math

wCam, hCam = 640, 480

POINTER = 8
MIDDLE = 12
RING = 16
PINKY = 20
THUMB = 4

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0

detector = htm.handDetector(detectionCon=0.7, trackCon=0.9)

while True:
    success, img = cap.read()
    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        
        pointerBent = detector.fingerBent(POINTER, -.65)
        middleBent = detector.fingerBent(MIDDLE, -.65)
        ringBent = detector.fingerBent(RING, -.65)
        pinkyBent = detector.fingerBent(PINKY, -.65)
        
        fingers = [pointerBent, middleBent, ringBent, pinkyBent]
        fingerCount = 0
        
        for fingerBent in fingers:
            if not fingerBent:
                fingerCount += 1
        
        
        if fingerCount == 4:
            print("paper")
        elif fingerCount > 1:
            print("scissors")
        else:
            print("rock")
            
    
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)