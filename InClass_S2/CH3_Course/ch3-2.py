letter = ['q','Q','a','A','z','Z','w','W','s','S','x','X',
          'e','E','d','D','c','C']
def check_letter(place):
    flag = place in letter
    return flag
def update_map(mymap, place, ch):
    if place in ['q','Q']:
        mymap[0][0] = ch
        letter.remove('q')
        letter.remove('Q')
    if place in ['a','A']:
        mymap[1][0] = ch
        letter.remove('a')
        letter.remove('A')
    if place in ['z','Z']:
        mymap[2][0] = ch
        letter.remove('z')
        letter.remove('Z')
    if place in ['w','W']:
        mymap[0][1] = ch
        letter.remove('w')
        letter.remove('W')
    if place in ['s','s']:
        mymap[1][1] = ch
        letter.remove('s')
        letter.remove('S')
    if place in ['x','X']:
        mymap[2][1] = ch
        letter.remove('x')
        letter.remove('X')
    if place in ['e','E']:
        mymap[0][2] = ch
        letter.remove('e')
        letter.remove('E')
    if place in ['d','D']:
        mymap[1][2] = ch
        letter.remove('d')
        letter.remove('D')
    if place in ['c','C']:
        mymap[2][2] = ch
        letter.remove('c')
        letter.remove('C')
    return mymap

def check_game(mymap,i):
    if i%2 == 0:
        chara = 'X'
    else:
        chara = 'O'
    win1cond = mymap[0][0] == chara and mymap[0][1] == chara and mymap[0][2] == chara
    win2cond = mymap[1][0] == chara and mymap[1][1] == chara and mymap[1][2] == chara
    win3cond = mymap[2][0] == chara and mymap[2][1] == chara and mymap[2][2] == chara
    win4cond = mymap[0][0] == chara and mymap[1][0] == chara and mymap[2][0] == chara
    win5cond = mymap[0][1] == chara and mymap[1][1] == chara and mymap[2][1] == chara
    win6cond = mymap[0][2] == chara and mymap[1][2] == chara and mymap[2][2] == chara
    win7cond = mymap[0][0] == chara and mymap[1][1] == chara and mymap[2][2] == chara
    win8cond = mymap[0][2] == chara and mymap[1][1] == chara and mymap[2][0] == chara
    wincond = win1cond or win2cond or win3cond or win4cond or win5cond or win6cond or win7cond or win8cond

    if wincond and i%2==0:
        flag_end = 1
    if wincond and i%2==1:
        flag_end = 2
    if (not wincond) and len(letter) == 0:
        flag_end = 3
    if (not wincond) and len(letter) > 0:
        flag_end = 0
    return flag_end

def demoOOXX():
    # step1 =>make a map
    mymap = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    i=0 #順序(x先下:/2==0)
    while True:
        #step2  =>user input
        if i%2 == 0: #順序(x先下:/2==0)
            placeX = input('X 手請下 :')
            flag = check_letter(placeX)
        else :
            placeO = input('O 手請下 :')
            flag = check_letter(placeO)

        #step3 =>check the letter
        if flag == False:
            print('無效字母')
            print(letter)
        else :
            if i%2==0:
                place = placeX
                ch = 'X'
            else :
                place = placeO
                ch = 'O'

            #step4  =>upload(show) the map
            mymap = update_map(mymap,place,ch)
            print(mymap[0][:])
            print(mymap[1][:])
            print(mymap[2][:])

            #step5  =>check if somebody win, lose or tie
            flag_end = check_game(mymap,i)
            if flag_end == 1:
                print('X 手勝利 !')
                return
            if flag_end == 2:
                print('O 手勝利 !')
                return
            if flag_end == 3:
                print('平手 !')
                return
            i+=1 #順序+1

demoOOXX()