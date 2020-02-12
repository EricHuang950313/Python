# Mental-Arithmetic-Exercise-Maker created by EricHuang
import tkinter as tk
from functools import partial
from tkinter import messagebox
import random
import math
import win32com
from win32com.client import Dispatch, constants
import os
import sys


def main():
    # Set Everything
    window = tk.Tk()
    window.title("Mental-Arithmetic-Exercise-Maker")
    window.geometry("600x400+0+0")
    window.configure(bg="light yellow")
    window.iconbitmap("icon.ico")

    Welcome(window)
    window.mainloop()

def Welcome(window):
    global  WL1, WB1
    WL1 = tk.Label(window, text="歡迎來到 \n\"心算單產生器\".", font=("微軟正黑體",40, "bold"), bg="light yellow")
    WL1.place(x=105,y=25)
    WB1 = tk.Button(window, text="製作", font=("微軟正黑體",48), fg="blue", command=partial(Make, window))
    WB1.place(x=200,y=190)
    

def Make(window):
    global ML1, ML2, ML3, ME1, ME2, MB1, MB2
    WL1.destroy()
    WB1.destroy()
    amount = tk.StringVar()
    name = tk.StringVar()
    ML1 = tk.Label(window, text="產生器", font=("微軟正黑體",28, "bold"), bg="light yellow")
    ML1.place(x=240,y=15)
    ML2 = tk.Label(window, text="我想做幾題 ?", font=("微軟正黑體",24), bg="light yellow")
    ML2.place(x=45,y=75)
    ME1 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=amount)
    ME1.place(x=10,y=130)
    ML3 = tk.Label(window, text="我的檔案名稱 ?", font=("微軟正黑體",24), bg="light yellow")
    ML3.place(x=45,y=190)
    ME2 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=name)
    ME2.place(x=10,y=250)
    MB1 = tk.Button(window, text="確定", font=("微軟正黑體",24, "bold"), bg="red", fg="yellow", command=partial(writeIn, window, amount, name))
    MB1.place(x=250, y=310)
    MB2 = tk.Button(window, text="↖", font=("微軟正黑體",20), bg="dark blue", fg="yellow", command=partial(back, window))
    MB2.place(x=545, y=335)

def back(window):
    window.destroy()
    main()

def writeIn(window, amount, name):
    if len(name.get()) == 0 and len(amount.get()) == 0:
        tk.messagebox.showinfo(title="Maker", message="請輸入檔案名稱、數目 !")
    elif len(amount.get()) == 0 or int(amount.get()) % 50 != 0:
        tk.messagebox.showinfo(title="Maker", message="數目除以50一定要等於0 !")
    elif len(name.get()) == 0:
        tk.messagebox.showinfo(title="Maker", message="請輸入檔案名稱 !")
    else:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = 1
        word.DisplayAlerts = 0
        doc = word.Documents.Add()

        rangee = doc.Range(0,0)
        rangee.Style.Font.Name = "微軟正黑體"
        rangee.Style.Font.Size = 18
        rangee.Style.Font.Outline = 0
        
        user_input = int(amount.get())
        column = math.floor(math.floor(user_input/3) + (math.floor((user_input/50+1)/3)+1))

        table = doc.Tables.Add(rangee, column, 3)
        l = []
        count = 0
        yesNo = False

        
        for i in range(user_input):
            while yesNo == False:
                n1 = str(random.randint(10, 90))
                n2 = str(random.randint(2, 9))
                if ((int(n2)*10) > int(n1) > int(n2)):
                    yesNo = True
                    break
                else:
                    continue
            yesNo = False
            mathWord = ("{}÷{}=   ...    ".format(n1,n2))
            l += [mathWord]        

        for i in range(1, math.floor(user_input/50)+1):
            l.insert(50*i+i-1, "  /  W:")

        with open ("./make_docx.txt", "w", encoding="utf-8") as file:
            for i in l:
                file.write(i+"\n")

        with open ("./make_docx.txt", "r", encoding="utf-8") as file:
            l2 = []
            file.seek(0)
            for line in file:
                if line[0] == " ":
                    l2 +=[" "]
                    continue
                else:
                    a = int(line[0]+line[1])
                    b = int(line[3])

                    for i in range(b+1):
                        if ((a-i) % b) == 0:
                            l2 += [str(math.floor((a-i)/b))+" , "+str(abs(-i))]
                            break
                        else:
                            continue

        with open ("./ans.txt", "w", encoding="utf-8") as file:
            for i in l2:
                file.write(i+"\n")


        for i in range(1, column+1):
            for j in range(1, 4):
                table.Cell(i, j).Range.Text = l[count]
                count += 1 
                if count == len(l):
                    doc.SaveAs(os.path.dirname(os.path.abspath("1.py"))+"\\"+name.get()+"ans.docx")
                    doc.Close()
                    break
            if count == len(l):
                break

        doc2 = word.Documents.Add()
        rangee2 = doc2.Range(0,0)
        rangee2.Style.Font.Name = "微軟正黑體"
        rangee2.Style.Font.Size = 18
        rangee2.Style.Font.Outline = 0
        table2 = doc2.Tables.Add(rangee2, column, 3)
        count = 0
        for i in range(1, column+1):
            for j in range(1, 4):
                table2.Cell(i, j).Range.Text = l2[count]
                count += 1 
                if count == len(l2):
                    doc2.SaveAs(os.path.dirname(os.path.abspath("1.py"))+"\\"+name.get()+".docx")
                    doc2.Close()
                    word.Quit()
                    window.destroy()
                    main()

if __name__ == "__main__":
    main()