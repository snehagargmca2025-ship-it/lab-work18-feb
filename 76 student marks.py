n = int(input())
d = {}
for _ in range(n):
    name, marks = input().split()
    d[name] = int(marks)

topper = max(d, key=d.get)
print(topper)