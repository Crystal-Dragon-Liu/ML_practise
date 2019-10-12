#-*- coding: utf-8 -*-
#Optimizer 优化器相关
'''
各种优化器对比：
标准梯度下降法：先计算所有样本汇总误差，然后根据总误差来更新权值
当样本太大时，更新一次权值耗时太长

随机梯度下降法：随机抽取一个样本来计算误差，然后更新权值
更新权值比较快，但问题是可能会引入噪声，权值更新的方向可能是错误的

批量梯度下降法：总样本中选取一个批次 如一万个样本 随机选取一个批次作为一个batch 计算这个batch总误差，根据总误差来更新权值

momentum 当前权值的改变会受到上一次权值改变的影响，类似于小球向下滚动的时候戴上了惯性，加快收敛速度

NAG（Nesterov accelerated gradient）
NAG与momentum 在同一个函数中，可以通过参数配置启用
在momentum中小球会盲目地跟从下坡的梯度，容易发生错误，需要一个更聪明的小球，提前知道他要去哪里，还要知道走到坡底的时候速度慢下来而不是冲上另一个坡   yvt-1 会用来修改W的值
计算W-Yt-1可以表示小球下一个位置大概在哪里，然后使用到当前位置

adagrad
i :代表第i个分类
t:代表出现的次数
e:避免分母为0 一般取1e-8
n:取值一般为0.01
基于SGD的一种算法，对比较常见的数据给予比较晓得学习率去调整参数
对罕见的数据给予比较大的学习率去调整参数，适合应用于数据分布不均匀，（其中某些数据比较稀疏）的数据集
但随着迭代次数增大，学习率会越来越第，最终趋向于0

RMSprop
root mean square 均方根的缩写
借鉴了adagrad 只用到了前t-1此梯度评分平均值加上当前梯度平方的和 的开瓶费作为学习率的分母

adadelta

adam



'''


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

init_truncated = tf.truncated_normal_initializer(mean=0.0, stddev=1.0, seed=None, dtype=tf.float32)

# 读取数据集
mnist = input_data.read_data_sets("F:/python/marchine_learning_note/MINST_test_set_images",one_hot=True)
#超参数 每个批次的大小
batch_size = 100 #以矩阵形式一次放入100个样本进行训练
n_batch = mnist.train.num_examples // batch_size #num_examples 代表训练集的数量 //batch_size 代表整出批次大小 从而得到有多少个批次

#定义两个placeholder x 代表样本 y 代表标签
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])
keep_prob = tf.placeholder(tf.float32)



#创建一个简单的两层神经网络


w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax(tf.matmul(x,w)+b)
#另一个简单的神经网络
'''

w1_1 = tf.get_variable('w1_1',shape=[784,10],initializer=init_truncated)

b1_1 = tf.get_variable('b1_1',shape=[10],initializer = init_truncated)
a1 = tf.matmul(x,w1_1)+b1_1
l1 = tf.nn.softmax(a1)
'''


'''

#三层神经网络-1

w1 = tf.get_variable('w1',shape=[784,70],initializer=init_truncated)

b1 = tf.get_variable('b1',shape=[70],initializer = init_truncated)
a1 = tf.matmul(x,w1)+b1
l1 = tf.nn.tanh(tf.matmul(x,w1)+b1)
#l1 = tf.nn.softmax(tf.matmul(x,w1)+b1)
w2 = tf.get_variable('w2',shape=[70,10],initializer=init_truncated)

b2 = tf.get_variable('b2',shape=[10],initializer = init_truncated)
prediction = tf.nn.softmax(tf.matmul(l1,w2)+b2)

'''
'''
#三层神经网络-2

w11 = tf.Variable(tf.truncated_normal([784,2000],stddev=0.1)) #截断正太分布，标准差为0.1
b11 = tf.Variable(tf.zeros([2000])+0.1) #b都是0.1
L1 = tf.nn.tanh(tf.matmul(x,w11)+b11)
L1_drop = tf.nn.dropout(L1,keep_prob) #keep_prob 设置百分之多少的神经元工作，如0.5

w22 = tf.Variable(tf.truncated_normal([2000,2000],stddev=0.1)) #截断正太分布，标准差为0.1
b22 = tf.Variable(tf.zeros([2000])+0.1) #b都是0.1
L2 = tf.nn.tanh(tf.matmul(L1_drop,w22)+b22)
L2_drop = tf.nn.dropout(L2,keep_prob) #keep_prob 设置百分之多少的神经元工作，如0.5

w33 = tf.Variable(tf.truncated_normal([2000,1000],stddev=0.1)) #截断正太分布，标准差为0.1
b33 = tf.Variable(tf.zeros([1000])+0.1) #b都是0.1
L3 = tf.nn.tanh(tf.matmul(L2_drop,w33)+b33)
L3_drop = tf.nn.dropout(L3,keep_prob) #keep_prob 设置百分之多少的神经元工作，如0.5

w44 = tf.Variable(tf.truncated_normal([1000,10],stddev=0.1)) #截断正太分布，标准差为0.1
b44 = tf.Variable(tf.zeros([10])+0.1) #b都是0.1
prediction = tf.nn.softmax(tf.matmul(L3_drop,w44)+b44)


'''



#二次代价函数 &交叉熵

#loss = tf.reduce_mean(tf.square(y-prediction))

#loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(prediction),reduction_indices=[1]))
#对数似然代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#梯度下降优化器
train_step = tf.train.GradientDescentOptimizer(0.8).minimize(loss)
#新的训练优化器
train_step = tf.train.AdamOptimizer(1e-2).minimize(loss) #一般adam学习率小
#初始化变量

init = tf.global_variables_initializer()

#定义求准确率的方法

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
#比较两个参数大小是否一样  argmax(y,1)求y标签最大值是哪个位置，后面同理，如两个参数都显示在第六个位置，代表识别准确，都是数字6

#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
#tf.cast 转换类型 把true 转换为1.0 false就是 0.0 然后reduce_mean求平均值
loss_list = []
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        #迭代21次
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)#获取batch_size大小批次的数据
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})
            #sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.0}) keep_prob =1.0表示所有神经元都工作
        v_acc = sess.run(accuracy,feed_dict={x:mnist.validation.images,y:mnist.validation.labels,keep_prob:0.7})
        t_acc = sess.run(accuracy,feed_dict={x:mnist.train.images,y:mnist.train.labels,keep_prob:0.7})
        #v_acc = sess.run(accuracy, feed_dict={x: mnist.validation.images, y: mnist.validation.labels, keep_prob: 1.0})
        #t_acc = sess.run(accuracy, feed_dict={x: mnist.train.images, y: mnist.train.labels, keep_prob: 1.0})

        print("v_accuracy: %s"% v_acc+"t_accuracy: %s" % t_acc)


