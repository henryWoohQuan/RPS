import cv2

class cvButton:
    def __init__(self, holdTime, botLeft, textSize, label):
        self.time = 0
        self.pushed = False
        self.holdTime = holdTime
        boxSize = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, textSize, 3)
        self.left = botLeft[0]
        self.bot = botLeft[1]
        self.right = self.left + boxSize.width
        self.top = self.bot + boxSize.height
        
    def push(self, isHeld):
        self.time += 1
        if not isHeld:
            self.time = 0
            self.pushed = False
            return 0
        elif self.time >= self.holdTime and not self.pushed:
            self.pushed = True
            return 1
        if self.time / self.holdTime > 1:
            return 1
        return self.time / self.holdTime
    
    def getTopLeft(self):
        return (self.left, self.top)
    
    def getBotRight(self):
        return (self.right, self.bot)
    
    def drawButton(self, img, lmList):
        buttonResult = 0
        if len(lmList) != 0 and self.isHovered(lmList):
            buttonResult = self.push(True)
        elif len(lmList) != 0:
            buttonResult = self.push(False)
            
        difference = self.right - self.left
        percentPressed = int(difference * buttonResult)
        
        cv2.rectangle(img, (self.left, self.top), ((self.left + percentPressed), self.bot), (0, 0, 0), -1)
        cv2.rectangle(img, (self.left, self.top), (self.right, self.top), (0, 0, 0), 1)
        cv2.putText(img, f'Play a Game', (400, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        return self.pushed
    
    def isHovered(self, lmList):
        TRPALM = 17
        BLPALM = 2
        
        handLeft = lmList[BLPALM][1]
        handBot = lmList[BLPALM][2]
        handRight = lmList[TRPALM][1]
        handTop = lmList[TRPALM][2] 
        
        return (handLeft < self.right and handBot < self.top) and (self.left < handRight and self.bot < handTop)