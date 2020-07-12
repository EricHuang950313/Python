import random, time, threading, os
def counter():
    while not time.time() - t > 5:
        int(time.time() - t)
        time.sleep(1)
    print("超過五秒")
    a = input("")
    os._exit(1)

print("---猜拳---")
print("您要出剪刀(1)石頭(2)布(3)")
t = float(time.time())

def psr():
    player = input()
    com = random.choice(["剪刀", "石頭", "布"])
    if com == "剪刀":
      if player == "1":
            print("電腦出：剪刀")
            print("平手")
      elif player == "2":
            print("電腦出：剪刀")
            print("你贏了")
      elif player == "3":
            print("電腦出：剪刀")
            print("你輸了")
      else:
            print("您要出 剪刀(1) 石頭(2) 布(3)")
    elif com == "石頭":
      if player == "1":
            print("電腦出：石頭")
            print("你輸了")
      elif player == "2":
            print("電腦出：石頭")
            print("平手")
      elif player == "3":
            print("電腦出：石頭")
            print("你贏了")
      else:
            print("您要出 剪刀(1) 石頭(2) 布(3)")
    elif com == "布":
      if player == "1":
            print("電腦出：布")
            print("你贏了")
      elif player == "2":
            print("電腦出：布")
            print("你輸了")
      elif player == "3":
            print("電腦出：布")
            print("平手")
      else:
            print("您要出 剪刀(1) 石頭(2) 布(3)")
    a = input("")
    os._exit(1)

tp = threading.Thread(target=psr)
ts = threading.Thread(target=counter)
tp.start()
ts.start()
