# -*- coding: utf-8 -*-
import cv2
import numpy as np


img_bgr = cv2.imread('F:/python/image/opencv-template-matching-python-tutorial.jpg')


img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
template = cv2.imread('F:/python/image/opencv-template-for-matching.jpg',0)

w, h = template.shape[::-1]  #从最后一个元素到第一个 翻转

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

thershold = 0.9

loc = np.where(res >= thershold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr,pt,(pt[0]+w, pt[1]+h), (0, 255, 255), 2)
cv2.imshow('img',img_bgr)
#cv2.imshow('detected', img_bgr)
cv2.waitKey(0)


