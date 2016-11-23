from PIL import Image

def load_image(path):
    pass

def get_resized_pixels(path, width=32, height=32):
    img = Image.open(path)
    img.resize((width, height), resample=Image.BILINEAR)
    p = list(img.getdata())
    return p, width, height

def crop_center(width=32, height=32):
    pass

"""
    Returns a 2d array of 3-tuples where each 3-tuple represents the RGB component of each pixel
    together with the info about the width and the height of the picture
"""
def image2pix(path):
    img = Image.open(path)
    w, h = img.size
    p = list(img.getdata())
    return p, w, h
