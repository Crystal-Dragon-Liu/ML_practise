import tensorflow as tf
import numpy as np
import PIL
from PIL import Image

sess = tf.InteractiveSession()
filehead = 'wbs/'
# 重构模型
x = tf.placeholder(tf.float32, [None, 784])
W01 = np.reshape(np.load(filehead+'w10.npy'),[784,100])
b01 = np.reshape(np.load(filehead+'b10.npy'),[100])
x01 = tf.nn.relu(tf.matmul(x, W01) + b01)
W02 = np.reshape(np.load(filehead+'w20.npy'),[100,50])
b02 = np.reshape(np.load(filehead+'b20.npy'),[50])
x02 = tf.nn.relu(tf.matmul(x01, W02) + b02)
W03 = np.reshape(np.load(filehead+'w30.npy'),[50,10])
b03 = np.reshape(np.load(filehead+'b30.npy'),[10])
y = tf.nn.softmax(tf.matmul(x02, W03) + b03)
# 输入图像
im = Image.open("data/num.JPG")
im2   = im.convert('L')
im2  = im2.resize((28, 28), PIL.Image.ANTIALIAS)
imar  = np.array(im2)
imarr = np.reshape(imar,[784])
x0    = np.reshape( imar, [1, 784] )/imar.max()
# 计算结果
h=sess.run(y,feed_dict={x:x0})
k=np.argmax(h[0,:])
print('This is %g with confidence %f'%(k,h[0,k]))
