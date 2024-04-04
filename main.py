import pygame as pg
import sys
from pygame.locals import *
from image import *
from const import *
from objectbase import ObjectBase
from BuBu import BubuBase



pg.init()

screen = pg.display.set_mode(GAME_SIZE)
label = pg.display.set_caption('一二！大战！布布！')
background = Image(PATH_BACK,0,GAME_SIZE)
bubu01 = BubuBase('/Users/bochengji/Documents/BuBuVSYiEr/ImgaeCollection/bubu/bubu01/%d.png',0,(150,150),(1850,100),5)



while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    background.draw(screen)
    bubu01.draw(screen)
    bubu01.update()
    pg.display.update()



