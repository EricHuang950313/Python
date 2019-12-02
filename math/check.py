import math
# 讀取資料時記得把1位數除1位數的那一行刪掉
with open("math.txt", mode="r", encoding="utf-8") as file:
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

with open("check.txt", mode="w", encoding="utf-8") as file:
    for i in l:
        file.write(i+"\n")
