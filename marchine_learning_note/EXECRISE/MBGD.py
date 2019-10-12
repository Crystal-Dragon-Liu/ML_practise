import random
#-*- coding: utf-8 -*-
#MBGD（Mini-batch gradient descent）小批量梯度下降：每次迭代使用b组样本
x=[[1,4],[2,5],[5,1],[4,2]]
y=[19,26,19,20]
theta=[1,1]
loss=10
step_size = 0.05
eps = 0.0001
max_iters=10000
error = 0
iter_count=0
print("线性回归预测")
while(loss>eps and iter_count<max_iters):
    loss=0
    #批量选取某几组样本进行更新，另一组样本选用本次选中的相邻组
    i = random.randint(0,3)
    j = (i+1)%4
    pred_y0 = theta[0]*x[i][0] + theta[1]*x[i][1] #预测值1
    pred_y1 = theta[0] * x[j][0] + theta[1] * x[j][1]# 预测值2
    theta[0] = theta[0] - step_size * (1 / 2) * ((pred_y0 - y[i]) * x[i][0] + (pred_y1 - y[j]) * x[j][0])
    theta[1] = theta[1] - step_size * (1 / 2) * ((pred_y0 - y[i]) * x[i][1] + (pred_y1 - y[j]) * x[j][1])
    for i in range(3):
        pred_y = theta[0]*x[i][0]+theta[1]*x[i][1]
        error  = (1/(2*2))*(pred_y-y[i])**2
        loss=loss+error
    iter_count+=1
    print("迭代%s次: "%str(iter_count))
print('预测的参数为 :'+str(theta))
print('损失总计 :'+str(loss))
print('迭代了'+str(iter_count))
