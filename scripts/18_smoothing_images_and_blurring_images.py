import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../sample/opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
# kernal has to be defined and divded by its witdh x height
dst = cv2.filter2D()

titles = ['image']
