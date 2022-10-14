a = int(input(""))
def make_pi(number):
    tick = 0
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < m * t:
            tick += 1
            if tick > number:
                break
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

digits = make_pi(a)
next(digits)
pi = "3."
for i in digits:
    pi += str(i)

print(pi)
b = input("")
