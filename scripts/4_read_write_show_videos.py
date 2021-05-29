import cv2

cap = cv2.VideoCapture(0)   # arg = 0 means device camera, can also provide file name
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('3_output.avi', fourcc, 20.0, (640, 480)) # 20 fps, 640x480 pixels

# cap.isOpened() = True if cv2.VideoCapture is reading video
while(cap.isOpened()):
    ret, frame = cap.read() # 'ret' will return True or False indicates the frame avilability, 'frame' will capture the frame.
    if ret == True:
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)       
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)    # get video width information, more paramters: https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d  
        print('the width of the video is ', width) 
        print('the height of the video is ', height)

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('front camera', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()   # release the captured variables
cv2.destroyAllWindows()
