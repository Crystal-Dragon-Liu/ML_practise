#-*- coding: utf-8 -*-
#tensorboard 网络结构


#交叉熵
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

init_truncated = tf.truncated_normal_initializer(mean=0.0, stddev=1.0, seed=None, dtype=tf.float32)

# 读取数据集
mnist = input_data.read_data_sets("F:/python/marchine_learning_note/MINST_test_set_images",one_hot=True)
#超参数 每个批次的大小






batch_size = 100 #以矩阵形式一次放入100个样本进行训练
n_batch = mnist.train.num_examples // batch_size #num_examples 代表训练集的数量 //batch_size 代表整出批次大小 从而得到有多少个批次

# 想要可视化，先定义命名空间

with tf.name_scope('input'):
  #定义两个placeholder x 代表样本 y 代表标签
   x = tf.placeholder(tf.float32,[None,784],name='x_input')
   y = tf.placeholder(tf.float32,[None,10],name='y_input')

with tf.name_scope("layer"):
    with tf.name_scope('weights'):
     w = tf.Variable(tf.zeros([784, 10]),name='w')
    with tf.name_scope('biases'):
     b = tf.Variable(tf.zeros([10]))
    with tf.name_scope('wx_plus_b'):
     wx_plus_b = tf.matmul(x,w)+b
    with tf.name_scope('softmax'):
     prediction = tf.nn.softmax(wx_plus_b)
#创建一个简单的神经网络



#另一个简单的神经网络
'''

w1_1 = tf.get_variable('w1_1',shape=[784,10],initializer=init_truncated)

b1_1 = tf.get_variable('b1_1',shape=[10],initializer = init_truncated)
a1 = tf.matmul(x,w1_1)+b1_1
l1 = tf.nn.softmax(a1)
'''

'''
#三层神经网络

w1 = tf.get_variable('w1',shape=[784,70],initializer=init_truncated)

b1 = tf.get_variable('b1',shape=[70],initializer = init_truncated)
a1 = tf.matmul(x,w1)+b1
l1 = tf.nn.tanh(tf.matmul(x,w1)+b1)
#l1 = tf.nn.softmax(tf.matmul(x,w1)+b1)
w2 = tf.get_variable('w2',shape=[70,10],initializer=init_truncated)

b2 = tf.get_variable('b2',shape=[10],initializer = init_truncated)
prediction = tf.nn.softmax(tf.matmul(l1,w2)+b2)


'''





#二次代价函数 &交叉熵

#loss = tf.reduce_mean(tf.square(y-prediction))

#loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(prediction),reduction_indices=[1]))
#对数似然代价函数

with tf.name_scope('loss'):

  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#梯度下降优化器
with tf.name_scope('train'):

  train_step = tf.train.GradientDescentOptimizer(0.8).minimize(loss)

#初始化变量
#初始化就不用其名字了，因为有默认的名字就叫initial
init = tf.global_variables_initializer()

#定义求准确率的方法
with tf.name_scope('accuracy'):
 with tf.name_scope('correct_prediction'):
   correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
#比较两个参数大小是否一样  argmax(y,1)求y标签最大值是哪个位置，后面同理，如两个参数都显示在第六个位置，代表识别准确，都是数字6
 with tf.name_scope('accuracy'):

#求准确率
   accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
#tf.cast 转换类型 把true 转换为1.0 false就是 0.0 然后reduce_mean求平均值
loss_list = []
with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('F:/python/marchine_learning_note/TF_learning/logs/',sess.graph)

    for epoch in range(1):
        #迭代21次
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)#获取batch_size大小批次的数据
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})
        acc = sess.run(accuracy,feed_dict={x:mnist.validation.images,y:mnist.validation.labels})

        print("accuracy: %s"% acc)


#对数似然代价函数迭代结果
'''
accuracy: 0.6658
accuracy: 0.7286
accuracy: 0.8536
accuracy: 0.8758
accuracy: 0.8858
accuracy: 0.8932
accuracy: 0.8982
accuracy: 0.9006
accuracy: 0.9054
accuracy: 0.9084
accuracy: 0.91
'''
#二次代价函数迭代结果
'''

accuracy: 0.275
accuracy: 0.4416
accuracy: 0.617
accuracy: 0.6788
accuracy: 0.7226
accuracy: 0.755
accuracy: 0.7776
accuracy: 0.7952
accuracy: 0.81
accuracy: 0.8226
accuracy: 0.8282
accuracy: 0.839
accuracy: 0.8442
accuracy: 0.8494
accuracy: 0.856
accuracy: 0.8596
accuracy: 0.8622
accuracy: 0.8636
accuracy: 0.8664
accuracy: 0.8696
accuracy: 0.8698

'''
