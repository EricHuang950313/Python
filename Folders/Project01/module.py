import ma
over = False
correct = False
print("輸入1是求中點數")
print("輸入2是科學記號")
print("輸入3是指數")
print("輸入4是離開")
user = input("")
while not over:
    if user == "1":
        print("===求中點數===")
        n1 = int(input("n1:"))
        n2 = int(input("n2:"))
        x = ma.midpoint(n1, n2)
        print(x)

    elif user == "2":
        while not correct:
            print("===科學記號===")
            num = float(input("n1:"))


            if num < 1 or num >= 10: 
                while not correct:
                    print("科學記號不符規定")
                    break
            else:
                correct = True
                s = int(input("n2:"))
                y = ma.ScNo(num, s)
                print(y)

    elif user == "3":
        print("===指數===")
        d = int(input("n1:"))
        i = int(input("n2:"))
        z = ma.Ef(d, i)
    
        print(d, "的", i, "次方是", z)


    elif user == "4":
        break

    else:
        print("輸入錯誤")
    user = input("")  