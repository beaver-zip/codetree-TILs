n, m = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]
num = 1
cnt = 0

while True:
    for i in range(cnt+1):
        try:
            mat[i][cnt-i] = num
            num += 1
        except: 
            continue
    cnt += 1
    if mat[-1][-1] != 0: 
        break

for row in mat:
    print(*row)