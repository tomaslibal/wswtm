import unittest
import os.path
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

    def setUp(self):
        self.clean()
        with open(self.dummy_file, 'w') as dummy:
            dummy.write('abc')

        self.dl = dataloader(self.dummy_file)

    @classmethod
    def tearDownClass(self):
        self.clean()

    def test_loads_all_lines_even_if_last_line_does_not_have_line_break(self):
        x, y = self.dl.load_data()
        self.assertEqual(1, len(x))
        self.assertEqual(1, len(y))
