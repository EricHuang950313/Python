import tkinter as tk
import os

def main():
    # Set Everything
    window = tk.Tk()
    window.title("成果發表")
    window.geometry("700x400+0+0")
    window.configure(bg="black")
    Welcome(window)
    window.mainloop()

def Welcome(window):
    tk.Label(window,fg="yellow", bg="black", font=("微軟正黑體",40), text="核果資訊學院\nPythonLevel2\n成果發表會").place(x=5, y=90)
    tk.Button(window, text="心算習題\n產生器", font=("微軟正黑體",24), width=10, command=math).place(x=430,y=40)
    tk.Button(window, text="自動\n走迷宮", font=("微軟正黑體",24), width=10, command=migong).place(x=430,y=220)

def math():
    os.system("Python MathGUI.py")

def migong():
    os.system("Python migong.py")

if __name__ == "__main__":
    main()