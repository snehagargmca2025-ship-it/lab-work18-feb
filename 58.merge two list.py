lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

merged = []
for i in lst1 + lst2:
    if i not in merged:
        merged.append(i)

print(merged)