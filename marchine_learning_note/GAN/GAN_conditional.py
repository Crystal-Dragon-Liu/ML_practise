import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.examples.tutorials.mnist import input_data
sess = tf.InteractiveSession()
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
def weights(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.contrib.layers.xavier_initializer())
def bias(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.constant_initializer(0))

C0 = tf.placeholder(tf.float32, shape=[None, 10])
C_FAKE = tf.placeholder(tf.float32, shape=[None, 10])

# 生成网络 G
Z = tf.placeholder(tf.float32, shape=[None, 50], name='Z')
C_G = tf.tile(C0,[1,5])
G_INPUT = tf.concat([Z,C_G],1)
th_G = [ weights([100, 256], 'G_W1'),bias([256], 'G_b1'),
         weights([256, 784], 'G_W2'),bias([784], 'G_b2')]
def GNET(z):
    h = tf.nn.relu(tf.matmul(z, th_G[0]) + th_G[1])
    G = tf.nn.sigmoid(tf.matmul(h, th_G[2]) + th_G[3])
    return G

# 辨别网络 D
X = tf.placeholder(tf.float32, shape=[None, 784])
C_D = tf.tile(C0,[1,20])
C_DF = tf.tile(C_FAKE,[1,20])


th_D = [ weights([984, 256], 'D_W1'),bias([256], 'D_b1'),
         weights([256, 1], 'D_W2'),bias([1], 'D_b2')]

def DNET(x):
    h = tf.nn.relu(tf.matmul(x, th_D[0]) + th_D[1])
    D = tf.nn.sigmoid(tf.matmul(h, th_D[2]) + th_D[3])
    return D

X_G = GNET(G_INPUT)

D_INPUT0 = tf.concat([X,C_D],1)
d_real_match = DNET(D_INPUT0)
D_INPUTG = tf.concat([X_G,C_D],1)
d_fake = DNET(D_INPUTG)
D_INPUTG = tf.concat([X,C_DF],1)
d_real_NOT_match = DNET(D_INPUTG)

L_D = -tf.reduce_mean(tf.log( d_real_match ) + tf.log(1.0 - d_fake)+ tf.log(1.0 - d_real_NOT_match))
L_G = -tf.reduce_mean(tf.log(d_fake))
D_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_D, var_list=th_D)
G_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_G, var_list=th_G)
sess.run(tf.global_variables_initializer())

def GET_FAKE_C(y):
    N=y.shape[0]
    y1=1-y+np.random.uniform(0.0,0.1,(N,10))
    argy=np.argmax(y1,axis=1)
    yN=np.zeros((N,10))
    for i in range(N):yN[i,argy[i]]=1
    return yN


for i in range(100000):
    xs, ys = mnist.train.next_batch(64)
    ysN=GET_FAKE_C(ys)
    zs=np.random.uniform(-1.0, 1.0, size=[64, 50])
    _,ld,_,lg=sess.run([D_train, L_D,G_train,L_G],feed_dict={X:xs,C0:ys,C_FAKE:ysN, Z: zs})
    if i % 100 == 0:
        print(i,ld,lg)
