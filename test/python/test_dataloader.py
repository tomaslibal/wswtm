import unittest
import os.path
import numpy as np
from os import remove

from src.python.dataloader import dataloader

class DataloaderTest(unittest.TestCase):
    dummy_file = 'test/resources/dummy.txt'

    @classmethod
    def clean(self):
        try:
            remove(self.dummy_file)
        except OSError:
            pass

    @classmethod
    def write_to_dummy(self, string):
        with open(self.dummy_file, 'w') as dummy:
            dummy.write(string)

    def setUp(self):
        self.clean()
        self.write_to_dummy('1,0,1,0\n0.5,0,0.5,1')

        self.dl = dataloader(self.dummy_file)

    @classmethod
    def tearDownClass(self):
        self.clean()

    def test_loads_all_lines(self):
        self.clean()
        self.write_to_dummy('1,2,3\n4,5,6\n7,8,9\n')
        x, y = self.dl.load_data(3, True)
        self.assertEqual(3, len(x))
        self.assertEqual(3, len(y))

    def test_loads_all_lines_even_if_last_line_does_not_have_line_break(self):
        x, y = self.dl.load_data(4, True)
        self.assertEqual(2, len(x))
        self.assertEqual(2, len(y))

    def test_it_does_throw_assertion_error_when_only_one_line(self):
        self.clean()
        self.write_to_dummy('1,2,3\n')
        self.assertRaises(AssertionError, self.dl.load_data)

    def test_it_can_handle_string_class_names(self):
        self.clean()
        self.write_to_dummy('1,2,3,a,b,c\n4,5,6,b,c,a')
        x, y = self.dl.load_data(3, True)
        self.assertEqual(True, np.array_equal([['a','b','c'], ['b','c','a']], y))

    def test_it_permutes_the_lines(self):
        self.clean()
        self.write_to_dummy('1,2,3,a,b,c\n4,5,6,b,c,a\n7,8,9,a,b\n10,11,12,a')
        x, y = self.dl.load_data(3, True)
        x, y = self.dl.permute(x, y)
        self.assertEqual(False, np.array_equal([[1,2,3], [4,5,6], [7,8,9], [10,11,12]], x))
        self.assertEqual(False, np.array_equal([['a','b','c'], ['b','c','a'], ['a','b'], ['a']], y))

    def test_it_can_handle_variable_number_of_class_names(self):
        self.clean()
        self.write_to_dummy('1,2,3,a,b\n4,5,6,b,c,a,d,e\n7,8,9,z')
        x, y = self.dl.load_data(3, True)
        self.assertEqual(True, np.array_equal([['a', 'b'], ['b', 'c', 'a', 'd', 'e'], ['z']], y))

    def test_it_flattens_labels_to_1d_list(self):
        labels=[ ['cat', 'animal'], ['dog', 'animal', 'nature'], ['fish'] ]
        r = self.dl.flatten_y_uniq(labels)
        self.assertEqual(True, np.equal(set(['cat', 'animal', 'dog', 'nature', 'fish']), r))

    def test_it_flattens_numpy_ndarray_to_1d_list(self):
        labels=np.asarray([['a'],['b'],['c'], ['d', 'c']])
        r = self.dl.flatten_y_uniq(labels)
        self.assertEqual(True, np.equal(set(['a','b','c', 'd']), r))

    def test_it_flattens_numpy_ndarray_even_if_each_element_has_just_1_label(self):
        labels=np.asarray([['a'],['b'],['c'],['d']])
        r = self.dl.flatten_y_uniq(labels)
        self.assertEqual(True, np.equal(set(['a','b','c','d']), r))

    def test_it_transforms_each_array_of_free_labels_to_0_and_1_array(self):
        y = [ ['cat', 'dog'], ['cat'], ['fish'] ]
        expected = [ [0, 1, 1], [0, 0, 1], [1, 0, 0] ]
        y_trans, dct = self.dl.transform_free_labels_to_array(y)
        self.assertEqual(True, np.array_equal(expected, y_trans))

    def test_it_transforms_2d_array_of_1s_and_0s_back_to_labels(self):
        y = [ ['cat', 'dog'], ['cat'], ['fish'] ]
        arr = [ [0, 1, 1], [0, 0, 1], [1, 0, 0] ]
        y_trans, dct = self.dl.transform_free_labels_to_array(y)

        labels = self.dl.transform_array_to_free_labels(y_trans, dct)
        for i in range(len(labels)):
            self.assertEqual(True, self.contains_all(y[i], labels[i]))

    @classmethod
    def contains_all(self, a, b):       
        if len(a) != len(b):
            return False
        for el in a:
            if el not in b:
                return False
        for el in b:
            if el not in a:
                return False
        return True
