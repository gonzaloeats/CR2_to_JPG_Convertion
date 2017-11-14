#!/usr/bin/env python

import rawpy
import imageio
import glob

paths =glob.glob(str(raw_input("Please provide path for where the .cr2 image files are located, Path example: /home/folder : ")+"/*CR2"))

def convert_images():
    for i in paths:
        raw = rawpy.imread(i)
        rgb = raw.postprocess()
        imageio.imsave(i[:-4]+".jpg", rgb)
        print i
convert_images()
