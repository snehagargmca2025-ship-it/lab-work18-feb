points = [25, -5, 40, 30, 15]

points = [p if p > 0 else 0 for p in points]
points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Winner:", winner)
print("Runner-up:", runner_up)
print("Leaderboard:", points)