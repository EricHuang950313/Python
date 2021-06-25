import tkinter as tk

class Game():
    def __init__(self, window):
        self.var = tk.StringVar()
        l = tk.Label(window, textvariable=self.var, width=15, height=2, bg="blue", fg="yellow", font=("微軟正黑體", 15))
        l.pack()

        self.on_hit = False
        def hit_me():
            if self.on_hit == False:
                self.on_hit = True
                self.var.set("You hit me.")
            else:
                self.on_hit = False
                self.var.set("")

        b = tk.Button(window,command=hit_me, text="Hit Me.",width=15, height=2, bg="yellow", fg="blue", font=("微軟正黑體", 15))
        b.pack(pady=10)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("XXD")
    window.geometry("200x150+0+0")
    game = Game(window)
    window.mainloop()