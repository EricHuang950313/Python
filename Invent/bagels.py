import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNumbers():
    num_range = list(range(1, 11))
    random.shuffle(num_range)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(num_range[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "You got it! Good job!"
    
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secretNum[i]:
            clues += ["Fermi"]
        elif guess[i] in secretNum:
            clues += ["Pico"]
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


def isDigit(guess):
    if guess == "":
        return False
    
    for i in guess:
        if i not in "0 1 2 3 4 5 6 7 8 9".split():
            return False
    return True


# The rules
print()
print("I'm taking a number of a %s-digit number. Try to guess what it is." %(NUM_DIGITS))
print()
print("The clues I give are......")
print("When I say:      That means:")
print("Bagels           None of the digit is correct.")
print("Pico             One digit is correct, but in the wrong position.")
print("Fermi            One digit is correct and in right position.")

while True:
    secretNum = getSecretNumbers()
    print("I have thought up a number. You have %s guesses to get it." %(MAX_GUESS))
    print()

    guessTaken = 1
    while guessTaken < MAX_GUESS:
        guess = ""
        while len(guess) != NUM_DIGITS or not isDigit(guess):
            print("guess #%s " %(guessTaken), end="")
            guess = input()
        
        print(getClues(guess, secretNum))
        guessTaken += 1
        if guess == secretNum:
            break
        if guessTaken > MAX_GUESS:
            print("You ran out of guesses. The Answer is %s." %(secretNum))
            break
    print("Do you want to play again ?")
    if not input().lower().startswith("y"):
        break