from src.python.modeltrainer import modeltrainer
from src.python.dataloader import dataloader
from keras import backend as K

# Config
img_rows = 150
img_cols = 150

trainer = modeltrainer()
trainer.path = 'resources/images/training.csv'
x, y = trainer.load_data(22500)

x = x.astype('float32')
x /= 255

# Set the shape as (channels, rows, cols) or (rows, cols, channels)
# based on the Keras config
if K.image_dim_ordering() == 'th':
    input_shape = (1, img_rows, img_cols)
else:
    input_shape = (img_rows, img_cols, 1)

x = x.reshape((x.shape[0],) + input_shape)

# Convert text labels into a binary 2d array
y_bin, dct = trainer.convert_labels_to_binary(y)

#permute the lines
dl = dataloader(trainer.path)
x, y_bin = dl.permute(x, y_bin)

x_train, y_train, x_test, y_test = trainer.split_data(x, y_bin, 0.3)

# Train and save the model
trainer.init_model(len(dct), input_shape)
trainer.train_model(x_train, y_train, x_test, y_test)
trainer.save_model(trainer.model, dct)
