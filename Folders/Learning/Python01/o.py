num = int(input("Please input the number of people:"))

score_list = []
for i in range(0, num):
    score = int(input("Please input the student's score:"))
    score_list += [score]

print("Students' score:", score_list)