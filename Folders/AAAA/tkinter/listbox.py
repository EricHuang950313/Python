import tkinter as tk

window = tk.Tk()
window.title("insert")
window.geometry("450x250+0+0")

var1 = tk.StringVar()
lab = tk.Label(window, textvariable=var1, bg="yellow", fg="red", font=("微軟正黑體", 15), width=15) 
lab.pack(pady=10)

def Print_selection():
    try:
        value = lb.get(lb.curselection())
        var1.set(value)
    except BaseException:
        var1.set("None")

b = tk.Button(window, command=Print_selection, text="Print Selection", bg="yellow", fg="red", font=("微軟正黑體", 15), width=15)
b.pack(pady=10)

var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable=var2, width=15, font=("微軟正黑體", 15))

lb.pack(pady=10)

window.mainloop()