import cv2
import numpy as np


img = cv2.imread("img/ref/bookpage.jpg")


retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# cleaning the image up a little
kernelo = np.array([50,50])
kernelc = np.array([100,100])

masko = cv2.morphologyEx(gaus, cv2.MORPH_OPEN, kernelo)
maskc = cv2.morphologyEx(masko, cv2.MORPH_CLOSE, kernelc)

final = maskc

cv2.imshow("img", img)
cv2.imshow("thresh", threshold)
cv2.imshow("thres2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("final", final)


cv2.waitKey(0)
cv2.destroyAllWindows()