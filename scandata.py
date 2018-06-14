#!usr/bin/python
import glob
import argparse as ap
import matplotlib.image as img
import numpy as np

#from PIL import Image

def getimages(fdir = "../dataset/PetImages/Cat", fformat = '.jpg'):

    filelist = glob.glob(fdir+'/*'+fformat)
    #images= np.array([np.array(Image.open(fname)) for fname in filelist])
    images = np.array([np.array(img.imread(fname)) for fname in filelist])

    #filter invalid images, where image dimension is != 3 and content is different from RGB
    images = np.array(list(filter(lambda x: x.ndim ==3 and x.shape[2] == 3, images)))

    return images

def alignimages(images):
    x_size = max(x.shape[0] for x in images)
    y_size = max(y.shape[1] for y in images)

    #append 0's to align image size
    imgs = np.array([np.pad(image,
                            ((0,(x_size - image.shape[0])),
                             (0,(y_size - image.shape[1])),
                            (0,0)),
                           'constant', constant_values=(0)) for image in images])
    return imgs

if __name__ == '__main__':

    """ Capture below inputs from the user and initiate imagescan
    """
    parser = ap.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, help="dir to pick images from", default="../dataset/PetImages/Cat")
    parser.add_argument("-f", "--format", type=str, help="format of images", default=".jpg")
    #parser.add_argument("-w", "--write", type=str, help="File name to dump array to")

    #parse the arguments received
    args = parser.parse_args()
    fdir = args.dir
    fformat = args.format
    #writeto = args.write

    #get images
    images = getimages(fdir=fdir, fformat=fformat)
    images = alignimages(images)


    """
    uncomment following line to dump output array to a file
    if writeto:
        images.dump(writeto)
    """
