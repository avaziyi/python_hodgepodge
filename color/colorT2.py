# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:53:09 2013

@author: Avaziyi
"""

import Image, ImageDraw, sys
from scipy import ones
from matplotlib import pyplot as p

strip_h, strip_w = 100, 720
strip = 255*ones((strip_h,strip_w,3), dtype='uint8')
image_val = Image.fromarray(strip)
image_sat = Image.fromarray(strip)
draw0 = ImageDraw.Draw(image_val)
draw1 = ImageDraw.Draw(image_sat)
for y in xrange(strip_h):
  sys.stderr.write('.')
  for x in xrange(strip_w):
    draw0.point([x, y], fill='hsl(%d,%d%%,%d%%)'%(x%360,y,50))
    draw1.point([x, y], fill='hsl(%d,%d%%,%d%%)'%(x%360,100,y))

p.subplot(2,1,1)
p.imshow(image_val)
p.subplot(2,1,2)
p.imshow(image_sat)
p.show()