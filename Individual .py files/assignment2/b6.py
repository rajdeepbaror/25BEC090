mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("row 1:", mat[1])

col2 = []
for r in range(len(mat)):
    col2.append(mat[r][2])
print("col 2:", col2)
