arr = np.random.rand(10)
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Original:", arr)
print("Normalized:", normalized)