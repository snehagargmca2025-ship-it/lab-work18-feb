base = int(input())
exp = int(input())
result = 1

for _ in range(exp):
    result *= base

print(result)