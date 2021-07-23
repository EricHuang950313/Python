def ffind(count, t, index):
    print(count, t, index)
    if index == len(string):
        return count, 0, index
    if t == "U":
        for i in range(goal):
            if index+i == len(string):
                return count, 0, len(string)
            if string[i+index].isupper() == True:
                continue
            else:
                return count, "L", i+index
        else:
            return ffind(count+goal, "L", index+1)      
    elif t == "L":
        for i in range(goal):
            if index+i == len(string):
                return count, 0, len(string)
            if string[i+index].islower() == True:
                continue
            else:
                return count, "U", i+index
        else:
            return ffind(count+goal, "U", index+1)

goal = int(input())
string = list(map(str, input()))
print(string)
count, index = 0, 0
biggest = 0
if string[0].isupper()==True:
    t = "U"  
else:
    t = "L"
while True:
    if index == len(string):
        break
    if t == "U":
        count, t, index = ffind(count, "U", index)
    else:
        count, t, index = ffind(count, "L", index)
    if count > biggest:
        biggest = count
    count = 0
print(biggest)