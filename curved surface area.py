import math

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

curved_surface_area = 2 * math.pi * r * h
total_surface_area = 2 * math.pi * r * (r + h)
volume = math.pi * r * r * h

print("Curved Surface Area =", curved_surface_area)
print("Total Surface Area =", total_surface_area)
print("Volume =", volume)