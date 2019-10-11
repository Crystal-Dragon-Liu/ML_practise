#-*- coding: utf-8 -*-
import cv2
import numpy as np


img1 = cv2.imread('F:/python/image/3dmatplotlib.png')
img2 = cv2.imread('F:/python/image/3dmatplotlib1.png')
img3 = cv2.imread('F:/python/image/python_logo.jpg')
#add = img1 + img2
#add =cv2.add(img1,img2) #cv2.add 是图像像素颜色相加

#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0) #实际上也是加法，只不过是按比例混合起来，有不同的权重 ，给人一种混合的或者透明的感觉
#公式如下
#g (x) = (1 − α)f0 (x) + αf1 (x)   #a→（0，1）不同的a值可以实现不同的效果
#cv2.imshow('add', weighted)


rows,cols,channels = img3.shape
roi = img1[0:rows,0:cols]
img3gray =cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV) #小于220 变成255 ，大于220 变为1
#Python: cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
# thresh 初始值 maxval 最大值 type 表示划分的时候使用什么类型算法
#THRESH_BINARY_INV 如图片源像素颜色>220,则将变为0 如果是其他的就变成max
mask_inv  = cv2.bitwise_not(mask)
#bitwise_not 对二进制数据进行非操作
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv) #xor

img3_fg = cv2.bitwise_and(img3,img3,mask=mask)

dst = cv2.add(img1_bg,img3_fg)
#cv2.imshow('v',img1)
img1[0:rows,0:cols] = dst

#cv2.imshow('r',img3)

#cv2.imshow('img3g',img3gray)
#cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
#cv2.imshow('img3_fg',img3_fg)
cv2.imshow('img1_bg',img1_bg)
#cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
