n, m = map(int, input().split())
mat = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c = tuple(map(int, input().split()))
    mat[r-1][c-1] = 1

for row in mat:
    print(*row)