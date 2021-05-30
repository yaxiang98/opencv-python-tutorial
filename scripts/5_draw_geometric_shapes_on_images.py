import numpy as np
import cv2

img = cv2.imread('lena_copy.png', 1) # 1 is colored mode, 0 is gray mode

img = cv2.line(img, (0,0), (500,500), (0, 255, 0), 10) # color in (B, G, R) order
img = cv2.arrowedLine(img, (0,250), (250, 0), (255, 0, 0), 10) # 10 is thickness

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10) # 10 is thickness or -1 would be a filled rectangle
img = cv2.circle(img, (159, 63), 63, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# create a black image using numpy and do the same drawing
img2 = np.zeros([512, 512, 3], np.uint8)

img2 = cv2.line(img2, (0,0), (500,500), (0, 255, 0), 10) # color in (B, G, R) order
img2 = cv2.arrowedLine(img2, (0,250), (250, 0), (255, 0, 0), 10) # 10 is thickness

img2 = cv2.rectangle(img2, (384, 0), (510, 128), (0, 0, 255), 10) # 10 is thickness or -1 would be a filled rectangle
img2 = cv2.circle(img2, (159, 63), 63, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img2 = cv2.putText(img2, 'OpenCv', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


