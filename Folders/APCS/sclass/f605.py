amount, d = input().split()
amount, d = int(amount), int(d)
final_amount, final_price = 0, 0
for i in range(amount):
    user = 0
    user = input().split()
    user = list(map(int, user))
    if max(user)-min(user) >= d:
        final_amount += 1
        final_price += sum(user)/3
print(final_amount, int(final_price))