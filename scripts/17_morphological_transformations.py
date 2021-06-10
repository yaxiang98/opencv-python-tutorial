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


