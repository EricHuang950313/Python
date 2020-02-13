import tkinter as tk 
import time 
from functools import partial

def main(): 
    global window, l
    window = tk.Tk()
    window.title("Timer")
    window.geometry("600x400+0+0")
    l = tk.Label(window, font=("微軟正黑體",50, "bold"))
    l.pack()
    update()
    window.mainloop()
    
def update():
    now = time.strftime("%H:%M:%S")
    l.configure(text=now)
    window.after(1000, update)

main()
