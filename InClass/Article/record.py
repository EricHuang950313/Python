import tkinter as tk 
from functools import partial
from tkinter import messagebox

def main(): 
    window = tk.Tk()
    window.title("Record")
    window.geometry("600x400+0+0")
    menu(window)
    window.mainloop()

def menu(window):
    global name, MEL, MEE, MEB, b
    MEL = tk.Label(window, text="新增檔案", font=("微軟正黑體",20), )
    MEL.place(x=5, y=20)
    name = tk.StringVar()
    MEE = tk.Entry(window, font=("微軟正黑體",20), width=23, textvariable=name)
    MEE.place(x=125, y=20)
    MEB = tk.Button(window, text="確定", font=("微軟正黑體",20), relief="solid", command=partial(make, window))
    MEB.place(x=510, y=10)
    if l != "":
        for i in range(len(l2)):
            b = tk.Button(window, text=l2[i], font=("微軟正黑體",20), relief="flat", command=partial(show, window, i))
            b.place(x=5, y=60+(i*60))

def make(window):
    global times, l, l2, MAB
    nameExist = False
    for i in l2:
        if name.get() == i:
            nameExist = True
            break
        else:
            nameExist = False
            continue
    if name.get() == "":
        tk.messagebox.showinfo(title="InputError", message="請輸入檔案名稱!")
    elif nameExist == True:
        tk.messagebox.showinfo(title="InputError", message="輸入重複檔案名稱!")
        name.set("")
    else:
        MAB = tk.Button(window, text=name.get(), font=("微軟正黑體",20), relief="flat", command=partial(show, window, times))
        MAB.place(x=5, y=60+(times*60))
        with open("./"+name.get()+".txt", "a", encoding="utf-8"):
            pass
        l += [MAB]
        l2 += [name.get()]
        name.set("")
        times += 1

def show(window, times):
    global first, SL, ST, SE, SB, SB2, ts
    if ts >= 1:
        b.place_forget()
    MAB.place_forget()
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

times = 0
l = []
l2 = []
ts = 0

main()
