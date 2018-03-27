import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sina.jpg', cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55]

roi = img[100:150, 100:150] = [0,0,0]


eye = img[400:700, 400:450]
img[0:300, 0:50] = eye




cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img, cmap='gray', interpolation='bicubic')
##plt.show()