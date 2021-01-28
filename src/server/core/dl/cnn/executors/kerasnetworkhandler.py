from .networkhandler import NetworkHandler
from ...parsing.vocabulary import Vocabulary

KERAS_ENABLE = False

import numpy as np

if KERAS_ENABLE:
    import keras
    from keras.models import Sequential
    from keras.layers import Dense, Flatten
    from keras.layers import Conv2D, MaxPooling2D


class KerasNetworkHandler(NetworkHandler):
    """
    Implementation for the default execution chain. This is the one described by our reference document:
    https://arxiv.org/pdf/1802.09957.pdf
    """

    def __init__(self):
        super().__init__()

    def init(self, **kwargs):
        embedded_size = kwargs['word_size']
        vector_size = kwargs['sent_size']
        train_input = kwargs['train_input']
        labels = kwargs['train_labels']

        validation = kwargs['validation_input']
        validation_labels = kwargs['validation_labels']
        print(train_input.shape)
        print(labels.shape)

        batch_size = 64
        epochs = 20

        train_input = train_input.reshape(np.append(np.asarray(train_input.shape), 1))
        validation = validation.reshape(np.append(np.asarray(validation.shape), 1))

        if KERAS_ENABLE:
            model = Sequential()
            model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', input_shape=(vector_size, embedded_size, 1), padding='same'))
            model.add(MaxPooling2D((2, 2), padding='same'))
            model.add(Conv2D(64, (3, 3), activation='linear', padding='same'))
            model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
            model.add(Conv2D(128, (3, 3), activation='linear', padding='same'))
            model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
            model.add(Flatten())
            model.add(Dense(128, activation='linear'))
            model.add(Dense(vector_size, activation='sigmoid'))
            model.compile(loss=keras.losses.binary_crossentropy, optimizer=keras.optimizers.Adam(),
                          metrics=['accuracy'])
            model.summary()

            model.fit(train_input, labels, batch_size=batch_size, epochs=epochs, verbose=1,
                                validation_data=(validation, validation_labels))

            self._model = model
            model.save("dl_model.h5py")
            return model
        else:
            return None

    def transform(self, input_text):
        return Vocabulary.w2v_model.wv.get_vector(input_text)
