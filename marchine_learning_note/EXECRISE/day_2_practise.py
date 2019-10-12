#-*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
'''
def relu(x):
    return (x>0)*x
t=np.arange(200)*0.01-1.0
plt.plot(t,relu(t))
plt.show()

def sigmoid(x):return 1/(1+np.exp(-x))

t=np.arange(1000)*0.01-5.0
plt.plot(t,sigmoid(t))
plt.show()
'''


'''
h = np.random.uniform(0,100,[64,7,30])
def softmax(h,n): #n =-1效果相同，指向最后一个维度
    p=np.exp(h) / np.sum(np.exp(h),n,keepdims=True) #不加最后的参数时，分母为[64，7]
   # [64,7,30]/[64,7,1]
    return p

p = softmax(h,2)
print(p[0,1,:])
'''
'''
x=np.zeros((64,180))
w=np.zeros((180,78))
xw=np.matmul(x,w)
# [64,180,1]
# [1,180,78]
xw = np.sum(np.reshape(x,[64,180,1])*np.reshape(w,[1,180,78]),1)

'''
