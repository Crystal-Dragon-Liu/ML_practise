#-*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('F:/python/marchine_learning_note/MINST_test_set_images',one_hot=True)
train_nums = mnist.train.num_examples
validation_nums = mnist.validation.num_examples
test_nums = mnist.test.num_examples
print("MNIST中")
print("验证集个数：%s" % validation_nums)
print("训练集数据个数：%s" % train_nums)
print("测试集数据个数：%s" % test_nums)
train_data = mnist.train.images #获得所有的训练集数据
val_data = mnist.validation.images #获得所有验证集数据
test_data = mnist.test.images#获得所有测试集数据
#print(type(train_data))
#print(len(train_data))
print('训练集数据大小：',train_data.shape,'\n')
#print(train_data[0])
train_labels = mnist.train.labels
val_labels = mnist.validation.labels
test_labels = mnist.test.labels
print("训练集标签大小",train_labels.shape,'\n')
print("一幅图像的标签大小",train_labels[0].shape,'\n')
print("一副图像的标签值:",train_labels[0])
for i in range(0,10):
 im = train_data[i].reshape(28,28)
 plt.figure()
 plt.imshow(im,'gray')
 plt.pause(0.0000001)
 plt.show()