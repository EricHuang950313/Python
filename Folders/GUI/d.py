import tkinter as tk
import tkinter.font as tkfont

def radbut_click():
    # 取得使用者點選的項目的值，然後顯示項目名稱
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])

# 建立Tk視窗
tk_win = tk.Tk()
tk_win.title('Radiobutton')

# 取得預設字型，修改字體大小，字形維持不變
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# 把Radiobutton的選項存入tuple資料組
AREA_OPTIONS = (("1", 0),
                ("2", 1),
                ("3", 2),
                ("4", 3),
                ("5", 4))

# 建立IntVar物件，記錄被點選的項目的值
area = tk.IntVar()
area.set(0)

# 根據每一個選項建立Radiobutton
for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(tk_win, text=item,
                    variable=area, value=value,
                    command=radbut_click, font=default_font)
    radbut.pack()

# 建立一個Label物件，用來顯示結果
lab_result = tk.Label(tk_win, font=default_font, fg='orange red')
lab_result.pack(padx=10, pady=(5, 10))

# 啟動GUI程式的處理迴圈
tk_win.mainloop()