n = int(input())
mat = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0; num = 1
for j in range(n-1, -1, -1):
    if cnt % 2 == 0:
        for i in range(n-1, -1, -1):
            mat[i][j] = num
            num += 1
    else:
        for i in range(n):
            mat[i][j] = num
            num += 1
    cnt += 1

for row in mat:
    print(*row)