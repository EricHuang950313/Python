import random

print("Hello! What's your name?")
username = input()

guesstake = 0
num = random.randint(1, 50)

print("Well," + username + " I'm taking a number between 1 and 50")

for guesstake in range(6):
    userinput = int(input("Take a guess, " + username + ": "))

    if userinput > num:
        print("Your guess is too high.")

    if userinput < num:
        print("Your guess is too low.")

    if userinput == num:
        print("Your are \"Correct\"!!!")
        break

if userinput == num:
    print("You guess my number in " + str(guesstake + 1) + " times.")
if userinput != num:
    print("Nope. The number I was thinking of was " + str(num) + " .") 