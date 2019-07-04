with open("data_d.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3\n10")
sum = 0
with open("data_d.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum += int(line)
print(sum)