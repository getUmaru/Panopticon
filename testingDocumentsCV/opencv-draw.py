import numpy as np
import cv2

img = cv2.imread('sina.jpg', cv2.IMREAD_COLOR)

#cv2.line(img, (250,250), (550,550), (0,0,0), 15)
cv2.rectangle(img, (5,25), (305,150), (0,255,0,), 5)









cv2.circle(img, (100,85), 55, (33,80,40), -1)

cv2.circle(img, (200,170), 55, (102,255,255), -1)











pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Opencv', (250,500), font, 5, (0,0,0,), 5,cv2.LINE_AA)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()