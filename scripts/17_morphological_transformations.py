import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/smarties.png', cv2.IMREAD_GRAYSCALE)
ret, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)
# the mask is a binary image that only has 1 and 0

kernal = np.ones((5, 5), np.uint8)
# kernal size of 2x2 and iterations = 1 will be the best
# performance in this picture.


dilation = cv2.dilate(mask, kernal, iterations=2)
# dilate method applies kernal to each pixel and if there
# at least one pixel within the kernal is 1, the pixel will be 1.
erosion = cv2.erode(mask, kernal, iterations=5)
# erosion method applies kernal to each pixel and only when
# all pixels are 1, the pixel applied will be 1.
openning = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# openning is an erosion followed by a dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# closing is a dilation followed by a erosion
morph_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
morph_tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)


titles = ['image', 'mask', 'dilation', 'erosion', 'openning', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, openning, closing, morph_gradient, morph_tophat]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()