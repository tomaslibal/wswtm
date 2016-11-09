import unittest
from mockito import *

from src.python.wswtm import wswtm

class wswtmTest(unittest.TestCase):
    mock_model = object()
    dct = { "foo": 42, "bar": 1337 }

    def setUp(self):
        when(wswtm).load_model('test/resources/models/', 'test_model').thenReturn((self.mock_model, self.dct))
        when(wswtm).load_model('resources/models/', 'basic_cnn').thenReturn((self.mock_model, self.dct))
        self.w = wswtm()

    def test_should_store_a_model(self):       
        self.w.load_model('test/resources/models/', 'test_model')
        self.assertEqual(self.mock_model, self.w.model)

    def test_should_return_1d_array(self):
        self.assertEqual(True, isinstance(self.w.image2tags('some/image.png'), list))

    def test_should_return_classes_from_the_dictionary(self):
        self.w.default_model_path='test/resources/models/'
        self.w.default_model_name='test_model'
        self.w.init()
        
        self.assertEqual(['foo', 'bar'], self.w.get_classes())


if __name__ == '__main__':
    unittest.main()
