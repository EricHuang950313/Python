# A Reversegam (or you can call Reversi/Othello) game
# Modified from "Invent Your Own Computer Games with Python"
# Modified by Eric Huang in "Taiwan"

# import modules
import random
import sys

WIDTH = 8 # board is 8 spaces wide (Non-changed variable)
HEIGHT = 8 # board is 8 spaces tall (Non-changed variable)

def drawBoard(board):
    # draw the board
    print("  12345678")
    print(" +--------+")
    for y in range(HEIGHT):
        print("%s|" %(y+1), end="")
        for x in range(WIDTH):
            print(board[x][y], end="")
        print("|%s" %(y+1))
    print(" +--------+")
    print("  12345678")

        
def getNewBoard():
    # create a new board
    board = []
    for i in range(WIDTH):
        board += [[" ", " ", " ", " ", " ", " ", " ", " "]]
    return board


def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != " " or not isOnBoard(xstart, ystart):
        return False
    
    if tile == "X":
        otherTile = "O"
    else:
        otherTile = "X"
    
    tilesToFlip = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection

            if isOnBoard(x, y) and board[x][y] == tile:		
                while True:		
                    x -= xdirection		
                    y -= ydirection		
                    if x == xstart and y == ystart:		
                        break		
                    tilesToFlip.append([x, y])


    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.		
        return False		
    return tilesToFlip	


def isOnBoard(x, y):			
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1	


def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(board, tile):
        boardCopy[x][y] = "."
    
    return boardCopy


def getValidMoves(board, tile):
    validMoves = []

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMoves +=[[x, y]]
    return validMoves


def getScoreOfBoard(board):
    Xscore = 0
    Oscore = 0

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == "X":
                Xscore += 1
            if board[x][y] == "O":
                Oscore += 1
    return {"X":Xscore, "O":Oscore}


def enterPlayerTile():
    tile = ""
    while not (tile == "X" or tile == "O"):
        print("Which do you want to be, \"O\" or \"X\" ?")
        tile = input().upper()

    if tile == "O":
        return ["O", "X"]
    else:
        return ["X", "O"]


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "player"
    else:
        return "computer"


def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False
    
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile

    return True


def getBoardCopy(board):
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]
    return boardCopy


def isOnCorner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)


def getPlayerMove(board, playerTile):
    DIGITS1T08 = "1 2 3 4 5 6 7 8".split()
    while True:
        print("Enter your move, \"quit\" to end the game, or \"hints\" to toggle hints.")
        move = input().lower()
        if move == "quit" or move == "hints":
            return move
        if len(move) == 2 and move[0] in DIGITS1T08 and move[1] in DIGITS1T08:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row (1-8).')		
            print('For example, 81 will move on the top-right corner.')	
    return[x, y] 


def playerMayMove(board, playerTile):
    possibleMoves = getValidMoves(board, playerTile)

    bestscore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, playerTile, x, y)
        score = getScoreOfBoard(boardCopy)[playerTile]
        if score > bestscore:
            bestscore = score
    return bestscore


def getComputerMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return[x, y]

    boardCopy = getBoardCopy(board)
    bestscore = -1

    PlayerOriginalScore = getScoreOfBoard(boardCopy)[playerTile]
    ComputerOriginalScore = getScoreOfBoard(boardCopy)[computerTile]

    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]

        if len(possibleMoves) == 1:
            return possibleMoves[0]

        if score > bestscore:
            makeMove(boardCopy, playerTile, x, y)
            scoreP = playerMayMove(boardCopy, playerTile)

            if (scoreP - PlayerOriginalScore) >= (score - ComputerOriginalScore):
                pass
            else:
                bestMove = [x, y]
                bestscore = score
    return bestMove


def printScore(board, playerTile, computerTile):		
    scores = getScoreOfBoard(board)		
    print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))		


def playGame(playerTile, computerTile):
    showhints = False
    turn = whoGoesFirst()
    print("The " + turn + " will be first.")

    board = getNewBoard()
    board[3][3] = "X"
    board[3][4] = "O"
    board[4][3] = "O"
    board[4][4] = "X"

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)
        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == "player":
            if playerValidMoves != []:
                if showhints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)
                move = getPlayerMove(board, playerTile)
                if move == "quit":
                    print("Thanks for playing")
                    sys.exit()
                elif move == "hints":
                    showhints = not showhints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = "computer"
        elif turn == "computer":  
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile )

                input("Press Enter to see computer's move.")
                move = getComputerMove(board, computerTile)

                makeMove(board, computerTile, move[0], move[1])
            turn = "player"



print("Welcome to Reversegam!")

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    drawBoard(finalBoard)

    scores = getScoreOfBoard(finalBoard)		
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))		
    if scores[playerTile] > scores[computerTile]:		
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))		
    elif scores[playerTile] < scores[computerTile]:		
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))		
    else:		
        print('The game was a tie!')		
        
    print('Do you want to play again? (yes or no)')		
    if not input().lower().startswith('y'):		
        break
