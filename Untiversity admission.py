marks = float(input("Enter 12th percentage: "))
maths = input("Studied Mathematics? (yes/no): ")
entrance = float(input("Enter entrance exam score: "))

if marks < 75:
    print("Not Eligible: Minimum 75% required in 12th.")
elif maths.lower() != "yes":
    print("Not Eligible: Mathematics is required.")
elif entrance < 80:
    print("Not Eligible: Entrance score must be at least 80.")
else:
    print("Eligible for Admission")