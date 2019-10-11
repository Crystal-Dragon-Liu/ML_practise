#-*- coding: utf-8 -*-
import cv2
import numpy as np
cap = cv2.VideoCapture('F:/python/image/video_sample.mp4')
#0 表示打开笔记本的内置摄像头，如果参数为路径则 按路径打开视频

fourcc = cv2.VideoWriter_fourcc(*'XVID') #指定编码器
#fourcc = -1
out = cv2.VideoWriter('F:/python/image/output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(frame)
    cv2.imshow('gray', gray) #显示灰色视频
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):#此处代码是防止bug? ord 是将字符转化为相应整数
        #waitkey(1) 参数为1 表示延时1ms切换到下一帧图像
        #0 视频暂停
        #1000 延时太久，卡顿
        break
cap.release()
out.release()
cv2.destroyAllWindows()
