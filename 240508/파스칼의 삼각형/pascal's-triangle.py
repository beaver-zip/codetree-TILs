n = int(input())
mat = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    mat[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        mat[i][j] = mat[i-1][j-1] + mat[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(mat[i][j], end = ' ')
    print()