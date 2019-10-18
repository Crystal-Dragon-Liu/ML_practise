#!/usr/local/bin/python3.7

import cv2
import numpy as np

import matplotlib.pyplot as plt
#卷积核

kernel = np.ones((5, 5),np.uint8)+1.2

img_bgr = cv2.imread('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock.jpeg')
#print(list(img_bgr.shape))
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#print(gray.shape)    201,4100
#二值化
ret, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)

#gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 187, 1)
#翻转
binary = cv2.bitwise_not(binary)
#中值滤波
#median = cv2.medianBlur(binary, 3)
#median = cv2.bitwise_not(median)
#opening = cv2.morphologyEx(median, cv2.MORPH_CLOSE, kernel)

'''
kernel_1 = np.zeros((2,2),np.uint8)+1
ero = cv2.erode(opening, kernel_1)

'''

#closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)




#closing = cv2.bitwise_not(binary)
#closing = cv2.bitwise_not(closing)
#过滤
ig_m = cv2.bitwise_and(img_bgr,img_bgr,mask=binary)
#edges = cv2.Canny(ig_m,400,500)
bilateral = cv2.bilateralFilter(binary,15,75,75)
#寻找边缘
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_bgr, contours, -1, (0, 255, ), 1)


#膨胀
#dilation = cv2.dilate(binary,kernel,iterations=1)

#cv2.imshow('ero',ero)
#cv2.imshow('gaus',gaus)
cv2.imshow('o',img_bgr)
#cv2.imshow('m',median)
#cv2.imshow('oo',opening)
cv2.imshow('binary', binary)
#cv2.imshow('cl',closing)
cv2.imshow('ig_m', ig_m)
cv2.imshow('can',bilateral)
#cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

hist = cv2.calcHist([img_bgr],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()

'''
