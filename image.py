from typing import Any
import pygame
import time
#from pygame.sprite import _Group


PLAYTIME = 0.2

class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt,pathIndex,size = None,position = (0,0),pathIndexCount = 0):
        super().__init__()
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathIndexCount = pathIndexCount
        self.size = size
        self.position = list(position)
        self.updateImage()

    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image,self.size)

    def updateSize(self,size):
        self.size = size
        self.updateImage()

    def update_index(self,pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.position

        return rect
    

    def doleft(self):
        self.position[0]-=1


    def draw(self,screen):
        screen.blit(self.image,self.getRect())




