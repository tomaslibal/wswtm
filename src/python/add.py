import argparse
from image import resize
from image import image2pix

"""
import scipy.misc
img = scipy.misc.imread(path, flatten=False, mode='RGB')
print(img.shape)
"""

dbfilepath = "resources/images/training.csv"

def append_to_file(path, line):
    with open(path, "a") as f:
        f.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transforms image pixel data into an array and saves the array together with labels.')
    parser.add_argument('path', metavar='I', 
                   help='path to the image')
    parser.add_argument('--labels', metavar='L',
                   help='comma separated labels for the image')

    args = parser.parse_args()
    path = args.path
    labels = args.labels

    print "got image path and its labels:"
    print (path, labels)

    p, _, _ = image2pix(path)

    line = ','.join(str(px[0]) + ',' + str(px[1]) + ',' + str(px[2]) for px in p) 
    line += ',' + labels
    line += '\n'

    append_to_file(dbfilepath, line)

    print "stored the image data in " + dbfilepath

        
