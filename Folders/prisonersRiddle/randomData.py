import random

 
if __name__ == "__main__":
  amount = int(input("Prisoners amount:"))
  n = 100000
  pardoned = 0
  prisoners = list(range(amount))
  for round_not_used in range(n):
    random.shuffle(prisoners)
    for prisoner in range(amount):
      nextOne = prisoner
      for fifty_not_used in range(int(amount/2)):
        inside = prisoners[nextOne]
        if inside == prisoner:
          break
        nextOne = inside
      else:
        break
    else:
      pardoned += 1
  print(f"P(success)={(pardoned / n * 100):.1f}%")