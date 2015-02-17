from PIL import Image
import sys

im_path = '' 
out_path = 'out.txt'

# Config
resample_w = 64
resample_h = 64

# Value 0 will return only the red component of each pixel value when passed
# to Image.getdata
pixel_component = 0

# Set up the variables from the arguments
if len(sys.argv) >= 2:
    im_path = sys.argv[1]
else:
    print "Usage: get-pixels.py imgPath [outputPath]"
    sys.exit()

if len(sys.argv) >= 3:
    out_path = sys.argv[2]

try:
    im = Image.open(im_path)
except IOError:
    print "Error opening the file ", im_path
    sys.exit()


im = im.resize((resample_w, resample_h))
pixels = list(im.getdata(pixel_component))
width, height = im.size
pixelsMN = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

print >> open('out.txt', 'w'), pixels

print "Reading image", im_path
print "Width (px): ", width
print "Height (px): ", height
