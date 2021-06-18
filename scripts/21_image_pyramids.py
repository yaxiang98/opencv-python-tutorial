# https://youtu.be/8yvln2atFkA
# Pyramid, or pyramid representation, is a type of multi-scale
# signal representation in which a signal or an image is subject
# to repeated smoothing and subsampling.	---- Wikipedia

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/lena.jpg')
print('Original image resolution is ', img.shape)

# -----------------------------------------
# Gaussian Pyramids
# -----------------------------------------
# cv2.pyrDown to reduce resolution
lower_resolution = cv2.pyrDown(img)
lower_resolution2 = cv2.pyrDown(lower_resolution)

# cv2.pyrUp to increase the resolution
higher_resolution = cv2.pyrUp(lower_resolution2)

# create a pyramid of multiple resolution using 'for' loop
layer = cv2.imread('../sample/sudoku.png')
gaussian_pyramid = [layer]

for i in range(6):
	layer = cv2.pyrDown(layer)
	gaussian_pyramid.append(layer)
	cv2.imshow(str(i), layer)

# ------------------------------------------
# Laplacian Pyramids
# ------------------------------------------
# there's no exclusive function to create Laplacian Pyramids
''' A level in Laplacian Pyramid is formed by the difference
between that level in Gaussian Pyramid and expanded version of
its upper level in Gaussian Pyramid.
In this case, the upper level Gaussian Pyramid is gaussian_pyramid[5] '''
layer = gaussian_pyramid[5]
cv2.imshow('Upper Level Gaussian Pyramid', layer)
laplacian_pyramids = [layer]

for i in range(5, 0, -1):	# start from 5 and go until 1 in the step of -1
	print(i)
	gaussian_extended = cv2.pyrUp(gaussian_pyramid[i])
	laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_extended)
	cv2.imshow(str(i), laplacian)


cv2.imshow('Original Image', img)
cv2.imshow('pyrDown Once', lower_resolution)
cv2.imshow('pyrDown Twice', lower_resolution2)
cv2.imshow('pyrUp Once', higher_resolution)
cv2.waitKey(0)
cv2.destroyAllWindows()