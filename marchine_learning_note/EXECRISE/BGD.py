import random
#-*- coding: utf-8 -*-
#BGD(Batch gradient descent)批量梯度下降法
#每次迭代都需要把所有样本都送入，这样的好处是每次迭代都顾及了全部的样本，做的是全局最优化。

x = [[1,4],[2,5],[5,1],[4,2]]
y = [19,26,19,20]
theta = [1,1]
loss = 10
step_size = 0.01 #步长
eps = 0.0001  #精度要求
max_iters=10000 #最大迭代次数
error= 0
iter_count=0

err1=[0,0,0,0]
err2=[0,0,0,0]
while(loss>eps and iter_count<max_iters): #损失大于精度并且迭代次数小于迭代规定最大次数时执行这个loop
    loss=0
    err1sum=0
    err2sum=0
    #每次迭代都对所有样本进行训练
    for i in range(4):
        pred_y=theta[0]*x[i][0]+theta[1]*x[i][1]
        # y= theta1*x1+theta2*x2 求预测值
        err1[i]=(pred_y-y[i])*x[i][0]  #损失函数对theta[0]求导的结果就是err1[i]
        err1sum=err1sum+err1[i]
        err2[i]=(pred_y-y[i])*x[i][1]
        err2sum=err2sum+err2[i]
    theta[0] = theta[0] - step_size * err1sum / 4
    theta[1] = theta[1] - step_size * err2sum / 4

    for i in range(4):
        pred_y=theta[0]*x[i][0]+theta[1]*x[i][1]
        error = 1/(2*4)*(pred_y-y[i])**2
        loss=loss+error
    iter_count+=1
    print("iter_count="+str(iter_count))
print('theta:'+str(theta))
print('finalloss:'+str(loss))
print('iters'+str(iter_count))

