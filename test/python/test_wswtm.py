import unittest

from src.python.wswtm import wswtm

w = None

class wswtmTest(unittest.TestCase):
    def setUp(self):
        w = wswtm()

    def test_should_return_1d_array(self):
        self.assertEqual(True, isinstance(w.image2tags('some/image.png'), list))


if __name__ == '__main__':
    unittest.main()
