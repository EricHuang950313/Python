import win32com
from win32com.client import Dispatch, constants
import os
import random
import math
import time
import sys

os.remove("./info/math.txt")
os.remove("./info/col.txt")

user = input("amount:")
user = int(user)
if user < 150:
    column = math.floor(user/3)+1
elif user > 150:
    column = math.floor(user/3) + math.ceil(user/150)

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

for i in range(1, table.Rows.Count+1):
    for j in range(1, table.Columns.Count+1):
        yesNo = False
        while yesNo == False:
            n1 = str(random.randint(10, 90))
            n2 = str(random.randint(2, 9))
            if ((int(n2)*10) > int(n1) > int(n2)):
                break
            else:
                continue
        table.Cell(i, j).Range.Text = ("{}÷{}=   ...    ".format(n1,n2))
            
        if count == user:
            with open("./info/math.txt", mode="a", encoding="utf-8")as file:    
                file.write("{}÷{}=   ...    ".format(n1,n2)+"\n")
            with open("./info/col.txt", mode="a", encoding="utf-8")as file:    
                file.write(str(column))
            doc.SaveAs(os.path.dirname(os.path.abspath("2.py"))+"\\Pratice+Answer\\Pratice.docx")
            table.Cell(i, j+1).Range.Text = ("   /   Wrong:")
            doc.Close()
            word.Quit()
            sys.exit()
        if count % 51 == 0:
            table.Cell(i, j).Range.Text = ("   /   Wrong:")
            count += 1
            user += 1
        else:
            with open("./info/math.txt", mode="a", encoding="utf-8")as file:    
                file.write("{}÷{}=   ...    ".format(n1,n2)+"\n")
            count += 1

        