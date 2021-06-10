import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/smarties.png', cv2.IMREAD_GRAYSCALE)
ret, mask = cv2.threshold(img, 220, 225, cv2.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
# dilate method applies kernal to each pixel and if there
# at least one pixel within the kernal is 1, the pixel will be 1.
erosion = cv2.erode(mask, kernal, iterations=5)
# erosion method applies kernal to each pixel and only when
# all pixels are 1, the pixel applied will be 1.
openning = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

morph_gradient = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# kernal size of 2x2 and iterations = 1 will be the best
# performance in this picture.

titles = ['image', 'mask', 'dilation', 'erosion', 'openning']
images = [img, mask, dilation, erosion]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()