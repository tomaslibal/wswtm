# import numpy as np

# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Convolution2D, MaxPooling2D

# np.random.seed(42)  # set deterministic reproducibility

import image
from log import debug

class wswtm():
    """
        loads given images into a numpy array of shape (N, ch, r, c)
        where 
         - N is the number of images,
         - ch is the number of the channels (3 for RGB, 4 for RGBA, etc.)
         - is the number of the rows (height in pixels)
         - is the number of the columns (width in pixels)
    """
    def load_data():
        pass
    """
        returns an array of possible tags for a give image (specified by a path)
    """
    def image2tags(self, path, treshold=0.75):
        pass

debug("wswtm init...") 

