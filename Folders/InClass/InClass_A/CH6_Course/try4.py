# ==< 針對彩色 >== #  -->改變藍色
import numpy as np
import cv2

img = cv2.imread("cat.png")

for row in img:
    for col in row:
        col[0] = 0 # col[第零層:藍色]

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()