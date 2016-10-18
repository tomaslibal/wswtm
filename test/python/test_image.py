import unittest

from src.python.image import image2pix

class ImageTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_return_pixelaccess_object(self):
        r = image2pix('test/resources/test1.png')
        self.assertEqual("PixelAccess", type(r).__name__)


if __name__ == '__main__':
    unittest.main()
