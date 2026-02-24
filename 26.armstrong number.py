n = int(input())
temp = n
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

temp = n
armstrong = 0

while temp > 0:
    digit = temp % 10
    armstrong += digit ** digits
    temp //= 10

if armstrong == n:
    print("Armstrong")
else:
    print("Not Armstrong")