#!/usr/local/bin/python3.7

import cv2
import numpy as np
from PIL import Image
img_bgr = cv2.imread('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock_detection/rock_dataset_2/rock_dataset_2/1571146380553.jpg')


'''

img = Image.open('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock_detection/rock_dataset_2/rock_dataset_2/1571146380553.jpg')
resize_image = img.resize((640,480),Image.ANTIALIAS)
resize_image.save('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock_detection/rock_dataset_2/rock_dataset_2/1571146380553_1.jpg')
img = cv2.imread('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/rock_detection/rock_dataset_2/rock_dataset_2/1571146380553_1.jpg')
v2.imshow('origin',img)
'''
#cv2.imshow('origin',img_bgr)

#调整图片曝光度



def nothing(x):
    pass
def gamma_trans(img, gamma):
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。
def change_exposure():

 cv2.namedWindow('demo', 0)
 cv2.createTrackbar('Value of Gamma', 'demo', 140, 1000, nothing)

 value_of_gamma = cv2.getTrackbarPos('Value of Gamma', 'demo')
 value_of_gamma = value_of_gamma * 0.011
 image_gamma_correct = gamma_trans(img_bgr, value_of_gamma)
 return image_gamma_correct
image_g = change_exposure() #得到image的曝光度
#cv2.imshow('image_g',image_g)

gray = cv2.cvtColor(image_g, cv2.COLOR_BGR2GRAY)

#cv2.imshow('gray',gray)

ret, binary = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)
binary = cv2.bitwise_not(binary)
#图像均衡
fil = np.array([[ 1/6,1/6, 1/6],
                [ 1/6, 1/6, 1/6],
                [ 1/6, 1/6, 1/6]])


res = cv2.filter2D(gray,-1,fil)

ret_1, binary_1 = cv2.threshold(res, 70, 255, cv2.THRESH_BINARY_INV)
binary_1 = cv2.bitwise_not(binary_1)

cv2.imshow('binary', binary)
cv2.imshow('av',binary_1)

#形态学开运算，去除白噪声
kernel = np.zeros((1,1), np.uint32) +0.2
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

#cv2.imshow('opening', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''


#形态学开运算，去除白噪声
kernel = np.zeros((3, 3), np.uint8)+0.0006
kernel_1 = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_1, iterations=1)
closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel, iterations=1)
#cv2.imshow('opening',opening)
#cv2.imshow('closing',closing)

#确定背景
sure_bg = cv2.dilate(closing,kernel_1,iterations=3)
#cv2.imshow('sur_bg',sure_bg)

dist_transform = cv2.distanceTransform(closing, cv2.DIST_L1, 5)
distance = cv2.normalize(dist_transform, 0, 1000.0, cv2.NORM_MINMAX)
#cv2.imshow('dist',distance)


ret, sure_fg = cv2.threshold(distance, 0.1*distance.min(), 255, 0)


#cv2.imshow('sure_fg',sure_fg)

#找到不确定的区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
#cv2.imshow('unknown',unknown)
#marker labelling
ret,markers = cv2.connectedComponents(sure_fg)

np.set_printoptions(threshold=np.inf)
#print(markers)
markers = markers +2
#print(markers)
markers[unknown==255] = 0

markers = cv2.watershed(image_g,markers)
image_g[markers == -1] = [250,206,135]


cv2.imshow('water',image_g)


cv2.waitKey(0)
cv2.destroyAllWindows()
'''