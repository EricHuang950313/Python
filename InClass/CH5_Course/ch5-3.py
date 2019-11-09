import numpy as np
import cv2
import random

img1 = np.zeros((512,768,3),np.uint8)

cv2.rectangle(img1, (0,0), (768,512), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1)
# (圓心座標:列與行相反, 半徑, 顏色, 實心或邊框的粗度:-1是實心)
cv2.circle(img1, (384,255), 175, (0, 0, 255), -1)
cv2.circle(img1, (384,255), 150, (0, 127, 255), -1)
cv2.circle(img1, (384,255), 125, (0, 255, 255), -1)
cv2.circle(img1, (384,255), 100, (0, 255, 0), -1)
cv2.circle(img1, (384,255), 75, (255, 127, 0), -1)
cv2.circle(img1, (384,255), 50, (255, 0, 0), -1)
cv2.circle(img1, (384,255), 25, (255, 0, 127), -1)

cv2.imshow("Title1", img1)


img2 = np.zeros((512,768,3),np.uint8)
cv2.rectangle(img2, (0,0), (768,512), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1)

l = [(255, 0, 127),(255, 0, 0),(255, 127, 0),(0, 255, 0),(0, 255, 255),(0, 127, 255),(0, 0, 255)]
x = 175
for c in l:
    cv2.circle(img2, (384,255), x, c, -1)
    x -= 25

cv2.imshow("Title2", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()