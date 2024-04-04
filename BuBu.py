import objectbase
import time

class BubuBase(objectbase.ObjectBase):
    def __init__(self, pathFmt,pathIndex,size = None,position = (0,0),pathIndexCount = 0):
        super(BubuBase,self).__init__(pathFmt,pathIndex,size ,position, pathIndexCount)



    def checkImagePosition(self):
        b = super(BubuBase,self).checkImagePosition()
        if b:
            self.position[0]-=2
        return b