import numpy as np
import cv2
import random

img = np.zeros((512,768,3),np.uint8)

cv2.rectangle(img, (0,0), (768,512), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), -1)

cv2.imshow("Title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()