#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:18:13 2019

@author: nozhan
"""

import os
#import gdal
import numpy
import affine
import pandas
#import imageio
import rasterio
import numpy.ma

#from scipy.stats import normaltest
#from rasterio.plot import show, show_hist

def data_frame():
    """ The following function will generate a dataFrame with four different columns for each pixel; red, green, blue, and infrared bands. Also,
    it assumes the uploaded images follow this naming syntax; "image__Sentinel2_*.png" where instead of * the user has to put the band number (e.g. B04).
    It, also, generates the height and width of the images to be used in visual.py. The output will be: data, height, width"""
#    path, direct, files = next(os.walk(os.path.join(os.getcwd(),'uploads')))
    landType  = ["image"]
    testFrameList = [] 
    for ltype in landType:
        redPath   = pathlib.Path("uploads/" + ltype + "_Sentinel2_B04.png")
        greenPath = pathlib.Path("uploads/" + ltype + "_Sentinel2_B03.png")
        bluePath  = pathlib.Path("uploads/" + ltype + "_Sentinel2_B02.png")
        irPath    = pathlib.Path("uploads/" + ltype + "_Sentinel2_B08.png")
        
        redImage   = numpy.moveaxis(numpy.array(Image.open(redPath)), 1, 0)
        greenImage = numpy.moveaxis(numpy.array(Image.open(greenPath)), 1, 0)
        blueImage  = numpy.moveaxis(numpy.array(Image.open(bluePath)), 1, 0)
        irImage    = numpy.moveaxis(numpy.array(Image.open(irPath)), 1, 0)
        
        # Take the width and height of our test image to be used in the last block for visualisation
        testImgDims= redImage.shape
        
        redBand   = redImage.flatten().astype(int)
        greenBand = greenImage.flatten().astype(int)
        blueBand  = blueImage.flatten().astype(int)
        irBand    = irImage.flatten().astype(int)
        
        label   = numpy.repeat(ltype, redImage.size).astype(str)
        stacked = numpy.column_stack((redBand, greenBand, blueBand, irBand))
        dataFrame = pandas.DataFrame(stacked, columns = ["red", "green", "blue", "IR"])
        testFrameList.append(dataFrame)
    finalTestFrame = pandas.concat(testFrameList)
    return finalTestFrame, testImageDims[1], testImageDims[0] 
