l = float(input("Enter length of cuboid: "))
b = float(input("Enter breadth of cuboid: "))
h = float(input("Enter height of cuboid: "))

curved_surface_area = 2 * h * (l + b)  # lateral surface area
total_surface_area = 2 * (l*b + b*h + l*h)
volume = l * b * h

print("Curved Surface Area =", curved_surface_area)
print("Total Surface Area =", total_surface_area)
print("Volume =", volume)