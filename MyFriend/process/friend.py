import os
DATA_FILE = "d:\Eric\Python\\friend.txt"


def open_file():
    file_path = os.path.dirname(DATA_FILE)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if os.path.isfile(DATA_FILE):
        file = open(DATA_FILE, "a+t")
    else:
        file = (DATA_FILE, "w+t")
    return file


def add (file, name, gender, age, tel):
    if gender == 1:
        gender = "男"
    else:
        gender = "女"

    line = name + " " + gender + " " + str(age) + " " + tel + "\n"
    file.write(line)


def close_file(file):
    file.close()


def find(file, name):
    file.seek(0, 0)
    for line in file:
        name_this_line, *others = line.split()
        if name_this_line == name:
            friend_data = [name_this_line]
            friend_data += others
            return friend_data

    return None


def iterate_start(file):
    file.seek(0, 0)


def iterate_next(file):
    line = file.readline()
    if line == "":
        return None

    friend = line.split()
    return friend
