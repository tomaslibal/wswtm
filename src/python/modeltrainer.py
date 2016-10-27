import pickle
from dataloader import dataloader
from models.basic_cnn import basic_cnn

class modeltrainer():
    path = 'resources/images/training.csv'
    model_path = 'resources/models/basic_cnn.json'
    split_test = 0.3

    """
        loads given images into a numpy array of shape (N, ch, r, c)
        where 
         - N is the number of images,
         - ch is the number of the channels (3 for RGB, 4 for RGBA, etc.)
         - is the number of the rows (height in pixels)
         - is the number of the columns (width in pixels)
    """
    def load_data(self, num_cols, y_enable=True):
        dl = dataloader(self.path)
        X_train, Y_train = dl.load_data(num_cols, y_enable)     

        return X_train, Y_train

    def split_data(self, x, y, split_test=0.3):
        mx = len(x)
        split = int(round(mx * split_test))
        X_train, X_val = x[:-split], x[-split:]
        Y_train, Y_val = y[:-split], y[-split:]
        return X_train, Y_train, X_val, Y_val

    def convert_labels_to_binary(self, y):
        dl = dataloader(self.path)
        return dl.transform_free_labels_to_array(y)

    def init_model(self, num_classes, input_shape):
        self.cnn = basic_cnn(num_classes, input_shape)
        m = self.cnn.get_model()
        self.model = m
        self.cnn.compile(m)

    def train_model(self, X_train, Y_train, X_test, Y_test):         
        self.cnn.fit(self.model, X_train, Y_train, X_test, Y_test, batch_size=256, nb_epoch=8)

    def save_model(self, model, dct):
        model_json = model.to_json()
        with open(self.model_path, 'w') as json_file:
	    json_file.write(model_json)

        # serialize weights to HDF5
        model.save_weights('resources/models/basic_cnn.h5')

        # serialize the dictionary to a pickle file
        pickle.dump(dct, open('resources/models/basic_cnn_dct.p', 'wb'))
        pass
