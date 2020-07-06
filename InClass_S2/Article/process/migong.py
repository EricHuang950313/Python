import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

img1 = np.zeros((512,768,3),np.uint8)
img = cv2.circle(img1, (384,255), 175, (0, 0, 255), -1)

# A root window for displaying objects
root = tk.Tk()

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

# Put it in the display window
tk.Label(root, image=imgtk).pack()

root.mainloop() # Start the GUI

