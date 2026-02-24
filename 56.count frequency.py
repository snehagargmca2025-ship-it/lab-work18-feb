lst = list(map(int, input().split()))
freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)