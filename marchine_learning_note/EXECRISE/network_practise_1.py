#-*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
#from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import random
import pickle
import gzip

# Third-party libraries
import numpy as np
def vr(j):
    e = np.zeros((10, 1))
    for i in range(0,10):
        e[i]= j[i]
    return e
def get_dataAndLabel():
    mnist = input_data.read_data_sets('F:/python/marchine_learning_note/MINST_test_set_images/', one_hot=True)
    train_nums = mnist.train.num_examples
    validation_nums = mnist.validation.num_examples
    test_nums = mnist.test.num_examples
    #print("MNIST中")
    #print("验证集个数：%s" % validation_nums)
    #print("训练集数据个数：%s" % train_nums)
    #print("测试集数据个数：%s" % test_nums)
    train_data = mnist.train.images  # 获得所有的训练集数据
    val_data = mnist.validation.images  # 获得所有验证集数据
    test_data = mnist.test.images  # 获得所有测试集数据
    # print(type(train_data))
    # print(len(train_data))
    #print('训练集数据大小：', train_data.shape, '\n')
    # print(train_data[0])
    train_labels = mnist.train.labels
    val_labels = mnist.validation.labels
    test_labels = mnist.test.labels
    #print("训练集标签大小", train_labels.shape, '\n')
    #print("一幅图像的标签大小", train_labels[0].shape, '\n')
    #print("一副图像的标签值:", train_labels[0])
    return train_data,train_labels,val_data,val_labels,test_data,test_labels
def load_data_1():
    tr_d,tr_l,va_d,va_l,te_d,te_l = get_dataAndLabel()
    training_inputs = [np.reshape(x,(784,1)) for x in tr_d]

    #training_results = vr(tr_l)
    training_results = tr_l
    training_data = zip(training_inputs,training_results)
    validation_inputs = [np.reshape(x,(784,1)) for x in va_d]
    validation_data = zip(validation_inputs,va_l)
    test_inputs = [np.reshape(x,(784,1)) for x in te_d]
    test_data = zip(test_inputs,te_l)

    #for i in test_data:
        ##print(i[1])
        #exit()
    return training_data, validation_data, test_data
#load_data()


def load_data():
    """Return the MNIST data as a tuple containing the training data,
    the validation data, and the test data.
    The ``training_data`` is returned as a tuple with two entries.
    The first entry contains the actual training images.  This is a
    numpy ndarray with 50,000 entries.  Each entry is, in turn, a
    numpy ndarray with 784 values, representing the 28 * 28 = 784
    pixels in a single MNIST image.
    The second entry in the ``training_data`` tuple is a numpy ndarray
    containing 50,000 entries.  Those entries are just the digit
    values (0...9) for the corresponding images contained in the first
    entry of the tuple.
    The ``validation_data`` and ``test_data`` are similar, except
    each contains only 10,000 images.
    This is a nice data format, but for use in neural networks it's
    helpful to modify the format of the ``training_data`` a little.
    That's done in the wrapper function ``load_data_wrapper()``, see
    below.
    """
    f = gzip.open('F:/python/DeepLearningPython35-master/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
    f.close()
    return (training_data, validation_data, test_data)

def load_data_wrapper():
    """Return a tuple containing ``(training_data, validation_data,
    test_data)``. Based on ``load_data``, but the format is more
    convenient for use in our implementation of neural networks.
    In particular, ``training_data`` is a list containing 50,000
    2-tuples ``(x, y)``.  ``x`` is a 784-dimensional numpy.ndarray
    containing the input image.  ``y`` is a 10-dimensional
    numpy.ndarray representing the unit vector corresponding to the
    correct digit for ``x``.
    ``validation_data`` and ``test_data`` are lists containing 10,000
    2-tuples ``(x, y)``.  In each case, ``x`` is a 784-dimensional
    numpy.ndarry containing the input image, and ``y`` is the
    corresponding classification, i.e., the digit values (integers)
    corresponding to ``x``.
    Obviously, this means we're using slightly different formats for
    the training data and the validation / test data.  These formats
    turn out to be the most convenient for use in our neural network
    code."""
    tr_d, va_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))#np.exp可以使得向量或数组的每个元素都执行exp

