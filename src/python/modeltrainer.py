from dataloader import dataloader
from models.basic_cnn import basic_cnn

class modeltrainer():
    path = 'resources/images/training.csv'
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

    def init_model(self):
        cnn = basic_cnn(2, (3, 28, 28))
        m = cnn.get_model()
        self.model = cnn.compile(m)

    def train_model(self):
        pass

    def save_model(self):
        pass
