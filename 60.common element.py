lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

common = []
for i in lst1:
    if i in lst2 and i not in common:
        common.append(i)

print(common)