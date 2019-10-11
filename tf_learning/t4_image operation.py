#-*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('F:/python/image/watch_sample.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
print(px)
img[55,55] = [255,255,255] #设定颜色
#region of image
roi = img[100:150, 100:150]
img[100:150,100:150] = [0,255,255] # 在img[100:150,100:150]区域中的方块会全都变为黑色

watch_face = img[37:111,107:194] #74*87
img[0:74,0:87] = watch_face



cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
