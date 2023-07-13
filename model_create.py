from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Conv2DTranspose, Lambda
import tensorflow as tf


inputs = Input(shape=(1080, 1920, 3), dtype='float32', name='input_2')

x = Conv2DTranspose(filters=8, kernel_size=(40, 40), strides=(2, 2), padding='same', activation='tanh', name='conv2d_transpose_4')(inputs)
x = Conv2DTranspose(filters=16, kernel_size=(20, 20), strides=(1, 1), padding='same', activation='tanh', name='conv2d_transpose_5')(x)
x = Conv2DTranspose(filters=16, kernel_size=(10, 10), strides=(1, 1), padding='same', activation='tanh', name='conv2d_transpose_6')(x)
x = Conv2DTranspose(filters=3, kernel_size=(5, 5), strides=(1, 1), padding='same', activation='tanh', name='conv2d_transpose_7')(x)

x=tf.constant(0.5)*x+tf.constant(0.5)

model = Model(inputs,x)

model.summary()
