# A tic-tac-toe GUI game
# Modified from "Invent Your Own Computer Games with Python"
# Modified by Eric Huang from "Taiwan"
# ------ Start ------

# import tkinter, messageboxx, random, pygame(music)
import tkinter as tk
from tkinter import messagebox
import random
import pygame
from functools import partial
import os

# reset the pygame music
pygame.mixer.init()
def music():
    # repeat the music
    pygame.mixer.music.load("Up_Above.mp3")
    pygame.mixer.music.play(loops=-1)
#music()

# open tkinter and set the interface
window = tk.Tk()
window.title("Tic-tac-toe")
window.geometry("450x320")
window.configure(background="light yellow")

            
def makeMove(board, letter, move):
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
    return board[move] == ""


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


def whoGoFirst():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


# ---< GUI Start >---


def inputPlayerXO(board, turn):
    # ask player to choose that player want to be "O" or "X"

    global OX, label, entry, button

    OX = tk.StringVar()
    label = tk.Label(window, text="Which do you want to be, \"O\" or \"X\"?", bg="light yellow", font=("微軟正黑體", 15))
    label.pack(pady=10)
    entry = tk.Entry(textvariable=OX, font=("微軟正黑體", 15))
    entry.pack(pady=10)
    button = tk.Button(window, text="= Confirm =", command=partial(setXO_goFirst, board, turn), font=("微軟正黑體", 15))
    button.pack(pady=10)
    
    
def setXO_goFirst(board, turn):
    # set player's XO and computer's XO and choose who will go first, finally, display them

    global playerLetter, computerLetter

    if(OX.get().upper() == "O" or OX.get().upper() == "X"):
        if OX.get().upper() == "X":
            playerLetter = "X"
            computerLetter = "O"
        else:
            playerLetter = "O"
            computerLetter = "X"


        LabelP = tk.Label(window, text="You : "+ playerLetter, fg="Blue", bg="light yellow", font=("微軟正黑體", 36, "bold"))
        LabelP.pack()
        LabelC = tk.Label(window, text="Computer : "+ computerLetter,fg="Red", bg="light yellow", font=("微軟正黑體", 15))
        LabelC.pack()
        LabelF = tk.Label(window, text="Go first : "+ turn, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.pack()
        window.update()
        window.after(3000)
        label.destroy()
        entry.destroy()
        button.destroy()
        LabelP.destroy()
        LabelC.destroy()
        LabelF.destroy()
        displayCanvas(board, turn)
    else:
        messagebox.showinfo("Error", "Please input \"O\" or \"X\".")


def num(i, j):
    # for return Label, which display OX

    if (i == 1):
        if (j == 1):
            return 1
        elif (j == 2):
            return 2
        elif (j == 3):
            return 3
    if (i == 2):
        if (j == 1):
            return 4
        elif (j == 2):
            return 5
        elif (j == 3):
            return 6
    if (i == 3):
        if (j == 1):
            return 7
        elif (j == 2):
            return 8
        elif (j == 3):
            return 9


def displayCanvas(board, turn):
    for i in range(70, 280, 70):           
        for j in range(70, 280, 70):
            tk.Label(window, text=board[num(j/70, i/70)], font=("微軟正黑體", 24)).place(x=i-50, y=j-50, width=50, height=50)
    getPlayerMove(board, turn)



def getPlayerMove(board, turn):
    
    global place, buttonB, turn2, userInput
    place = tk.StringVar()
    
    turn2 = tk.Label(window, text="Turn :\n "+turn, font=("微軟正黑體", 20), bg="light yellow", fg="dark blue")
    turn2.place(x=240, y=10)
    userInput = tk.Entry(textvariable=place, font=("微軟正黑體", 20), width=10)
    userInput.place(x=240, y=100)
    buttonB = tk.Button(window, text="= Confirm =", command=partial(checkPlayerMove, board, turn), font=("微軟正黑體", 15))
    buttonB.place(x=240, y=150)

def checkPlayerMove(board, turn):
    global move
    if place.get() not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(place.get())):
        messagebox.showinfo("Error", "Please input \"1\" ~ \"9\".")
    else:
        move = int(place.get())
    if turn == "player":
        makeMove(board, playerLetter, move)
        displayCanvas(board, turn)
        if isWinner(board, playerLetter):
            messagebox.showinfo("Win", "Wow! You win the computer, you are so strong!")
            os._exit(0)
        else:
            if isBoardFull(board):
                messagebox.showinfo("Tie", "Oh, the game is a tie.")
                os._exit(0)
            '''else:
                turn = "computer"'''
    '''else:
        print(1)
        # Computer's turn
        move = getComputerMove(board, computerLetter)
        makeMove(board, computerLetter, move)

        if isWinner(board, computerLetter):
            messagebox.showinfo("Lose", "Oh no! You lose the Computer. It was awful!")
            os._exit(0)
        else:
            if isBoardFull(theBoard):
                messagebox.showinfo("Tie", "Oh, the game is a tie.")
                os._exit(0)
            else:
                turn = "player"'''
                



theBoard = ["   "] * 10    
turn = whoGoFirst()            

inputPlayerXO(theBoard, turn)
window.mainloop()
