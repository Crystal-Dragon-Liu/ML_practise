# -*- coding: utf-8 -*-
import cv2
import numpy as np
img_bgr = cv2.imread('F:/python/image/rock_1.jpg')
ig = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 二值化



ret, binary = cv2.threshold(ig, 100, 255, cv2.THRESH_BINARY_INV)
ret1, binary1 = cv2.threshold(ig, 90, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(
    binary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 107, 1)
mask = cv2.bitwise_not(binary)
ig_m = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)
contours, hierarchy = cv2.findContours(
    binary1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_bgr, contours, -1, (0, 255, ), 1)
# cv2.imshow('ga',gaus)
cv2.imshow('o', img_bgr)
cv2.imshow('m', mask)
cv2.imshow('ig_m', ig_m)

#cv2.imshow('b', binary)
# cv2.imshow('c',binary1)
cv2.waitKey(0)
