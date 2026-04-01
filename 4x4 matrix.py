matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])

row_sum = np.sum(matrix, axis=1)
col_sum = np.sum(matrix, axis=0)

print("Row Sum:", row_sum)
print("Column Sum:", col_sum)