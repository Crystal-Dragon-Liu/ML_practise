#-*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
#遥控器
x= tf.placeholder(tf.float32,[None])
y = 3*tf.sin(x)
sess = tf.InteractiveSession()
yout = sess.run(y,feed_dict={x:np.array([3.14/2.0])})
print(yout)


sess = tf.InteractiveSession()
mnist = input_data



