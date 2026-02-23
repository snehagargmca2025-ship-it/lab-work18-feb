temps = [38, 42, 46, 29, 41]

print("Hottest:", max(temps))
print("Coldest:", min(temps))

alerts = ["Heat Alert" if t > 45 else t for t in temps]
extreme_days = len([t for t in temps if t > 40])

print("Temperature Status:", alerts)
print("Extreme Days:", extreme_days)