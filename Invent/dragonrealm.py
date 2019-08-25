import random
import time

def info():
    print()
    print('''You are in a land full of dragons. In front of you,		
you see two caves. In one cave, the dragon is friendly		
and will share his treasure with you. The other dragon		
is greedy and hungry, and will eat you on sight.''')
    print()


def ChooseCave():
    cave = ""
    while (cave != "1") and (cave != "2"):
        print("Which cave will you go into?")
        cave = input()
    return cave


def CheckCave(user):
    print("You approach the cave...")
    time.sleep(2)
    print()
    print("It is dark and spooky...")
    time.sleep(2)
    print()
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)
    print()
    
    cave = random.randint(1, 2)
    if (user == str(cave)):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

playagain = "yes"
while playagain =="yes":
    info()
    user = ChooseCave()
    CheckCave(user)

    print("Do you want to play again?")
    playagain = input()