#--coding='utf-8'--

# ConsNet For MNIST
# Copyright By Lijf@fudan.edu.cn Apr 2017
import numpy as np
import PIL
import pickle
import tensorflow as tf
from PIL import Image
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

NN = 2  ### number of categories


def binarize_array(numpy_array, threshold=200):
    """Binarize a numpy array."""
    for i in range(len(numpy_array)):
        for j in range(len(numpy_array[0])):
            if numpy_array[i][j] > threshold:
                numpy_array[i][j] = 255
            else:
                numpy_array[i][j] = 0
    return numpy_array


sess = tf.InteractiveSession()

# ����ճ��1  ��������������ͼƬ
im =Image.open('F:/����ѧϰ/ABCD/101.jpg')
im2   = im.convert('L')
im2  = im2.resize((32, 32), PIL.Image.ANTIALIAS)
imar  = np.array(im2)
xs = np.reshape(imar, [1, 1024]).astype(float) / imar.max().astype(float)
x = tf.placeholder(tf.float32, [None, 1024])

# ����ճ����2  ��������������������¹������硣

with open('/lesson_5/ABCD/wb.txt','rb') as f:
    W01,b01 =pickle.load(f)
y = tf.nn.softmax(tf.matmul(x, W01) + b01)

# ����ճ����3  ��������ģ�Ͳ��õ������
y=sess.run(y,feed_dict={x:xs})
k=np.argmax(y[0,:])


if k == 0:
    print('����Ц��+���ۣ����Ŷ�Ϊ: %f' % y[0, k])
if k == 1:
    print('����Ц��+���ۣ����Ŷ�Ϊ: %f' % y[0, k])
if k == 2:
    print('������Į+���ۣ����Ŷ�Ϊ: %f' % y[0, k])
if k == 3:
    print('������Į+���ۣ����Ŷ�Ϊ: %f' % y[0, k])