# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:51:46 2013

@author: Mars
"""

from matplotlib.patches import Circle
from matplotlib import pyplot as plt
import pygame, sys, random

pygame.init()
screen=pygame.display.set_mode([244,300])
screen.fill([0,0,0])
red = [83,112,24,147,50,214]
gre = [64,103,21,151,37,182]
blu = [58,86,21,130,34,52]
for i in range (255):
	s = random.randint(0,5)
	r = red[s]
	g = gre[s]
	b = blu[s]
	x = random.randint(0,640)
	y = random.randint(0,480)
	ballsize = random.randint(15,35)
	border = random.randint(0,10)
	pygame.draw.circle(screen,[r,g,b],[x,y],ballsize,border)
	pygame.display.flip()
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
#import matplotlib.pyplot as plt
#circle1=plt.Circle((0,0),.2,color='r')
#circle2=plt.Circle((.5,.5),.2,color='b')
#circle3=plt.Circle((1,1),.2,color='g',clip_on=False)
#fig = plt.gcf()
#fig.gca().add_artist(circle1)
#fig.gca().add_artist(circle2)
#fig.gca().add_artist(circle3)

#from Tkinter import *
#canvas = Canvas(width=300, height=300, bg='white')
#canvas.pack(expand=YES, fill=BOTH)
#
#canvas.create_oval(10, 10, 200, 200, width=2, fill=(22,22,22))
#
#mainloop()

'''
import pygame
import random
#创建一个窗口  
screen_size = (640, 480)  
screen = pygame.display.set_mode(screen_size, 0, 32)  
drawcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))  
top = random.randint(0,400)  
left = random.randint(0,500)  
width = random.randint(0,5)  
#画圆  
radiu = random.randint(width,100)  
pygame.draw.circle(screen, drawcolor, [top, left], radiu, width)  
'''