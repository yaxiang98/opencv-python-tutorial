import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('../sample/lena.jpg', -1)

cv2.imshow('imshow() with OpenCV', img)
plt.imshow(img)
# matplotlib shows image in RBG format, the image
# read by opencv is in BGR, need to convert it first

img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rbg)
plt.show()


# --- showing all six simple thresholding results in one matplotlib window ---
gradient_img = cv.imread('../sample/gradient.png', 0)

ret, thres1 = cv.threshold(gradient_img, 50, 255, cv.THRESH_BINARY)
ret, thres2 = cv.threshold(gradient_img, 200, 255, cv.THRESH_BINARY_INV)
ret, thres3 = cv.threshold(gradient_img, 50, 255, cv.THRESH_TRUNC)
ret, thres4 = cv.threshold(gradient_img, 50, 255, cv.THRESH_TOZERO)
ret, thres5 = cv.threshold(gradient_img, 50, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thres1, thres2, thres3, thres4, thres5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
