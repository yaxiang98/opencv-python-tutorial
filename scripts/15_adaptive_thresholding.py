import cv2 as cv
import numpy as np

img = cv.imread('../sample/sudoku.png', 0)

# colored image need to be converted to gray scale to apply thresholding methods
ret, thres1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thres2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
thres3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Image', img)
cv.imshow('Static thresholding', thres1)
cv.imshow('Adaptive thresholding Mean C', thres2)
cv.imshow('Adaptive thresholding Gaussian C', thres3)

cv.waitKey(0)
cv.destroyAllWindows()
