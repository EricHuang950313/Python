import pandas as pd
import numpy as np

def find_average(data):
    result = []
    for i in range(len(data)):
        s = (data[i,1]+data[i,2]+data[i,3])/3
        result.append(s)
    return result

def find_rank(average):
    aver = np.asarray(average)
    myindex = np.argsort(aver)
    rank = [0]*len(myindex)
    for i in range(len(myindex),0,-1):
        rank[myindex[i-1]] = len(myindex) - i + 1
    return rank

sheet = pd.read_excel(r"D:\Eric\VsCode\Python\InClass_S2\CH8_Course\Hw.xlsx", sheet_name="Sheet1")
print(sheet)
print("==================")
data = sheet.values
print(data)
print("==================")
average = find_average(data)
print(average)
print("==================")
x = pd.Series(average)
sheet = sheet.assign(Avarage=x)
print(sheet)
print("==================")
rank = find_rank(average)
x = pd.Series(rank)
sheet = sheet.assign(Rank=x)
print(sheet)
sheet.to_excel(r"D:\Eric\VsCode\Python\InClass_S2\CH8_Course\Hw.xlsx", sheet_name="Sheet1", index=False)