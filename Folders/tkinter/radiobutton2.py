import tkinter as tk

window = tk.Tk()
window.title("Radiobutton")
window.geometry("450x300+0+0")


lab = tk.Label(window, text="Empty", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
lab.pack(pady=10)

def Print_selection():
    lab.config(text="you have selected " + var.get())

var = tk.StringVar()

listrange = ["a", "b", "c", "d"]
for i in range(0, 4):
    listrange[i] = tk.Radiobutton(window, text=("Option " + listrange[i]), variable=var, value=listrange[i], command=Print_selection, font=("微軟正黑體", 15), width=15)
    listrange[i].pack(pady=10)

window.mainloop()