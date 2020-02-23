# AtomicPlatform created by EricHuang (file:OpenFile.txt&Product information.txt)
import tkinter as tk
from functools import partial
from tkinter import messagebox
import random
import math
import win32com
from win32com.client import Dispatch, constants
import os
import sys
import time


def main():
    # Set Everything
    window = tk.Tk()
    window.title("Atomic-Platform")
    window.geometry("600x400+0+0")
    window.configure(bg="black")
    Welcome(window)
    window.mainloop()

def Welcome(window):
    window.configure(bg="black")
    global  WL1, WL2, WL3, WL4, WL5, WL6, WL7, WB1, TL1, WB2, WB3, WL8, WL9
    def update():
        now = time.strftime("%H:%M:%S")
        TL1.configure(text=now)
        window.after(1000, update)
    WL1 = tk.Label(window, text="Atomic", font=("微軟正黑體",50, "bold"), fg="yellow", relief="solid", bg="black")
    WL1.place(x=10,y=20)
    WL2 = tk.Label(window, text="-", font=("微軟正黑體",50, "bold"), fg="yellow", relief="solid", bg="black")
    WL2.place(x=240,y=20)
    WL3 = tk.Label(window, text="-", font=("微軟正黑體",50, "bold"), fg="light green", relief="solid", bg="black")
    WL3.place(x=270,y=20)
    WL4 = tk.Label(window, text="Platform", font=("微軟正黑體",50, "bold"), fg="light green", relief="solid", bg="black")
    WL4.place(x=305,y=20)
    WL5 = tk.Label(window, text="1.01 to the power of 365 ≒ 37.78    &    0.99 to the power of 365 ≒ 0.03", font=("Ariel",14), fg="white", relief="solid", bg="black")
    WL5.place(x=30,y=110)
    WL6 = tk.Label(window, text="||\n||\n||\n||\n||\n||\n||", font=("微軟正黑體",20), fg="white", bg="black")
    WL6.place(x=270,y=140)
    WL7 = tk.Label(window, text="產生數學心算練習單", font=("微軟正黑體",18), fg="white", bg="black")
    WL7.place(x=25,y=320)
    WB1 = tk.Button(window, text="製作", font=("微軟正黑體",48), fg="blue", relief="solid", command=partial(Make, window))
    WB1.place(x=45,y=165)
    TL1 = tk.Label(window, font=("微軟正黑體",36, "bold"), fg="white",bg="black")
    TL1.place(x=330,y=140)
    WB2 = tk.Button(window, text="筆記", font=("微軟正黑體",24), relief="solid",command=note)
    WB2.place(x=315,y=215)
    WL8 = tk.Label(window, text="寫寫東西~~~\n~~~記錄生活", font=("微軟正黑體",18), fg="white", bg="black")
    WL8.place(x=415,y=215)
    WB3 = tk.Button(window, text="資訊", font=("微軟正黑體",24), relief="solid",command=partial(info, window))
    WB3.place(x=315,y=300)
    WL9 = tk.Label(window, text="多多支持~~~\n~~~相關產品", font=("微軟正黑體",18), fg="white", bg="black")
    WL9.place(x=415,y=300)
    update()

def info(window):
    global IL, IB
    window.configure(bg="white")
    WL1.place_forget()
    WL2.place_forget()
    WL3.place_forget()
    WL4.place_forget()
    WL5.place_forget()
    WL6.place_forget()
    WL7.place_forget()
    WB1.place_forget()
    TL1.place_forget()
    WB2.place_forget()
    WB3.place_forget()
    WL8.place_forget()
    WL9.place_forget()
    ILS = tk.StringVar()
    IL = tk.Label(window, textvariable=ILS)
    IL.place(x=75, y=50)
    IB = tk.Button(window, text="↖", font=("微軟正黑體",20), bg="dark blue", fg="yellow", command=partial(infoB, window))
    IB.place(x=545, y=335)
    with open("./Product Infomation.txt", "r", encoding="utf-8") as file:
        ILS.set(file.read())

def infoB(window):
    IL.place_forget()
    IB.place_forget()
    Welcome(window)

def Make(window):
    global ML1, ML2, ML3, ME1, ME2, MB1, MB2
    WL1.place_forget()
    WL2.place_forget()
    WL3.place_forget()
    WL4.place_forget()
    WL5.place_forget()
    WL6.place_forget()
    WL7.place_forget()
    WB1.place_forget()
    TL1.place_forget()
    WB2.place_forget()
    WB3.place_forget()
    WL8.place_forget()
    WL9.place_forget()
    window.configure(bg="light yellow")
    amount = tk.StringVar()
    name = tk.StringVar()
    ML1 = tk.Label(window, text="產生器 MAKER", font=("微軟正黑體",36, "bold"), bg="light yellow")
    ML1.place(x=125,y=20)
    ML2 = tk.Label(window, text="- 我想做幾題 ?", font=("微軟正黑體",24), bg="light yellow")
    ML2.place(x=20,y=95)
    ME1 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=amount)
    ME1.place(x=10,y=145)
    ML3 = tk.Label(window, text="- 我的檔案名稱 ?", font=("微軟正黑體",24), bg="light yellow")
    ML3.place(x=20,y=205)
    ME2 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=name)
    ME2.place(x=10,y=250)
    MB1 = tk.Button(window, text="確定", font=("微軟正黑體",24, "bold"), bg="red", fg="yellow", command=partial(writeIn, window, amount, name))
    MB1.place(x=250, y=305)
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
                    doc.SaveAs(os.path.dirname(os.path.abspath("make_docx.py"))+"\\"+name.get()+".docx")
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
                    doc2.SaveAs(os.path.dirname(os.path.abspath("make_docx.py"))+"\\"+name.get()+"ans.docx")
                    doc2.Close()
                    word.Quit()
                    window.destroy()
                    main()

def note():
    os.system("Python note.py")


if __name__ == "__main__":
    main()
