import cv2
import numpy as np 
import sys


i_start, j_start = 1, 1
i_end, j_end = 8, 8

l =    [[2,2,2,2,2,2,2,2,2,2],
        [2,0,2,2,0,0,0,2,0,2],
        [2,0,0,2,0,0,2,2,0,2],
        [2,2,0,0,0,2,2,2,0,2],
        [2,2,2,2,0,2,0,0,0,2],
        [2,2,0,0,0,0,0,2,0,2],
        [2,2,0,2,2,0,2,0,0,2],
        [2,0,0,0,0,0,2,0,2,2],
        [2,2,2,2,2,0,2,0,0,2],
        [2,2,2,2,2,2,2,2,2,2]]


mazeA = np.array(l)
row,col = mazeA.shape
pixelZoomin = 70
mazeB = np.zeros((row*pixelZoomin,col*pixelZoomin),np.uint8)

for i in range(row):
    for j in range(col):
        if mazeA[i,j] == 0:
            mazeB[i*pixelZoomin:(i+1)*pixelZoomin,j*pixelZoomin:(j+1)*pixelZoomin] = 255

def print_maze():
    for i in range(mazeA.shape[0]): #列
        for j in range(mazeA.shape[1]): #行
            if mazeA[i][j] == 2:
                print("X", end="")
            else:
                print(" ", end="")
        print()
    reach(i_start, j_start)

def reach(i, j):
    mazeA[i][j] = 1
    '''print("\nprint road\n")
    print(i, j)
    for m in range(mazeA.shape[0]):
        for n in range(mazeA.shape[1]):
            if mazeA[m][n]==2:
                print("X",end='')
            elif mazeA[m][n]==1:
                print("o",end='')
            else:
                print(" ",end='')
        print()'''

    for x in range(row):
        for y in range(col):
            if mazeA[x][y] == 1:
                mazeB[x*pixelZoomin+10:(x+1)*pixelZoomin-10,y*pixelZoomin+10:(y+1)*pixelZoomin-10] = 127
            elif mazeA[x][y] == 0:
                mazeB[x*pixelZoomin:(x+1)*pixelZoomin,y*pixelZoomin:(y+1)*pixelZoomin] = 255
    
    cv2.imshow("Migong",mazeB)
    cv2.waitKey(200)

    if mazeA[i+1][j] == 0:
        reach(i+1, j)
    if mazeA[i-1][j] == 0:
        reach(i-1, j)
    if mazeA[i][j+1] == 0:
        reach(i,j+1)
    if mazeA[i][j-1] == 0:
        reach(i, j-1)
    mazeA[i][j] = 0

    if i==i_end and j==j_end:
        cv2.waitKey(1000)
        sys.exit()

print_maze()
cv2.destroyAllWindows()
