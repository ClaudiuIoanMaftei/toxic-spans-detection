from .executionstrategy import ExecutionStrategy

import numpy as np
import keras
from keras.models import Sequential, Input, Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU


class DefaultExecution(ExecutionStrategy):
    """
    Implementation for the default execution chain. This is the one described by our reference document:
    https://arxiv.org/pdf/1802.09957.pdf
    """

    def __init__(self):
        super().__init__()

    def init(self, **kwargs):
        embedded_size = kwargs['word_size']
        vector_size = kwargs['sent_size']
        input = kwargs['input']
        labels = kwargs['labels']

        batch_size = 64
        epochs = 20
        num_classes = 10

        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', input_shape=(embedded_size, vector_size, 1), padding='same'))
        model.add(MaxPooling2D((2, 2), padding='same'))
        model.add(Conv2D(64, (3, 3), activation='linear', padding='same'))
        model.add(MaxPooling2D(pool_size=(4, 4), padding='same'))
        model.add(Conv2D(128, (3, 3), activation='linear', padding='same'))
        model.add(MaxPooling2D(pool_size=(5, 5), padding='same'))
        model.add(Flatten())
        model.add(Dense(36, activation='linear'))
        model.add(Dense(num_classes, activation='sigmoid'))
        model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adam(),
                              metrics=['accuracy'])
        model.summary()

        return model
