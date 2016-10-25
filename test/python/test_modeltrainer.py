import unittest
import numpy as np


from src.python.modeltrainer import modeltrainer

class ModelTrainerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.trainer = modeltrainer()
        self.trainer.path = 'test/resources/training_2_by_2.csv'

    def test_it_loads_the_data(self):
        x_train, y_train = self.trainer.load_data(4)
        self.assertEqual(6, len(x_train))
        self.assertEqual(6, len(y_train))

    def test_it_splits_data_accordingly(self):
        x, y = self.trainer.load_data(4)
        x_train, y_train, x_test, y_train = self.trainer.split_data(x, y, 0.3)
        self.assertEqual(4, len(x_train)) # 6 rows, 70% train (rounded) = 4 rows
        self.assertEqual(2, len(x_test))

    def test_it_loads_labels_correctly(self):
        _, y_train = self.trainer.load_data(4)
        self.assertEqual(True, np.array_equal([['cat'], ['dog', 'animal'], ['seagul'], ['bird'], ['anaconda'], ['zebra'] ], y_train))

    def test_it_can_transform_labels_correctly(self):
        _, y_train = self.trainer.load_data(4)
        y_bin, dct = self.trainer.convert_labels_to_binary(y_train)

        self.assertEqual(True, np.array_equal([ [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0] ], y_bin))
