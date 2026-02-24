p, r, t = map(float, input().split())
ci = p * ((1 + r / 100) ** t) - p
print(ci)