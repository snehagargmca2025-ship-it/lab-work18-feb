a = int(input())
b = int(input())
c = int(input())
d = int(input())

greatest = a
if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print(greatest)