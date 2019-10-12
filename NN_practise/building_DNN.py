#!/usr/local/bin/python3.7
import numpy as np
import h5py
import matplotlib.pyplot as plt
import testCase
import dnn_utils
import ir_utils
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
#初始化参数练习
np.random.seed(1)
#两层网络初始化练习
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
    b1 = np.zeros((n_h, 1))
    w2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros((n_y, 1))

    #使用断言确保我的数据格式是正确的

    assert(w1.shape == (n_h, n_x))
    assert(b1.shape == (n_h, 1))
    assert(w2.shape == (n_y, n_h))
    assert(b2.shape == (n_y, 1))

    parameters = {

        "w1": w1,
        "b1": b1,
        "w2": w2,
        "b2": b2
    }
    return parameters
#L层网络初始化练习
def initialize_para_deep(layer_dims):

    '''



    此函数是为了初始化多层网络参数而使用的函数。
    参数：
        layers_dims - 包含我们网络中每个图层的节点数量的列表

    返回：
        parameters - 包含参数“W1”，“b1”，...，“WL”，“bL”的字典：
                     W1 - 权重矩阵，维度为（layers_dims [1]，layers_dims [1-1]）
                     bl - 偏向量，维度为（layers_dims [1]，1）

 '''

    np.random.seed(3)
    parameter = {}

    L = len(layer_dims)
    for l in range(1, L):
        parameter['w'+str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) / np.sqrt((layer_dims[l-1]))
        parameter['b'+str(l)] = np.zeros((layer_dims[l], 1))
        assert(parameter['w'+str(l)].shape == (layer_dims[l], layer_dims[l-1]))
        assert(parameter['b'+str(l)].shape == (layer_dims[l], 1))



    return parameter
#前向传播
'''
前向传播有以下三个步骤

LINEAR
LINEAR - >ACTIVATION，其中激活函数将会使用ReLU或Sigmoid。
[LINEAR - > RELU] ×（L-1） - > LINEAR - > SIGMOID（整个模型）
线性正向传播模块（向量化所有示例）使用公式(3)进行计算： 

Z[l]=W[l]A[l−1]+b[l](3)
 
'''

#两层网络前向传播——线性部分
def  linear_forward(A, W ,b ):
    '''



    """
    实现前向传播的线性部分。

    参数：
        A - 来自上一层（或输入数据）的激活，维度为(上一层的节点数量，示例的数量）
        W - 权重矩阵，numpy数组，维度为（当前图层的节点数量，前一图层的节点数量）
        b - 偏向量，numpy向量，维度为（当前图层节点数量，1）

    返回：
         Z - 激活功能的输入，也称为预激活参数
         cache - 一个包含“A”，“W”和“b”的字典，存储这些变量以有效地计算后向传递
    """

    '''

    Z=np.dot(W,A) + b
    assert(Z.shape  == (W.shape[0],A.shape[1]))

    cache = (A,W,b)

    return Z,cache

#两层网络前向传播--线性激活部分
def linear_activation_forward(A_pre, W, b, activation):
    '''
        实现LINEAR-> ACTIVATION 这一层的前向传播

        参数：
            A_prev - 来自上一层（或输入层）的激活，维度为(上一层的节点数量，示例数）
            W - 权重矩阵，numpy数组，维度为（当前层的节点数量，前一层的大小）
            b - 偏向量，numpy阵列，维度为（当前层的节点数量，1）
            activation - 选择在此层中使用的激活函数名，字符串类型，【"sigmoid" | "relu"】

        返回：
            A - 激活函数的输出，也称为激活后的值
            cache - 一个包含“linear_cache”和“activation_cache”的字典，我们需要存储它以有效地计算后向传递
    '''
    if activation =="sigmoid":
        Z, linear_cache = linear_forward(A_pre, W, b)
        A, activation_cache = dnn_utils.sigmoid(Z)
    elif activation =="relu":
        Z, linear_cache = linear_forward(A_pre, W, b)
        A, activation_cache = dnn_utils.sigmoid(Z)

    assert(A.shape ==(W.shape[0],A_pre.shape[1]))

    cache = (linear_cache,activation_cache)

    return  A, cache

