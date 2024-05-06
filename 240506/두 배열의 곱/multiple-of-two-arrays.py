mat3 = [[0 for _ in range(3)] for _ in range(3)]
mat1, mat2 = [], []

for _ in range(3):
    arr = list(map(int, input().split()))
    mat1.append(arr)
input()
for _ in range(3):
    arr = list(map(int, input().split()))
    mat2.append(arr)

for i in range(3):
    for j in range(3):
        mat3[i][j] = mat1[i][j] * mat2[i][j]

for row in mat3:
    print(*row)