import numpy as np
import cv2


# create a script to listen for the mouse event
# create a callback function which is executed  when mouse event takes place
def click_event(event, x, y, flags, param): # event is the mouse event, (x, y) is the position of the event
    if event == cv2.EVENT_LBUTTONDOWN: # left click
        print(x, ',', y)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        # points = []
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 255, 255), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]
        cv2.imshow('color', mycolorImage)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('../sample/lena.jpg')
cv2.imshow('image', img)

points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()


