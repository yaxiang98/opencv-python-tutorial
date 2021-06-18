# https://youtu.be/aDY4aBLFOIg
# An image gradient is a directional change in the
# intensity or color in an image

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('../sample/messi5.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('../sample/sudoku.png', cv2.IMREAD_GRAYSCALE)

# Laplacian gradient method
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
lap_k3 = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap_k3 = np.uint8(np.absolute(lap_k3))
lap_k5 = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
lap_k5 = np.uint8(np.absolute(lap_k5))

# Sobel Gradient Representation
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # third arguement is the x 导数的阶
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) # fourth arguement is the y 导数的阶
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

SobelCombined = cv2.bitwise_or(sobelX, sobelY)
SobelCombined_inv = cv2.bitwise_not(SobelCombined)

titles = ['iamge', 'Laplacian (Default Kernal Size = 1)', 'Laplacian (Kernal Size = 3)', 'Laplacian (Kernal Size = 5)', 'SobelX', 'SobelY', 'Sobel X and Y Combined', 'Sobel X and Y Combined Inv']
images = [img, lap, lap_k3, lap_k5, sobelX, sobelY, SobelCombined, SobelCombined_inv]
for i in range(8):
	plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])

plt.show()