import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from os import walk
import os
import PIL
from PIL import Image

Lx=64
Ly=64
#反卷积

def input_image(filename='test.jpg'):
    im = Image.open(filename)
    im2  = im.resize((Lx, Ly), PIL.Image.ANTIALIAS)
    imar  = np.array(im2)
    return np.reshape( imar, [1, Lx, Ly,3] ).astype(float)/imar.max().astype(float)
def input_ALL_images(path='input'):
    # input data
    for (dirpath, dirnames, filenames) in walk(path):
        xs_list=[]
        for fn in filenames:

            f=os.path.join(dirpath,fn)
            xs1=input_image(f)
            xs_list.append(xs1)
    ns = len(xs_list)
    xs=np.reshape(xs_list,(-1,Lx, Ly,3))
    return xs,ns
XS,nx = input_ALL_images(path='X')
YS,ny = input_ALL_images(path='Y')

print('number of X domain:',nx)
print('number of Y domain:',ny)
MAX_N = max(nx,ny)
Batch_N = 64
if Batch_N>MAX_N:Batch_N=int(MAX_N/2)

sess = tf.InteractiveSession()
def weights(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.contrib.layers.xavier_initializer())
def bias(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.constant_initializer(0))



X = tf.placeholder(tf.float32, shape=[None, Lx, Ly,3])
Y = tf.placeholder(tf.float32, shape=[None, Lx, Ly,3])
Z = tf.placeholder(tf.float32, shape=[None, Lx, Ly,3])

# 生成网络 G, X->Y
th_GXY = [ weights([3,3,3,32], 'G1_W1'),bias([32], 'G1_b1'),
           weights([3,3,32,64], 'G1_W2'),bias([64], 'G1_b2'),
           weights([3,3,64,64], 'G1_W3'),bias([64], 'G1_b3'),
           weights([3,3,64,64], 'G1_W4'),bias([64], 'G1_b4'), # deconv1
           weights([3,3,32,64], 'G1_W5'),bias([32], 'G1_b5'),
           weights([3,3,3,32], 'G1_W6'),bias([3], 'G1_b6')]
th_GYX = [ weights([3,3,3,32], 'G2_W1'),bias([32], 'G2_b1'),
           weights([3,3,32,64], 'G2_W2'),bias([64], 'G2_b2'),
           weights([3,3,64,64], 'G2_W3'),bias([64], 'G2_b3'),
           weights([3,3,64,64], 'G2_W4'),bias([64], 'G2_b4'), # deconv1
           weights([3,3,32,64], 'G2_W5'),bias([32], 'G2_b5'),
           weights([3,3,3,32], 'G2_W6'),bias([3], 'G2_b6')]
def G0(x,th):
    x1=x+Z
    h1 = tf.nn.relu(tf.nn.conv2d(x1,th[0],strides=[1,1,1,1],padding='SAME') + th[1])
    h1 = tf.nn.max_pool(h1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h2 = tf.nn.relu(tf.nn.conv2d(h1,th[2],strides=[1,1,1,1],padding='SAME') + th[3])
    h2 = tf.nn.max_pool(h2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h3 = tf.nn.relu(tf.nn.conv2d(h2,th[4],strides=[1,1,1,1],padding='SAME') + th[5])
    h3 = tf.nn.max_pool(h3,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h4 = tf.nn.relu(tf.nn.conv2d_transpose(h3,th[6],
          [Batch_N,16,16,64],strides=[1,2,2,1],padding='SAME') + th[7])
    h5 = tf.nn.relu(tf.nn.conv2d_transpose(h4,th[8],
          [Batch_N,32,32,32],strides=[1,2,2,1],padding='SAME') + th[9])
    G = tf.nn.sigmoid(tf.nn.conv2d_transpose(h5,th[10],
          [Batch_N,64,64,3],strides=[1,2,2,1],padding='SAME') + th[11])
    return G

# D网络 D
th_DX = [ weights([3,3,3,32], 'D1_W1'),bias([32], 'D1_b1'),
           weights([3,3,32,64], 'D1_W2'),bias([64], 'D1_b2'),
           weights([3,3,64,64], 'D1_W3'),bias([64], 'D1_b3'),
           weights([8*8*64,256], 'D1_W4'),bias([256], 'D1_b4'), # FC
           weights([256,1], 'D1_W5'),bias([1], 'D1_b5')]
th_DY = [ weights([3,3,3,32], 'D2_W1'),bias([32], 'D2_b1'),
           weights([3,3,32,64], 'D2_W2'),bias([64], 'D2_b2'),
           weights([3,3,64,64], 'D2_W3'),bias([64], 'D2_b3'),
           weights([8*8*64,256], 'D2_W4'),bias([256], 'D2_b4'), # FC
           weights([256,1], 'D2_W5'),bias([1], 'D2_b5')]

def D0(x,th):
    h1 = tf.nn.relu(tf.nn.conv2d(x,th[0],strides=[1,1,1,1],padding='SAME') + th[1])
    h1 = tf.nn.max_pool(h1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h2 = tf.nn.relu(tf.nn.conv2d(h1,th[2],strides=[1,1,1,1],padding='SAME') + th[3])
    h2 = tf.nn.max_pool(h2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h3 = tf.nn.relu(tf.nn.conv2d(h2,th[4],strides=[1,1,1,1],padding='SAME') + th[5])
    h3 = tf.nn.max_pool(h3,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    h3 = tf.reshape(h3,[-1,8*8*64])
    h4 = tf.nn.relu(tf.matmul(h3,th[6]) + th[7])
    D = tf.nn.sigmoid(tf.matmul(h4,th[8]) + th[9])
    return D



# x->y_x'-x'
y_x = G0(X,th_GXY)
x_yx = G0(y_x,th_GYX)
# y->x_y'-y'
x_y = G0(Y,th_GYX)
y_xy = G0(x_y,th_GXY)

# LOSSES
L_DX = -tf.reduce_mean(tf.log( D0(X,th_DX) ) + tf.log(1.0 - D0(x_yx,th_DX))
          + tf.log(1.0 - D0(x_y,th_DX)))
L_DY = -tf.reduce_mean(tf.log( D0(Y,th_DY) ) + tf.log(1.0 - D0(y_x,th_DY))
          + tf.log(1.0 - D0(y_xy,th_DY)))
al=10.0
l2 =  al*(tf.reduce_mean((X-x_yx)**2,[0,1,2,3])+tf.reduce_mean((Y-y_xy)**2,[0,1,2,3]))
L_GXY = -tf.reduce_mean(tf.log(D0(y_x,th_DY)) ) +l2
L_GYX = -tf.reduce_mean(tf.log(D0(x_y,th_DX)) ) +l2

DX_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_DX, var_list=th_DX)
DY_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_DY, var_list=th_DY)
GXY_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_GXY, var_list=th_GXY)
GYX_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_GYX, var_list=th_GYX)
sess.run(tf.global_variables_initializer())


Id_X=np.arange(nx)
Id_Y=np.arange(ny)

for i in range(100000):
    np.random.shuffle(Id_X)
    np.random.shuffle(Id_Y)
    xs = XS[Id_X[:Batch_N]]
    ys = YS[Id_Y[:Batch_N]]
    zs=np.random.uniform(0.0, 0.1, size=[Batch_N, Lx,Ly,3])

    _,ldx,_,ldy,_,lgxy,_,lgyx=sess.run([DX_train,L_DX,DY_train,L_DY,
               GXY_train,L_GXY,GYX_train,L_GYX],feed_dict={X:xs,Y:ys,Z: zs})


    if i % 10 == 0:
        print(i,ldx,ldy,lgxy,lgyx)
