print("Welcome to the circle calculator!")
print("This program calculate area amd circumference of the circle.")

import math

radius = float(input("Enter the radius of the circle: "))

circle_area = math.pi * (5 ** 2)
circumference = 2 * math.pi * radius

print()
print("Area: " + str(circle_area))
print("circumference: " + str(circumference))