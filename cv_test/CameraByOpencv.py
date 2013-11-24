# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:06:30 2013

@author: Avaziyi
"""

import cv
cam = cv.CaptureFromCAM(-1)
cv.GrabFrame(cam)
img = cv.RetrieveFrame(cam)
cv.SaveImage("opentest.jpg", img)