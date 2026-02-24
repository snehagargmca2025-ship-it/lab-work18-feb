s = input()
vowels = "aeiouAEIOU"
res = ""
for ch in s:
    res += "*" if ch in vowels else ch
print(res)