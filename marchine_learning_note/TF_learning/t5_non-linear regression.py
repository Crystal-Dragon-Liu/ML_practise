#-*- coding: utf-8 -*-


#简单的神经网络分类--不加hiddenlayer

#回归的例子---非线性回归
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#使用numpy 生成200个随机点
x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]
#在-0.5，0.5之间以均匀分布创建200个随机点 newaxis是新建一个维度 ":"俩边不填默认对全部数据进行增加维度
noise = np.random.normal(0,0.02,x_data.shape)
#生成噪音，形状跟x_data的形状一样
y_data = np.square(x_data) + noise
# 大致是一个U型图，但noise 会让图变得相对混乱

#定义两个placeholder
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

#构建一个简单的神经网络 ，解决这个回归问题 输入层为一个神经元 中间层为10个神经元 输出层为 1 个神经元
#定义中间层
weights_l1 = tf.Variable(tf.random.normal([1,10]))#输入层有1个神经元，中间层有10个神经元
biases_l1 = tf.Variable(tf.zeros([1,10]))#输入层有1个神经元，中间层有10个神经元
Wx_plus_b_l1 = tf.matmul(x,weights_l1)+biases_l1
#定义一个双曲正切函数作为激活函数
l1 = tf.nn.tanh(Wx_plus_b_l1)

#定义输出层
weights_l2 = tf.Variable(tf.random_normal([10,1]))#中间层有10个神经元，而输出层只有一个
biases_l2 = tf.Variable(tf.zeros([1,1]))#输出层只有一个神经元，所以只有一个偏置
Wx_plus_b_l2 = tf.matmul(l1,weights_l2) + biases_l2
prediction = tf.nn.tanh(Wx_plus_b_l2)


#定义代价函数 继续使用二次代价函数

loss = tf.reduce_mean(tf.square(y-prediction))
#定义优化器
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
with tf.Session() as sess:
    #initial variable
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    #获得预测值
    prediction_value = sess.run(prediction,feed_dict={x:x_data})
    #画图
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_value,'m-',lw=5)
    plt.show()