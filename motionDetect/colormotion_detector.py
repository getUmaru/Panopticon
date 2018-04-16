import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import winsound


upper = np.array([100,100,100])
lower = np.array([255,255,255])


# set what colors to detect from lowerBound to upperBound
    ## Eg) upper < x < lower
    ## where x is the color being detected

switch = True
switch2 = False


cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(0)


kernelO = np.ones((10, 10))
#bg
kernelC = np.ones((20, 20))
#fg

# we need two kernels (2d matrix) since we have two morphological transformation
# this kernel acts as a sort of intensity for the color filtration
font = cv2.FONT_HERSHEY_SIMPLEX


while True:
    #  Everything within this loop is the processing part and everything outside is constant
    ret, img = cam.read()
    img = cv2.resize(img, (600, 500))
    ret2, im2 = cam2.read()
    # resize the image being outputted for easier image process


    ## HORIZONTAL GRID LINES ##

    #cv2.line(img, (50, 0), (50, 500), (0, 0, 0), 1)
    cv2.line(img, (100, 0), (100, 500), (0, 0, 0), 1)
    #cv2.line(img, (150, 0), (150, 500), (0, 0, 0), 1)
    cv2.line(img, (200, 0), (200, 500), (0, 0, 0), 1)
    #cv2.line(img, (250, 0), (250, 500), (0, 0, 0), 1)
    cv2.line(img, (300, 0), (300, 500), (0, 0, 0), 1)
    #cv2.line(img, (350, 0), (350, 500), (0, 0, 0), 1)
    cv2.line(img, (400, 0), (400, 500), (0, 0, 0), 1)
   # cv2.line(img, (450, 0), (450, 500), (0, 0, 0), 1)
    cv2.line(img, (500, 0), (500, 500), (0, 0, 0), 1)
    #cv2.line(img, (550, 0), (550, 500), (0, 0, 0), 1)
    cv2.line(img, (600, 0), (600, 500), (0, 0, 0), 1)


    ## VERTICAL GRID LINES ##

    #cv2.line(img, (0,50), (600,50), (0, 0, 0), 1)
    cv2.line(img, (0,100), (600,100), (0, 0, 0), 1)
    #cv2.line(img, (0,150), (600,150), (0, 0, 0), 1)
    cv2.line(img, (0,200), (600,200), (0, 0, 0), 1)
    #cv2.line(img, (0,250), (600,250), (0, 0, 0), 1)
    cv2.line(img, (0,300), (600,300), (0, 0, 0), 1)
    #cv2.line(img, (0,350), (600,350), (0, 0, 0), 1)
    cv2.line(img, (0,400), (600,400), (0, 0, 0), 1)
    #cv2.line(img, (0,450), (600,450), (0, 0, 0), 1)
    cv2.line(img, (0,500), (600,500), (0, 0, 0), 1)


    if switch == True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # convert BGR to HSV
        mask = cv2.inRange(imgHSV, upper, lower)
        # create the Mask

    else:

        #imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # convert BGR to RGB
        mask = cv2.inRange(img, upper, lower)
        # create the Mask


    firstFilter = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelO)
    # Remove background noise // erosion followed by dialation
    secondFilter = cv2.morphologyEx(firstFilter, cv2.MORPH_CLOSE, kernelC)
    # Remove foreground noise // dialation followed by erosion
    # morphology

    lastFilter = secondFilter

    _, conts, _ = cv2.findContours(lastFilter.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ## cv2.drawContours(img, conts, -1, (0,255,0), 3) ##
    # The line above is where line bordering is declared

    #cv2.rectangle(img, (200, 200), (400, 300), (0, 0, 255), -1, 100)
    cv2.rectangle(img,(0,0), (600,500), (0,0,255), 200, 1000)


    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if 0 <= x <= 100 or 500 <= y <= 600 or 0 <= y <= 100 or 400 <= y <= 500:
            print("SOMETHING IS WRONG!!!")

            while True:
                #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
                print("hello")
        else:
            print(x, y)

    if switch2 == True:
        plt.imshow(secondFilter, cmap="hsv", interpolation="none")
        plt.imshow(firstFilter, cmap="hsv", interpolation="none")
        plt.imshow(mask, cmap="hsv", interpolation="none")
        plt.imshow(img, cmap="hsv", interpolation="none")
        plt.show()
        plt.waitforbuttonpress(10)
    else:
        cv2.imshow("maskClose", secondFilter)
        cv2.imshow("maskOpen", firstFilter)
        cv2.imshow("mask", mask)
        cv2.imshow("imgGrid", img)
        #cv2.imshow("imgNorm", im2)
        cv2.waitKey(10)
