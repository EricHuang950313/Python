import cv2
import numpy as np
def drawTriangle(points,img):
    triangle_cnt = np.asarray(points,dtype='int64')
    cv2.drawContours(img, [triangle_cnt], 0, (0,0,0), -1)

img=np.ones((768,768,3), np.uint8)*255
myPoints = [[0,768],[384,0],[768,768]]
myPoints = np.asarray(myPoints)
p1 = (myPoints[0]+myPoints[1])/2
p2 = (myPoints[0]+myPoints[2])/2
p3 = (myPoints[1]+myPoints[2])/2
drawTriangle([p1,p2,p3],img)
cv2.imshow('test',img)
cv2.waitKey(0)
