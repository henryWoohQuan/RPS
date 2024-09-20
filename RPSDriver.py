import cv2
import time
import RPSDetector
from cvButton import cvButton

# cam width and height
wCam, hCam = 640, 480

playButton = cvButton(25, (395, 120), "Play Game", (255, 0, 0))


# mp indices for each finger
POINTER = 8
MIDDLE = 12
RING = 16
PINKY = 20
THUMB = 4

# setting up camera
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0

detector = RPSDetector.rpsDetector(detectionCon=0.7, trackCon=0.9)

while True:
    # reading camera + finding hands using mp + finding positions of joints
    success, img = cap.read()
    img = cv2.flip(img, 1)
    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        result = detector.rockPaperOrScissors()
    
    if(playButton.drawButton(img, lmList)):
        print("pushed")
    
        
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (30, 40), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)