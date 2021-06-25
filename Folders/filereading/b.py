import os

FILE = "d:\\note.txt"

if os.path.isfile(FILE):
    print("mistake")
    exit()

with open(FILE, "w+t")as file:

    for i in range(1, 11):
        line = "This is line" + str(i) + ",Ya\n"
        file.write(line)

    file.seek(0)

    for line in file:
        print(line)


os.remove(FILE)