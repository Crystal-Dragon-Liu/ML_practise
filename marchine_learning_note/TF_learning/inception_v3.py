#-*- coding: utf-8 -*-
import tensorflow as tf
import os
import tarfile
import request

inception_pretrain_model_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
#模型存放地址
inception_pretrain_model_url_dir = 'F:/python/models/'
if not os.path.exists(inception_pretrain_model_url_dir):
    os.makedirs(inception_pretrain_model_url_dir)
print(inception_pretrain_model_url)

#模型保存位置
filename = inception_pretrain_model_url.split('/')[-1]
print(filename)
#['http:', '', 'download.tensorflow.org', 'models', 'image', 'imagenet', 'inception-2015-12-05.tgz']
filepath = os.path.join(inception_pretrain_model_url_dir,filename)


#将爬取数据携入文件


if not os.path.exists(filepath):
    print('download:',filename)
    r =requests.get(inception_pretrain_model_url,stream=True)
    with open(filepath,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            #print(1)
            if chunk:
                f.write(chunk)
                #print(chunk)
print('finish:',filename)

#解压文件
tarfile.open(filepath,'r:gz').extractall(inception_pretrain_model_url_dir)
#模型结构存放文件
log_dir = 'F:/python/models/inception_log/'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


inception_graph_def_file = os.path.join(inception_pretrain_model_url_dir,'classify_image_graph_def.pb')
with tf.Session() as sess:
 with tf.gfile.FastGFile(inception_graph_def_file,'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def,name='')

    #保存图结构在log_dir里面
 writer = tf.summary.FileWriter(log_dir,sess.graph)
 writer.close()