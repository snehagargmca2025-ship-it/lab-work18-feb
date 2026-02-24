n = int(input())
a, b = 0, 1
i = 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1