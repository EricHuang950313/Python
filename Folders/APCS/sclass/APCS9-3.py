import sys

y = [".", ",", "!"]
n = ["(", ")", "-", "[", "]", "{", "}", ";", ":", "<", ">", "?", "@", "#", "$", "%", "^", "&", "*"]
final = ""

for s in sys.stdin:
    for i in s:
        if i not in n:
            final += i
    print(final[:-1])