#!/usr/local/bin/python3.7
import tensorflow as tf
mnist = tf.keras.datasets.fashion_mnist
import keras
import numpy as np
#keras.layers.Dense
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train /255.0, x_test / 255.0
# 搭建模型
model = tf.keras.Sequential()

model.add(tf.keras.layers.Flatten(input_shape = (28, 28))) #Flatten 将输入压平成1维
'''

keras.layers.Dense(
units, #该层有几个神经元
activation=None, #该层使用的激活函数
use_bias=True,  #是否添加偏执
kernel_initializer='glorot_uniform',  # 权重初始化方法
bias_initializer='zeros', #偏置初始化方法
kernel_regularizer=None, #权重规范化函数
bias_regularizer=None, #偏置值规范化函数
activity_regularizer=None, #激活函数规范化方法
kernel_constraint=None, #权重变化限制函数
bias_constraint=None)  #偏置变化限制函数


'''
model.add(tf.keras.layers.Dense(128, activation= 'relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))
model.summary()
'''
结果如下：
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten (Flatten)            (None, 784)               0         
_________________________________________________________________
dense (Dense)                (None, 128)               100480    
_________________________________________________________________
dense_1 (Dense)              (None, 10)                1290      
=================================================================
Total params: 101,770
Trainable params: 101,770
Non-trainable params: 0

'''

# model compliation
keras.models.Sequential.compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

'''
# Arguments
            optimizer: String (name of optimizer) or optimizer instance.
                See [optimizers](/optimizers).
            loss: String (name of objective function) or objective function or
                `Loss` instance. See [losses](/losses).
                If the model has multiple outputs, you can use a different loss
                on each output by passing a dictionary or a list of losses.
                The loss value that will be minimized by the model
                will then be the sum of all individual losses.
            metrics: List of metrics to be evaluated by the model
                during training and testing. Typically you will use
                `metrics=['accuracy']`. To specify different metrics for different
                outputs of a multi-output model, you could also pass a dictionary,
                such as
                `metrics={'output_a': 'accuracy', 'output_b': ['accuracy', 'mse']}`.
                You can also pass a list (len = len(outputs)) of lists of metrics
                such as `metrics=[['accuracy'], ['accuracy', 'mse']]` or
                `metrics=['accuracy', ['accuracy', 'mse']]`. #mse = mean_squared_error
            loss_weights: Optional list or dictionary specifying scalar
                coefficients (Python floats) to weight the loss contributions
                of different model outputs.
                The loss value that will be minimized by the model
                will then be the *weighted sum* of all individual losses,
                weighted by the `loss_weights` coefficients.
                If a list, it is expected to have a 1:1 mapping
                to the model's outputs. If a dict, it is expected to map
                output names (strings) to scalar coefficients.
            sample_weight_mode: If you need to do timestep-wise
                sample weighting (2D weights), set this to `"temporal"`.
                `None` defaults to sample-wise weights (1D).
                If the model has multiple outputs, you can use a different
                `sample_weight_mode` on each output by passing a
                dictionary or a list of modes.
            weighted_metrics: List of metrics to be evaluated and weighted
                by sample_weight or class_weight during training and testing.
            target_tensors: By default, Keras will create placeholders for the
                model's target, which will be fed with the target data during
                training. If instead you would like to use your own
                target tensors (in turn, Keras will not expect external
                Numpy data for these targets at training time), you
                can specify them via the `target_tensors` argument. It can be
                a single tensor (for a single-output model), a list of tensors,
                or a dict mapping output names to target tensors.
            **kwargs: When using the Theano/CNTK backends, these arguments
                are passed into `K.function`.
                When using the TensorFlow backend,
                these arguments are passed into `tf.Session.run`.

        # Raises
            ValueError: In case of invalid arguments for
                `optimizer`, `loss`, `metrics` or `sample_weight_mode`.
        """

'''

model.fit(x_train,y_train,epochs = 10)


'''
 # Arguments
            x: Input data. It could be:
                - A Numpy array (or array-like), or a list of arrays
                  (in case the model has multiple inputs).
                - A dict mapping input names to the corresponding
                  array/tensors, if the model has named inputs.
                - A generator or `keras.utils.Sequence` returning
                  `(inputs, targets)` or `(inputs, targets, sample weights)`.
                - None (default) if feeding from framework-native
                  tensors (e.g. TensorFlow data tensors).
            y: Target data. Like the input data `x`,
                it could be either Numpy array(s), framework-native tensor(s),
                list of Numpy arrays (if the model has multiple outputs) or
                None (default) if feeding from framework-native tensors
                (e.g. TensorFlow data tensors).
                If output layers in the model are named, you can also pass a
                dictionary mapping output names to Numpy arrays.
                If `x` is a generator, or `keras.utils.Sequence` instance,
                `y` should not be specified (since targets will be obtained
                from `x`).
            batch_size: Integer or `None`.
                Number of samples per gradient update.
                If unspecified, `batch_size` will default to 32.
                Do not specify the `batch_size` if your data is in the
                form of symbolic tensors, generators, or `Sequence` instances
                (since they generate batches).
            epochs: Integer. Number of epochs to train the model.
                An epoch is an iteration over the entire `x` and `y`
                data provided.
                Note that in conjunction with `initial_epoch`,
                `epochs` is to be understood as "final epoch".
                The model is not trained for a number of iterations
                given by `epochs`, but merely until the epoch
                of index `epochs` is reached.
            verbose: Integer. 0, 1, or 2. Verbosity mode.
                0 = silent, 1 = progress bar, 2 = one line per epoch.
            callbacks: List of `keras.callbacks.Callback` instances.
                List of callbacks to apply during training and validation
                (if ).
                See [callbacks](/callbacks).
            validation_split: Float between 0 and 1.
                Fraction of the training data to be used as validation data.
                The model will set apart this fraction of the training data,
                will not train on it, and will evaluate
                the loss and any model metrics
                on this data at the end of each epoch.
                The validation data is selected from the last samples
                in the `x` and `y` data provided, before shuffling.
                This argument is not supported when `x` is a generator or
                `Sequence` instance.
            validation_data: Data on which to evaluate
                the loss and any model metrics at the end of each epoch.
                The model will not be trained on this data.
                `validation_data` will override `validation_split`.
                `validation_data` could be:
                    - tuple `(x_val, y_val)` of Numpy arrays or tensors
                    - tuple `(x_val, y_val, val_sample_weights)` of Numpy arrays
                    - dataset or a dataset iterator
                For the first two cases, `batch_size` must be provided.
                For the last case, `validation_steps` must be provided.
            shuffle: Boolean (whether to shuffle the training data
                before each epoch) or str (for 'batch').
                'batch' is a special option for dealing with the
                limitations of HDF5 data; it shuffles in batch-sized chunks.
                Has no effect when `steps_per_epoch` is not `None`.
            class_weight: Optional dictionary mapping class indices (integers)
                to a weight (float) value, used for weighting the loss function
                (during training only).
                This can be useful to tell the model to
                "pay more attention" to samples from
                an under-represented class.
            sample_weight: Optional Numpy array of weights for
                the training samples, used for weighting the loss function
                (during training only). You can either pass a flat (1D)
                Numpy array with the same length as the input samples
                (1:1 mapping between weights and samples),
                or in the case of temporal data,
                you can pass a 2D array with shape
                `(samples, sequence_length)`,
                to apply a different weight to every timestep of every sample.
                In this case you should make sure to specify
                `sample_weight_mode="temporal"` in `compile()`. This argument
                is not supported when `x` generator, or `Sequence` instance,
                instead provide the sample_weights as the third element of `x`.
            initial_epoch: Integer.
                Epoch at which to start training
                (useful for resuming a previous training run).
            steps_per_epoch: Integer or `None`.
                Total number of steps (batches of samples)
                before declaring one epoch finished and starting the
                next epoch. When training with input tensors such as
                TensorFlow data tensors, the default `None` is equal to
                the number of samples in your dataset divided by
                the batch size, or 1 if that cannot be determined.
            validation_steps: Only relevant if `steps_per_epoch`
                is specified. Total number of steps (batches of samples)
                to validate before stopping.
            validation_steps: Only relevant if `validation_data` is provided
                and is a generator. Total number of steps (batches of samples)
                to draw before stopping when performing validation at the end
                of every epoch.
            validation_freq: Only relevant if validation data is provided. Integer
                or list/tuple/set. If an integer, specifies how many training
                epochs to run before a new validation run is performed, e.g.
                `validation_freq=2` runs validation every 2 epochs. If a list,
                tuple, or set, specifies the epochs on which to run validation,
                e.g. `validation_freq=[1, 2, 10]` runs validation at the end
                of the 1st, 2nd, and 10th epochs.
            max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
                input only. Maximum size for the generator queue.
                If unspecified, `max_queue_size` will default to 10.
            workers: Integer. Used for generator or `keras.utils.Sequence` input
                only. Maximum number of processes to spin up
                when using process-based threading. If unspecified, `workers`
                will default to 1. If 0, will execute the generator on the main
                thread.
            use_multiprocessing: Boolean. Used for generator or
                `keras.utils.Sequence` input only. If `True`, use process-based
                threading. If unspecified, `use_multiprocessing` will default to
                `False`. Note that because this implementation relies on
                multiprocessing, you should not pass non-picklable arguments to
                the generator as they can't be passed easily to children processes.
            **kwargs: Used for backwards compatibility.

        # Returns
            A `History` object. Its `History.history` attribute is
            a record of training loss values and metrics values
            at successive epochs, as well as validation loss values
            and validation metrics values (if applicable).

        # Raises
            RuntimeError: If the model was never compiled.
            ValueError: In case of mismatch between the provided input data
                and what the model expects.
'''

test_loss, test_acc = model.evaluate(x_test, y_test)
'''
            # Arguments
            x: Input data. It could be:
                - A Numpy array (or array-like), or a list of arrays
                  (in case the model has multiple inputs).
                - A dict mapping input names to the corresponding
                  array/tensors, if the model has named inputs.
                - A generator or `keras.utils.Sequence` returning
                  `(inputs, targets)` or `(inputs, targets, sample weights)`.
                - None (default) if feeding from framework-native
                  tensors (e.g. TensorFlow data tensors).
            y: Target data. Like the input data `x`,
                it could be either Numpy array(s), framework-native tensor(s),
                list of Numpy arrays (if the model has multiple outputs) or
                None (default) if feeding from framework-native tensors
                (e.g. TensorFlow data tensors).
                If output layers in the model are named, you can also pass a
                dictionary mapping output names to Numpy arrays.
                If `x` is a generator, or `keras.utils.Sequence` instance,
                `y` should not be specified (since targets will be obtained
                from `x`).
            batch_size: Integer or `None`.
                Number of samples per gradient update.
                If unspecified, `batch_size` will default to 32.
                Do not specify the `batch_size` if your data is in the
                form of symbolic tensors, generators, or
                `keras.utils.Sequence` instances (since they generate batches).
            verbose: 0 or 1. Verbosity mode.
                0 = silent, 1 = progress bar.
            sample_weight: Optional Numpy array of weights for
                the test samples, used for weighting the loss function.
                You can either pass a flat (1D)
                Numpy array with the same length as the input samples
                (1:1 mapping between weights and samples),
                or in the case of temporal data,
                you can pass a 2D array with shape
                `(samples, sequence_length)`,
                to apply a different weight to every timestep of every sample.
                In this case you should make sure to specify
                `sample_weight_mode="temporal"` in `compile()`.
            steps: Integer or `None`.
                Total number of steps (batches of samples)
                before declaring the evaluation round finished.
                Ignored with the default value of `None`.
            callbacks: List of `keras.callbacks.Callback` instances.
                List of callbacks to apply during evaluation.
                See [callbacks](/callbacks).
            max_queue_size: Integer. Used for generator or `keras.utils.Sequence`
                input only. Maximum size for the generator queue.
                If unspecified, `max_queue_size` will default to 10.
            workers: Integer. Used for generator or `keras.utils.Sequence` input
                only. Maximum number of processes to spin up when using
                process-based threading. If unspecified, `workers` will default
                to 1. If 0, will execute the generator on the main thread.
            use_multiprocessing: Boolean. Used for generator or
                `keras.utils.Sequence` input only. If `True`, use process-based
                threading. If unspecified, `use_multiprocessing` will default to
                `False`. Note that because this implementation relies on
                multiprocessing, you should not pass non-picklable arguments to
                the generator as they can't be passed easily to children processes.

'''
#print(test_acc)

#求准确率的包
from sklearn.metrics import accuracy_score
y_pred = model.predict_classes(x_test)
print(accuracy_score(y_test, y_pred))

pred = model.predict(x_test)
print(pred[0])
print(np.argmax(pred[0]))
'''输出结果如下
[7.0730295e-08 1.7534002e-09 2.0095550e-07 1.0445919e-12 8.6672308e-08
 4.2656483e-03 2.8859665e-08 2.9400734e-02 1.2311918e-08 9.6633321e-01]
9
'''

