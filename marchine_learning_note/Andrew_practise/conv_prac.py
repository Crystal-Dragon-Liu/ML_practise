#-*- coding: utf-8 -*-
import numpy as np
import  h5py
import matplotlib.pyplot as plt


# 填充输入图像
def zero_pad(X,pad):
    x_paded = np.pad(X,((0,0),(pad,pad),(pad,pad),(0,0)),'constant',constant_values=0)

    return x_paded


'''

#test

np.random.seed(1)

x = np.random.randn(4,3,3,2)

x_paded = zero_pad(x, 1)

#print('x.shape = ', x.shape)
#print('x_paded.shape = ',x_paded.shape)
#print('x=',x_paded)

#绘制图

fig,axarr =plt.subplots(1, 2) #建立两张表  在一行里

axarr[0].set_title('x')
axarr[0].imshow(x[1,:,:,0])
axarr[1].set_title('x_paded')
axarr[1].imshow(x_paded[1,:,:,0])
plt.show()

'''

#单步卷积
w=[[2,2,2],[2,2,2],[2,2,2]]
s=[[2,2,2],[2,2,2],[2,2,2]]
b = [[[1]]]
print(np.multiply(s,w)+b)
z=np.sum(s)
def conv_single_step(a_slice_prev,W,b):
    """
        在前一层的激活输出的一个片段上应用一个由参数W定义的过滤器。
        这里切片大小和过滤器大小相同

        参数：
            a_slice_prev - 输入数据的一个片段，维度为（过滤器大小，过滤器大小，上一通道数）
            W - 权重参数，包含在了一个矩阵中，维度为（过滤器大小，过滤器大小，上一通道数）
            b - 偏置参数，包含在了一个矩阵中，维度为（1,1,1）

        返回：
            Z - 在输入数据的片X上卷积滑动窗口（w，b）的结果。
        """
    s =np.multiply(a_slice_prev,W)+b #multiply 数组对应元素位置相乘

