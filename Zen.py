with open("ZenRead.txt", mode="r", encoding="utf-8") as file:
  for count, line in enumerate(file):
      print(line)
      if (count+1) % 2 == 0:
        print()