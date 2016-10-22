import unittest

from src.python.wswtm import wswtm

class wswtmTest(unittest.TestCase):
    def setUp(self):
        self.w = wswtm()

    def test_should_store_a_model(self):
        mock_model = object()
        self.w.load_model(mock_model)
        self.assertEqual(mock_model, self.w.model)

    def test_should_return_1d_array(self):
        self.assertEqual(True, isinstance(self.w.image2tags('some/image.png'), list))


if __name__ == '__main__':
    unittest.main()
