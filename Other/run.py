import random, math, time
FILE = "./run.txt"

def read():
    already = []
    with open(FILE, "r")as file:
        for line in file:
            already += [line.rstrip("\n")]
    return already

def RandomADigit():
    return str(random.randint(1, 275))
    
def yesNo(digit):
    for i in range(len(already)):
        if digit == already[i]:
            return True
    return False 

already = read()
digit = RandomADigit()

while True:
    if yesNo(digit) == True:
        digit = RandomADigit()
        continue
    else:
        break
    
with open(FILE, "a")as file:
    file.write(digit+"\n")

print()
print("=========================")
print("||",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"||")
print("=========================")
print("Today's Program : {}".format(digit))
print()