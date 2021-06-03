import cv2

cap = cv2.VideoCapture('../sample/yt1s.com - YouTuber Performs Despacito 2 With Strangers on a Street in Portugal_v720P.mp4')

print("The original size of the video is ", cap.get(cv2.CAP_PROP_FRAME_WIDTH), "x", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Trying to set the size to 640 x 480")
cap.set(3, 640)    # 3 means width
cap.set(4, 480)     # 4 means height
print("The final displayed size is", cap.get(3), "x", cap.get(4))
# print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # this line convert colored video to gray video
        cv2.imshow('front camera', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



