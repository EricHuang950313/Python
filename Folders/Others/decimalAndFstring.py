import decimal as de 

print("==No Scientific notation==")
print(1e20)
print(int(1e20))
print(f"{1.234e-1:.4f}")
print()

print("==Decimal default accurate digits (including integers and decimals)==")
print(f"Value: {de.getcontext().prec}")
print()

d1 = de.Decimal("12345678901234567890.12345678901234567890")
d2 = de.Decimal("1E-20")

print("==Print_A==")
print(f"{d1}+{d2}\n={d1+d2}")
print()

print("==Set Decimal accurate digits (including integers and decimals)==")
de.getcontext().prec = 50
print(f"Value: {de.getcontext().prec}")
print()

print("==Print_B==")
print(f"{d1}+{d2}\n={d1+d2}")
print()