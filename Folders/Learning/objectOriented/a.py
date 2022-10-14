import math

circle_radius = [1, 2, 3, 4, 5]

print("area")
for radius in circle_radius:
    area = math.pi * radius * radius

    print("{:.2f}".format(area), end = " ")
print("\nperimeter")
for radius in circle_radius:
    perimeter = 2 * math.pi * radius

    print("{:.2f}".format(perimeter), end = " ")
