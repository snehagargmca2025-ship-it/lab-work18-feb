lst = list(map(int, input().split()))
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)