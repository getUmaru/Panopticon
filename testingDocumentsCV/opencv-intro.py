import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/sina.jpg',cv2.IMREAD_GRAYSCALE)

##cv2.imshow('image', img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

plt.imshow(img, cmap='magma', interpolation='mitchell')
plt.plot([50,100],[80,100],'c', linewidth=5)
plt.show()

#cv2.imshow('sinagray.png',img)