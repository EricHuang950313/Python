import numpy as np 
import cv2

img = np.zeros((512,768,3), np.uint8)
cv2.rectangle(img, (0,0), (768,512), (255,255,255), -1)

BlackWhiteList = [0,64,128,192,256,320,384,448,512,576,640,704]
OutList = [0,16,32,16,0,16,32,16]
Black = True
Time = 0

for i in OutList:
    for j in BlackWhiteList:
        if Black == True:
            cv2.rectangle(img, (j+i,BlackWhiteList[Time]), (j+64+i,BlackWhiteList[Time+1]), (0,0,0), -1)
            Black = False
        else:
            cv2.rectangle(img, (j+i,BlackWhiteList[Time]), (j+64+i,BlackWhiteList[Time+1]), (255,255,255), -1)
            Black = True
    cv2.rectangle(img, (0,BlackWhiteList[Time]), (768,BlackWhiteList[Time]+64), (0,0,0), 2)
    Time += 1

cv2.imshow("Title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()