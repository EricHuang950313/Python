import shape as sh

circle_radius = [1, 2, 3, 4, 5]
circles = []

for radius in circle_radius:
    c = sh.Circle(radius)
    circles += [c]

print("area")
for c in circles:
    print("{:.2f}".format(c.get_area()), end=" ")

print("\nperimeter")
for c in circles:
    print("{:.2f}".format(c.get_perimeter()), end=" ")