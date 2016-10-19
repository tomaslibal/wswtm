import unittest
import os.path
from os import remove

from src.python.add import append_to_file

class AddTest(unittest.TestCase):
    dummy_file = 'test/resources/dummy.txt'

    @classmethod
    def clean(self):
        try:
            remove(self.dummy_file)
        except OSError:
            pass

    def setUp(self):
        self.clean()

    @classmethod
    def tearDownClass(self):
        self.clean()

    def test_append_to_file_creates_file_if_not_existing(self):
        self.assertEqual(False, os.path.isfile(self.dummy_file))
        append_to_file(self.dummy_file, 'foo')
        self.assertEqual(True, os.path.isfile(self.dummy_file))

    def test_append_to_file_appends_to_file(self):
        append_to_file(self.dummy_file, 'foo\n')
        append_to_file(self.dummy_file, 'bar')
        with open(self.dummy_file, 'r') as f:
            content = f.readlines()
            self.assertEqual(['foo\n', 'bar'], content)
        
