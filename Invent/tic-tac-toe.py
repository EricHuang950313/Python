# A tic-tac-toe game
# Modified from "Invent Your Own Computer Games with Python"
# Modified by Eric Huang in "Taiwan"

import random

def drawboard(board):
    # This Function prints the board\
    # Board is a list of 10 strings (Ignore the First String index"[0]"")

    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def inputPlayerXO():
    # Ask Player which do he or she want, X or O ?
    # Returns [player's letter, computer's letter] as a string in list

    letter = ""
    while not (letter == "O" or letter == "X"):
        print("Which do you want to be, \"X\" or \"O\" ?")
        letter = input().upper()

        if letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]


def whoGoFirst():
    # Use module "random" to choose who go first
    # return player or computer

    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def makeMove(board, letter, move):
    # Change the list, board
    board[move] = letter


def isWinner(bo, le):
    # bo equal board, le equal letter
    # Give the function board(a list) and player's letter
    # The function "isWinner" will return True or False

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le) )


def copyBoard(board):
    # Copy the list, board with a new reference
    boardCopy = []
    for i in board:
        boardCopy += [i]
    return boardCopy


def isSpaceFree(board, move):
    # return True or False
    return board[move] == " "


def getPlayerMove(board):
    # Let player input their move
    move = ""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is Your Move ?")
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movelist):
    # Return a move or None
    possibleMoves = []
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMoves += [i]
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def dragon(board, computerLetter):
    two = []
    for i in range(1, 10):
        D_boardCopy = copyBoard(board)
        if isSpaceFree(D_boardCopy, i) or D_boardCopy[i] == computerLetter:
            continue
        else:
            two += [int(i)]
    if two == [1, 6]:  #[1, 8] or [3, 8]:
        return 3
    elif two == [6, 7]:
        return 9
    elif two == [3, 4]:
        return 1
    elif two == [4, 9]:
        return 7
    elif two == [2, 7]:
        return 1
    elif two == [2, 9]:
        return 3
    elif two == [1, 8]:
        return 7
    elif two == [3, 8]:
        return 9
    else:
        return None 


def doubleGo(board, computerLetter):
    three = []
    for i in range(1, 10):
        D_boardCopy = copyBoard(board)
        if isSpaceFree(D_boardCopy, i) or D_boardCopy[i] == computerLetter:
            continue
        else:
            three += [int(i)]
    if three == [1, 9]:
        return 6
    elif three == [3, 7]:
        return 4
    else:
         return None


def getComputerMove(board, computerLetter):
    # Computer letter and player letter
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Tic-Tac-Toe AI
    # check if AI can win
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if isSpaceFree(board, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # stop player to win
    for i in range(1, 10):
        boardCopy = copyBoard(board)
        if isSpaceFree(board, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    # dragon
    Vdragon = dragon(board, computerLetter)
    if Vdragon != None:
        return Vdragon

    # doubleGo
    VdoubleGo = doubleGo(board, computerLetter)
    if VdoubleGo != None:
        return VdoubleGo

    # center
    if isSpaceFree(board, 5):
        return 5

    # corner  
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    #side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True



print("!!!!! Welcome to Tic-Tac-Toe !!!!!")

while True:
    # Reset the board
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerXO()
    turn = whoGoFirst()
    print("The " + turn + " will go first.")

    gameIsPlaying = True

    while gameIsPlaying:
        
        if turn == "player":
            # Player's turn
            drawboard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawboard(theBoard)
                print("Wow! You win the computer, you are so strong!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie.")
                    break
                else:
                    turn = "computer"
        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawboard(theBoard)
                print("Oh no! You lose the Computer. It was awful!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawboard(theBoard)
                    print("The game is a tie.")
                    break
                else:
                    turn = "player"

    print("Do you want to play again? It's fun!")

    # Ask player to play again
    if not input().lower().startswith("y"):
        break
