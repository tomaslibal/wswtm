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
