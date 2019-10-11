# -*- coding: utf-8 -*-
import cv2
import numpy as np

cap = cv2.VideoCapture('F:/python/image/vs_4.mp4')
#cap =cv2.VideoCapture(0)
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

    kernel = np.ones((15,15), np.uint8)
    erosion = cv2.erode(res,kernel)
    dilation = cv2.dilate(erosion,kernel,iterations=1)
    '''
腐蚀：腐蚀会把物体的边界腐蚀掉，卷积核沿着图象滑动，如果卷积核对应的原图的所有像素值为1，那么中心元素就保持原来的值，否则变为零。主要应用在去除白噪声，也可以断开连在一起的物体。

膨胀：卷积核所对应的原图像的像素值只要有一个是1，中心像素值就是1。一般在除噪是，先腐蚀再膨胀，因为腐蚀在去除白噪声的时候也会使图像缩小，所以我们之后要进行膨胀。当然也可以用来将两者物体分开。
————————————————
版权声明：本文为CSDN博主「SongpingWang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wsp_1138886114/article/details/82917661
'''
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #先腐蚀，再膨胀 排除小团的物体
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel) #先膨胀再腐蚀，排除小型黑洞

    #cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('ero', erosion)
    cv2.imshow('di', dilation)

    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)



    if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处代码是防止bug? ord 是将字符转化为相应整数
        # waitkey(1) 参数为1 表示延时1ms切换到下一帧图像
        # 0 视频暂停
        # 1000 延时太久，卡顿
        break
cv2.destroyAllWindows()
cv2.release()