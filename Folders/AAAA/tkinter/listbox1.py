import tkinter as tk

class User():

    def __init__(self, window):
        self.var1 = tk.StringVar()
        self.lab = tk.Label(window, textvariable=self.var1, bg="yellow", fg="red", font=("微軟正黑體", 15), width=15) 
        self.lab.pack(pady=10)

        def Print_selection():
            try:
                self.value = self.lb.get(self.lb.curselection())
                self.var1.set(self.value)
            except BaseException:
                self.var1.set("None")

        self.b = tk.Button(window, command=Print_selection, text="Print Selection", bg="yellow", fg="red", font=("微軟正黑體", 15), width=15)
        self.b.pack(pady=10)

        self.var2 = tk.StringVar()
        self.var2.set((1,2,3,4))
        self.lb = tk.Listbox(window, listvariable=self.var2, width=15, font=("微軟正黑體", 15))
        self.lb.pack(pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("insert")
    window.geometry("400x250+0+0")
    User(window)
    window.mainloop()