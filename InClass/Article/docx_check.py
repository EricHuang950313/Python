import win32com
from win32com.client import Dispatch, constants
import os
import random
import math
import time
import sys

with open("./info/col.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        column = str(line)
word = win32com.client.Dispatch("Word.Application")
word.Visible = 1
word.DisplayAlerts = 0
doc = word.Documents.Add()

rangee = doc.Range(0,0)
rangee.Style.Font.Name = "微軟正黑體"
rangee.Style.Font.Size = 18
rangee.Style.Font.Outline = 0
table = doc.Tables.Add(rangee, column, 3)
count = 1

with open("./info/math.txt", mode="r", encoding="utf-8") as file:
    l = []
    data = file.read()
    file.seek(0)
    for line in file:
        a = int(line[0]+line[1])
        b = int(line[3])

        for i in range(b+1):
            if ((a-i) % b) == 0:
                l += [str(math.floor((a-i)/b))+" , "+str(abs(-i))]
                break
            else:
                continue

l += [" "]
count = 0
user = int(column) * 3
x = 0
for i in range(1, table.Rows.Count+1):
    for j in range(1, table.Columns.Count+1):
        table.Cell(i, j).Range.Text = l[count+x]
        count += 1
        if count == user:
            doc.SaveAs(os.path.dirname(os.path.abspath("2.py"))+"\\Pratice+Answer\\Answer.docx")
            doc.Close()
            word.Quit()
            sys.exit()
        if count != 0 and count % 51 == 0:
            table.Cell(i, j).Range.Text = " "
            x -= 1
