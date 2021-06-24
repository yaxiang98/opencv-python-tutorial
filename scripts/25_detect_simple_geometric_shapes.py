import numpy as np
import cv2

img = cv2.imread('../sample/shapes.jpg', cv2.IMREAD_COLOR)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, ret = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
	approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)	# approximate polygon curve
	cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
	x = approx.ravel()[0]	# set text position
	y = approx.ravel()[1] - 10

	if len(approx) == 3:	# if len(approx) is 3, it's gonna be a triangle
		cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

	elif len(approx) == 4:	# maybe a square or a rectangle
		x, y, w, h = cv2.boundingRect(approx)
		aspectRatio = float(w)/h
		print("The aspect ratio is: ", aspectRatio)
		if aspectRatio >= 0.95 and aspectRatio <= 1.05:
			cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
		else:	
			cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

	elif len(approx) == 5:	# maybe a square or a rectangle
		cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

	elif len(approx) == 10:	# maybe a square or a rectangle
		cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

	else:
		cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()