# Mental-Arithmetic-Exercise-Maker created by EricHuang

import tkinter as tk
from functools import partial
from tkinter import messagebox
import random
import math

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
    global  WL1, WB1, WB2
    WL1 = tk.Label(window, text="Welcome To \n\"Mental-Arithmetic-Exercise-Maker\".", font=("微軟正黑體",24, "bold"), bg="light yellow")
    WL1.place(x=10,y=25)
    WB1 = tk.Button(window, text="I Want to\nMake one.", font=("微軟正黑體",24), fg="blue", command=partial(Make, window))
    WB1.place(x=70,y=170)
    WB2 = tk.Button(window, text="I Want to\nCheck Ans.", font=("微軟正黑體",24), fg="red", command=partial(Check, window))
    WB2.place(x=330,y=170)

def Make(window):
    global ML1, ML2, ML3, ME1, ME2, MB1, MB2
    WL1.destroy()
    WB1.destroy()
    WB2.destroy()
    amount = tk.StringVar()
    name = tk.StringVar()
    ML1 = tk.Label(window, text="Maker", font=("微軟正黑體",28, "bold"), bg="light yellow")
    ML1.place(x=240,y=15)
    ML2 = tk.Label(window, text="How much do you want to make?", font=("微軟正黑體",24), bg="light yellow")
    ML2.place(x=45,y=75)
    ME1 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=amount)
    ME1.place(x=10,y=130)
    ML3 = tk.Label(window, text="What's your file's name(To write)?", font=("微軟正黑體",24), bg="light yellow")
    ML3.place(x=45,y=190)
    ME2 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=name)
    ME2.place(x=10,y=250)
    MB1 = tk.Button(window, text="Confirm", font=("微軟正黑體",24, "bold"), bg="red", fg="yellow", command=partial(writeIn, window, amount, name))
    MB1.place(x=230, y=310)
    MB2 = tk.Button(window, text="↖", font=("微軟正黑體",20), bg="dark blue", fg="yellow", command=partial(back, window))
    MB2.place(x=545, y=335)

def back(window):
    window.destroy()
    main()

def writeIn(window, amount, name):
    if ME2.get()=="":
        tk.messagebox.showinfo(title="Maker", message="You didn't input the file name!")
    else:
        FILE = "./" + ME2.get() + ".txt"
    try:
        ques = int(ME1.get())

        yesNo = False
        with open(FILE, mode="w", encoding="utf-8")as file:    
            for i in range(ques):
                while yesNo == False:
                    n1 = str(random.randint(10, 90))
                    n2 = str(random.randint(2, 9))
                    if ((int(n2)*10) > int(n1) > int(n2)):
                        break
                    else:
                        continue
                file.write("{}÷{}=   ...    ".format(n1,n2)+"\n")
        tk.messagebox.showinfo(title="Maker", message="Write it Successfully.")
        window.destroy()
        main()
    except BaseException:
        tk.messagebox.showinfo(title="Maker", message="You didn't input the amount!")

    

def Check(window):
    global CL1, CL2, CL3, CE1, CB1, CB2
    WL1.destroy()
    WB1.destroy()
    WB2.destroy()
    writeFileName = tk.StringVar()
    CL1 = tk.Label(window, text="Maker", font=("微軟正黑體",28, "bold"), bg="light yellow")
    CL1.place(x=240,y=15)
    CL2 = tk.Label(window, text="What file do you want to check?", font=("微軟正黑體",24), bg="light yellow")
    CL2.place(x=55,y=75)
    CE1 = tk.Entry(window, font=("微軟正黑體",20), width=36,textvariable=writeFileName)
    CE1.place(x=10,y=130)
    CB1 = tk.Button(window, text="Confirm", font=("微軟正黑體",24, "bold"), bg="red", fg="yellow", command=partial(checkAndSave, window, writeFileName))
    CB1.place(x=230, y=190)
    CB2 = tk.Button(window, text="↖", font=("微軟正黑體",20), bg="dark blue", fg="yellow", command=partial(back, window))
    CB2.place(x=545, y=335)

def checkAndSave(window, writeFileName):
    if writeFileName.get()=="":
        tk.messagebox.showinfo(title="Maker", message="You didn't input the file name!")
        return True
    else:
        F1 = "./" + writeFileName.get() + ".txt"
        F2 = "./" + writeFileName.get() + "ANS.txt"
    try:
        with open(F1, mode="r", encoding="utf-8") as file:
            l = []
            data = file.read()
            file.seek(0)
            for line in file:
                a = int(line[0]+line[1])
                b = int(line[3])

                for i in range(b+1):
                    if ((a-i) % b) == 0:
                        l += [str(math.floor((a-i)/b))+" , "+str(abs(-i))]
                        break
                    else:
                        continue

        with open(F2, mode="w", encoding="utf-8") as file:
            for i in l:
                file.write(i+"\n")
        tk.messagebox.showinfo(title="Checker", message="Check it Successfully.\nThe answer's file name is "+F2)
        window.destroy()
        main()
    except BaseException:
        tk.messagebox.showinfo(title="Maker", message="You inputed the wrong file name!")
if __name__ == "__main__":
    main()
