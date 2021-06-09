import cv2
import numpy as np


def callbackAction(x):
    pass

# cap = cv2.VideoCapture('../sample/yt1s.com - YouTuber Performs Despacito 2 With Strangers on a Street in Portugal_v720P.mp4')
cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower_Hue", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Lower_Saturation", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Lower_Value", "Tracking", 0, 255, callbackAction)
cv2.createTrackbar("Upper_Hue", "Tracking", 255, 255, callbackAction)
cv2.createTrackbar("Upper_Saturation", "Tracking", 255, 255, callbackAction)
cv2.createTrackbar("Upper_Value", "Tracking", 255, 255, callbackAction)



while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos("Lower_Hue", "Tracking")
    lower_saturation = cv2.getTrackbarPos("Lower_Saturation", "Tracking")
    lower_value = cv2.getTrackbarPos("Lower_Value", "Tracking")
    upper_hue = cv2.getTrackbarPos("Upper_Hue", "Tracking")
    upper_saturation = cv2.getTrackbarPos("Upper_Saturation", "Tracking")
    upper_value = cv2.getTrackbarPos("Upper_Value", "Tracking")

    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])

    print('lower_hue is ', lower_hue)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('video', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('rgb:')
print(frame)
print('hsv:')
print(hsv)
print('mask:')
print(mask)

cap.release()
cv2.destroyAllWindows()
print('q was pressed, window closed!')



