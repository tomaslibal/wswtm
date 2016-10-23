import numpy as np
import csv

class dataloader():
    def __init__(self, path):
        self.path = path

    def load_data(self, num_cols=0, y_enable=True, abc=False):
        X = []
        Y = []

        data = np.loadtxt(self.path, delimiter=',', usecols=range(num_cols))

        assert data.ndim == 2

        X = np.array(data[:,0:num_cols-1])
        if y_enable is True:  
            with open(self.path, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    mx = len(row)
                    Y.append(row[num_cols:])
            Y = np.array(Y)
    
        return X, Y
