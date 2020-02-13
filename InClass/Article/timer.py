import tkinter as tk 
import time 
def main(): 
    window = tk.Tk()
    window.title("Timer")
    window.geometry("600x400+0+0")
    timer(window)
    window.mainloop()
    
def timer(window):
    t = time.strftime('%H:%M:%S')
    s = tk.StringVar()
    l = tk.Label(window, textvariable=s, font=("微軟正黑體",50, "bold"))
    l.pack()
    while True:
        t = time.strftime('%H:%M:%S')
        s.set(t)
        window.update()

main()