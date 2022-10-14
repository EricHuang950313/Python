# ==< 灰階影像 >== #
import numpy as np
import cv2

img = cv2.imread("cat.png", 0) # 讀取檔案(灰階影像:控制function)

cv2.imshow("cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()