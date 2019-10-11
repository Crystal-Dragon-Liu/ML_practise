#-*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.contrib.tensorboard.plugins import projector
#可视化 未掌握

# 载入数据集
mnist = input_data.read_data_sets("F:/python/marchine_learning_note/MINST_test_set_images",one_hot=True)
#运行次数
max_steps = 1001
#图片数量
image_num = 3000
#文件路径
dir = 'F:/python/marchine_learning_note/TF_learning'
#定义会话
sess = tf.Session()

#载入图片
embedding = tf.Variable(tf.stack(mnist.test.images[:image_num] ,name='embedding'))
#打包测试集
#参数概要
def variable_summaries(var):
    with tf.name_scope("summaries"):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean',mean) #平均值
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev',stddev) # 标准差
        tf.summary.scalar('max',tf.reduce_max(var)) # 最大值
        tf.summary.scalar('min', tf.reduce_min(var)) # 最小值
        tf.summary.histogram('histogram',var) #直方图

#命名空间
with tf.name_scope('input'):
  #定义两个placeholder x 代表样本 y 代表标签
   x = tf.placeholder(tf.float32,[None,784],name='x_input')
   y = tf.placeholder(tf.float32,[None,10],name='y_input')
#显示图片
with tf.name_scope('input_reshape'):
    image_shaped_input = tf.reshape(x,[-1,28,28,1]) #-1 代表不确定的值 1代表图片维度是1 因为是黑白图片

    tf.summary.image('input',image_shaped_input,10) #把图片传进去，放10张图片

with tf.name_scope("layer"):
    with tf.name_scope('weights'):
     w = tf.Variable(tf.zeros([784, 10]),name='w')
     variable_summaries(w)
    with tf.name_scope('biases'):
     b = tf.Variable(tf.zeros([10]))
     variable_summaries(b)
    with tf.name_scope('wx_plus_b'):
     wx_plus_b = tf.matmul(x,w)+b
    with tf.name_scope('softmax'):
     prediction = tf.nn.softmax(wx_plus_b)

with tf.name_scope('loss'):

  loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=prediction))
  tf.summary.scalar('loss',loss)
  #收集loss
#梯度下降优化器
with tf.name_scope('train'):

  train_step = tf.train.GradientDescentOptimizer(0.8).minimize(loss)

#初始化变量
sess.run(tf.global_variables_initializer())

#定义求准确率的方法
with tf.name_scope('accuracy'):
 with tf.name_scope('correct_prediction'):
   correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1))
#比较两个参数大小是否一样  argmax(y,1)求y标签最大值是哪个位置，后面同理，如两个参数都显示在第六个位置，代表识别准确，都是数字6
 with tf.name_scope('accuracy'):

#求准确率
   accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
   tf.summary.scalar('accuracy',accuracy)
#产生metadata文件 将3000标签写入 metadata 中
'''

if tf.gfile.Exists(dir+'projector/projector/metadata.tsv'):
    tf.gfile.DeleteRecursively(dir+'projector/projector/metadata.tsv')
    tf.gfile.MkDir(dir+'projector/projector/metadata.tsv')
with open(dir+'projector/projector/metadata.tsv','w') as f:
    labels = sess.run(tf.argmax(mnist.test.labels[:],1))
    for i in range(image_num):
        f.write(str(labels[i])+'\n')
'''



if tf.gfile.Exists(dir + '/projector/projector/metadata.tsv'):
    tf.gfile.DeleteRecursively(dir + 'projector/projector')
    tf.gfile.MkDir(dir + '/projector/projector')
with open(dir + '/projector/projector/metadata.tsv', 'w')  as f:
    labels = sess.run(tf.argmax(mnist.test.labels[:],1))
    for i in range(image_num):
        f.write(str(labels[i]) + '\n')
#合并所有的summary
merged = tf.summary.merge_all()

projector_writer = tf.summary.FileWriter(dir+'/projector/projector',sess.graph)
saver = tf.train.Saver()
config = projector.ProjectorConfig()
embed =  config.embeddings.add()
embed.tensor_name = embedding.name
embed.sprite.image_path = dir + '/projector/data/mnist_10k_sprite.png'
embed.metadata_path = dir +'/projector/projector/metadata.tsv'
embed.sprite.single_image_dim.extend([28,28])
projector.visualize_embeddings(projector_writer,config)

for i in range(max_steps):
    #每个批次100样本
    batch_xs,batch_ys = mnist.train.next_batch(100)
    run_optioins = tf.RunOptions(trace_level = tf.RunOptions.FULL_TRACE)
    run_metadata= tf.RunMetadata()
    summary, _ = sess.run([merged, train_step], feed_dict={x: batch_xs, y: batch_ys},options=run_optioins,run_metadata=run_metadata)
    projector_writer.add_run_metadata(run_metadata,'step%03d' % i)
    projector_writer.add_summary(summary,i)

    if i %100 ==0:
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print('iter'+str(i) + ', testing acc = ' + str(acc))
#保存训练好的模型
saver.save(sess,dir+'/projector/projector/a_amodel.ckpt',global_step=max_steps)
projector_writer.close()
sess.close()

