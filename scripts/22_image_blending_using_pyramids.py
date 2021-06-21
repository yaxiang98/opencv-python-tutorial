import cv2
import numpy as np

apple = cv2.imread('../sample/apple.jpg')
orange = cv2.imread('../sample/orange.jpg')

print(apple.shape)
print(orange.shape)

# simply stack two image (arrays) horizontally
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# using Pyramids to better blend images
'''
1. Load the two images of apple and orange
2. Find the Gaussian Pyramids for apple and orange
(in this particular example, number os levels is 6).
3. From Gaussian Pyramids, find their Laplacian Pyramids.
4. Now join the left half of apple and right half of orange
in each levels of Laplacian Pyramids.
5. Finally from this joint image pyramids, reconstruct the 
original image.
'''
# generate Gaussian pyramid for apple
apple_copy = apple.copy()
gaussian_apple = [apple_copy]
for i in range(6):
	apple_copy = cv2.pyrDown(apple_copy)
	gaussian_apple.append(apple_copy)

# generate Gaussian Pyramid for orange
orange_copy = orange.copy()
gaussian_orange = [orange_copy]
for i in range(6):
	orange_copy = cv2.pyrDown(orange_copy)
	gaussian_orange.append(orange_copy)

# generate Laplacian Pyramid for apple
apple_copy = gaussian_apple[5]
laplacian_apple = [apple_copy]
for i in range(5, 0, -1):
	gaussian_expended = cv2.pyrUp(gaussian_apple[i])
	laplacian = cv2.subtract(gaussian_apple[i-1], gaussian_expended)
	laplacian_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gaussian_orange[5]
laplacian_orange = [orange_copy]
for i in range(5, 0, -1):
	gaussian_expended = cv2.pyrUp(gaussian_orange[i])
	laplacian = cv2.subtract(gaussian_orange[i-1], gaussian_expended)
	laplacian_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(laplacian_apple, laplacian_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()