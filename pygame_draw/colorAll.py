# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:54:02 2013

@author: Avaziyi
"""

from random import *
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            # 画随机矩形
            rc = (randint(0,255), randint(0,255), randint(0,255))
            rp = (randint(0,639), randint(0,479))
            rs = (639-randint(rp[0], 639), 479-randint(rp[1], 479))
            pygame.draw.rect(screen, rc, Rect(rp, rs))
        if event.type==pygame.QUIT:
            sys.exit()	
    pygame.display.update()