import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window.geometry("350x500+0+0")

canvas = tk.Canvas(window, bg="light green", height=350, width=300)
image_file = tk.PhotoImage(file="happy.png")
image = canvas.create_image(10, 10, anchor="nw", image=image_file)
x0, y0, x1, y1 =150, 150, 200, 200
x2 = 20
line = canvas.create_line(x0, y0, x1, y1, width=3)
circle = canvas.create_oval(x0, y0, x1, y1, fill="yellow", width=3, outline="red")
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(x2, 10, 130, 130, outline="dark blue", width=3)
canvas.pack(pady=10)

lab = tk.Label(window, text="Start", bg="yellow", fg="red", font=("微軟正黑體", 15), width=20) 
lab.pack(pady=10)

pos = []
def up():
    canvas.move(rect, 0, -5)
    pos = canvas.coords(rect)
    print(pos)
    if pos[1] == 10:
        lab.config(text="Correct Position "+str(pos[1]), fg="dark blue")
    else:
        lab.config(text="Wrong Position "+str(pos[1]), fg="red")
def down():
    canvas.move(rect, 0, 5)
    pos = canvas.coords(rect)
    print(pos)
    if pos[1] == 10:
        lab.config(text="Correct Position "+str(pos[1]), fg="dark blue")
    else:
        lab.config(text="Wrong Position "+str(pos[1]), fg="red")


b1 = tk.Button(window, text="Move UP", command=up, width=15, fg="dark blue", font=("Arail", 15))
b1.pack(pady=5)
b2 = tk.Button(window, text="Move Down", command=down, width=15, fg="dark blue", font=("Arail", 15))
b2.pack(pady=5)

window.mainloop()