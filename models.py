import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten, UpSampling2D, BatchNormalization
np.random.seed(42)

def createModel(IMG_DIMS):
    # Encoder
    model = Sequential()
    model.add(Conv2D(3, (3, 3), activation = 'relu', padding = 'same', input_shape = IMG_DIMS))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.2))
    
    model.add(Conv2D(6, (5, 5), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))
    
    model.add(Flatten())
    model.add(Dense(512, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(13, activation = 'sigmoid'))

    return model

def createModel_2(IMG_DIMS):
    model = Sequential()
    model.add(Conv2D(3, (3, 3), activation = 'relu', padding = 'same', input_shape = IMG_DIMS))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(6, (5, 5), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(3, (3, 3), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Flatten())
    model.add(Dense(512, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(13, activation = 'sigmoid'))

    return model

def createModel_3(IMG_DIMS):
    model = Sequential()
    model.add(Conv2D(6, (3, 3), activation = 'relu', padding = 'same', input_shape = IMG_DIMS))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(3, (5, 5), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(3, (3, 3), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Flatten())
    model.add(Dense(512, activation = 'relu'))
    model.add(Dropout(0.5))
    model.add(Dense(13, activation = 'sigmoid'))

    return model

def createModel_4(IMG_DIMS):
    model = Sequential()
    model.add(Conv2D(6, (3, 3), activation = 'relu', padding = 'same', input_shape = IMG_DIMS))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(12, (3, 3), activation = 'relu', padding = 'same'))
   
    model.add(Conv2D(12, (3, 3), activation = 'relu', padding = 'same'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(12, (3, 3), activation = 'relu', padding = 'same'))   
    model.add(Dropout(0.3))

    model.add(Flatten())
    model.add(Dense(512, activation = 'relu'))
    model.add(Dropout(0.3))
    model.add(Dense(256, activation = 'relu'))
    model.add(Dropout(0.3))
    model.add(Dense(13, activation = 'sigmoid'))

    return model
