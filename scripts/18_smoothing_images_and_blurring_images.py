import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_2 = cv2.imread('../sample/salt-and-pepper-noise-from-wikipedia.png')
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)

img_3 = cv2.imread('../sample/lena.jpg')
img_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2RGB)

# Homogeneous Filter:
# each output pixel is the mean of its kernel neighbors
# the weight is the same across the kernel
kernel = np.ones((5, 5), np.float32)/25
# kernal has to be defined this way: a matrix of 1 divded by its witdh x height
dst = cv2.filter2D(img, -1, kernel)
dst_2 = cv2.filter2D(img_2, -1, kernel)
dst_3 = cv2.filter2D(img_3, -1, kernel)

# --------------------------------------------------------

# low-pass and high-pass filters:
# low-pass helps in removing noises and blurring images
# high-pass helps in finding edges in images
# it is designed to remove the high frequence noise
blur = cv2.blur(img, (5, 5))
blur_2 = cv2.blur(img_2, (5, 5))
blur_3 = cv2.blur(img_3, (5, 5))

# --------------------------------------------------------

# Gaussian filter:
# Gaussian filter is nothing but using 
# different-weight-kernel in both x and y direction
# it is designed to remove the high frequence noise
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
gaussian_blur_2 = cv2.GaussianBlur(img_2, (5, 5), 0)
gaussian_blur_3 = cv2.GaussianBlur(img_3, (5, 5), 0)

# --------------------------------------------------------

# Median Filter:
# a filter that replace each pixel's value with the median of
# its neighboring pixels. Great for dealing with "salt and pepper"
# noise. (椒盐噪音)
median_blur = cv2.medianBlur(img, 5)
median_blur_2 = cv2.medianBlur(img_2, 5)
median_blur_3 = cv2.medianBlur(img_3, 5)

# ---------------------------------------------------------

# Bilateral Filter:
# bilateral filter is very helpful in noise removal while keeping 
# the edge sharp, best example for lena.jpg
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)
bilateralFilter_2 = cv2.bilateralFilter(img_2, 9, 75, 75)
bilateralFilter_3 = cv2.bilateralFilter(img_3, 9, 75, 75)

titles = ['Original Image', '2D Convolution', 'Blurring', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gaussian_blur, median_blur, bilateralFilter]

titles_2 = ['Original Image', '2D Convolution', 'Blurring', 'GaussianBlur', 'Median Blur', 'Bilateral Filter']
images_2 = [img_2, dst_2, blur_2, gaussian_blur_2, median_blur_2, bilateralFilter_2]

titles_3 = ['Original Image', '2D Convolution', 'Blurring', 'GaussianBlur', 'Median Blur', 'Bilateral Filter']
images_3 = [img_3, dst_3, blur_3, gaussian_blur_3, median_blur_3, bilateralFilter_3]



for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()

for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images_2[i], 'gray')
	plt.title(titles_2[i])
	plt.xticks([])
	plt.yticks([])
plt.show()

for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images_3[i], 'gray')
	plt.title(titles_3[i])
	plt.xticks([])
	plt.yticks([])
plt.show()
