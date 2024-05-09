dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
x, y = 0, 0

for _ in range(int(input())):
    dir_char, n = input().split()
    n = int(n)
    if dir_char == 'W':
        x += dx[0] * n
        y += dy[0] * n
    elif dir_char == 'S':
        x += dx[1] * n
        y += dy[1] * n
    elif dir_char == 'N':
        x += dx[2] * n
        y += dy[2] * n
    elif dir_char == 'E':
        x += dx[3] * n
        y += dy[3] * n

print(x, y)