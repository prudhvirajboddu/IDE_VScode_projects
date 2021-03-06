# -*- coding: utf-8 -*-
"""FashionMnistCoursera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/prudhviraj9999/TensorFlowML/blob/master/FashionMnistCoursera.ipynb
"""

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from time import time
from tensorflow.python.keras.callbacks import TensorBoard

mnsit=tf.keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=mnsit.load_data()

plt.imshow(train_images[0])
print(train_images[0])
print(train_labels[0])

train_images=train_images/255.0
test_images=test_images/255.0

model=tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),
                                 tf.keras.layers.Dense(512,activation=tf.nn.relu),
                                 tf.keras.layers.Dense(10,activation=tf.nn.softmax)])

tensorboard=TensorBoard(log_dir="logs/{}".format(time()))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy')

#early_stop=keras.callbacks.EarlyStopping(monitor='loss',patience=10)

model.fit(train_images,train_labels,epochs=5,callbacks=[tensorboard])

model.evaluate(test_images,test_labels)
