#-*- coding: utf-8 -*-
#变量的使用

#F:\python\marchine_learning_note\TF_learning

import tensorflow  as tf
x = tf.Variable([1,2])
#还未进行初始化的变量
#初始化
init = tf.global_variables_initializer()
a = tf.constant([3,3])
#增加一个减法OP
sub = tf.subtract(x,a)
#增加一个加法OP
add = tf.add(x,sub)

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))

#循环
state = tf.Variable(0,name='counter')

#创建一个变量初始化为0
#创建一个OP作用是state 加1
new_value = tf.add(state,1)
#赋值方法
update = tf.assign(state,new_value)
#将后面的值赋给前面
#变量初始化
init= tf.global_variables_initializer()
with tf.Session( ) as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))
