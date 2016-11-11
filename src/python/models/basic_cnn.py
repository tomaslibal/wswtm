from keras.models import Sequential
from keras.layers import Dense, Dropout,  Flatten, Convolution2D, MaxPooling2D, Activation

class basic_cnn():
    def __init__(self, number_classes, shape):
        self.number_classes = number_classes
        self.name = "basic cnn model"

        input_shape = shape
        nb_filters = 16
        kernel_size = 3

        self.feature_layers = [
    		Convolution2D(nb_filters, kernel_size, kernel_size, input_shape=input_shape, border_mode='valid', activation='relu'),
		Dropout(0.2),
    		Convolution2D(nb_filters, kernel_size, kernel_size, activation='relu'),
	        MaxPooling2D(pool_size=(2,2)),
    	        # Dropout(0.25),
    	        Convolution2D(nb_filters*2, kernel_size, kernel_size, activation='relu', border_mode='same'),
                Flatten(),
	]

	self.classification_layers = [
    		Dense(64, activation='relu'),
		# Dropout(0.5),
    		Dense(64, activation='relu'),
	        Dropout(0.5),    
                Dense(self.number_classes),
       		Activation('softmax')
	]

    def get_model(self):
        return Sequential(self.feature_layers + self.classification_layers)


    def compile(self, model):
        loss_fcn = 'binary_crossentropy'
        if (self.number_classes > 2):
            loss_fcn = 'categorical_crossentropy'
        model.compile(loss=loss_fcn,
                  optimizer='adam',
                  metrics=['accuracy'])

    def fit(self, model, X_train, Y_train, X_test, Y_test, batch_size=256, nb_epoch=32, verbose=1):
        model.fit(X_train, Y_train,
              batch_size=batch_size, nb_epoch=nb_epoch,
              verbose=verbose,
              validation_data=(X_test, Y_test))

    def evaluate(self, model, X_test, Y_test, verbose=0):
        score = model.evaluate(X_test, Y_test, verbose=verbose)
    	print('Test score:', score[0])
    	print('Test accuracy:', score[1])

    
    
