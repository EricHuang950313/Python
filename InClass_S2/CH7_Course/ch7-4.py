import pandas as pd
import numpy as np
sheet = pd.read_excel(r"C:\Users\Eric Huang\Desktop\test.xlsx", sheet_name="Sheet1")
print(sheet)
x = sheet.years
xlist = list(x)
xarray = np.array(x)
print(xlist)
print(xarray)
mylist = sheet.columns.values.tolist()
print(mylist)
sheet = sheet.rename(columns={"years" : "AC:Years"})
print(sheet)
sheet.item[1] = "*B*"
sheet.value[1] = 200
print(sheet)
print(sheet.describe())
sheet.to_excel(r"C:\Users\Eric Huang\Desktop\test2.xlsx", sheet_name="Sheet1", index=False)
