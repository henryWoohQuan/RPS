import cv2
import mediapipe as mp
import math


class rpsDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, 1, self.detectionCon, self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        return img

    def findPosition(self, img, handNo=0, draw= True):
        self.lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return self.lmList
    
    def fingerBent(self, fingerID, bentCon): 
        tip = fingerID
        mid = fingerID - 2
        knuc = fingerID - 3
        axDiff = (self.lmList[tip][1] - self.lmList[mid][1])
        ayDiff = (self.lmList[tip][2] - self.lmList[mid][2])
        a = math.sqrt(axDiff * axDiff + ayDiff * ayDiff) #distance from 8 to 6
        bxDiff = (self.lmList[mid][1] - self.lmList[knuc][1])
        byDiff = (self.lmList[mid][2] - self.lmList[knuc][2])
        b = math.sqrt(bxDiff * bxDiff + byDiff * byDiff) #distance from 6 to 5
        cxDiff = (self.lmList[tip][1] - self.lmList[knuc][1])
        cyDiff = (self.lmList[tip][2] - self.lmList[knuc][2])
        c = math.sqrt(cxDiff * cxDiff + cyDiff * cyDiff) #distance from 8 to 5
        
        #law of cos to get the angle at point 5
        angle = ((b * b) + (a * a) - (c * c)) / (2 * a * b)
        
        return angle > bentCon
    
    def rockPaperOrScissors(self):
        pointerBent = self.fingerBent(8, -.65)
        middleBent = self.fingerBent(12, -.65)
        ringBent = self.fingerBent(16, -.65)
        pinkyBent = self.fingerBent(20, -.65)
        
        fingers = [pointerBent, middleBent, ringBent, pinkyBent]
        fingerCount = 0
         
        for fingerBent in fingers:
            if not fingerBent:
                fingerCount += 1
        
        if fingerCount == 4:
            return "p"
        elif not fingers[0] and not fingers[1]:
            return "s"
        else:
            return "r"
