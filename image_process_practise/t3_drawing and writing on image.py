#-*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('F:/python/image/watch_sample.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (150, 150), (255, 255, 0),15) # 255,0,0 代表蓝 BGR 15是line-width

cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

cv2.circle(img, (100, 63), 55, (0, 255, 0),-1)  # 55是 radius -1 是填充

pts  = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts  =pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (255, 255, 255), 1)


#write sth
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV Tuts! ', (0,130), font, 3, (200,255,255),2,cv2.LINE_AA) #3的位置代表大小，2位置代表字体粗细
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
