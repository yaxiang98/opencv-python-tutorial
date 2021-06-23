# https://youtu.be/FbR9Xr0TVdY
'''
for using cv2.findContours() to automatically find contours,
we generally use binary images for better accuracy.
First of all, we generate the binary image, then before finding
the contours, we will apply the threshold or canny edge detection
to find the contours in the image.
'''

import numpy as py
import cv2

img = cv2.imread('../sample/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours is a Python list of all the contours in the image.
# Each individual contour is a Numpy array of (x, y) coordinates
# of boundary points of the object.
print('Number of contours = ' + str(len(contours)))
print('Value of the first contour: ', contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.imshow('Thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()