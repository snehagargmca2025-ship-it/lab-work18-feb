d = eval(input())
print(dict(sorted(d.items(), key=lambda x: x[1])))