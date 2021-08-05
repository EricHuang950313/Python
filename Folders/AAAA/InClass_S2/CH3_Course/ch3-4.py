mymap = [["●", " ", "▲", " "], [" ", "▲", " ", " "], [" ", " ", " ", " "], [" ", " ", "▲", " "]]
letter = ["W", "w", "A", "a", "S", "s", "D", "d"]

def check_input(userinput):
    return userinput in letter

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

def endIfWin(pos):
    return True if pos[0] == 3 and pos[1] == 3 else None

def gaming():
    show_map()
    currentPos = (0, 0)
    while True:
        userinput = input("Please input Ww/Aa/Ss/Dd to move.")
        canMove = check_input(userinput)
        if canMove == False:
            print("Input Letter Interrupt.")
            print(letter)
        else:
            if userinput == "W" or userinput == "w":
                if currentPos[0] - 1 < 0:
                    print("Input Position Interrupt.")
                elif mymap[currentPos[0] - 1][currentPos[1]] == "▲":
                    print("Input Position Interrupt.")
                else:
                    mymap[currentPos[0] - 1][currentPos[1]] = "●"
                    mymap[currentPos[0]][currentPos[1]] = " "
            elif userinput == "A" or userinput == "a":
                if currentPos[1] - 1 < 0:
                    print("Input Position Interrupt.")
                elif mymap[currentPos[0]][currentPos[1] - 1] == "▲":
                    print("Input Position Interrupt.")
                else:
                    mymap[currentPos[0]][currentPos[1] - 1] = "●"
                    mymap[currentPos[0]][currentPos[1]] = " "
            elif userinput == "S" or userinput == "s":
                if currentPos[0] + 1 > 3:
                    print("Input Position Interrupt.")
                elif mymap[currentPos[0] + 1][currentPos[1]] == "▲":
                    print("Input Position Interrupt.")
                else:
                    mymap[currentPos[0] + 1][currentPos[1]] = "●"
                    mymap[currentPos[0]][currentPos[1]] = " "
            else:
                if currentPos[1] + 1 > 3:
                    print("Input Position Interrupt.")
                elif mymap[currentPos[0]][currentPos[1] + 1] == "▲":
                    print("Input Position Interrupt.")
                else:
                    mymap[currentPos[0]][currentPos[1] + 1] = "●"
                    mymap[currentPos[0]][currentPos[1]] = " "
            show_map()
            currentPos = findPos()
            if endIfWin(currentPos):
                break
    print("Great Job!")

gaming()