import tkinter as tk

class Game():
    def __init__(self, window):
        self.lab = tk.Label(window, text="Empty", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
        self.lab.pack(pady=10)

        def Print_selection():
            self.lab.config(text="you have selected " + self.var.get())

        self.var = tk.StringVar()

        self.a = tk.Radiobutton(window, text="Option A", variable=self.var, value="A", command=Print_selection, font=("微軟正黑體", 15), width=15)
        self.a.pack(pady=10)

        self.b = tk.Radiobutton(window, text="Option B", variable=self.var, value="B", command=Print_selection, font=("微軟正黑體", 15), width=15)
        self.b.pack(pady=10)

        self.c = tk.Radiobutton(window, text="Option C", variable=self.var, value="C", command=Print_selection, font=("微軟正黑體", 15), width=15)
        self.c.pack(pady=10)

        self.d = tk.Radiobutton(window, text="Option D", variable=self.var, value="D", command=Print_selection, font=("微軟正黑體", 15), width=15)
        self.d.pack(pady=10)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Radiobutton")
    window.geometry("450x300+0+0")
    game = Game(window)
    window.mainloop()