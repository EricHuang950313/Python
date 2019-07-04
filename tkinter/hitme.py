import tkinter as tk

window = tk.Tk()
window.title("XXD")
window.geometry("200x150+0+0")

var = tk.StringVar()
l = tk.Label(window, textvariable=var, width=15, height=2, bg="blue", fg="yellow", font=("微軟正黑體", 15))
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("You hit me.")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window,command=hit_me, text="Hit Me.",width=15, height=2, bg="yellow", fg="blue", font=("微軟正黑體", 15))
b.pack(pady=10)

window.mainloop()