#-*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture('F:/python/image/video_sample.mp4')

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res =cv2.bitwise_and(frame,frame,mask=mask)



    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):#此处代码是防止bug? ord 是将字符转化为相应整数
        #waitkey(1) 参数为1 表示延时1ms切换到下一帧图像
        #0 视频暂停
        #1000 延时太久，卡顿
        break
cv2.destroyAllWindows()
cv2.release()