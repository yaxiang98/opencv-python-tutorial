# https://youtu.be/FbR9Xr0TVdY
'''
for using cv2.findContours() to automatically find contours,
we generally use binary images for better accuracy.
First of all, we generate the binary image, then before finding
the contours, we will apply the threshold or canny edge detection
to find the contours in the image.