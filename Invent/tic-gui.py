import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title("Tic-tac-toe")
window.geometry("400x300")
window.configure(background="light yellow")

def whoGoFirst():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

def setXO():
    global playerLetter, computerLetter
    if(OX.get().upper() == "O" or OX.get().upper() == "X"):
        if OX.get().upper() == "X":
            playerLetter = "X"
            computerLetter = "O"
        else:
            playerLetter = "O"
            computerLetter = "X"
        first = whoGoFirst()

        LabelP = tk.Label(window, text="You : "+ playerLetter, fg="Blue", bg="light yellow", font=("微軟正黑體", 36))
        LabelP.pack()
        LabelC = tk.Label(window, text="Computer : "+ computerLetter,fg="Red", bg="light yellow", font=("微軟正黑體", 15))
        LabelC.pack()
        LabelF = tk.Label(window, text="Go first : "+ first, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.pack()
        window.update()
        window.after(3000)
        label.destroy()
        entry.destroy()
        button.destroy()
        LabelP.destroy()
        LabelC.destroy()
        LabelF.destroy()
        B()
    else:
        messagebox.showinfo("Error", "Please input \"O\" or \"X\".")


def inputPlayerXO():
    global OX, label, entry, button
    OX = tk.StringVar()
    label = tk.Label(window, text="Which do you want to be, \"O\" or \"X\"?", bg="light yellow", font=("微軟正黑體", 15))
    label.pack(pady=10)
    entry = tk.Entry(textvariable=OX, font=("微軟正黑體", 15))
    entry.pack(pady=10)
    button = tk.Button(window, text="= Confirm =", command=setXO, font=("微軟正黑體", 15))
    button.pack(pady=10)
    window.mainloop()


def B():
    theBoard = ["   ", " O ", " X ", " O ", "   ", "   ", "   ", " O ", " X ", "   "]

    def num(i, j):
        if (i == 1):
            if (j == 1):
                return 1
            elif (j == 2):
                return 2
            elif (j == 3):
                return 3
        if (i == 2):
            if (j == 1):
                return 4
            elif (j == 2):
                return 5
            elif (j == 3):
                return 6
        if (i == 3):
            if (j == 1):
                return 7
            elif (j == 2):
                return 8
            elif (j == 3):
                return 9

    for i in range(1, 4):
        for j in range(1, 4):
            f = tk.Frame(window)
            f.grid(row=i, column=j, padx=20, pady=20)
            tk.Label(f, text=theBoard[num(i, j)], font=("Arail", 20), fg="dark blue").pack()
    f2 = tk.Frame(window)
    f2.grid()
    tk.Label(f2, text="Turn : ", font=("微軟正黑體", 20), bg="light yellow", fg="dark blue").pack()

inputPlayerXO()