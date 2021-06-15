mymap = [["●", " ", "▲", " ","▲"], [" ", "▲", " ", " "," "], [" ", " ", " ", "▲"," "], [" ", "▲", " ", "▲"," "], ["▲", " ", "▲", " "," "]]
letter = ["W", "w", "A", "a", "S", "s", "D", "d"]

def check_input(userinput):
    return userinput in letter

def update_map(currentPos_old, currentPos):
    mymap[currentPos_old[0]][currentPos_old[1]] = " "
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

def check_path(direction, mymap, currentPos):
    currentPos_old = currentPos.copy()
    currentPos_new = currentPos.copy()
    print(currentPos, type(currentPos))
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
    elif mymap[currentPos_new[0]][currentPos_new[1]] == "▲":
        flag = 0
    else:
        flag = 1
    return flag, currentPos_old, currentPos_new

def endIfWin(pos):
    return True if pos[0] == 4 and pos[1] == 4 else None

def gaming(mymap):
    show_map()
    currentPos = [0, 0]
    while True:
        userinput = input("Please input Ww/Aa/Ss/Dd to move.")
        inLetter = check_input(userinput)
        if inLetter == False:
            print("Input Letter Interrupt.")
            print(letter)
        else:
            flag, currentPos_old, currentPos_new = check_path(userinput, mymap, currentPos)
            print(flag)
            if flag == 0:
                currentPos = currentPos_old
                print("Input Wrong Position")
                show_map()
            else:
                currentPos = currentPos_new
                mymap = update_map(currentPos_old, currentPos)
                show_map()
            if endIfWin(currentPos) == True:
                break
    print("Great Job!")

gaming(mymap)