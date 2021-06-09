import cv2 as cv
import numpy as np

img = cv.imread('../sample/gradient.png', 0)

# these thresholding methods can only be used to gray scale image
# if it is colored image, convert it first!
ret, thres1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
ret, thres2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
ret, thres3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
ret, thres4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
ret, thres5 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)

cv.imshow('image', img)
cv.imshow('Thresh_Binary', thres1)
cv.imshow('Thresh_Binary_Inv', thres2)
cv.imshow('Thresh_Trunc', thres3)
cv.imshow('Thresh_Tozero', thres4)
cv.imshow('Thresh_Tozero_Inv', thres5)

cv.waitKey(0)
cv.destroyAllWindows()
