import cv2
import time

class Button:
    def __init__(self, holdTime, botLeft, label, textSize,  color):
        self.time = 0
        self.pushed = False
        self.holdTime = holdTime
        self.textSize = textSize
        boxSize = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, textSize, 3)
        self.width = boxSize[0][0]
        self.height = boxSize[0][1]
        self.left = botLeft[0]
        self.bot = botLeft[1]
        self.right = self.left + self.width
        self.top = self.bot - self.height
        self.label = label
        self.color = color
        
    def setPos(self, botLeft):
        self.left = botLeft[0]
        self.bot = botLeft[1]
        self.right = self.left + self.width
        self.top = self.bot - self.height
        
        
    def reset(self):
        self.time = 0
        self.pushed = False

    def push(self, isHeld):
        if self.time == 0:
            self.time = time.time()
        
        cTime = time.time()
        elapsedTime = cTime - self.time

        if not isHeld:
            self.reset()
            return 0
        elif elapsedTime >= self.holdTime and not self.pushed:
            self.pushed = True
            return 1
        
        if elapsedTime / self.holdTime > 1:
            return 1
        return elapsedTime / self.holdTime

    def drawButton(self, img, lmList, draw):
        buttonResult = 0
        if len(lmList) != 0 and self.isHovered(lmList) and draw:
            buttonResult = self.push(True)
        elif len(lmList) != 0 and draw:
            buttonResult = self.push(False)
        else:
            self.reset()
        difference = self.right + 5 - self.left
        percentPressed = int(difference * buttonResult)
        
        # drawing button percentage bar and outline, then drawing button label over it
        if draw:
            cv2.rectangle(img, (self.left - 5, self.top - 5), ((self.left - 5 + percentPressed), self.bot + 12), self.color, -1)
            cv2.rectangle(img, (self.left - 5, self.top - 5), (self.right, self.bot + 12), self.color, 1)
            cv2.putText(img, self.label, (self.left, self.bot), cv2.FONT_HERSHEY_SIMPLEX, self.textSize, (255, 255, 255), 3)
        
        # returns whether or not the button was fully pushed
        return self.pushed
    
    def isHovered(self, lmList):
        TRPALM = 17
        BLPALM = 2
        
        handLeft = lmList[BLPALM][1]
        handBot = lmList[BLPALM][2]
        handRight = lmList[TRPALM][1]
        handTop = lmList[TRPALM][2] 
        
        return (handLeft < self.right + 20 and handBot > self.top - 20) and (self.left - 20 < handRight and self.bot + 30 > handTop)
    
    
                
        