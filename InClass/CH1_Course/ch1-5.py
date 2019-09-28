# for:有範圍 
# while:沒有範圍
# 看有沒有範圍用 len()
# 判斷:布林值

a = 123
b = "abc"
c = [1,2,3,4]

for i in range(len(c)):
    print(c[i])

d = 3.14159
print("{} {} {:.2f}".format(b, c, d))