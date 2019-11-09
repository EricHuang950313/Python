import numpy as np
import cv2
import random

img = np.zeros((512,768,3),np.uint8)
cv2.rectangle(img, (0,0), (768,512), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1)
cv2.line(img, (0,0), (768,512), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 20)
cv2.ellipse(img, (384,255), (384,384),0,0,360, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 20)
# (圓心, (一半長軸,一半短軸),長軸從0開始轉幾度,從x度開始畫,從y度停止,顏色,實心或邊框的粗度:-1是實心)

cv2.imshow("Title1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()