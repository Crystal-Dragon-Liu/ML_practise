#-*- coding: utf-8 -*-
import numpy as np
import PIL
import matplotlib.pylab as plt
import pickle
from PIL import Image
from pylab import *


NN = 4 ### number of categories
def binarize_image(img,threshold):
    """Binarize an image."""
     # convert image to monochrome
    img = np.array(img)
    image = binarize_array(img, threshold)
    return image

def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
                #将图片变为黑白

    print(numpy_array)
    return numpy_array

kk=1
zero10 = np.zeros(NN)

for i in range(3):
    for j in range(NN):
        if i<9:
           im = Image.open('F:/机器学习/ABCD/'+str(j+1)+'0'+str(i+1)+'.jpg')
        if i>=9:
           im = Image.open('F:/机器学习/ABCD/'+str(j+1)+str(i+1)+'.jpg')
        im2   = im.convert('L')
        im2  = im2.resize((32, 32), PIL.Image.ANTIALIAS) #变小
        imar  = np.array(im2)   #变为数组
        imarr = np.reshape(imar,[1024])  #变成1024
        thres = (imarr.max()*0.45+imarr.min()*0.55)   #所有数值乘以最大值，归一 变为0-1
        imar   = binarize_array(imar, thres)
        x0    = np.reshape( imar, [1, 1024] )/imar.max()
        if   kk==1:
            train_img = x0
            t_lab = zero10*0
            t_lab[j]=int(1)
            train_lab=t_lab
        if kk>1:
            train_img =np.vstack((train_img, x0))
            t_lab = zero10*0
            t_lab[j]=int(1)
            train_lab = np.vstack((train_lab,t_lab))
        kk=kk+1

with open('F:/python/marchine_learning_note/trainABCD.txt','wb') as f:
    pickle.dump([train_img,train_lab],f)


#with open('train_lab.txt','wb') as f:
#    pickle.dump(train_lab,f)
