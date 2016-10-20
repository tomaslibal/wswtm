import unittest

from src.python.image import image2pix, get_resized_pixels

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

    def test_should_return_pix_unchanged_if_same_w_and_h_used(self):
        p, w, h = image2pix('test/resources/test1.png')
        p2, w2, h2 = get_resized_pixels('test/resources/test1.png', w, h)

        self.assertEqual(p, p2)
        self.assertEqual(w, w2)
        self.assertEqual(h, h2)


if __name__ == '__main__':
    unittest.main()
