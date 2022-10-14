# ==< 彩色改變 >== #  -->可以
import numpy as np
import cv2

img = cv2.imread("cat.png") 

for row in img:
    for col in row: 
        col[0] = 0 # col裡面有三個值(像list一樣包起來,實際上是ndarray)所以可以用[0][1][2]改變裡面的三個值
        ''' for c in col:  #測試
            print(col)     #測試     ''' 

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()