import tkinter as tk

window = tk.Tk()
window.title("Radiobutton")
window.geometry("450x300+0+0")


lab = tk.Label(window, text="Empty", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
lab.pack(pady=10)

def Print_selection():
    lab.config(text="you have selected " + var.get())

var = tk.StringVar()

a = tk.Radiobutton(window, text="Option A", variable=var, value="A", command=Print_selection, font=("微軟正黑體", 15), width=15)
a.pack(pady=10)

b = tk.Radiobutton(window, text="Option B", variable=var, value="B", command=Print_selection, font=("微軟正黑體", 15), width=15)
b.pack(pady=10)

c = tk.Radiobutton(window, text="Option C", variable=var, value="C", command=Print_selection, font=("微軟正黑體", 15), width=15)
c.pack(pady=10)

d = tk.Radiobutton(window, text="Option D", variable=var, value="D", command=Print_selection, font=("微軟正黑體", 15), width=15)
d.pack(pady=10)

window.mainloop()