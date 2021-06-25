import tkinter as tk

class Game():
    def __init__(self, window):
        
        self.lab = tk.Label(window, text="Empty", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
        self.lab.pack(pady=10)

        def Print_selection(v):
            self.lab.config(text="you have selected " + v)

        self.s = tk.Scale(window, label="Try Me", from_=1, to=10, orient=tk.HORIZONTAL, length=400, showvalue=0, tickinterval=3, resolution=0.01, command=Print_selection, font=("微軟正黑體", 15))
        self.s.pack()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Scale")
    window.geometry("450x300+0+0")
    game = Game(window)
    window.mainloop()