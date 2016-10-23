import unittest
import numpy as np

from collections import OrderedDict


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

    def test_it_should_set_values_to_one_for_each_given_class(self):
        dct = { 'foo': 0, 'bar': 1, 'baz': 2 }
        classes = [ 'foo', 'baz' ]
        a = self.mch.classes_to_array(classes, dct)
        self.assertEqual(True, np.array_equal([1, 0, 1], a))

    def test_it_should_translate_an_array_back_to_its_respective_labels(self):
        dct = OrderedDict([ ('foo', 0), ('bar', 1), ('baz', 2)])
        a = [0, 1, 1]
        labels = self.mch.array_to_classes(a, dct)
        self.assertTrue(np.array_equal(['bar', 'baz'], labels))

