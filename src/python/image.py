from PIL import Image

def load_image(path):
    pass

def resize(width=32, height=32):
    pass

def crop_center(width=32, height=32):
    pass

"""
    Returns a 2d array of 4-tuples where each 4-tuple represents the RGBA component of each pixel
"""
def image2pix(path):
    img = Image.open(path)
    return img.load()
