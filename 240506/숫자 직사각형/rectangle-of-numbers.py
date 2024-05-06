n, m = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        mat[i][j] = num
        num += 1

for row in mat:
    print(*row)