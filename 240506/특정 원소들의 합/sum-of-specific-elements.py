mat = []
total = 0

for _ in range(4):
    arr = list(map(int, input().split()))
    mat.append(arr)

for i in range(4):
    for j in range(i+1):
        total += mat[i][j]
    
print(total)