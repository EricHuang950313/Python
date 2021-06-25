import tkinter as tk

window = tk.Tk()
window.title("Scale")
window.geometry("450x300+0+0")


lab = tk.Label(window, text="Empty", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
lab.pack(pady=10)

def Print_selection(v):
    lab.config(text="you have selected " + v)

s = tk.Scale(window, label="Try Me", from_=5, to=11, orient=tk.HORIZONTAL, length=400, showvalue=0, tickinterval=3, resolution=0.01, command=Print_selection, font=("微軟正黑體", 15))
# 因為 Python 有 from xxx import xxx, 所以 from --> from_
# 在 scale 的 command 中有一個默認傳入值 --> 在 "Print_selection" 加入參數
# orient：導向、方向；horizontal：橫向；without "orient=tk.HORIZONTAL" ：直向
s.pack()

window.mainloop()