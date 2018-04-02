import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerRed = np.array([50,100,200])
    upperRed = np.array([255,255,255])

    mask = cv2.inRange(hsv, lowerRed, upperRed)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("res",res)
    cv2.imshow("mask",mask)
    cv2.imshow("framwe",frame)

    cv2.waitKey(1)
