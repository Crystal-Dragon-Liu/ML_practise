# -*- coding: utf-8 -*-
import cv2
import numpy as np

#cap = cv2.VideoCapture('F:/python/image/vs_4.mp4')
cap =cv2.VideoCapture(0)
while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    fg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(fg,100,200)
    #cv2.imshow('original',frame)
    #cv2.imshow('lap',laplacian)
    #cv2.imshow('sobelx', sobelx)
    #cv2.imshow('sobely', sobely)
    cv2.imshow('cann',edges)









    if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处代码是防止bug? ord 是将字符转化为相应整数
        # waitkey(1) 参数为1 表示延时1ms切换到下一帧图像
        # 0 视频暂停
        # 1000 延时太久，卡顿
        break
cv2.destroyAllWindows()
cv2.release()