
# Copyright By Lijf@fudan.edu.cn Apr 2017

#import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#from pylab import *
import pickle
NN = 19*3*4
filename ='F:/python/marchine_learning_note/emoji/train_ABCD.txt'
with open(filename,'rb') as f:
    xs,ys = pickle.load(f)
m,NN=xs.shape
xim = np.reshape(xs,[-1,32,32])
N=12
for i in range(18):
    for j in range(12):
        k = (i)*N+j
        if j==0:xh = xim[k,:,:]
        if j>0: xh = np.hstack((xh,xim[k,:,:]))
    if i==0:xvh = xh
    if i>0:xvh = np.vstack((xvh,xh))

xm = np.reshape(xvh,[32*18,32*12])*255
filename="F:/python/marchine_learning_note/emoji/Faces.jpeg"
im=Image.fromarray(xm)
if im.mode != 'RGB':
 im = im.convert('RGB')
im.save(filename)









#
#imshow(x_image)
#show()
