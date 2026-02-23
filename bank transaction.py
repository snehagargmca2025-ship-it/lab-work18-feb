transactions = [15000, -5000, 20000, -12000, 8000]

balance = sum(transactions)
largest_withdrawal = min(transactions)

big_deposits = len([t for t in transactions if t > 10000])

print("Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", big_deposits)