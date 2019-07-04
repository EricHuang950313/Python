try:    
    import random
    A = 0
    B = 0
    c = 0
    num = ("123456789")
    p = (random.sample(num,4))
    computer = (p[0],p[1],p[2],p[3])
    player = input("請輸入四個不同的數字:")
    digit = False
    while not digit:
        if (player[0] == player[1]) or (player[0] == player[2]) or (player[0] == player[3]) or (player[1] == player[2]) or (player[1] == player[3]) or (player[2] == player[3]) or (player[0] == player[1] == player[2]) or (player[0] == player[1] == player[3]) or(player[0] == player[2] == player[3]) or (player[1] == player[2] == player[3]) or (player[0] == player[1] == player[2] == player[3]):
            player = input("請再輸入四個不同的數字一次:")
        else:
            break
    while (player != computer):
        A = 0
        B = 0
        for i in range(4):
            if computer[i] == player[i]:
                A += 1
            else:
                for j in range(4):
                    if player[i] == computer[j]:
                        B += 1
        print("{}A{}B".format(A, B))
        c += 1
        if (A == 4):
            break
        if c == 10:
            break
        player = input("請輸入四個不同的數字:")
        digit = False
        while not digit:
            if (player[0] == player[1]) or (player[0] == player[2]) or (player[0] == player[3]) or (player[1] == player[2]) or (player[1] == player[3]) or (player[2] == player[3]) or (player[0] == player[1] == player[2]) or (player[0] == player[1] == player[3]) or(player[0] == player[2] == player[3]) or (player[1] == player[2] == player[3]) or (player[0] == player[1] == player[2] == player[3]):
                player = input("請再輸入四個不同的數字一次:")
            else:
                break
    print("The Answer Is {}{}{}{}".format(p[0],p[1],p[2],p[3]))
    abc = input("")
except BaseException:
    print("Error, Please close the program, and open it again.")
    abc = input("")