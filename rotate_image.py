def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()

# Input
mat = [[1,2,3],[4,5,6],[7,8,9]]
rotate(mat)
print(mat)
# Output: [[7,4,1],[8,5,2],[9,6,3]]
