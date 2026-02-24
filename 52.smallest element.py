lst = list(map(int, input().split()))
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print(smallest)