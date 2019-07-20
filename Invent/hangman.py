import random
# Prepare
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
HANGMAN_PICS = ['''  
+---+		
    |		
    |		
    |		
    ===''', '''		
+---+		
O   |		
    |		
    |		
    ===''', '''		
+---+		
O   |		
|   |		
    |		
    ===''', '''		
 +---+		
 O   |		
/|   |		
     |		
     ===''', '''		
 +---+		
 O   |		
/|\  |		
     |		
     ===''', '''		
 +---+		
 O   |		
/|\  |		
/    |		
     ===''', '''		
 +---+		
 O   |		
/|\  |		
/ \  |		
     ===''']


# Functions
def getRandomWord(wordlist):
    # Return the correct word.
    wordIndex  = words[random.randint(0, (len(wordlist)-1))]    
    return wordIndex


def displayBoard(missedLetters, correctLetters, secretWords):
    # Print the ASC2 picture(Hangman)
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    # Print missedletters
    print("MissedLetters:", end="")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    # Check the word and blanks
    blanks = "_" * len(secretWords)
    for i in range(len(secretWords)):
        if secretWords[i] in correctLetters:
            blanks = blanks[:i] + secretWords[i] + blanks[i+1:]
    
    # Print the blank and correctwords
    for letter in blanks:
        print(letter, end=" ")
    print()


def getGuess(alreadyGuess):
    # Check user's answer
    while True:
        print()
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuess:
            print("You have already guess that letter.Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("print a \"English Letter\"")
        else:
            return guess


def playAgain():
    # Ask user to play again or not
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


# Main Program
print("=== H A N G M A N ===")
missedLetters = ""
correctLetters = ""
secrectWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secrectWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secrectWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secrectWord)):
            if secrectWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print()
            print(secrectWord)
            print("Yes, the screct word is "+ secrectWord +"! You won!!!")
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS)-1:
            print("You have run out of guesses!\nAfter " + str(len(missedLetters)) + 
                "missed guess and " + str(len(correctLetters)) + "correct guesses, " +
                "the word was " + secrectWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secrectWord = getRandomWord(words)
        else:
            break