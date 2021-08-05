ques = input().split()

if ques[1] == "+":
    print(int(ques[0]) + int(ques[2]))
elif ques[1] == "-":
    print(int(ques[0]) - int(ques[2]))
elif ques[1] == "*":
    print(int(ques[0]) * int(ques[2]))
elif ques[1] == "/":
    print(int(ques[0]) / int(ques[2]))