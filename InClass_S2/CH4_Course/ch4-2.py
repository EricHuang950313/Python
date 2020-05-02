# illegal_pos:check not triangle
# edit find_select_N

mymap = [["●", " ", "▲", " ","▲"], [" ", "▲", " ", " "," "], [" ", " ", " ", "▲"," "], [" ", "▲", " ", "▲"," "], ["▲", " ", "▲", " "," "]]
letter = ["W", "w", "A", "a", "S", "s", "D", "d"]

def check_input(userinput):
    return userinput in letter

def update_map(currentPos_old, currentPos):
    mymap[currentPos[0]][currentPos[1]] = "●"
    return mymap

def show_map():
    for i in range(0, len(mymap)):
        print(mymap[i])

def findPos():
    for i in range(0, len(mymap)):
        for j in range(0, len(mymap)):
            if mymap[i][j] == "●":
                return (i, j)
            else:
                pass

def illegal_pos(pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] > 4 or pos[1] > 4:
        illegal_flag = 0
    else:
        illegal_flag = 1
    return illegal_flag

def check_path(direction, mymap, currentPos):
    currentPos_old = currentPos.copy()
    currentPos_new = currentPos.copy()
    if direction in ["A", "a"]:
        currentPos_new[1] -= 1
    if direction in ["D", "d"]:
        currentPos_new[1] += 1
    if direction in ["W", "w"]:
        currentPos_new[0] -= 1
    if direction in ["S", "s"]:
        currentPos_new[0] += 1

    if currentPos_new[0] < 0 or currentPos_new[1] < 0 or currentPos_new[0] > 4 or currentPos_new[1] > 4:
        flag = 0
    elif mymap[currentPos_new[0]][currentPos_new[1]] in ["▲", "●"]:
        flag = 0
    else:
        flag = 1
    return flag, currentPos_old, currentPos_new

def endIfWin(pos):
    return True if pos[0] == 4 and pos[1] == 4 else None

def find_select_N(currentPos):
    a = illegal_pos([currentPos[0], currentPos[1] - 1])
    b = illegal_pos([currentPos[0], currentPos[1] + 1])
    c = illegal_pos([currentPos[0] + 1, currentPos[1]])
    d = illegal_pos([currentPos[0] - 1, currentPos[1]])
    print(a, b, c, d)
    return a+b+c+d

def gaming(mymap):
    show_map()
    currentPos = [0, 0]
    pos_record = [currentPos]
    select_N_record = [find_select_N(currentPos)]
    while True:
        userinput = input("Please input Ww/Aa/Ss/Dd to move.")
        inLetter = check_input(userinput)
        if inLetter == False:
            print("Input Letter Interrupt.")
            print(letter)
        else:
            flag, currentPos_old, currentPos_new = check_path(userinput, mymap, currentPos)
            if flag == 0:
                currentPos = currentPos_old
                print("Input Wrong Position")
                show_map()
            else:
                currentPos = currentPos_new
                pos_record += [currentPos]
                mymap = update_map(currentPos_old, currentPos)
                show_map()
                select_N = find_select_N(currentPos)
                select_N_record += [select_N]
                if select_N == 0:
                    print("You have no place to go.")
                    a = input("Click anything to contiune")
            if endIfWin(currentPos) == True:
                print("Great Job!")
                break


gaming(mymap)