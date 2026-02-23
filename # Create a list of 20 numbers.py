# Create a list of 20 numbers
numbers = [5, 8, 3, 5, 9, 1, 5, 7, 2, 5, 6, 4, 5, 10, 11, 5, 12, 13, 5, 14]

print("Original List:")
print(numbers)

# Take user input
num = int(input("Enter a number to delete its extra occurrences: "))

# Check if number exists in list
if num in numbers:
    first_index = numbers.index(num)  # Get first occurrence index
    
    # Traverse list in reverse to safely remove elements
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == num and i != first_index:
            numbers.pop(i)
    
    print("Updated List:")
    print(numbers)
else:
    print("Number not found in the list.")