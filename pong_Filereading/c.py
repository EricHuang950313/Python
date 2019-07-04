with open("data_c.txt", mode="w", encoding="utf-8") as file:
    file.write("中文\n太神啦")

with open("data_c.txt", mode="r", encoding="utf-8") as file:
    data = file.read()
print(data)