
import tensorflow as tf
from keras.utils.vis_utils import plot_model
import numpy as np
import pandas as pd
from keras.utils import plot_model
import keras
import ssl
from keras import backend as k
ssl._create_default_https_context = ssl._create_unverified_context

#1.1 创建网络


'''
model = tf.keras.Sequential()

model.add(tf.keras.layers.Flatten(input_shape = (28, 28))) #Flatten 将输入压平成1维

model.add(tf.keras.layers.Dense(128, activation= 'relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))
model.summary()

'''

inputs = tf.keras.Input(shape = (784, ), name='img')
h1 = tf.keras.layers.Dense(32, activation='relu')(inputs)
h2 = tf.keras.layers.Dense(32, activation='relu')(h1)
outputs =tf.keras.layers.Dense(10, activation='softmax')(h2)
model = tf.keras.Model(inputs=inputs, outputs=outputs, name='mnist-model')
model.summary()

#训练及验证

(x_train,y_train) , (x_test, y_test) = keras.datasets.mnist.load_data()
print(type(x_train))
x=x_train.reshape((60000,784)).astype('float32')/255
print(np.shape(x))
x_t=x_test.reshape((10000,784)).astype('float32')/255
print(np.shape(x_t))
#print(np.shape(x_test))


model.compile(optimizer = tf.keras.optimizers.RMSprop(),
              loss = 'sparse_categorical_crossentropy',
              metrics =['accuracy'])

history = model.fit(x, y_train, batch_size = 64, epochs=5)
test_scores = model.evaluate(x_t, y_test, verbose= 0)
print('test_loss = ', test_scores[0])
print('test_acc = ',test_scores[1])

#plot_model(model, to_file='/Users/crystal-dragon-lyb/PycharmProjects/project_demo/marchine_learning_note/TF2_0_learning/mnist_model.png',show_shapes=True)
#plot_model(model, to_file='/Users/crystal-dragon-lyb/PycharmProjects/project_demo/marchine_learning_note/TF2_0_learning/model_info.png',show_shapes=True)

model.save('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/marchine_learning_note/TF2_0_learning/model_save.h5')
#del model
model_1 = tf.keras.models.load_model('/Users/crystal-dragon-lyb/PycharmProjects/project_demo/marchine_learning_note/TF2_0_learning/model_save.h5')
#这里不用tf.keras会报错

