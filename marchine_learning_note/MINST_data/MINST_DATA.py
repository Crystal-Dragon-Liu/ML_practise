#-*- coding: utf-8 -*-
import numpy as np
import struct
import matplotlib.pyplot as plt
#训练集的文件
train_images_idx3_ubyte_file = 'F:/python/marchine_learning_note/MINST_data/train-images.idx3-ubyte'
#训练集标签文件
train_labels_idx1_ubyte_file = 'F:/python/marchine_learning_note/MINST_data/train-labels.idx1-ubyte'
## 测试集文件
test_images_idx3_ubyte_file = 'F:/python/marchine_learning_note/MINST_data/t10k-images.idx3-ubyte'
# 测试集标签文件
test_labels_idx1_ubyte_file = 'F:/python/marchine_learning_note/MINST_data/t10k-labels.idx1-ubyte'

#读取并解析idx3的通用函数
def decode_idx3_ubyte(idx3_ubyte_file):
    #读取二进制数据
    bin_data = open(idx3_ubyte_file,'rb').read()
    #解析文件头信息
    offset = 0  #从文件的第几个字节开始读取
    fmt_header = '>iiii' #>代表大端，内存从左到右存储的字节越来越大 i代表无符号整型
    magic_number,num_images,num_rows,num_cols=struct.unpack_from(fmt_header,bin_data,offset)
    print("magic_number: %d\nthe number of images: %d\nthe size of images: %d,%d\n" % (magic_number,num_images,num_rows,num_cols))

    #解析数据集
    image_size = num_rows * num_cols
    offset += struct.calcsize(fmt_header) #获得数据在缓存中的指针位置 calcsize函数可以计算参数给定的数据格式占用的内存字节大小
    print(offset)
    fmt_image = '>' + str(image_size) + 'B' #读取image_size（28*28）个B格式数据 B对应unsignedchar
    print("读取的数据  开始的内存指针位置 读取数据的大小")
    print(fmt_image,offset,struct.calcsize(fmt_image))
    images = np.empty((num_images,num_rows,num_cols))

    for i in range(num_images):
        if(i + 1) % 10000 ==0:
            print("%d pieces of images have been parsed" % (i + 1))
            print(offset)

        images[i] = np.array(struct.unpack_from(fmt_image,bin_data,offset)).reshape((num_rows,num_cols))
        #print(images[i])
        offset += struct.calcsize(fmt_image) #指针移动fmt_image个大小的位置
        plt.imshow(images[i],'gray')#用matplotlib的imshow可以通过传入数组和图谱参数来显示图像
        plt.pause(0.00001)
        plt.show()
        exit()
    return images

def decode_idx1_ubyte(idx1_ubyte_file):
    #读取二进制数据
    bin_data = open(idx1_ubyte_file,'rb').read()

    #解析文件头信息 分别是magic_number 和 num_images
    offset = 0
    fmt_header = '>ii'
    magic_number,num_images = struct.unpack_from(fmt_header,bin_data,offset)
    print("the magic number : %d" %magic_number)
    print("the label number : %d" %num_images)

    #解析数据集
    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(num_images)
    for i in range(num_images):
        if(i + 1) % 10000 == 0:
            print('%d pieces of labels have been parsed' % (i + 1))
        labels[i] = struct.unpack_from(fmt_image,bin_data,offset)[0] #只读取从offset位置开始的fmt_image数据的第一个
        offset += struct.calcsize(fmt_image) #把指针更新到offset的位置
        #print(labels[i])
        #print(type(labels[i]))
        #exit()
    #print(labels[5000])
    return labels





#decode_idx1_ubyte(train_labels_idx1_ubyte_file)
#decode_idx3_ubyte(train_images_idx3_ubyte_file)


