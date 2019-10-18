#!/usr/local/bin/python3.7
import tensorflow as tf
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from tensorflow import keras
import tensorflow_datasets as tfds



tf.compat.v1.enable_eager_execution()
print(tf.__version__)
import numpy as np
import matplotlib.pyplot as plt

#另一种读取方式
'''
mnist_train = tfds.load(name="mnist", split="train")
mnist_test = tfds.load(name='mnist',split='test')
#print(mnist_train)

def one_hot(l):

    label=np.zeros([10])
    label[l-1]=1
    return label

for mnis in mnist_train:
    #print(mnis['image'])
    print(mnis['label'])
    label = int(mnis['label'].numpy())
    label =  one_hot(label)
    print(label)
    #print(mnis['image'].numpy().shape)
    #print(mnis['image'].numpy)
    #print(mnis['label'].numpy().shape)
    #print(type(mnis['label'].numpy()))
    #plt.imshow( mnis['image'].numpy()[:, :, 0].astype(np.float32), cmap=plt.get_cmap('gray'))
    #plt.show()
    #print("label: "+str(mnis['label'].numpy()))
    break

'''



mnist = keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Data Exploration
#class_name = ['top','trouser','pullover','dress', 'coat', 'sandal','shirt','sneaker','bag','ankle boot']

#print(x_train.shape, y_train.shape)
#print(x_test.shape)

plt.figure()
#plt.imshow(x_train[0])
#plt.colorbar()

x_train = x_train/255.0
x_test = x_test/255.0
#plt.imshow(x_train[0],cmap='gray')
plt.show()

#Build the model with TF2.0


