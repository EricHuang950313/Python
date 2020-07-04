import tkinter as tk
def main():
    # Set Everything
    window = tk.Tk()
    window.title("Test")
    window.geometry("600x400+0+0")
    window.configure(bg="black")
    photo = tk.PhotoImage(file="A.gif")
    imgLabel = tk.Label(window, image=photo)  # 把圖片整合到標簽類中
    imgLabel.pack() # 自動對齊
    window.mainloop()

main()