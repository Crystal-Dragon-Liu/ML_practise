import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import PIL
from tensorflow.examples.tutorials.mnist import input_data
sess = tf.InteractiveSession()
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
def weights(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.contrib.layers.xavier_initializer())
def bias(shape, name):
    return tf.get_variable(name=name, shape=shape, initializer=tf.constant_initializer(0))

# 生成网络 G
Z = tf.placeholder(tf.float32, shape=[None, 64], name='Z')
th_G = [ weights([64, 256], 'G_W1'),bias([256], 'G_b1'),
         weights([256, 784], 'G_W2'),bias([784], 'G_b2')]
def GNET(z):
    h = tf.nn.relu(tf.matmul(z, th_G[0]) + th_G[1])
    G = tf.nn.sigmoid(tf.matmul(h, th_G[2]) + th_G[3])
    return G
# 辨别网络 D
X = tf.placeholder(tf.float32, shape=[None, 784])
th_D = [ weights([784, 256], 'D_W1'),bias([256], 'D_b1'),
         weights([256, 1], 'D_W2'),bias([1], 'D_b2')]
def DNET(x):
    h = tf.nn.relu(tf.matmul(x, th_D[0]) + th_D[1])
    D = tf.nn.sigmoid(tf.matmul(h, th_D[2]) + th_D[3])
    return D

L_D = -tf.reduce_mean(tf.log(DNET(X)) + tf.log(1.0 - DNET(GNET(Z))))
L_G = -tf.reduce_mean(tf.log(DNET(GNET(Z))))
D_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_D, var_list=th_D)
G_train= tf.train.AdamOptimizer(1.0e-4).minimize(L_G, var_list=th_G)
sess.run(tf.global_variables_initializer())

for i in range(100000):
    xs, _ = mnist.train.next_batch(32)

    zs=np.random.uniform(-1.0, 1.0, size=[32, 64])

    _,ld=sess.run([D_train, L_D],feed_dict={X:xs, Z: zs})
    zs=np.random.uniform(-1.0, 1.0, size=[100, 64])
    _,lg=sess.run([G_train,L_G],feed_dict={ Z: zs})
    if i % 100 == 0:
        zs = np.random.uniform(-1.0, 1.0, size=[1, 64])
        img = sess.run(G_train, feed_dict={Z: zs})
        img = np.reshape(img, [28, 28])
        img = PIL.Image.fromarray(img)
        img.show()
        print(i,ld,lg)
