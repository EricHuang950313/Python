import tkinter as tk

def but_click():
    input_name = name.get()
    lab_result.config(text=input_name)

tk_win = tk.Tk()
tk_win.title("GUI programs")
tk_win.geometry("300x150")

lab = tk.Label(tk_win, text="Account:", font=("微軟正黑體", 20))
lab.pack()

name = tk.StringVar()

ent_name = tk.Entry(tk_win, textvariable=name, font=("微軟正黑體", 20))
ent_name.pack()

but = tk.Button(tk_win, text="確定", command=but_click,)
but.config(font=("微軟正黑體", 20), fg="yellow", bg="red", padx=20,)
but.pack()


lab_result = tk.Label(tk_win)
lab_result.pack()

tk_win.mainloop()