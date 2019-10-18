

'''

Steps for building your first ANN

Data Preprocessing
Add input layer
Random w init
Add Hidden Layers
Select Optimizer, Loss, and Performance Metrics
Compile the model
use model.fit to train the model
Evaluate the model
Adjust optimization parameters or model if needed
'''

import tensorflow as tf
import keras
import numpy as np
import pandas as pd

#卷积神经网络

#加载数据
mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) =  mnist.load_data()
x_train, x_test = x_train /255.0, x_test / 255.0
x_train = x_train.reshape(x_train.shape[0],28,28,1)/255

print(x_train.shape)
x_test = x_test.reshape(x_test.shape[0],28,28,1)/255
print(x_test.shape)

model = tf.keras.models.Sequential([

    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape = (28,28,1),padding='same'), #64 是filter的个数，3，3是滤波器的维度
    tf.keras.layers.MaxPooling2D((2, 2),padding='same'),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu',padding='same'),
    tf.keras.layers.MaxPooling2D((2,2),padding='same'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation = 'relu'),
    tf.keras.layers.Dense(10,activation = 'softmax')

     ])
model = model(x_train, training = True)
'''
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,epochs = 10)


'''
'''
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration','Model Year','Origin']
dataset_path = '/Users/crystal-dragon-lyb/PycharmProjects/project_demo/marchine_learning_note/TF2_0_learning/auto-mpg.data'
raw_dataset = pd.read_csv(dataset_path, names= column_names, na_values='?', comment='\t', sep=' ', skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()
print(dataset)


'''
