# ==< 針對灰階 >== #  -->全部變黑色
import numpy as np
import cv2

img = cv2.imread("cat.png")

(rows,cols, channel) = img.shape # 彩色影像會存入三個值,可以只用前兩個
for row in range(rows):
    for col in range(cols):
        img[row,col] = 0

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()