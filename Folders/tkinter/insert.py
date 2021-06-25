import tkinter as tk

window = tk.Tk()
window.title("insert")
window.geometry("400x250+0+0")

e = tk.Entry(window, show=None, font=("微軟正黑體", 15))
e.pack()

def Insert_Point():
    var = e.get()
    t.insert("insert", var)

def Insert_End():
    var = e.get()
    t.insert("end", var)

b1 = tk.Button(window,command=Insert_Point, text="Insert Point",width=10, height=1, bg="yellow", fg="blue", font=("微軟正黑體", 15))
b1.pack(pady=10)

b2 = tk.Button(window,command=Insert_End, text="Insert End",width=10, height=1, bg="yellow", fg="blue", font=("微軟正黑體", 15))
b2.pack(pady=10)

t = tk.Text(window, height=1, font=("微軟正黑體", 15))
t.pack()

window.mainloop()