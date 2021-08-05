import tkinter as tk
from functools import partial

class interface():
    def __init__(self, window):
        self.window = window
        pass

    def start(self):
        self.window = tk.Tk()
        self.window.title("Main")
        self.window.geometry("600x400+0+0")
        self.window.configure(bg="black")
        interface.main_interface()
        self.window.mainloop()

    def main_interface(self):
        self.a = tk.Label(self.window, text="Main-Interface", font=("微軟正黑體",50, "bold"), fg="yellow", bg="black")
        self.a.place(x=60,y=40)
        self.b = tk.Button(self.window, text="課程演示", font=("微軟正黑體",32), command=partial(interface.course_demo,))
        self.b.place(x=50,y=180)
        self.c = tk.Button(self.window, text="範例實作", font=("微軟正黑體",32), command=partial(interface.example,))
        self.c.place(x=330,y=180)

    def course_demo(self):
        self.a.place_forget()
        self.b.place_forget()
        self.c.place_forget()
        self.window.configure(bg="SystemButtonFace")
        d = tk.Button(self.window, text="↖", font=("微軟正黑體", 20), bg="dark blue", fg="yellow",command=partial(interface.back,))
        d.place(x=545, y=335)

    def example(self):
        self.a.place_forget()
        self.b.place_forget()
        self.c.place_forget()
        self.window.configure(bg="SystemButtonFace")

    def back(self):
        self.window.destroy()
        interface.start()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Main")
    window.geometry("600x400+0+0")
    window.configure(bg="black")
    interface = interface(window)
    interface.main_interface()
    window.mainloop()
