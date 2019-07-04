print("Wait for a moment")
import tkinter as tk
from tkinter import messagebox

def checkPW():
    if(pw.get() == "Technology" and ac.get() == "FaceUgly"):
        lable1.destroy()
        lable2.destroy()
        entry1.destroy()
        entry2.destroy()
        button.destroy() 
        messagebox.showinfo("Welcome", "Hahaha!!!\n恭喜你知道很......的帳密\n歡迎登入~~~") 
        B()  
    else:
        messagebox.showinfo("Bad News", "哈哈哈！我笑你。\n帳號密碼有錯喔！！！")


def A():
    global ac, pw, msg, lable1, entry1, lable2, entry2, button
    ac = tk.StringVar()
    pw = tk.StringVar()
    msg = tk.StringVar()
    lable1 = tk.Label(win, text="請輸入帳號：", font=("微軟正黑體", 20))
    lable1.pack()
    entry1 = tk.Entry(textvariable=pw, font=("微軟正黑體", 20))
    entry1.pack()
    lable2 = tk.Label(win, text="請輸入密碼：", font=("微軟正黑體", 20))
    lable2.pack()
    entry2 = tk.Entry(show = "*", textvariable=ac, font=("微軟正黑體", 20))
    entry2.pack()
    button = tk.Button(win, text="登入", command=checkPW, font=("微軟正黑體", 20))
    button.pack()
    win.mainloop()


def B():
    a = tk.Label(win, text="請選擇您對 \"許XX\" 的憎恨程度( 1~5 )：", font=("微軟正黑體", 20))
    a.pack()

    def level():
        if area.get() == 0:
            a1 = tk.Tk()
            a1.title("你選了\"1\"")
            a1.geometry("480x240")
            lable11 = tk.Label(a1, text="事蹟 ------\n許素華 潑硫酸\n許虹儀 炸實驗室\n許XX 分不清\"100和350\" 哪個比較大…", font=("微軟正黑體", 20))
            lable11.pack()
            a1.mainloop()

        elif area.get() == 1:
            a2 = tk.Tk()
            a2.title("你選了\"2\"")
            a2.geometry("480x240")
            lable22 = tk.Label(a2, text="魚兒天空 Blue Blue Blue\n素華頭腦 呆 呆 呆 ！！！", font=("微軟正黑體", 20))
            lable22.pack()
            a2.mainloop()

        elif area.get() == 2:
            a3 = tk.Tk()
            a3.title("你選了\"3\"")
            a3.geometry("480x240")
            lable3 = tk.Label(a3, text="國際亂象   光武亂象\n東有特朗普  生科有許虹儀\n西有習維尼    童家有計時器\n南有杜特蒂    歷史有管笑話\n北有金正恩    英文有接力棒", font=("微軟正黑體", 20))
            lable3.pack()
            a3.mainloop()

        elif area.get() == 3:
            a4 = tk.Tk()
            a4.title("你選了\"4\"")
            a4.geometry("480x240")
            lable4 = tk.Label(a4, text="新竹市某國中生活與科技、資訊、\n圖書館老師，因上課分不清 100與300，\n仍不斷辯解，因此遭到學生恥笑。\n以下採訪到兩位學生：\n請問您對許XX的看法？\n學生：叫她不要再雜嘴了......\n記者 許素華 / 新竹市報導", font=("微軟正黑體", 20))
            lable4.pack()
            a4.mainloop()    
        
        else:
            a5 = tk.Tk()
            a5.title("你選了\"5\"")
            a5.geometry("480x240")
            lable5 = tk.Label(a5, text="素華噴硫酸，\n虹儀炸房子。\n學人真幼稚，\n好似老巫婆。", font=("微軟正黑體", 20))
            lable5.pack()
            a5.mainloop()


    def radbut_click():
        global selected_item
        selected_item = area.get()
        lab_result.config(text=AREA_OPTIONS[selected_item][0])

    AREA_OPTIONS = (("1", 0),
                    ("2", 1),
                    ("3", 2),
                    ("4", 3),
                    ("5", 4))

    area = tk.IntVar()
    area.set(0)
    

    for item, value in AREA_OPTIONS:
        radbut = tk.Radiobutton(win, text=item,
                        variable=area, value=value,
                        command=radbut_click, font="微軟正黑體")
        radbut.pack(fill = "y",expand = 1,side = "left")

    lab_result = tk.Label(win, font="微軟正黑體")
    lab_result.pack(padx=10, pady=(5, 10))

    b = tk.Button(win, text="確定", font=("微軟正黑體", 20), command=level)
    b.pack(anchor="se")

    win.mainloop()

win = tk.Tk()
win.title("Hack The World")
win.geometry("480x240")

A()

