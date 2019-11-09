import numpy as np # 資料型態:ndarray(矩陣)
import cv2

img = np.zeros((512,768,3),np.uint8)
# zero:全部初始化為0  e.g.print(np.zeros((3,3),np.uint8)) or print(np.ones((3,3),np.uint8))
# Part1: row(列)*col(行)*ch(層) 資料型態:tuple
# Part2: DataType資料型態:unsigned(正數)int 8(每個pixel可以存0~255的值:在二進位中255是11111111)
# 1byte = 8bit, 1個bit只能儲存0和1
# 程式人員計算機 BIN=2進位, OCT=8進位, DEC=16進位, HEX=10進位

cv2.imshow("Title", img)
# (視窗名稱,矩陣) 
cv2.waitKey(0)
# 0:任意指令 其他:毫秒 e.g.1000是1秒
cv2.destroyAllWindows()
# 關閉視窗
cv2.imwrite("A.png", img)
# (檔案名稱,矩陣) 檔案程式會儲存 重新打開會自動覆蓋

# OpenCV中三層顏色是BGR, OpenCV中列與行相反, numpy中列與行正常
cv2.rectangle(img, (0,0), (768,512), (255,255,255), -1)
# (左上角座標:列與行相反, 右下角座標:列與行相反, 顏色, 邊框的粗度:-1是沒有)

cv2.imshow("Title", img)
# (視窗名稱,矩陣) 
cv2.waitKey(0)
# 0:任意指令 其他:毫秒 e.g.1000是1秒
cv2.destroyAllWindows()
# 關閉視窗