#!/usr/local/bin/python3.7

'''

初始化网络参数

前向传播

2.1 计算一层的中线性求和的部分

2.2 计算激活函数的部分（ReLU使用L-1次，Sigmod使用1次）

2.3 结合线性求和与激活函数

计算误差

反向传播

4.1 线性部分的反向传播公式

4.2 激活函数部分的反向传播公式

4.3 结合线性部分与激活函数的反向传播公式

更新参数

'''


import numpy as np
import h5py
import matplotlib.pyplot as plt

np.random.seed(1)
def initialize_parameters(n_x,n_h,n_y):

    '''

  此函数是为了初始化两层网络参数而使用的函数。
    参数：
        n_x - 输入层节点数量
        n_h - 隐藏层节点数量
        n_y - 输出层节点数量

    返回：
        parameters - 包含你的参数的python字典：
            W1 - 权重矩阵,维度为（n_h，n_x）
            b1 - 偏向量，维度为（n_h，1）
            W2 - 权重矩阵，维度为（n_y，n_h）
            b2 - 偏向量，维度为（n_y，1）

    '''
    w1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.random.randn((n_h, 1))
    w2 = np.random.randn(n_y,n_h)* 0.01
    b2 = np.random.randn((n_y,1))

    #使用断言确保我的数据格式是正确的

    assert(w1.shape==(n_h,n_x))
    assert(b1.shape==(n_h,1))
    assert(w2.shape==(n_y,n_h))
    assert(b2.shape==(n_y,1))

    parameters = {

        "w1":w1,
        "b1":b1,
        "w2":w2,
        "b2":b2
    }
    return parameters
