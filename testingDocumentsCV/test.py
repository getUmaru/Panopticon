import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('img/sina.jpg')
x = 250

y =  250

cv2.rectangle(img, (100,100), (400,500), (0, 0, 255,), 100, 1)


if 100 <= x <= 400 and 100 <= y <= 500:
    print("SOMETHING IS WRONG!!!")
else:
    print(x, y)

cv2.imshow("name", img)
cv2.waitKey(0)
cv2.destroyAllWindows()