#L层网络前向传播（包含线性部分以及线性激活部分）
def L_model_forward(X,parameters):
    '''


    实现[LINEAR-> RELU] *（L-1） - > LINEAR-> SIGMOID计算前向传播，也就是多层网络的前向传播，为后面每一层都执行LINEAR和ACTIVATION

    参数：
        X - 数据，numpy数组，维度为（输入节点数量，示例数）
        parameters - initialize_parameters_deep（）的输出

    返回：
        AL - 最后的激活值
        caches - 包含以下内容的缓存列表：
                 linear_relu_forward（）的每个cache（有L-1个，索引为从0到L-2）

    '''


    caches = []

    A = X
    L = len(parameters) // 2
    for l in range(1, L):
        A_pre =A
        A, cache = linear_activation_forward(A_pre, parameters['W'+str(l)], parameters['b'+str(l)],"relu")
        caches.append(cache)
    AL, cache = linear_activation_forward(A,parameters['W'+str(L)],parameters['b'+str(L)],"sigmoid")
    caches.append(cache)

    assert(AL.shape == (1, X.shape[1]))
    return AL, caches

#计算成本
def compute_cost(AL,Y):

    '''


实施等式（4）定义的成本函数。

    参数：
        AL - 与标签预测相对应的概率向量，维度为（1，示例数量）
        Y - 标签向量（例如：如果不是猫，则为0，如果是猫则为1），维度为（1，数量）

    返回：
        cost - 交叉熵成本

    '''

    m = Y.shape[1]
    cost = -np.sum(np.multiply(np.log(AL),Y)+np.multiply(np.log(1-AL),1-Y)) / m

    cost = np.squeeze(cost)#从数组的形状中删除单维条目，即把shape中为1的维度去掉

    assert(cost.shape ==())
    return cost

#反向传播线性部分，即已知dZ直接求dW,db,dA_prev

def linear_backward(dZ,cache):
    '''

   为单层实现反向传播的线性部分（第L层）

    参数：
         dZ - 相对于（当前第l层的）线性输出的成本梯度
         cache - 来自当前层前向传播的值的元组（A_prev，W，b）

    返回：
         dA_prev - 相对于激活（前一层l-1）的成本梯度，与A_prev维度相同
         dW - 相对于W（当前层l）的成本梯度，与W的维度相同
         db - 相对于b（当前层l）的成本梯度，与b维度相同

    '''

    A_prev, W, b = cache
    m = A_prev.shape[1]
    dW = np.dot(dZ, A_prev.T) / m

    db = np.sum(dZ,axis=1,keepdims=True) /m
    dA_prev = np.dot(W.T, dZ)

    assert(dA_prev.shape == A_prev.shape)
    assert(dW.shape == W.shape)
    assert(db.shape == b.shape)

    return dA_prev, dW, db

#线性激活部分反向传播 定义 sigmoid_backward用于实现sigmoid函数的反向传播 relu_backward实现relu函数的反向传播

def linear_activation_backward(dA, cache, activation):
    '''

     实现LINEAR-> ACTIVATION层的后向传播。

    参数：
         dA - 当前层l的激活后的梯度值
         cache - 我们存储的用于有效计算反向传播的值的元组（值为linear_cache，activation_cache）
         activation - 要在此层中使用的激活函数名，字符串类型，【"sigmoid" | "relu"】
    返回：
         dA_prev - 相对于激活（前一层l-1）的成本梯度值，与A_prev维度相同
         dW - 相对于W（当前层l）的成本梯度值，与W的维度相同
         db - 相对于b（当前层l）的成本梯度值，与b的维度相同
    '''
    linear_cache, activation_cache = cache
    if activation == "relu":
        dZ = dnn_utils.sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)
        return dA_prev, dW, db
    if activation == "sigmoid":
        dZ = dnn_utils.relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)
        return dA_prev, dW, db

#求多层模型的backward每层的梯度

