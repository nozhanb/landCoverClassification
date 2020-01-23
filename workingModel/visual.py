#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:33:23 2019

@author: nozhan
"""

from matplotlib import colors
import matplotlib.pyplot as plt

def city_map(inputData, height = None, width = None):
    """ This method creates a thematic map of a given image."""
    
    inputData[inputData == 'b'] = 0
    inputData[inputData == 'c'] = 1
    inputData[inputData == 'f'] = 2
    inputData[inputData == 't'] = 3
    inputData[inputData == 'w'] = 4

    inputData = inputData.reshape(height, width)

    cmap = colors.ListedColormap(['red','white','yellow','green','blue'])

    fig, ax = plt.subplots(figsize=(15, 15))
    
    # The following line turns the axes off.
    plt.axis('off') 
    ax.imshow(inputData.astype('float32'), cmap = cmap)

    fig.savefig('thematicMap.png', bbox_inches='tight', format = 'png')





