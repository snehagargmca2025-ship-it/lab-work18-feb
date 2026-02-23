marks = [78, 95, 102, -5, 88, 95]

valid_marks = [m for m in marks if 0 <= m <= 100]

average = sum(valid_marks) / len(valid_marks)

topper = max(valid_marks)

print("Valid Marks:", valid_marks)
print("Average:", average)
print("Topper:", topper)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)