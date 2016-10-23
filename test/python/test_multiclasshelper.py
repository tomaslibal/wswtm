import unittest
import numpy as np


from src.python.multiclasshelper import MultiClassHelper

class ModelTrainerTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.mch = MultiClassHelper()

    def test_it_should_not_double_count_a_duplicate_class(self):
        classes = ['foo', 'bar', 'baz', 'foo', 'minky', 'binky']
        dct, l = self.mch.get_class_dict(classes)
        self.assertEqual(5, l)
        self.assertEqual(5, len(dct))

