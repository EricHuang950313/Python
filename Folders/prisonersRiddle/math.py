amount = int(input("Prisoners amount:"))
total = 0
for i in range(int(amount/2)+1, amount+1):
  total += 1/i
print(f"P(success)=1-{total:.2f}={1-(total):.2f}")