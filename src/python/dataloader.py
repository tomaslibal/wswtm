import numpy as np

class dataloader():
    def __init__(self, path):
        self.path = path

    def load_data(self, num_cols=0, y_enable=True):
        X = []
        Y = []

        if num_cols > 0:
	    data = np.loadtxt(self.path, delimiter=',', usecols=range(num_cols))
        else:
            data = np.loadtxt(self.path, delimiter=',')
        
        assert data.ndim == 2

        X = np.array(data[:,[0,num_cols-1]])
        if y_enable is True:
            Y = np.array(data[:,-num_cols])
    
        return X, Y
