import cv2
import numpy as np

leftlowerMin = np.array([33,80,40])
righthigherMax = np.array([102,255,255])
# set what colors to detect from lowerBound to upperBound
    ## Eg) lowerbound < x < upperBound
    ## where x is the color being detected

switch = True

cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    #  Everything within this loop is the processing part and everything outside is constant
    ret, img = cam.read()
    img = cv2.resize(img, (600, 500))
    # resize the image being outputted


    if switch == True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # convert BGR to HSV
        mask = cv2.inRange(imgHSV, leftlowerMin, righthigherMax)
        # create the Mask
    else:

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # convert BGR to RGB
        mask = cv2.inRange(imgRGB, leftlowerMin, righthigherMax)
        #  create the Mask

    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)
    # morphology

    maskFinal = maskClose

    _, conts, _ = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, conts, -1, (0,255,0), 3) ##
    # The line above is where line bordering the color is declared

    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        ## cv2.putText(img, str(i + 1), (x, y + h), font, (0, 255, 255),5,cv2.LINE_AA)
    cv2.imshow("maskClose", maskClose)
    cv2.imshow("maskOpen", maskOpen)
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    cv2.waitKey(10)