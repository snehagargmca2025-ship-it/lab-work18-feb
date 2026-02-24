lst = list(map(int, input().split()))
result = [0 if x < 0 else x for x in lst]
print(result)