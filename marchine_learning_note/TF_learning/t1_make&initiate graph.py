#-*- coding: utf-8 -*-
import tensorflow  as tf
#创建图，启动图
#F:\python\marchine_learning_note\TF_learning
#创建一个常量OP
m1 =  tf.constant([[3,3]])
#创建一个常量OP
m2 =  tf.constant([[2],[3]])
#创建一个矩阵相乘的OP 把m1和m2 传入
product = tf.matmul(m1,m2)
print(product)
#输出结果为Tensor("MatMul:0", shape=(1, 1), dtype=int32)

'''


  #定义一个会话 启动默认图
  sess = tf.Session()
  #调用sess 的run方法，来执行矩阵乘法op，触发图中三个op
  result = sess.run(product)
  print(result)
  sess.close()

'''

with tf.Session() as sess:
    result = sess.run(product)
    print(result)