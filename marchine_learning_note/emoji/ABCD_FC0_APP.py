# -*- coding: utf-8 -*-
import numpy as np
import PIL
import matplotlib.pylab as plt
import pickle
import tensorflow as tf
from PIL import Image
from pylab import *
#表情包识别

NN = 2 ### number of categories
def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array

sess = tf.InteractiveSession()
im = Image.open('F:/机器学习/ABCD/101.jpg')
im2   = im.convert('L')
im2  = im2.resize((32, 32), PIL.Image.ANTIALIAS)
imar  = np.array(im2)
imarr = np.reshape(imar,[1024])
thres = (imarr.max()*0.45+imarr.min()*0.55)
imar   = binarize_array(imar, thres)

xs    = np.reshape( imar, [1, 1024] )/imar.max()
x =  tf.placeholder(tf.float32, [None, 1024])

with open('F:/python/marchine_learning_note/emoji/wbconv.txt','rb') as f: #有问题
     print(f.decode())
     W01,b01 = pickle.load(f)
y = tf.nn.softmax(tf.matmul(x, W01) + b01)
y=sess.run(y,feed_dict={x:xs})
k=np.argmax(y[0,:])
if k==0:
    print('this is a smiling face with eyes open, confidence: %f'%y[0,k])
if k==1:
    print('this is a smiling face with eyes closed, confidence: %f'%y[0,k])
if k==2:
    print('this is a cool face with eyes open, confidence: %f'%y[0,k])
if k==3:
    print('this is a cool face with eyes closed, confidence: %f'%y[0,k])
