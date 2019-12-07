import numpy as np
import cv2

img = cv2.imread("cat.png") # 讀取檔案
print(img.shape) # 顯示寬高比
#img[:,:,0] = 0 # img[列,行,第幾層(BGR)] = 第幾層(BGR)要設定的數值

cv2.imshow("cat", img[120:360,120:360]) # 顯示某個範圍(列,行)
cv2.waitKey(0)
cv2.destroyAllWindows()