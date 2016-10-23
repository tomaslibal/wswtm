import numpy as np

class dataloader():
    def __init__(self, path):
        self.path = path

    def load_data(self, num_cols=784, y_enable=True):
        # assert isinstance(self.path, str)
        # assert len(self.path) > 0
        X = []
        Y = []
	data = np.loadtxt(self.path, delimiter=",", usecols=range(num_cols))
        X = np.array(data[:,[0,num_cols-1]])
        if y_enable is True:
            Y = np.array(data[:,-num_cols])
    
        return X, Y
