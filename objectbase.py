from image import *


class ObjectBase(Image):
    def __init__(self, pathFmt,pathIndex,size = None,position = (0,0),pathIndexCount = 0):
        super(ObjectBase,self).__init__(pathFmt,pathIndex,size ,position, pathIndexCount)
        self.preIndexTime = 0
        self.prePositionTime = 0

    def update(self):
        self.checkImageIndex()
        self.checkImagePosition()
    

    def checkImageIndex(self):
        if time.time() - self.preIndexTime <= 0.3:
            return
        
        self.preIndexTime = time.time()
        index = self.pathIndex + 1
        if index >= self.pathIndexCount:
            index = 0
        self.update_index(index) 

    def checkImagePosition(self):
        if time.time() - self.prePositionTime <= 0.2:
            return False
        self.prePositionTime = time.time()
        return True
        