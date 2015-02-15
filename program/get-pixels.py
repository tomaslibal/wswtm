from PIL import Image
import sys

im_path = "../data/class_building/images/152451710_87e0045334_q.jpg"
 
try:
    im = Image.open(im_path)
except IOError:
    print "Error opening the file ", im_path
    sys.exit()


pixels = list(im.getdata())
width, height = im.size
pixelsMN = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

print >> open('out.txt', 'w'), pixels

print "Reading image", im_path
print "Width (px): ", width
print "Height (px): ", height
