lst = [1,2,2,3,4,3]
result = []

for i in lst:
    if i not in result:
        result.append(i)

print(result)