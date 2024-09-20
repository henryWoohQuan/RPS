import cv2

class cvButton:
    def __init__(self, holdTime, botLeft, label, color):
        self.time = 0
        self.pushed = False
        self.holdTime = holdTime
        boxSize = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 3)
        self.left = botLeft[0]
        self.bot = botLeft[1]
        self.right = self.left + boxSize[0][0]
        self.top = self.bot - boxSize[0][1]
        self.label = label
        self.color = color
        
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
    
    def drawButton(self, img, lmList):
        buttonResult = 0
        # if hand is on screen and hovering the button, increase the percentPressed up to holdTime
        if len(lmList) != 0 and self.isHovered(lmList): 
            buttonResult = self.push(True)
        elif len(lmList) != 0:
            buttonResult = self.push(False)
        difference = self.right + 5 - self.left
        percentPressed = int(difference * buttonResult)
        
        # drawing button percentage bar and outline, then drawing button label over it
        cv2.rectangle(img, (self.left - 5, self.top - 5), ((self.left - 5 + percentPressed), self.bot + 12), self.color, -1)
        cv2.rectangle(img, (self.left - 5, self.top - 5), (self.right, self.bot + 12), self.color, 1)
        cv2.putText(img, self.label, (self.left, self.bot), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        
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