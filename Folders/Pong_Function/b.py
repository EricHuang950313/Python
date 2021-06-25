# 回傳值

def hello(word):
    print(word)
    return 1  # 如果沒有，就是None


value = hello("Hello World")  # 呼叫函式、取得回傳值
print(value)  # 印出回傳值

def word(n1, n2):
    result = n1 + n2
    return result


value = word(2, 3)
print(value)
