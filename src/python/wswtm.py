# import numpy as np

# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Convolution2D, MaxPooling2D

# np.random.seed(42)  # set deterministic reproducibility

import image
from log import debug

class wswtm():
    """
        Determines which pixel data is used.
    """
    red = True
    green = False
    blue = False


    """
        Loads a trained model
    """
    def load_model(self, model):
        self.model = model

    """
        returns an array of possible tags for a give image (specified by a path)
    """
    def image2tags(self, path, treshold=0.75):
        pass
    
    """
        returns a list of all classes known to the classifier
    """
    def get_classes(self):
        pass

debug("wswtm init...") 

