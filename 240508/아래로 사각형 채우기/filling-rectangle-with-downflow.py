n = int(input())
mat = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for j in range(n):
    for i in range(n):
        mat[i][j] = num
        num += 1

for row in mat:
    print(*row)