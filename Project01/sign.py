print("==== 抽籤軟體 ====")
print("~~~~ 每次抽一枝 ~~~~")
print("~~~~ 按 0 可結束 ~~~~")
import random
choiced = []
over = False
x = int(input("請輸入最小數字："))
y = int(input("請輸入最大數字："))
y += 1

try:
    while not over:
        for i in range(1):
            choiced.insert(0, random.choice([x for x in range(x, y) if x not in choiced]))
            print("數字是：", choiced[0])
        a = input("==== 按任意鍵抽籤 ====")
        if a == "0":
            break
except IndexError:
    print("籤已抽完!!!")
finally:
    print("==== 程式結束 ====")