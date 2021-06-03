import numpy as np
import cv2

img = cv2.imread('../sample/messi5.jpg')
img2 = cv2.imread('../sample/opencv-logo.png')

print("The shape of the image is: ", img.shape)
print("The total pixels of the image: ", img.size)
print("The data type of the image: ", img.dtype)
b, g, r = cv2.split(img)
print(b)
img = cv2.merge((b, g, r))

# copying a ROI (region of interest) into another region
ball = img[280:340, 330:390]
# print(ball)
img[273:333, 100:160] = ball

# resizing the two image into the same size
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
dst = cv2.add(img, img2)    # simply add the numbers
dst2 = cv2.addWeighted(img, 0.1, img2, 0.9, 0)

cv2.imshow('image', dst)
cv2.imshow('image2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

