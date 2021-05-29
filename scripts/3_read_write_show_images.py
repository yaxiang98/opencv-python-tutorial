import cv2
import os   

img = cv2.imread('/home/yaxiang/yx_ws/opencv_python_tutorial/sample/lena.jpg', 0)   # read an image

print(img)

cv2.imshow('image', img)
# cv2.waitKey(5000)   # wait for 5000ms = 5s
k = cv2.waitKey(0)

lena_copy_path = '/home/yaxiang/yx_ws/opencv_python_tutorial/sample/lena_copy.png'

if k == 27:     # k will be 27 is esc is pressed
    cv2.destroyAllWindows()
    print('ESC key was pressed, window closed!')

elif k == ord('s'):     # if press key 's' in the keybord
    if os.path.exists(lena_copy_path) == False:
        cv2.imwrite(lena_copy_path, img)    # write a image as a new file
    elif os.path.exists(lena_copy_path) == True:
        print('File lena_copy.png already exists!')

