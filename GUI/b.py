import tkinter as tk
import tkinter.font as tkfont


def but_click():
    input_name = name.get()
    lab_result.config(text=input_name)
    
tk_win = tk.Tk()

tk_win.title('輸入姓名')
tk_win.geometry('300x150')  

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

lab = tk.Label(tk_win, text='請輸入姓名：', font= default_font)
lab.pack()  

name = tk.StringVar()

ent_name = tk.Entry(tk_win, textvariable=name,
width=15, font= default_font)
ent_name.pack()  

but = tk.Button(tk_win, text='確定', command=but_click)
but.config(font=default_font, fg='blue', bg='sky blue', padx=15)
but.pack()

lab_result = tk.Label(tk_win, font=default_font, fg='orange red')
lab_result.pack()
tk_win.mainloop()