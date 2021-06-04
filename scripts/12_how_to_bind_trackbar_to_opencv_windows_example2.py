import numpy as np
import cv2 as cv


def callbackAction(x):
    print(x)


cv.namedWindow('image')

cv.createTrackbar('CurrentPos', 'image', 10, 400, callbackAction)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, callbackAction)


while(1):
    img = cv.imread('../sample/lena.jpg')
    pos = cv.getTrackbarPos('CurrentPos', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('image', img)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