class Network(object):
    #初始化神经网络的层数，偏置，权重
    def __init__(self,sizes): #size 是每一层包含的神经元数量
        self.num_layers = len(sizes) #[1,2,3]len值为3,说明层数是3
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]# 生成了 两个 元素为偏置一维矩阵的 列表
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]
        #生成了拥有两个 元素为权重二维矩阵 的 列表
        #zip(size[:-1],size[1:]) 假如size是[2,3,1]则 zip就是将[2,3]以及[3,1]组合 形成[2,3]和[3,1]两个列表
        #randn(y,x) 基于高斯分布规律形成一个y行x列的权重矩阵
    #激活函数

    #前馈函数,给定a从而得到输出
    def feedforward(self,a):
        for b,w in zip(self.biases,self.weights):#这里：第一层和第二层之间的权重二维矩阵对应于第二层的偏置 以及 第二层和第三层之间的权重二维矩阵对应于第三层的偏置
            a = sigmoid(np.dot(w,a)+b) #最终a是激活向量
        return a
    def SGD(self,training_data,epochs,mini_batch_size,eta,test_data=None):
        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
        training_data = list(training_data)
        n = len(training_data)
        #小批次
        for j in  range(epochs):
            #每次迭代都将训练数据打乱
            random.shuffle(training_data)
            #将训练数据集分成一些小批量数据集
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0,n,mini_batch_size)#这里第三个参数是步长，n是trainingdata的数量
            ]
            # 对每个小批量数据都应用一次梯度下降
            for mini_batch in mini_batches:
             #print(mini_batch)
             self.update_mini_batch(mini_batch,eta)
             #update 函数仅使用mini_batch训练数据,每次梯度下降都迭代更新网络的权重和偏置。

            #如果test_data参数存在，则可以对这个网络做评估，否则直接打印迭代次数即可
            if test_data:
             print("迭代次数 {0}：{1} / {2}".format(j,self.evaluate(test_data),n_test))
            else:
             print("迭代{0}完成".format(j))
    def update_mini_batch(self,mini_batch,eta):
        #利用反向传播算法
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        #np.zeros意味，初始化0矩阵np.zeros(b.shape)意味着按照b矩阵的形状来初始化一个矩阵
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        #同理
        #以上代码就是重新构造一个和偏置矩阵以及权重矩阵相同的两个矩阵，根据权重和偏置的变化来更新每一个矩阵当中的元素
        for x,y in mini_batch:#mini_batch里有多少数据集，就反馈多少次
            delta_nabla_b,delta_nabla_w = self.backprop(x,y) #均方误差分别对偏置以及权重矩阵求偏导，可以用来计算偏置和权重的变化量
            nabla_b = [nb+dnb for nb,dnb in zip(nabla_b,delta_nabla_b)]
            nabla_w = [nw+dnw for nw,dnw in zip(nabla_w,delta_nabla_w)]
        self.weights = [w - (eta/len(mini_batch)) * nw for w, nw in zip(self.weights, nabla_w)]
            #zip(self.weights,nabla_w)
            # 元素1 为2行3列的原权重矩阵      以及     2行3列权重矩阵的总变化量    的结合
            # 和
            # 元素2 为3行1列的原权重矩阵   以及   3行1列 权重每个元素总变化量矩阵的结合
            # 形成的 列表

        self.biases = [b - (eta/len(mini_batch)) * nb for b, nb in zip(self.biases, nabla_b)]
            #同理





    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]  # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        yy = vr(y)
        delta = self.cost_derivative(activations[-1], yy) * \
            self.sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def chan(self,y):
        sum = 0
        for i in y:

            if i != 1:
                sum += 1
            else:
                return sum
    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y) for (x, y) in test_data]
        #print(test_results)
        #return sum(int(x == self.chan(y)) for (x, y) in test_results)

        #return sum(int(x == np.argmax(y)) for (x, y) in test_results)
        return sum(int(x == y) for (x, y) in test_results)


    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)

    def sigmoid_prime(self,z):
        """Derivative of the sigmoid function."""
        #return self.sigmoid(z) * (1 - self.sigmoid(z))
        return  sigmoid(z) * (1-sigmoid(z))

training_data, validation_data, test_data = load_data_wrapper()
#training_data,validation_data,test_data = load_data_1()
#for t in training_data:
    #print(t)
    #exit()
#training_data,validation_data,test_data = load_data_wrapper()
print("-------------------------------------运行")
net = Network([784,10])

net.SGD(training_data=training_data,epochs=30,mini_batch_size=10,eta=3.0,test_data=test_data)
