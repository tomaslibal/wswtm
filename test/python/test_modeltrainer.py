import unittest
import numpy as np


from src.python.modeltrainer import modeltrainer

class ModelTrainerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.trainer = modeltrainer()
        self.trainer.path = 'test/resources/training_2_by_2.csv'

    def test_it_loads_the_data(self):
        x_train, y_train, x_test, y_test = self.trainer.load_data(4)
        self.assertEqual(4, len(x_train)) # 6 rows, 70% train (rounded) = 4 rows
        self.assertEqual(2, len(x_test))

    def test_it_loads_labels_correctly(self):
        _, y_train, _, y_test = self.trainer.load_data(4)
        self.assertEqual(True, np.array_equal([['cat'], ['dog', 'animal'], ['seagul'], ['bird']], y_train))
