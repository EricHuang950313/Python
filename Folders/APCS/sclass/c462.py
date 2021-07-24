goal = int(input())
string, digit = list(map(str, input())), []
for i in string:
    if i.isupper() == True:
        digit += [1]
    else:
        digit += [0]

count, biggest, index = 0, 0, 0
for i in range(len(string)):
    b = False
    now = digit[0]
    while b == False:
        for j in range(goal):
            if digit[index] == now:
                count += 1
            else:
                b = True
                break
            if index+1 == len(digit):
                b = True
                break
            index += 1
        else:
            if count > biggest:
                    biggest = count
        now = 0 if now == 1 else 1
    count, index = 0, 0
    digit = digit[1:]
if len(string) == 1:
    print(1)
else:
    print(biggest)