import numpy as np
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk
import sys
import time

currentPos = [1,1]
l = [[2,2,2,2,2,2,2,2,2,2],
     [2,1,2,2,0,0,0,2,0,2],
     [2,0,0,2,0,0,2,2,0,2],
     [2,2,0,0,0,2,2,2,0,2],
     [2,2,2,2,0,2,0,0,0,2],
     [2,2,0,0,0,0,0,2,0,2],
     [2,2,0,2,2,0,2,0,0,2],
     [2,0,0,0,0,0,2,0,2,2],
     [2,2,2,2,2,0,2,0,0,2],
     [2,2,2,2,2,2,2,2,2,2]]
mazeA = np.array(l)


def make_a_Maze():
    row, col = mazeA.shape
    pixelZoomin = 70
    mazeB = np.zeros((row*pixelZoomin,col*pixelZoomin),np.uint8)
    for i in range(row):
        for j in range(col):
            if mazeA[i,j] == 0 or mazeA[i,j] == 1:
                mazeB[i*pixelZoomin:(i+1)*pixelZoomin,j*pixelZoomin:(j+1)*pixelZoomin] = 255
            if mazeA[i, j] == 1:
                mazeB[i * pixelZoomin+10:(i + 1) * pixelZoomin-10, j * pixelZoomin+10:(j + 1) * pixelZoomin-10] = 127

    img = Image.fromarray(mazeB.astype(np.uint8))
    imgtk = ImageTk.PhotoImage(img)
    l = tk.Label(window, image=imgtk)
    l.place(x=20, y=20)
    window.update()
    if endIfWin(currentPos) == True:
        time.sleep(1)
        sys.exit()

    b1 = tk.Button(window, text="↑", font=("微軟正黑體",28), command=partial(main,1))
    b1.place(x=880,y=450)
    b2 = tk.Button(window, text="←", font=("微軟正黑體", 28), command=partial(main,3))
    b2.place(x=780, y=550)
    b3 = tk.Button(window, text="↓", font=("微軟正黑體", 28), command=partial(main,2))
    b3.place(x=880, y=550)
    b4 = tk.Button(window, text="→", font=("微軟正黑體", 28), command=partial(main,4))
    b4.place(x=980, y=550)
    window.mainloop()


def update_map(currentPos_old, currentPos):
    mazeA[currentPos_old[0]][currentPos_old[1]] = 0
    mazeA[currentPos[0]][currentPos[1]] = 1

def findPos():
    for i in range(0, len(mazeA)):
        for j in range(0, len(mazeA)):
            if mazeA[i][j] == 1:
                return (i, j)
            else:
                pass

def check_path(direction, currentPos):
    currentPos_old = currentPos.copy()
    currentPos_new = currentPos.copy()
    if direction == 1:
        currentPos_new[0] -= 1
    if direction == 2:
        currentPos_new[0] += 1
    if direction == 3:
        currentPos_new[1] -= 1
    if direction == 4:
        currentPos_new[1] += 1

    if mazeA[currentPos_new[0]][currentPos_new[1]] == 2:
        flag = 0
    else:
        flag = 1
    return flag, currentPos_old, currentPos_new

def endIfWin(pos):
    return True if pos[0] == 8 and pos[1] == 8 else None

def main(button_status):
    global currentPos
    currentPos_0 = findPos()
    currentPos = [currentPos_0[0], currentPos_0[1]]
    flag, currentPos_old, currentPos_new = check_path(button_status,currentPos)
    if flag == 0:
        currentPos = currentPos_old
    else:
        currentPos = currentPos_new
        update_map(currentPos_old, currentPos)
        make_a_Maze()

window = tk.Tk()
window.title("Migong")
window.geometry("1100x750+0+0")
window.configure(bg="black")
make_a_Maze()
window.mainloop()


