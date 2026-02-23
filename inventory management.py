stock = [0, 5, 20, 8, 50]

stock = [s for s in stock if s > 0]

stock = [s+50 if s < 10 else s for s in stock]

total_inventory = sum(stock)

print("Stock:", stock)
print("Total Inventory:", total_inventory)