salaries = [20000, 55000, 80000, 15000, 60000]

min_wage = 18000
salaries = [s for s in salaries if s >= min_wage]

salaries = [s*1.05 if s > 50000 else s for s in salaries]

salaries.sort(reverse=True)

print("Top 3 Salaries:", salaries[:3])