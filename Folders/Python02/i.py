import random

students = {}
id = 1

for i in range(65, 91):
    student = chr(i), chr(i),chr(i) # ASCii

    score01 = random.randint(0, 100)
    score02 = random.randint(0, 100)
    score03 = random.randint(0, 100)

    if id < 10:
        id_string = "G00" + str(id)
    else:
        id_string = "G0" + str(id)

    students[id_string] = (student, score01, score02, score03)

    id += 1
    if id > 20:
        break

input_id = input("Please input your id (G001 ~ G020):")
print(students[input_id])