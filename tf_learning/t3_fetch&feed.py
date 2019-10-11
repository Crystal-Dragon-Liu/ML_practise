#-*- coding: utf-8 -*-
#fetch and feed

#fetch
import tensorflow as tf
#Fetch 会话里可以进行多个OP，得到多个结果
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
add = tf.add(input2,input3)
mul = tf.multiply(input1,add)
with tf.Session() as sess:
    result = sess.run([mul,add])
    #这里运行两个op 结果也将是两个op的结果
    print(result)
    print(type(result))


#feed
input1= tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
#创建占位符
output = tf.multiply(input1,input2)
#可以在运行时，再把值传入
with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.0],input2:[2.]}))
    #feed 的数据以字典形式传入

    