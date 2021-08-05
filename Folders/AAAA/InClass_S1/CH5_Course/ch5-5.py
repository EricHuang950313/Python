import numpy as np
import cv2
import random

img = np.zeros((200,200,1),np.uint8)

img[0:80,:,0] = 127
img[80:150,:,0] = 255
img[150:200,:,0] = 0

cv2.imshow("Title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()