import unittest

from src.python.image import image2pix

class ImageTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_return_pixelaccess_object(self):
        r, _, _ = image2pix('test/resources/test1.png')
        self.assertEqual("list", type(r).__name__)

    def test_should_return_img_dims(self):
        _, w, h = image2pix('test/resources/test1.png')
        self.assertEqual(28, w)
        self.assertEqual(28, h)


if __name__ == '__main__':
    unittest.main()
