import tkinter as tk

class User():
    def __init__(self, window):
        self.e = tk.Entry(window, show=None, font=("微軟正黑體", 15))
        self.e.pack()

        def Insert_Point():
            self.var = self.e.get()
            self.t.insert("insert", self.var)

        def Insert_End():
            self.var = self.e.get()
            self.t.insert("end", self.var)

        self.b1 = tk.Button(window,command=Insert_Point, text="Insert Point",width=10, height=1, bg="yellow", fg="blue", font=("微軟正黑體", 15))
        self.b1.pack(pady=10)

        self.b2 = tk.Button(window,command=Insert_End, text="Insert End",width=10, height=1, bg="yellow", fg="blue", font=("微軟正黑體", 15))
        self.b2.pack(pady=10)

        self.t = tk.Text(window, height=1, font=("微軟正黑體", 15))
        self.t.pack() 


if __name__ == "__main__":
    window = tk.Tk()
    window.title("insert")
    window.geometry("400x250+0+0")
    User(window)
    window.mainloop()