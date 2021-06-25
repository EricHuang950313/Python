s = set() # if data is clear, must use funcion "set()"
t = {1, 2, "abc", (10, 20)}
u = set({1, 22, "abc", (10, 20)})
v = set([1, 22, "abc", (10, 20)])
frozen_set = frozenset({1, 22, "abc", (10, 20)})
print(s, t, u, v, frozen_set)

print(len(s))
s.add(3)
print(s)

s.update((5, 20))
print(s)

s.clear()
print(s)

print(1 in s)