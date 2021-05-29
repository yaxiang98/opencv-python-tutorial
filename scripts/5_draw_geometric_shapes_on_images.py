import numpy as np
import cv2

img = cv2.imread('lena_copy.png', 1) # 1 is colored mode, 0 is gray mode

img = cv2.line(img, (0,0), (500,500), (0, 255, 0), 10) # color in (G,B,R) order

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
