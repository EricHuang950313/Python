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
import time


def main():
    # Set Everything
    window = tk.Tk()
    window.title("Atomic-Platform")
    window.geometry("600x400+0+0")
    window.configure(bg="black")
    window.iconbitmap("icon.ico")
    Welcome(window)
    window.mainloop()

def Welcome(window):
    global  WL1, WL2, WL3, WL4, WL5, WL6, WL7, WB1, TL1
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
    WL8 = tk.Label(window, text="做點筆記也不錯", font=("微軟正黑體",18), fg="white", bg="black")
    WL8.place(x=415,y=215)
    update()

def Make(window):
    global ML1, ML2, ML3, ME1, ME2, MB1, MB2
    WL1.destroy()
    WL2.destroy()
    WL3.destroy()
    WL4.destroy()
    WL5.destroy()
    WL6.destroy()
    WL7.destroy()
    WB1.destroy()
    TL1.destroy()
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
    global times, l, l2, ts, tss
    times = 0
    l = []
    l2 = []
    ts = 0
    tss = 0
    def main(): 
        window2 = tk.Tk()
        window2.title("Record")
        window2.geometry("600x400+0+0")
        menu(window2)
        window2.mainloop()

    def menu(window):
        global name, MEL, MEE, MEB, tss, l2, l, times, iiii
        MEL = tk.Label(window, text="新增檔案", font=("微軟正黑體",20), )
        MEL.place(x=5, y=20)
        name = tk.StringVar()
        MEE = tk.Entry(window, font=("微軟正黑體",20), width=23, textvariable=name)
        MEE.place(x=125, y=20)
        MEB = tk.Button(window, text="確定", font=("微軟正黑體",20), relief="solid", command=partial(make, window))
        MEB.place(x=510, y=10)
        if tss == 0 or l == "":
            with open("./OpenFile.txt", "r", encoding="utf-8") as file:
                a = list([file.read()])
                if a == ["['']"] :
                    a.clear()
                    iiii = -1
                else:
                    l2 = a[0][2:-2].split("\', \'")
                    for i in range(len(l2)):
                        MAB = tk.Button(window, text=l2[i], font=("微軟正黑體",20), relief="flat", command=partial(show, window, times))
                        MAB.place(x=5, y=60+(i*60))
                        l += [MAB]
                        times += 1
                    #times -= 1
                    iiii = times-1
        else:
            for i in range(len(l)):
                l[i].place(x=5, y=60+(i*60))
            iiii = i
        tss += 1

    def make(window):
        global times, l, l2, MAB, tss, ts, iiii
        nameExist = False
        checkNext2 = True
        do = True
        for i in l2:
            if name.get() == i:
                nameExist = True
                break
            else:
                nameExist = False
                continue
        try:
            if name.get()[0]+name.get()[1]+name.get()[2]+name.get()[3] == "del,":
                try:
                    g = int(name.get()[4:])
                except BaseException:
                    tk.messagebox.showinfo(title="InputError", message="請輸入數字!")
                    checkNext2 = False          
                finally:
                    if checkNext2 == True:
                        if name.get() == "del,":
                            tk.messagebox.showinfo(title="InputError", message="請輸入要刪除的列!")
                            do = False
                        elif int(name.get()[4:]) > len(l2):
                            tk.messagebox.showinfo(title="InputError", message="輸入了無效的數字!")
                            do = False
                        elif int(name.get()[4:]) < 0:
                            tk.messagebox.showinfo(title="InputError", message="輸入了無效的數字!")
                            do = False
                        else:
                            l2.pop(int(name.get()[4:]) - 1)
                            l[int(name.get()[4:]) - 1].destroy()
                            l.pop(int(name.get()[4:]) - 1)
                            name.set("")
                            window.update()
                            for i in range(len(l)):
                                l[i].place(x=5, y=60+(i*60))
                            with open("./OpenFile.txt", "w", encoding="utf-8") as file:
                                file.truncate()
                            with open("./OpenFile.txt", "a", encoding="utf-8") as file:
                                file.write(str(l2))
                            do = False
                            tss = 0
                            ts = 0
                            times = 0
                            l = []
                            l2 = []
                            tk.messagebox.showinfo(title="資料整理", message="系統資料整理,將重新啟動!")
                            window.destroy()
                            main()

        except BaseException:
            pass
        finally:
            if do == True:
                if name.get() == "":
                    tk.messagebox.showinfo(title="InputError", message="請輸入檔案名稱!")
                elif nameExist == True:
                    tk.messagebox.showinfo(title="InputError", message="輸入重複檔案名稱!")
                    name.set("")
                else:
                    MAB = tk.Button(window, text=name.get(), font=("微軟正黑體",20), relief="flat", command=partial(show, window, times))
                    MAB.place(x=5, y=60+((iiii+1)*60))
                    iiii += 1
                    with open("./"+name.get()+".txt", "a", encoding="utf-8"):
                        pass
                    with open("./OpenFile.txt", "w", encoding="utf-8") as file:
                        file.truncate()
                    l += [MAB]
                    l2 += [name.get()]
                    with open("./OpenFile.txt", "a", encoding="utf-8") as file:
                        file.write(str(l2))
                    name.set("")
                    times += 1
                    
    def show(window, times):
        global SL, ST, SE, SB, SB2, ts
        for i in range(len(l)):
            l[i].place_forget()
        MEL.place_forget()
        MEE.place_forget()
        MEB.place_forget()
        things = tk.StringVar()
        SL = tk.Label(window, text="輸入列：", font=("微軟正黑體",10))
        SL.place(x=5, y=10)
        ST = tk.Text(window, font=("微軟正黑體",10), height=15, width=73)
        ST.place(x=5, y=85)
        SE = tk.Entry(window, font=("微軟正黑體",20), width=30, textvariable=things)
        SE.place(x=5, y=30)
        SB = tk.Button(window, text="確定", font=("微軟正黑體",20), relief="solid", command=partial(save, things, times, ST))
        SB.place(x=505, y=10)
        SB2 = tk.Button(window, text="返回", font=("微軟正黑體",14), relief="solid", command=partial(back, window))
        SB2.place(x=540, y=355)
        with open("./"+str(l2[times])+".txt", "r", encoding="utf-8") as file:
            ST.delete(1.0,tk.END)
            for i in file:
                ST.insert("end", i)

    def save(things, times, ST):
        with open("./"+str(l2[times])+".txt", "r", encoding="utf-8") as file:
            l3 = []
            for i in file:
                l3 += [i]
        writeIn = True
        checkNext = True
        popl3 = False
        if things.get() == "":
            tk.messagebox.showinfo(title="InputError", message="警告:輸入空白!")
        try:
            if things.get()[0]+things.get()[1]+things.get()[2]+things.get()[3] == "del,":
                try:
                    a = int(things.get()[4:])
                except BaseException:
                    tk.messagebox.showinfo(title="InputError", message="請輸入數字!")
                    checkNext = False  
                    writeIn = False          
                finally:
                    if checkNext == True:
                        if things.get() == "del,":
                            tk.messagebox.showinfo(title="InputError", message="請輸入要刪除的列!")
                            writeIn = False
                        elif int(things.get()[4:]) > len(l3):
                            tk.messagebox.showinfo(title="InputError", message="輸入了無效的數字!")
                            writeIn = False
                        elif int(things.get()[4:]) < 0:
                            tk.messagebox.showinfo(title="InputError", message="輸入了無效的數字!")
                            writeIn = False
                        else:
                            l3.pop(int(things.get()[4:]) - 1)
                            popl3 = True

        except BaseException:
            pass
        finally:
            if writeIn == True:
                with open("./"+str(l2[times])+".txt", "w", encoding="utf-8") as file:
                    l3 += [things.get()+"\n"]
                    if popl3 == True:
                        l3.pop(len(l3)-1)
                    file.truncate()
                    file.writelines(l3)
                with open("./"+str(l2[times])+".txt", "r", encoding="utf-8") as file:
                    ST.delete(1.0,tk.END)
                    for i in file:
                        ST.insert("end", i)
            things.set("")

    def back(window):
        global ts
        ts += 1
        SL.place_forget()
        ST.place_forget()
        SE.place_forget()
        SB.place_forget()
        SB2.place_forget()
        menu(window)

    main()


if __name__ == "__main__":
    main()