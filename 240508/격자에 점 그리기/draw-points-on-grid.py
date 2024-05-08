n, m = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    mat[r-1][c-1] = num
    num += 1

for row in mat:
    print(*row)