Aa, Ba, Ca = input().split()
Ab, Bb, Cb = input().split()
Aa, Ba, Ca, Ab, Bb, Cb = int(Aa), int(Ba), int(Ca), int(Ab), int(Bb), int(Cb)
n = int(input())
biggest = -20000000000000000000000000000000

for i in range(0, n+1):
    Xa, Xb = i, n-i
    Ya = Aa*Xa*Xa + Ba*Xa + Ca
    Yb = Ab*Xb*Xb + Bb*Xb + Cb
    if Ya+Yb > biggest:
        biggest = Ya+Yb
print(biggest)