s = input()
 
n = len(s)
total = 0
 
for i in range(n):
 if s[i] == "1":
   total += 1*(10**(n-1))
   n -= 1
 if s[i] == "2":
   total += 2*(10**(n-1))
   n -= 1
 if s[i] == "3":
   total += 3*(10**(n-1))
   n -= 1
 if s[i] == "4":
   total += 4*(10**(n-1))
   n -= 1
 if s[i] == "5":
   total += 5*(10**(n-1))
   n -= 1
 if s[i] == "6":
   total += 6*(10**(n-1))
   n -= 1
 if s[i] == "7":
   total += 7*(10**(n-1))
   n -= 1
 if s[i] == "8":
   total += 8*(10**(n-1))
   n -= 1
 if s[i] == "9":
   total += 9*(10**(n-1))
   n -= 1
 if s[i] == "0":
   total += 10*(10**(n-1))
   n -= 1
 
print(total)

