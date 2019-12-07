# ==< 針對彩色 >== #  -->改變藍色
import numpy as np
import cv2

img = cv2.imread("cat.png")

(rows,cols,channel) = img.shape
for row in range(rows):
    for col in range(cols):
        img[row,col,0] = 0 # img[列,行,第零層:藍色] -->只改變藍色

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()