def L_model_backward(AL, Y, caches):

    '''

     对[LINEAR-> RELU] *（L-1） - > LINEAR - > SIGMOID组执行反向传播，就是多层网络的向后传播

    参数：
     AL - 概率向量，正向传播的输出（L_model_forward（））
     Y - 标签向量（例如：如果不是猫，则为0，如果是猫则为1），维度为（1，数量）
     caches - 包含以下内容的cache列表：
                 linear_activation_forward（"relu"）的cache，不包含输出层
                 linear_activation_forward（"sigmoid"）的cache

    返回：
     grads - 具有梯度值的字典
              grads [“dA”+ str（l）] = ...
              grads [“dW”+ str（l）] = ...
              grads [“db”+ str（l）] = ...

    '''
    grads = {}
    L = len(caches) #层数
    m = AL.shape[1] #样本数
    Y = Y.reshape(AL.shape)
    dAL = - (np.divide(Y, AL) - np.divide(1-Y, 1-AL))

    current_cache = caches[L-1]
    grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache,"sigmoid")
    for l in reversed(range(L-1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA" + str(l+2)], current_cache, "relu")

        grads["dA" + str(l+1)] = dA_prev_temp
        grads["dW" + str(l+1)] = dA_prev_temp
        grads["db" + str(l+1)] = db_temp
    return grads


#print(Y.shape)
'''
Y = np.asarray([[1, 1, 1]])
aL = np.array([[.8,.9,0.4]])

'''

'''
#两层网络初始化练习
print("=====initialize_parameters=====")
parameters = initialize_parameters(3, 2, 1)
print("w1:" +str(parameters['w1']))

#L层网络初始化练习
print("=====initialize_para_deep=====")
layer_dims = [5, 4, 3]
parameters = initialize_para_deep(layer_dims)
print(parameters)

#两层网络前向传播——线性部分
print("=====linear_forward=====")
A, W, b = testCase.linear_forward_test_case()
print("A: "+ str(A))
print("W: "+ str(W))
print("b: "+ str(b))
Z, linear_cache = linear_forward(A, W, b)
print("Z:"+str(Z))

#两层网络前向传播--线性激活部分
print('=====linear_activation_forward=====')
A_pre, W, b =testCase.linear_activation_forward_test_case()
A, linear_activation_cache = linear_activation_forward(A_pre, W, b, activation="sigmoid")
print("sigmoid, A: ",str(A))
A, linear_activation_cache = linear_activation_forward(A_pre, W, b, activation="relu")
print("ReLU, A: ",str(A))

#L层网络前向传播（包含线性部分以及线性激活部分）
print("=====L_model_forward=====")
X, parameters = testCase.L_model_forward_test_case()
AL, caches = L_model_forward(X, parameters)
print("AL: "+str(AL))
print("cache长度为"+str(len(caches)))


#计算成本
print("=====compute_cost=====")
Y,AL = testCase.compute_cost_test_case()
cost = compute_cost(AL, Y)
print("cost = "+str(cost))


#反向传播线性部分
print("=====linear_backforward=====")
dZ, linear_cache = testCase.linear_backward_test_case()
dA_prev, dW, db = linear_backward(dZ, linear_cache)

print("dA_prev = " + str(dA_prev)+"  the shape of dA_prev is :"+ str(dA_prev.shape))
print("dW = " + str(dW)+"  the shape of dW is : "+ str(dW.shape))
print("db = " + str(db)+"  the shape of db is : "+ str(db.shape))


#反向传播线性激活部分
print("=====linear_activation_backward=====")
AL, linear_activation_cache = testCase.linear_activation_backward_test_case()
# (testCase.linear_activation_backward_test_case())    return dA, linear_activation_cache
#linear_cache = (A, W, b)
#activation_cache = Z
#linear_activation_cache = (linear_cache, activation_cache)
dA_prev, dW, db = linear_activation_backward(AL, linear_activation_cache, activation="sigmoid")
print("relu")
print("dA_prev = " + str(dA_prev))
print("dW = " + str(dW))
print("db = " + str(db) + "\n")



#求多层模型的backward每层的梯度
print("=====L_model_backward=====")
AL, Y_assess, caches = testCase.L_model_backward_test_case()
grads = L_model_backward(AL, Y_assess, caches)

print("dW1 = " + str(grads["dW1"]))
print("db1 = " + str(grads["db1"]))
print("dA1 = " + str(grads["dA1"]))
print(grads)


'''

