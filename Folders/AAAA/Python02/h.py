d1 = {"id": 12, "name": "Eric", "age": 12}
d2 = dict(id=12, name="Eric", age=12)

print(d1["id"])
print(d2["name"])

print(len(d1))

d2["name"] = "score"
print(d2)

del d1["id"]
print(d1)

d2.clear()
print(d2)

print("a" in d1.keys())
print(12 in d1.values())

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

print(d1 == d2)
print(d1 != d2)