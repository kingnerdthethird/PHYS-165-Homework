#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 10:54:43 2018

@author: largueta
"""
# Assignment 1
import scipy.ndimage as sim
import numpy as np
import matplotlib.pyplot as plt


impulse = np.zeros( (51,51) )
impulse [25, 25] = 1.0
myfilter = np.ones( (3, 3) ) / 9
response = sim.convolve(impulse, myfilter)
plt.figure()
plt.imshow(response)
np.array_equal(impulse, response)


# Assignment 2
cat = plt.imread('bwCat.tif')
plt.set_cmap('gray')
myfilter = np.ones( (3, 3) ) / 9
plt.figure()
plt.imshow(cat)


cat2  = sim.convolve(cat, myfilter)
plt.figure()
plt.imshow(cat2)

mysecondfilter= np.ones( (15, 15) ) / 9
cat3 = sim.convolve(cat, mysecondfilter)
plt.figure()
plt.imshow(cat3)

gauss_filter=np.loadtxt("gaussfilter.csv", delimiter= ',')
gaussycat=sim.gaussian_filter(cat, sigma=5)
plt.figure()
plt.imshow(gaussycat)
