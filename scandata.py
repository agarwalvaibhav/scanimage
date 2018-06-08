#!usr/bin/python
import glob
import argparse as ap
import matplotlib.image as img
import numpy as np

#from PIL import Image

def getimages(fdir = "../dataset/PetImages/Cat", fformat = '.jpg'):

    filelist = glob.glob(fdir+'/*'+fformat)
    #imgarray = np.array([np.array(Image.open(fname)) for fname in filelist])
    imgarray = np.array([np.array(img.imread(fname)) for fname in filelist])

    return imgarray

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
    imgarray = getimages(fdir=fdir, fformat=fformat)

    """
    uncomment following line to dump output array to a file
    if writeto:
        imgarray.dump(writeto)
    """
