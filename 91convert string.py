s = input().split()
res = []
for word in s:
    res.append(word[0].upper() + word[1:].lower())
print(" ".join(res))