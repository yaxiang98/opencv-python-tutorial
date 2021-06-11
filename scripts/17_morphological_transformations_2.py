import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/j.png', cv2.IMREAD_GRAYSCALE)
# ret, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)
# the mask is a binary image that only has 255 and 0
# don't need mask here because j.png is already a binary image
cv2.imshow('image', img)

kernal = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(img, kernal, iterations=2)
# dilate method applies kernal to each pixel and if there
# at least one pixel within the kernal is 1, the pixel will be 1.
erosion = cv2.erode(img, kernal, iterations=5)
# erosion method applies kernal to each pixel and only when
# all pixels are 1, the pixel applied will be 1.
openning = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
# openning is an erosion followed by a dilation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)
# closing is a dilation followed by a erosion
morph_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
morph_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)


titles = ['image', 'mask', 'dilation', 'erosion', 'openning', 'closing', 'mg', 'th']
images = [img, img, dilation, erosion, openning, closing, morph_gradient, morph_tophat]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()