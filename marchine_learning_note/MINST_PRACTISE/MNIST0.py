#-*- coding: utf-8 -*-
# ConsNet For MNIST
# Copyright By Lijf@fudan.edu.cn Apr 2017
import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
#MINST手写数字识别
sess = tf.InteractiveSession()
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

x = tf.placeholder(tf.float32, [None, 784])

def weight_variable(shape,name1):
  initial = tf.truncated_normal(shape, stddev=0.1) #stddev标准差 truncated_normal 截断正态分布

  return tf.Variable(initial,name=name1)
def bias_variable(shape,name1):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial,name=name1)

W01 = weight_variable([784, 10],'W01')
b01 = bias_variable([10],'b01')


y = tf.nn.softmax(tf.matmul(x, W01) + b01) # 归一化函数
y_ = tf.placeholder(tf.float32, [None, 10])
saver=tf.train.Saver()
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),
                                reduction_indices=[1]))

#熵
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#tf.global_variables_initializer().run()
#W10 = tf.constant(W01.eval())
#b10 = tf.constant(b01.eval())

sess.run(tf.global_variables_initializer())
for i in range(4001):
 batch_xs, batch_ys = mnist.train.next_batch(64)
 sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
 if i%200 ==0:
     print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                   y_: mnist.test.labels}))

     W10 = sess.run(W01)

     b10 = sess.run(b01)
     np.save('w10',W10)
     np.save('b10',b10)


print(sess.run(accuracy, feed_dict={x: mnist.test.images,
              y_: mnist.test.labels}))
