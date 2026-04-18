matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = matrix.copy()
matrix.append(10) #only independent for the outer list.
matrix[0].append(10)

print(matrix)
