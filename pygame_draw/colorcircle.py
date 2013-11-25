# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:20:54 2013

@author: Mars
"""
import random
import pygame, sys

width = 480
height = 640
pygame.init()
screen=pygame.display.set_mode([width, height])
screen.fill([0,0,0])
for i in range (255):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    x = random.randint(0,width)
    y = random.randint(0,height)
    ballsize = random.randint(15,35)
    border = random.randint(0,10)
    pygame.draw.circle(screen,[r,g,b],[x,y],ballsize,border)
    pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()		