# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

#卷积核

kernel = np.zeros((2,2),np.uint8)+1.5

img_bgr = cv2.imread('F:/python/image/rock.jpg')
#print(list(img_bgr.shape))
gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
#print(gray.shape)    201,414

#二值化
ret, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
#gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 187, 1)
#翻转
#binary = cv2.bitwise_not(binary)
#中值滤波
median = cv2.medianBlur(binary, 11)
#median = cv2.bitwise_not(median)
opening = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel)

'''
kernel_1 = np.zeros((2,2),np.uint8)+1
ero = cv2.erode(opening, kernel_1)

'''

closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)




closing = cv2.bitwise_not(closing)
#closing = cv2.bitwise_not(closing)
#过滤
ig_m = cv2.bitwise_and(img_bgr,img_bgr,mask=closing)


#寻找边缘
contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_bgr, contours, -1, (0, 255, ), 1)


#膨胀
#dilation = cv2.dilate(binary,kernel,iterations=1)

#cv2.imshow('ero',ero)
#cv2.imshow('gaus',gaus)
cv2.imshow('o',img_bgr)
cv2.imshow('m',median)
cv2.imshow('oo',opening)
#cv2.imshow('binary', binary)
#cv2.imshow('cl',closing)
cv2.imshow('ig_m', ig_m)
#cv2.imshow('dilation', dilation)

cv2.waitKey(0)

'''

hist = cv2.calcHist([img_bgr],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()

'''
