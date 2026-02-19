cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Membership discount
if membership.lower() == "silver":
    discount = 5
elif membership.lower() == "gold":
    discount = 10
elif membership.lower() == "platinum":
    discount = 15

# Festival discount
if festival.lower() == "yes":
    discount = max(discount, 20)

final_amount = cart_value - (cart_value * discount / 100)

print("Discount Applied:", discount, "%")
print("Final Payable Amount:", final_amount)