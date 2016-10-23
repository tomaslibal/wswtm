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
        mx = len(X_train)
        split = int(round(mx * self.split_test))
        X_train, X_val = X_train[:-split], X_train[-split:]
        Y_train, Y_val = Y_train[:-split], Y_train[-split:]
        return X_train, Y_train, X_val, Y_val

    def train_model(self):
        pass

    def save_model(self):
        pass
