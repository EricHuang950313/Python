import pandas as pd
import numpy as np
sheet = pd.read_excel(r"D:\Eric\VsCode\Python\InClass_S2\CH7_Course\test.xlsx", sheet_name="Sheet1")
print(sheet)
print("==================")
data = sheet.values
print(data)
print("==================")
x = sheet.years
xlist = list(x)
print(xlist)
print("==================")
xarray = np.array(x)
print(xarray)
print("==================")
mylist = sheet.columns.values.tolist()
print(mylist)
print("==================")
sheet = sheet.rename(columns={"years" : "AC:Years"})
print(sheet)
print("==================")
sheet.item[1] = "*B*"
sheet.value[1] = 200
print(sheet)
print("==================")
print(sheet.describe())
sheet.to_excel(r"D:\Eric\VsCode\Python\InClass_S2\CH7_Course\test2.xlsx", sheet_name="Sheet1", index=False)

