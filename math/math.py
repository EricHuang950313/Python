import random, time
FILE = "./math.txt"

ques = int(input(""))

yesNo = False

with open(FILE, mode="w", encoding="utf-8")as file:    
    for i in range(ques):
        while yesNo == False:
            n1 = str(random.randint(1, 90))
            n2 = str(random.randint(2, 9))
            if ((int(n2)*10) > int(n1) > int(n2)):
                break
            else:
                continue
        file.write("{}÷{}=   ...    ".format(n1,n2)+"\n")

print()
print("=========================")
print("||",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),":",str(ques),"||")
print("=========================")
print()