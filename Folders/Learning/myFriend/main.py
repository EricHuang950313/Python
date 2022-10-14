import process.friend as fr

file = fr.open_file()

if file is None:
    exit()
print("==== 歡迎使用通訊錄程式 v1.0 ====")
abc123 = input("")
while True:
    print("請選擇下列功能：\n")
    print("1) Add The New Friend")
    print("2) Find Your Friend By Name")
    print("3) List Your Friend Out")
    print("4) View The Version")
    print("5) Close")
    op = input("輸入選項：")

    if op == "1":
        try:
            name, gender, age, tel = input("請輸入朋友姓名、性別(1.男、2.女)、年齡、電話，資料以空白分隔\n").split()
            gender = int(gender)
            age = int(age)
        except ValueError:
            print("資料格式錯誤\n")
        else:
            fr.add(file, name, gender, age, tel)
            print("Add your friend successfully")

    elif op == "2":
        name = input("請輸入朋友姓名 \n")
        friend_data = fr.find(file, name)
        if not friend_data:
            print(name + "is not find")
        else:
            print(friend_data, "\n")

    elif op == "3":
        fr.iterate_start(file)
        while True:
            my_friend = fr.iterate_next(file)
            if not my_friend:
                break

            print(my_friend)
        print()

    elif op == "4":
        print("version:")
        print("v0.1 (Test) ------ 2018/09/02")
        print("程式創立")
        print("v0.2 ------2018/09/08")
        print("加入 3、4、5 的功能")
        print("v1.0 ------2018/09/09")
        print("加入 2 的功能")

    elif op == "5":
        fr.close_file(file)
        break

    else:
        print("Your Option is Wrong")
