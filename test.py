import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import imageio
import sys, os, re

num_outfiles = 4
infile = 'dataset\AyamBrand_Sardines_425g\AYAMBRAND_SARDINES_425G0001.jpg'

img = imageio.imread(infile)

path, filename = os.path.split(infile)
print(path)

name, text = os.path.splitext(path + '/' + filename)
justName, type = os.path.splitext(filename)
print("name: ", name)
print("path: ", path)
annotfile = (name+".txt")
file = open(annotfile, 'r')
print(justName)
print("filename: ", filename)