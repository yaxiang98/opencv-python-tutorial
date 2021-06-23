# https://youtu.be/MkcUgPhOlP8

import numpy as np
import cv2

cap = cv2.VideoCapture('../sample/vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
	diff = cv2.absdiff(frame1, frame2) # absolute difference
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	ret, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations=3)
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	frame3 = frame1.copy()	
	cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

	# draw rectangles, not contours and show rectangles in a different window
	for contour in contours:
		(x, y, width, height) = cv2.boundingRect(contour)

		if cv2.contourArea(contour) < 700:
			continue # if the contour size is less than 700, draw nothing. This is for ignore the noise which is the strips in the videos
		else:
			cv2.rectangle(frame3, (x, y), (x+width, y+height), (0, 255, 0), 2)
			cv2.putText(frame3, 'Status: {}'.format('Movement'), (10, 21),
						cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255, 3))
	cv2.imshow('rectangle', frame3)
	

	cv2.imshow('diff', diff)
	cv2.imshow('initial detection and tracking', frame1)
	frame1 = frame2
	ret, frame2 = cap.read()

	if cv2.waitKey(40) == 27:
		break

cv2.destroyAllWindows()
cap.release()
