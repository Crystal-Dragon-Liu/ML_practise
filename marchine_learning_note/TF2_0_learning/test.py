import tensorflow as tf
from keras.utils.vis_utils import plot_model
import numpy as np
import pandas as pd
from keras.utils import plot_model

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

(x_train, y_train) = (x_test, y_test) =  tf.keras.datasets.mnist.load_data()

print(type(x_train))

x_train = np.reshape(x_train,(-1,784)).astype('float32') /255