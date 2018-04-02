import numpy as np
import cv2

img = cv2.imread('img/sina.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (100,0), (100,700), (0,0,0), 1)
cv2.rectangle(img, (5,25), (305,150), (0,255,0,), 5)

## HORIZONTAL GRID LINES ##
cv2.line(img, (50, 0), (50, 500), (0, 0, 0), 1)
cv2.line(img, (100, 0), (100, 500), (0, 0, 0), 1)
cv2.line(img, (150, 0), (150, 500), (0, 0, 0), 1)
cv2.line(img, (200, 0), (200, 500), (0, 0, 0), 1)
cv2.line(img, (250, 0), (250, 500), (0, 0, 0), 1)
cv2.line(img, (300, 0), (300, 500), (0, 0, 0), 1)
cv2.line(img, (350, 0), (350, 500), (0, 0, 0), 1)
cv2.line(img, (400, 0), (400, 500), (0, 0, 0), 1)
cv2.line(img, (450, 0), (450, 500), (0, 0, 0), 1)
cv2.line(img, (500, 0), (500, 500), (0, 0, 0), 1)
cv2.line(img, (550, 0), (550, 500), (0, 0, 0), 1)
cv2.line(img, (600, 0), (600, 500), (0, 0, 0), 1)

## VERTICAL GRID LINES ##
cv2.line(img, (0, 50), (600, 50), (0, 0, 0), 1)
cv2.line(img, (0, 100), (600, 100), (0, 0, 0), 1)
cv2.line(img, (0, 150), (600, 150), (0, 0, 0), 1)
cv2.line(img, (0, 200), (600, 200), (0, 0, 0), 1)
cv2.line(img, (0, 250), (600, 250), (0, 0, 0), 1)
cv2.line(img, (0, 300), (600, 300), (0, 0, 0), 1)
cv2.line(img, (0, 350), (600, 350), (0, 0, 0), 1)
cv2.line(img, (0, 400), (600, 400), (0, 0, 0), 1)
cv2.line(img, (0, 450), (600, 450), (0, 0, 0), 1)
cv2.line(img, (0, 500), (600, 500), (0, 0, 0), 1)







#cv2.circle(img, (100,85), 55, (33,80,40), -1)

#cv2.circle(img, (200,170), 55, (102,255,255), -1)











pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (255,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Opencv', (250,500), font, 5, (0,0,0,), 5,cv2.LINE_AA)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()