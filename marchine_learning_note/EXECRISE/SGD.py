#-*- coding: utf-8 -*-
import random


#SGD（Stochastic gradientdescent）随机梯度下降法：每次迭代使用一组样本
#针对BGD算法训练速度过慢的缺点，提出了SGD算法，普通的BGD算法是每次迭代把所有样本都过一遍，每训练一组样
#本就把梯度更新一次。而SGD算法是从样本中随机抽出一组，训练后按梯度更新一次，然后再抽取一组，再更新一次，在
#样本量及其大的情况下，可能不用训练完所有的样本就可以获得一个损失值在可接受范围之内的模型了。
x=[[1,4],[2,5],[5,1],[4,2]]
y=[19,26,19,20]

theta=[1,1]
loss=10
step_size = 0.05
eps = 0.0001
max_iters=10000
error = 0
iter_count=0


while(loss>eps and iter_count<max_iters):

    loss=0
    i = random.randint(0,3) #随机选取一组数据，进行训练，本次迭代中为i
    pred_y = theta[0]*x[i][0]+theta[1]*x[i][1] #如果本次迭代为第一次迭代，则根据初始化的theta值和选中的某一组数据，算出本次迭代的预测值
    theta[0]=theta[0]-step_size*(pred_y-y[i])*x[i][0] #更新一次theta
    theta[1]=theta[1]-step_size*(pred_y-y[i])*x[i][1] #更新一次theta
    #更新theta过后，再一次计算预测值，并求出新损失的总和
    for i in range(3):
        pred_y=theta[0]*x[i][0] + theta[1]*x[i][1]
        error=0.5*(pred_y-y[i])**2 #与BGD算法不同，计算损失值时不除以样本个数
        loss=error+loss
    iter_count=iter_count+1
    print("iter_count: "+str(iter_count))


print('theta:'+str(theta))
print('finalloss:'+str(loss))
print('iters'+str(iter_count))

