units = int(input("Enter electricity units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ")

# Bill calculation
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

# Senior citizen discount
if senior.lower() == "yes":
    discount = bill * 0.10
    bill -= discount

print("Total Electricity Bill = ₹", bill)