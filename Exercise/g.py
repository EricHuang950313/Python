import pandas as pd
import matplotlib.pyplot as plt
sheet = pd.read_excel(r"D:\Eric\VsCode\Python\InClass_S2\Article\Temp.xlsx", sheet_name="Sheet1")
data = sheet.values
plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.show()