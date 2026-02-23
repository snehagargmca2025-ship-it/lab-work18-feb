cart = [1200, 2500, 1200, 1800]

cart = list(set(cart))
total = sum(cart)

if total > 5000:
    total *= 0.9   # 10% discount

total *= 1.18      # 18% GST

print("Final Payable Amount:", total)