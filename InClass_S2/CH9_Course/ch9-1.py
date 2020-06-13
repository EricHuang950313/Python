import cv2
import numpy as np
import sys

def drawTriangle(points,img):
    triangle_cnt = np.asarray(points,dtype='int64')
    cv2.drawContours(img, [triangle_cnt], 0, (0,0,0), -1)

def sierpinski(myPoints,degree,img):
    p1 = myPoints[0]
    p2 = myPoints[1]
    p3 = myPoints[2]
    q1 = (p1+p2)/2
    q2 = (p1+p3)/2
    q3 = (p2+p3)/2
    drawTriangle([q1, q2, q3], img)
    if degree > 1:
        sierpinski([p1,q1,q2], degree-1, img)
        sierpinski([q1,p2,q3], degree-1, img)
        sierpinski([q2,q3,p3], degree-1, img)
    else:
        return

def mymain(degree):
    img=np.ones((768,768,3), np.uint8)*255 # 產生畫布
    myPoints = [[0,768],[384,0],[768,768]] # 三角形的3個頂點
    myPoints = np.asarray(myPoints)
    sierpinski(myPoints,degree,img)
    cv2.imshow('test',img)
    k = cv2.waitKey(100)
    if k == ord("q"):
        sys.exit()
degree = 1
increase = True
while True:
    if degree == 7:
        increase = False
    elif degree == 1:
        increase = True
    if increase == True:
        degree += 1
    else:
        degree -= 1
    mymain(degree)