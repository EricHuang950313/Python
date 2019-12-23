# This Program ism't complete
import tkinter as tk
from functools import partial
import random
from win32com.client import Dispatch, constants
import os
import sys
import math
import win32com

def main():
    
    window = tk.Tk()
    window.geometry("100x80+0+0")
    window.configure(bg="light yellow")
    Button(window)
    window.mainloop()


def Button(window):
    B1 = tk.Button(window,text="Confirm", font=("微軟正黑體", 16), command=partial(WriteIn, window))
    B1.place(x=10, y=10)

def WriteIn(window):

    user = 100

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = 1
    word.DisplayAlerts = 0
    doc = word.Documents.Add()

    rangee = doc.Range(0,0)
    rangee.Style.Font.Name = "微軟正黑體"
    rangee.Style.Font.Size = 18
    rangee.Style.Font.Outline = 0
    column = 3
    table = doc.Tables.Add(rangee, column, 3)
    count = 1

    for i in range(1, 10):
        table.Cell(i).Range.Text = ("{}÷{}=   ...    ".format(n1,n2))
    doc.Close()
    word.Quit()
    sys.exit()           
            


if __name__ == "__main__":
    main()
