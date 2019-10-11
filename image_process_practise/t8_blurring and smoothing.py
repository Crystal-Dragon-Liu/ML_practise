# -*- coding: utf-8 -*-
import cv2
import numpy as np

#cap = cv2.VideoCapture('F:/python/image/vs_2.mp4')
cap =cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lower_red = np.array([150, 150, 50])
    #upper_red = np.array([180, 255, 150])

    lower_red = np.array([100, 43, 46])
    upper_red = np.array([124, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    #lower_red 表明低于这个lower_red的值，图像值变为0
    #upper_red 表明高于这个upper_red的值，图像值变为0
    #在这个区间内图像值变为225
    res = cv2.bitwise_and(frame, frame, mask=mask)


    #使用自定义内核对图像进行卷积
    #kernel = np.random.randn(15, 15)/225
    #kernel = np.array(([0.0625,0.125,0.0625], [0.125,0.25,0.125],[0.0625,0.125,0.0625]))
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)

    blur = cv2.GaussianBlur(res,(15,15),0)
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)


    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    #cv2.imshow('smoothed',smoothed)
    cv2.imshow('Gblur',blur)
    cv2.imshow('Mblur',median)
    cv2.imshow('bi',bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处代码是防止bug? ord 是将字符转化为相应整数
        # waitkey(1) 参数为1 表示延时1ms切换到下一帧图像
        # 0 视频暂停
        # 1000 延时太久，卡顿
        break
cv2.destroyAllWindows()
cv2.release()