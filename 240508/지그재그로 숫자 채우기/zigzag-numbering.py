# for문  j -> i if문

n, m = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]

num = 0
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            mat[i][j] = num
            num += 1
    else:
        for i in range(n-1, -1, -1):
            mat[i][j] = num
            num += 1

for row in mat:
    print(*row)