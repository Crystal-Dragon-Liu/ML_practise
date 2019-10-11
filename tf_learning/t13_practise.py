#-*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data



#定义一个卷积神经网络class

class CNN_practise(object):

    def __init__(self,kernel_x,kernel_y,n_batch,batch_size, mnist):
        self.mnist = mnist
        self.batch_size = batch_size
        self.n_batch = n_batch
        self.x = tf.placeholder(tf.float32, [None, 784])
        self.x_image = tf.reshape(self.x,[-1,28,28,1])
        self.y = tf.placeholder(tf.float32, [None, 10])
        self.kernel_x = kernel_x
        self.kernel_y = kernel_y
        self.keep_prob = tf.placeholder(tf.float32)
        #第二层卷积和池
        self.w_conv_1 = self.weight_variable([self.kernel_x, self.kernel_y, 1, 32])
        self.b_conv_1 = self.bias_variable([32])
        self.h_conv_1 = tf.nn.relu(self.conv2d(self.x_image, self.w_conv_1) + self.b_conv_1)
        self.h_pool_1 = self.max_pool_2x2(self.h_conv_1)

        #第三层卷积和池
        self.w_conv_2 = self.weight_variable([self.kernel_x, self.kernel_y, 32, 64])
        self.b_conv_2 = self.bias_variable([64])
        self.h_conv_2 = tf.nn.relu(self.conv2d(self.h_pool_1,self.w_conv_2)+self.b_conv_2)
        self.h_pool_2 = self.max_pool_2x2(self.h_conv_2)

        #第四层 全连接层

        self.h_pool_2_flat = tf.reshape(self.h_pool_2, [-1, 7*7*64])





        self.w_fc1 = self.weight_variable([7*7*64,1024])
        self.b_fc1 = self.bias_variable([1024])
        h_fc1 = tf.nn.relu(tf.matmul(self.h_pool_2_flat,self.w_fc1)+self.b_fc1)
        h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob)

        #第五层全连接层

        self.w_fc2  = self.weight_variable([1024,10])
        self.b_fc2  = self.bias_variable([10])

        #计算输出
        self.prediction = tf.nn.softmax(tf.matmul(h_fc1_drop,self.w_fc2)+self.b_fc2)
        self.loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.y,logits=self.prediction))
        self.train_step =tf.train.AdamOptimizer(1e-4).minimize(loss=self.loss)

        self.init = tf.global_variables_initializer()

        self.correct_prediction = tf.equal(tf.argmax(self.y,1),tf.argmax(self.prediction,1))

        self.accuracy = tf.reduce_mean(tf.cast(self.correct_prediction,tf.float32))






    def weight_variable(self,shape):
        initial = tf.truncated_normal(shape,stddev=0.1)
        return tf.Variable(initial)
    def bias_variable(self,shape):
        initial  = tf.constant(0.1,shape=shape)
        return tf.Variable(initial)
    def conv2d(self,x,w):
        return tf.nn.conv2d(x,w,strides=[1,1,1,1],padding = 'SAME')
    def max_pool_2x2(self,x):
        return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
    def train(self):
        with tf.Session() as sess:
            sess.run(self.init)
            for epoch in range(21):
                for batch in range(self.n_batch):
                  batch_xs ,batch_ys = self.mnist.train.next_batch(self.batch_size)
                  sess.run(self.train_step,feed_dict={self.x:batch_xs,self.y:batch_ys,self.keep_prob:0.7})
                acc  = sess.run(self.accuracy,feed_dict={self.x:self.mnist.validation.images,self.y:self.mnist.validation.labels,self.keep_prob:1.0})
                print('Iter' + str(epoch) + ',testing acc = ' + str(acc))

def main():
    mnist = input_data.read_data_sets("F:/python/marchine_learning_note/MINST_test_set_images", one_hot=True)
    print('1')
    batch_size = 100  # 每个批次大小
    n_batch = mnist.train.num_examples // batch_size

    cnn = CNN_practise(5,5,n_batch,batch_size,mnist)
    cnn.train()



if __name__ == '__main__':
    main()








