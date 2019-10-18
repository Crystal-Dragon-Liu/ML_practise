#!/usr/local/bin/python3.7

import cv2
import numpy as np

img_bgr = cv2.imread('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock.jpeg')

gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)
ret, binary = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV )

binary = cv2.bitwise_not(binary)

#cv2.imshow('binary',binary)
#形态学开运算 去除小的白噪声

kernel = np.ones((3, 3),np.uint8)
opening =  cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel,iterations=2)

#cv2.imshow('opening',opening)
#closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE,kernel,iterations=2)

#形态学闭运算 去除物体的小洞

#确定背景区域
sure_bg = cv2.dilate(opening,kernel,iterations=3)
#cv2.imshow('sure_bg',sure_bg)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)


#显示骨骼
distance =cv2.normalize(dist_transform,0,1.0,cv2.NORM_MINMAX)



#cv2.imshow('dist_out',distance*50)
#print(type(dist_transform))
#print(dist_transform.max())
ret, sure_fg = cv2.threshold(dist_transform, 0.2*dist_transform.max() , 255, 0)
#cv2.imshow('sure_fg',sure_fg)
#靠近物体中心的区域是前景，远离物体的区域是背景



#找到不确定的区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
cv2.imshow('unknown',unknown)
#marker labelling
ret,markers = cv2.connectedComponents(sure_fg)

np.set_printoptions(threshold=np.inf)
#print(markers)
markers = markers +1
#print(markers)
markers[unknown==255] = 0

markers = cv2.watershed(img_bgr,markers)
img_bgr[markers == -1] = [250,206,135]



afterwatershed = cv2.convertScaleAbs(markers)

colorTab = np.zeros((np.max(markers)+1,3))
for i in range(len(colorTab)):
    aa = np.random.uniform(0, 255)
    bb = np.random.uniform(0, 255)
    cc = np.random.uniform(0, 255)
    colorTab[i] = np.array([aa, bb, cc], np.uint8)
bgrImage = np.zeros(img_bgr.shape,np.uint8)

#遍历marks每一个元素值，对每一个区域进行颜色填充
for i in range(markers.shape[0]):
    for j in range(markers.shape[1]):
        #index值一样的像素表示在一个区域
        index = markers[i][j]
        #判断是不是区域与区域之间的分界,如果是边界(-1)，则使用白色显示
        if index == -1:
            bgrImage[i][j] = np.array([255,255,255])
        else:
            bgrImage[i][j]  = colorTab[index]
cv2.imshow('After ColorFill',bgrImage)

#填充后与原始图像融合
result = cv2.addWeighted(img_bgr,0.6,bgrImage,0.4,0)
cv2.imshow('addWeighted',result)
#cv2.imshow('aft',afterwatershed)

#cv2.imshow('img_bgr',img_bgr)
#cv2.imshow('unknown',unknown)
#cv2.imshow('sure_fg',sure_fg)
#cv2.imshow('binary',binary)
#cv2.imshow('opening',opening)
#cv2.imshow('closing',closing)
#cv2.imshow('dilate',sure_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
