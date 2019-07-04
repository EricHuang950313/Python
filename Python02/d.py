s1 = "KLAY"
s2 = "Consins"
s3 = "stephen curry"
s4 = " Kevin Durant "

s_new = s3.capitalize()
print(s_new)
print()

s_new = s3.title()
print(s_new)
print()

s_new = s3.upper()
print(s_new)
print()

s_new = s1.lower()
print(s_new)
print()

s_new = s4.swapcase()
print(s_new)
print()

s_new = s3.replace("stephen", "seth")
print(s_new)
print()

s_new = s4.lstrip()
print(s_new)
print()

s_new = s4.rstrip()
print(s_new)
print(id(s_new))
print()

s_new = s4.strip()
print(s_new)
print(id(s_new))
print()