# ConsNet For MNIST
# Copyright By Lijf@fudan.edu.cn Apr 2017
import tensorflow as tf
import numpy as np
import pickle

NN = 4 ### number of categories
sess = tf.InteractiveSession()
filename ='ABCD/trainABCD.txt'
with open(filename,'rb') as f:
    x_img,y_lab = pickle.load(f)
print(x_img.shape)
print(y_lab.shape)

def weight_variable(shape,name1):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial,name=name1)
def bias_variable(shape,name1):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial,name=name1)

def next_batch_ABCD(x_img,y_lab,n):
  m,size_fa=x_img.shape
  idx = np.arange(m)
  np.random.shuffle(idx)
  xs = x_img [idx[:n], :]
  ys  = np.zeros([n,4],dtype =float)
  ys0 =y_lab[idx[:n], :]
  ys =ys0
  return xs,ys

x = tf.placeholder(tf.float32, [None, 1024])
W01 = weight_variable([1024, NN],'W01')
b01 = bias_variable([NN],'b01')
y = tf.nn.softmax(tf.matmul(x, W01) + b01)
y_ = tf.placeholder(tf.float32, [None, NN])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),
                                reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#tf.global_variables_initializer().run()
#W10 = tf.constant(W01.eval())
#b10 = tf.constant(b01.eval())

sess.run(tf.global_variables_initializer())
for i in range(4001):
 xs, ys = next_batch_ABCD(x_img,y_lab,30)
 sess.run(train_step, feed_dict={x: xs, y_: ys})
 if i%100 ==0:
     print('cross_entropy')
     print(sess.run(cross_entropy, feed_dict={x: x_img,
                   y_: y_lab}))
     print('accuracy')
     print(sess.run(accuracy, feed_dict={x: x_img,
                   y_: y_lab}))

     W10 = sess.run(W01)
     b10 = sess.run(b01)
     with open('wb.txt','wb') as f:
         pickle.dump([W10,b10],f)
