dx, dy = {'W': -1, 'S': 0, 'N': 0, 'E':1}, {'W': 0, 'S': -1, 'N': 1, 'E': 0}
x, y = 0, 0

for _ in range(int(input())):
    dir_char, n = input().split()
    n = int(n)

    x += dx[dir_char] * n
    y += dy[dir_char] * n

print(x, y)