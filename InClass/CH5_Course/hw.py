import numpy as np 
import cv2

img = np.zeros((450,675,3),np.uint8)

cv2.rectangle(img, (0,0), (675,450), (255,255,255), -1)

cv2.rectangle(img, (0,0), (675,50), (137,20,0), -1)
cv2.rectangle(img, (0,100), (675,150), (137,20,0), -1)
cv2.rectangle(img, (0,200), (675,250), (137,20,0), -1)
cv2.rectangle(img, (0,300), (675,350), (137,20,0), -1)
cv2.rectangle(img, (0,400), (675,450), (137,20,0), -1)

cv2.rectangle(img, (0,0), (108,108), (137,20,0), -1)
cv2.rectangle(img, (162,0), (270,108), (137,20,0), -1)
cv2.rectangle(img, (0,150), (108,250), (137,20,0), -1)
cv2.rectangle(img, (150,150), (270,250), (137,20,0), -1)

cv2.rectangle(img, (0,100), (270,150), (255,255,255), -1)
cv2.rectangle(img, (108,270), (162,0), (255,255,255), -1)

cv2.imshow("Title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()