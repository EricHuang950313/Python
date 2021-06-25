man = [
'''
   |-----|
          |
         |
         |
         |
         |
         |
_____ | _____
''',

'''
   |-----|
   O     |
         |
         |
         |
         |
         |
_____ | _____
''',
'''
   |-----|
   O     |
   l     |
   l     |
         |
         |
         |
_____ | _____
''',
'''
   |-----|
   O     |
   l     |
   l     |
   l     |
         |
         |
_____ | _____
''',
'''
   |-----|
   O     |
  \l/    |
   l     |
   l     |
         |
         |
_____ | _____
''',
'''
   |-----|
   O     |
  \l/    |
   l     |
   l     |
  /      |
         |
_____ | _____
''',
'''
   |-----|
   O     |
  \l/    |
   l     |
   l     |
  / \    |
         |
_____ | _____
'''
]
import random
word = random.choice(["apple","banana","watermelon","guava","orange"])
gameover = False
time = 0
count = 0

correct = ""

while not gameover:
    underscores = ""
    for i in range(len(word)):
        if word[i] in correct:
            #如果 A 在 correct中，就......
            underscores += word[i]
            underscores += " "
        else:
            #毫無目的的加底線
            underscores += "_ "
        #while  後面是條件 ( gameover )
        #for  後面是範圍 ( range )
    print(underscores)
    guess = input("猜一個字母：").lower()
    if guess in word:
        print("猜到")
        #  a)
        correct += guess
        #  b)
        all_correct = True
        for x in word:
            # print(x)是apple
            if x not in correct:
                #如果 x 不在 correct
                all_correct = False
                break
        if all_correct:
             #全部的 x 都在 correct
             #all_correct = True
             print("===========================")
             print("You Win!!!!!!!!!!!!!!!!!!!!")
             print("===========================")
             z = input("")
             gameover = True
    else:
        print("沒猜到")
        time = time + 1
        print(man[time])
        if time == 6:
            print("=========")
            print("Game Over")
            print("=========")
            z = input("")
            gameover = True