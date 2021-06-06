import cv2
import numpy as np


def callbackAction(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower_Hue", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Lower_Saturation", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Lower_Value", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Upper_Hue", "Tracking", 255, 255, callbackAction)
cv2.createTrackbar("Upper_Saturation", "Tracking", 255, 255, callbackAction)
cv2.createTrackbar("Upper_Value", "Tracking", 255, 255, callbackAction)



while True:
    frame = cv2.imread('../sample/smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('original_image_bgr', frame)
    # cv2.imshow('original_image_hsv', hsv)

    lower_hue = cv2.getTrackbarPos("Lower_Hue", "Tracking")
    lower_saturation = cv2.getTrackbarPos("Lower_Saturation", "Tracking")
    lower_value = cv2.getTrackbarPos("Lower_Value", "Tracking")
    upper_hue = cv2.getTrackbarPos("Upper_Hue", "Tracking")
    upper_saturation = cv2.getTrackbarPos("Upper_Saturation", "Tracking")
    upper_value = cv2.getTrackbarPos("Upper_Value", "Tracking")

    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])

    print(lower_hue)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 第一个参数：hsv指的是原图
    # 第二个参数：lower_blue指的是图像中低于这个lower_blue的值，图像值变为0
    # 第三个参数：upper_blue指的是图像中高于这个upper_blue的值，图像值变为0
    # 而在lower_blue～upper_blue之间的值变成255

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(1)
    if k == 27:     # k will be 27 is esc is pressed
        break

print('rgb:')
print(frame)
print('hsv:')
print(hsv)
print('mask:')
print(mask)

cv2.destroyAllWindows()
print('ESC key was pressed, window closed!')



