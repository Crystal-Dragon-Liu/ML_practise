#-*- coding: utf-8 -*-

#使用案例
import tensorflow as tf
import numpy as np

#使用numpy 生成100个随机点
x_data = np.random.rand(100)
y_data = x_data*0.1 + 0.2
#此为一条直线


#构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

#使用tensorflow 优化这个线性模型 接近于y_data


#定义一个二次代价函数
loss = tf.reduce_mean(tf.square(y_data-y))
#定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
#定义一个最小化代价函数
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
#初始化变量

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if  step %20 ==0:
            print(step,sess.run([k,b]))

'''
结果是：
0 [0.056665994, 0.101081364]
20 [0.10555838, 0.19686554]
40 [0.10327158, 0.19815513]
60 [0.101925604, 0.19891414]
80 [0.10113337, 0.19936089]
100 [0.10066709, 0.19962382]
120 [0.10039263, 0.1997786]
140 [0.1002311, 0.19986968]
160 [0.10013603, 0.19992329]
180 [0.10008007, 0.19995484]
200 [0.10004713, 0.19997342]

'''