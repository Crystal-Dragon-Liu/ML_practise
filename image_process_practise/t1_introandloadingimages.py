#-*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
#imread_grayscale -0
img = cv2.imread('F:/python/image/watch_sample.jpg',cv2.IMREAD_GRAYSCALE)
#imread_color - 1
#imrea_unchanged - -1

#显示图像

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.plot([600, 100], [100, 600], 'c', linewidth=5) #可以在图片上划跳直线
plt.show()
'''
cv2.imwrite('F:/python/image/watch_sample.png', img) #将img保存成png格式图片
