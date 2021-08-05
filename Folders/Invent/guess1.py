import random
import os

class Guess():
    num = 0
    def __init__(self, username, dif):
        Guess.num = random.randint(1, 80)
        self._username = username
        self._dif = dif

    def times(self, dif):
        self._dif = dif
        
        if (self._dif == 1):
            return 9
        elif (self._dif == 2):
            return 7
        else:
            return 5


    def guess(self, dif):
        self._dif = dif
        for Guess.guesstake in range(self._dif):
            try:
                self.userinput = int(input("Take a guess, " + self._username + ": "))
            except BaseException:
                print("Error! ...... \"What did you do?\"......")
                os._exit(0)
            if self.userinput > Guess.num:
                print("Your guess is too high.")
            if self.userinput < Guess.num:
                print("Your guess is too low.")
            if self.userinput == Guess.num:
                print("Your are \"Correct\"!!!")
                print("You guess "+str(Guess.guesstake+1)+" times.")
                os._exit(0)
        print("The answer is " + str(Guess.num) + ", you can be better.")

if __name__ == "__main__":
    print("Hello! What's your name?")
    try:
        username = input()  
    except BaseException:
        print("Error! ...... \"What did you do?\"......")
        os._exit(0)
    
    print("How difficult do you want? \"Please input 1~3 \": ", end="")

    try:
        dif = int(input())
        while not (0 < dif < 4):
            dif = int(input("1 / 2 / 3:"))    
    except BaseException:
        print("Error,Please input...... \"1~3 next time\" ......")
        os._exit(0)
                

    Cl = Guess(username, dif)

    dif = Cl.times(dif)
    print("Well," + username + ",I'm taking a number between 1 and 80.")
    Cl.guess(dif)