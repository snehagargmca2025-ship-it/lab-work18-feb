def unique_elements(lst):
    return list(set(lst))

lst = list(map(int, input().split()))
print(unique_elements(lst))