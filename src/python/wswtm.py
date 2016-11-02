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

    default_model_path = 'resources/models/'
    default_model_name = 'basic_cnn'

    load_on_init = True

    def __init__(self):
        if load_on_init is True:
            self.init()

    def init(self):
        model, dct = self.load_model(self.default_model_path, self.default_model_name)

        self.model = model
        self.dct = dct

    """
        Loads a trained model
    """
    def load_model(self, model_path, model_name):
        self.model_path = model_path
        self.model_name = model_name

        json_file = open(self.model_path + self.model_name + '.json', 'r')
        loaded_model = json_file.read()
        json_file.close()
        
        model = model_from_json(loaded_model)
        model.load_weights(self.model_path + self.model_name + ".h5")
        dct = pickle.load(open(self.model_path + self.model_name + '_dct.p', 'rb'))

        return model, dct

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

