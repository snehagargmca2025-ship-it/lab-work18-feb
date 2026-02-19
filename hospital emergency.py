age = int(input("Enter patient age: "))
condition = input("Enter condition (critical/moderate/normal): ").lower()

if condition == "critical":
    priority = "Critical"
elif condition == "moderate":
    if age > 65:
        priority = "Critical (Upgraded Priority)"
    else:
        priority = "Moderate"
else:
    priority = "Normal"

print("Patient Priority:", priority)