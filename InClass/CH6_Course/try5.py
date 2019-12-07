# ==< 灰階改變 >== #  -->不行
import numpy as np
import cv2

img = cv2.imread("cat.png", 0) # 讀取檔案(灰階影像:控制function)

for row in img:
    for col in row:
        col = 0 # 如果是灰階圖片,不能改變,只能像list一樣取出值
                # col裡面只有一個值,無法改變裡面的值

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()