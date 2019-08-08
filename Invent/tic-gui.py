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
    return board[move] == " "


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
    elif three == [2, 4]:
        return 1
    elif three == [2, 6]:
        return 3
    elif three == [4, 8]:
        return 7
    elif three == [6, 8]:
        return 3
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


# ---< GUI Start >--- #


def inputPlayerXO(board):
    # ask player to choose that player want to be "O" or "X"

    global label, ButtonO,ButtonX 

    label = tk.Label(window, text="Which do you want to be, \"O\" or \"X\"?", bg="light yellow", font=("微軟正黑體", 16))
    label.place(x=50, y=5)
    ButtonO = tk.Button(window, text="O", command=partial(O, board), fg="blue", font=("微軟正黑體", 30))
    ButtonO.place(x=140, y=60, width=60, height=60)
    ButtonX = tk.Button(window, text="X", command=partial(X, board), fg="red", font=("微軟正黑體", 30))
    ButtonX.place(x=240, y=60, width=60, height=60)
    

def O(board):
    global playerLetter, computerLetter
    
    playerLetter = "O"
    computerLetter = "X"

    
    LabelP = tk.Label(window, text="You : "+ playerLetter, fg="Blue", bg="light yellow", font=("微軟正黑體", 36, "bold"))
    LabelP.place(x=132, y=150)
    LabelC = tk.Label(window, text="Computer : "+ computerLetter,fg="Red", bg="light yellow", font=("微軟正黑體", 15))
    LabelC.place(x=155, y=223)
    if turn == "player":
        LabelF = tk.Label(window, text="Go first : "+ turn, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.place(x=127, y=260)
    else:
        LabelF = tk.Label(window, text="Go first : "+ turn, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.place(x=110, y=260)
    window.update()
    window.after(3000)
    label.destroy()
    ButtonO.destroy()
    ButtonX.destroy()
    LabelP.destroy()
    LabelC.destroy()
    LabelF.destroy()
    displayCanvas(board)


def X(board):
    global playerLetter, computerLetter
    
    playerLetter = "X"
    computerLetter = "O"

    LabelP = tk.Label(window, text="You : "+ playerLetter, fg="Blue", bg="light yellow", font=("微軟正黑體", 36, "bold"))
    LabelP.place(x=132, y=150)
    LabelC = tk.Label(window, text="Computer : "+ computerLetter,fg="Red", bg="light yellow", font=("微軟正黑體", 15))
    LabelC.place(x=155, y=223)
    if turn == "player":
        LabelF = tk.Label(window, text="Go first : "+ turn, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.place(x=127, y=260)
    else:
        LabelF = tk.Label(window, text="Go first : "+ turn, bg="light yellow", font=("微軟正黑體", 18, "bold"))
        LabelF.place(x=110, y=260)
    window.update()
    window.after(3000)
    label.destroy()
    ButtonO.destroy()
    ButtonX.destroy()
    LabelP.destroy()
    LabelC.destroy()
    LabelF.destroy()
    displayCanvas(board)
    

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


def displayCanvas(board):
    for i in range(70, 280, 70):           
        for j in range(70, 280, 70):
            tk.Label(window, text=board[num(j/70, i/70)], font=("微軟正黑體", 24)).place(x=i-50, y=j-50, width=50, height=50)
    
    tk.Label(window, text=1, font=("微軟正黑體", 18)).place(x=260, y=20, width=25, height=25)  
    tk.Label(window, text=2, font=("微軟正黑體", 18)).place(x=300, y=20, width=25, height=25)
    tk.Label(window, text=3, font=("微軟正黑體", 18)).place(x=340, y=20, width=25, height=25)  
    tk.Label(window, text=4, font=("微軟正黑體", 18)).place(x=260, y=60, width=25, height=25)  
    tk.Label(window, text=5, font=("微軟正黑體", 18)).place(x=300, y=60, width=25, height=25)
    tk.Label(window, text=6, font=("微軟正黑體", 18)).place(x=340, y=60, width=25, height=25)  
    tk.Label(window, text=7, font=("微軟正黑體", 18)).place(x=260, y=100, width=25, height=25)  
    tk.Label(window, text=8, font=("微軟正黑體", 18)).place(x=300, y=100, width=25, height=25)
    tk.Label(window, text=9, font=("微軟正黑體", 18)).place(x=340, y=100, width=25, height=25)  
    getPlayerMove(board)


def computerMove(board, computerLetter):
    global turn
    move = getComputerMove(board, computerLetter)
    makeMove(board, computerLetter, move)
    displayCanvas(board)
    if isWinner(board, computerLetter):
        messagebox.showinfo("Lose", "Oh No! You lose the computer, it was awful.")
        os._exit(0)
    else:
        if isBoardFull(board):
            messagebox.showinfo("Tie", "Oh, the game is a tie.")
            os._exit(0)
        else:
            getPlayerMove(board)
            turn = "player"

def getPlayerMove(board):
    
    global place, buttonB, userInput, times
    place = tk.StringVar()
    
    if turn == "computer" and times == 0:
        cp = "= Start ="
        times = 1
    else:
        cp = "= Confirm ="
        times = 1
    userInput = tk.Entry(textvariable=place, font=("微軟正黑體", 20), width=10)
    userInput.place(x=240, y=150)
    buttonB = tk.Button(window, text=cp , command=partial(checkPlayerMove, board), font=("微軟正黑體", 15))
    buttonB.place(x=240, y=200)
    

def checkPlayerMove(board):
    global move
    if turn == "player":
        if place.get() not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(place.get())):
            messagebox.showinfo("Error", "Please input \"1\" ~ \"9\", or input the other space place.\nThe game will close......")
            os._exit(0)
        else:
            move = int(place.get())

        makeMove(board, playerLetter, move)
        displayCanvas(board)
        if isWinner(board, playerLetter):
            messagebox.showinfo("Win", "Wow! You win the computer, you are so strong!")
            os._exit(0)
        else:
            if isBoardFull(board):
                messagebox.showinfo("Tie", "Oh, the game is a tie.")
                os._exit(0)
            else:
                computerMove(board, computerLetter)
    else:
         computerMove(board, computerLetter)     


def main():
    # open tkinter and set the interface

    global turn, theBoard, times, window
    window = tk.Tk()
    window.title("Tic-tac-toe")
    window.geometry("450x320")
    window.configure(background="light yellow")

    theBoard = [" "] * 10    
    turn = whoGoFirst()            
    times = 0
    
    inputPlayerXO(theBoard)

    music()

    window.mainloop()

if __name__ == "__main__":
    main()
