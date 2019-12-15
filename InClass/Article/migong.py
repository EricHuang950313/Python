import tkinter as tk 
import numpy as np 
import cv2
from functools import partial
import sys
def format():
    global VarList, NewList
    VarList = [[],[],[],[],[],[],[],[]]
    NewList =  [[2,2,2,2,2,2,2,2,2,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,0,0,0,0,0,0,0,0,2,],
                [2,2,2,2,2,2,2,2,2,2,],]


def main():
    window = tk.Tk()
    window.title("Migong")
    window.geometry("800x800+0+0")
    window.configure(bg="light yellow")
    format()
    CheckButton(window)
    window.mainloop()

def check(window):
    for times in range(0, 8):
        for item in range(0, 8):
            if VarList[times][item].get() == 1:
                NewList[times+1][item+1] += 2
    print(NewList)
    window.destroy()
    choose(window)
            
def CheckButton(window):
    for times in range(0, 8):
        for item in range(0, 8):
            Var = tk.IntVar()
            VarList[times] += [Var]
            tk.Checkbutton(window, text="", variable=VarList[times][item]).place(x=item*100+10, y=times*100+10)
                
    tk.Button(window, text="Confirm", command=partial(check, window), font=("微軟正黑體",12)).place(x=720, y=750)

def choose(window):
    window = tk.Tk()
    window.title("Try")
    window.geometry("400x400+0+0")
    window.configure(bg="light yellow")
    tk.Button(window, text="Show Image", font=("微軟正黑體",24), command=showImage).place(x=70, y=100)
    tk.Button(window, text="Run", command=Run, font=("微軟正黑體",24)).place(x=70, y=230)
    tk.Button(window, text="↖", font=("微軟正黑體",18), bg="dark blue", fg="yellow", command=partial(back, window)).place(x=340, y=340)
    window.mainloop()

def back(window):
    window.destroy()
    main()

def showImage():
    mazeA = np.array(NewList)
    row,col = mazeA.shape
    pixelZoomin = 70
    mazeB = np.zeros((row*pixelZoomin,col*pixelZoomin),np.uint8)
    for i in range(row):
        for j in range(col):
            if mazeA[i,j] == 0:
                mazeB[i*pixelZoomin:(i+1)*pixelZoomin,j*pixelZoomin:(j+1)*pixelZoomin] = 255
    cv2.imshow("Migong",mazeB)

def Run():
    i_start, j_start = 1, 1
    i_end, j_end = 8, 8
    l = NewList

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
        print("\nprint road\n")
        print(i, j)
        for m in range(mazeA.shape[0]):
            for n in range(mazeA.shape[1]):
                if mazeA[m][n]==2:
                    print("X",end='')
                elif mazeA[m][n]==1:
                    print("o",end='')
                else:
                    print(" ",end='')
            print()

        for x in range(row):
            for y in range(col):
                if mazeA[x][y] == 1:
                    mazeB[x*pixelZoomin+10:(x+1)*pixelZoomin-10,y*pixelZoomin+10:(y+1)*pixelZoomin-10] = 127
                elif mazeA[x][y] == 0:
                    mazeB[x*pixelZoomin:(x+1)*pixelZoomin,y*pixelZoomin:(y+1)*pixelZoomin] = 255
                
        cv2.imshow("Migong",mazeB)
        cv2.waitKey(200)

        if mazeA[i-1][j] == 0:
            reach(i-1, j)
        if mazeA[i][j+1] == 0:
            reach(i,j+1)
        if mazeA[i][j-1] == 0:
            reach(i, j-1)
        if mazeA[i+1][j] == 0:
            reach(i+1, j)
        mazeA[i][j] = 0

        if i==i_end and j==j_end:
            cv2.waitKey(1000)
            sys.exit()
    print_maze()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()