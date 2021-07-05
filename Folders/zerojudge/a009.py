a = input()
for i in a:
    if i == " ":
        print(end=" ")
    else:
        print(chr(ord(i)-7), end="")