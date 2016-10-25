import numpy as np
import csv

from multiclasshelper import MultiClassHelper

class dataloader():
    def __init__(self, path):
        self.path = path

    def load_data(self, num_cols=0, y_enable=True):
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

    def flatten_y_uniq(self, labels):        
        return set(sum(labels, []))

    """
        transforms string labels to an array where the length of the array
        is the number of the labels present and each row of the original
        string label array is transformed to an array of 0s and 1s where
        1 corresponds to the original label being present. To be able to 
        reconstruct the labels back from such array, a dictionary is also
        produced which remembers which string label is which index in the
        resulting array.
    """
    def transform_free_labels_to_array(self, y):
        labels = self.flatten_y_uniq(y)
        mchelper = MultiClassHelper()
        dct, num = mchelper.get_class_dict(labels)
        out = []
        for row in y:
            out.append(mchelper.classes_to_array(row, dct))

        return out, dct

    def transform_array_to_free_labels(self, y, dct):
        labels = []
        mchelper = MultiClassHelper()
        for row in y:
            labels.append(mchelper.array_to_classes(row, dct))

        return labels
