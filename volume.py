import math

r = float(input("Enter radius of cone: "))
h = float(input("Enter height of cone: "))

l = math.sqrt(r*r + h*h)   # slant height

curved_surface_area = math.pi * r * l
total_surface_area = math.pi * r * (r + l)
volume = (1/3) * math.pi * r * r * h

print("Curved Surface Area =", curved_surface_area)
print("Total Surface Area =", total_surface_area)
print("Volume =", volume)