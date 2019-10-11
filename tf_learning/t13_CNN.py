#-*- coding: utf-8 -*-
#卷积神经网络练习
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("F:/python/marchine_learning_note/MINST_test_set_images",one_hot=True)


#每个批次的大小
batch_size = 100
#计算一共有多少个批次

n_batch = mnist.train.num_examples // batch_size


#初始化权值
def weight_variable(shape):
    initial =tf.truncated_normal(shape,stddev=0.1) #生成 服从截断正太分布的矩阵
    return tf.Variable(initial)
#初始化偏置

def bias_variable(shape):
    initial = tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,w):
    return tf.nn.conv2d(x,w,strides=[1,1,1,1],padding='SAME')#2d代表2维的卷积操作
#x 代表输入一个tensor[batch,in_height,in_width,in_channels]
#w 滤波器 filter/kernel tensor[filter_height,filter_width,in_channels,out_channels]
# strides第0和第3个值都是1 ，stride 代表x方向的步长，strides[2]代表y方向的步长
# padding sameh和valid
#池化层
def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
#ksize 代表窗口大小

#定义两个placeholder
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#改变x的格式转换为4D向量[batch,in_height,in_width,in_channels]
x_image = tf.reshape(x,[-1,28,28,1])


#初始化第一个卷积层的权值和偏置

w_conv1 = weight_variable([5,5,1,32]) #[5,5的采样窗口，32个卷积核从一个平面抽取特征
b_conv1 = bias_variable([32])

#把x_image和权值向量进行卷积，再加上偏置值，然后应用于relu激活函数

h_conv1 = tf.nn.relu(conv2d(x_image,w_conv1)+b_conv1)
h_pool1 = max_pool_2x2(h_conv1) #进行max_pooling

#初始化第二个卷积层的权值和偏置

w_conv2 = weight_variable([5,5,32,64]) #因为之前有32个卷积核扫描一个平面，生成了32个特征
b_conv2 = bias_variable([64]) #每一个卷积核一个偏置值

#把h_pool1和权值向量进行卷积，再加上偏置值，然后应用于relu 激活函数
h_conv2 = tf.nn.relu(conv2d(h_pool1,w_conv2)+b_conv2)
h_pool2 = max_pool_2x2(h_conv2)


# 28*28 图片第一次卷积后是28 * 28，第一次池化后变为14*14
# 第二次卷积后为14*14 第二次池化后变为了7*7
#经过上面操作后，得到64张 7*7的平面

#初始化第一个全连接层的权值
w_fc1 = weight_variable([7*7*64,1024])
b_fc1 = bias_variable([1024])

#把池化层2的输出扁平化为1维
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64]) # -1代表任意值 在这里代表100

#求第一个全连接层的输出
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,w_fc1)+b_fc1)

#keep_prob 用来表示神经元的输出概率

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

#初始化第二个全连接层
w_fc2 = weight_variable([1024,10])
b_fc2 = bias_variable([10])

#计算输出
prediction  = tf.nn.softmax(tf.matmul(h_fc1_drop,w_fc2)+b_fc2)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)


init = tf.global_variables_initializer()

correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})
        acc =  sess.run(accuracy,feed_dict={x:mnist.validation.images,y:mnist.validation.labels,keep_prob:1.0})
        print('Iter' + str(epoch)+',testing acc = '+ str(acc))

