lst = list(map(int, input().split()))
largest = second = float('-inf')

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)