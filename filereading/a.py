import os

FILE = "d:\\note.txt"

if os.path.isfile(FILE):
    print("mistake")
    exit()

file = open(FILE, "w+t")

for i in range(1, 11):
    line = "This is line" + str(i) + ",Ya\n"
    file.write(line)

file.seek(0)

while True:
    line = file.readline()

    if not line:
        break

    print(line)

file.close()
os.remove(FILE)