T = int(input())

U = 0
R = 1
D = 2
L = 3

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def move(x, y, commands):
    to = U

    for c in commands:
        # print(x,y)
        if c == "A":
            nx = x + dx[to]
            ny = y + dy[to]
            if 0 <= nx < N and 0 <= ny < N and land[ny][nx] != "T":
                x = nx
                y = ny

        elif c == "L":
            to -= 1
            if to == -1:
                to = L

        elif c == "R":
            to = (to + 1) % 4

    return 1 if land[y][x] == "Y" else 0


for tc in range(1, T + 1):
    N = int(input())

    land = [input() for _ in range(N)]

    Q = int(input())

    arrived = []

    for i in range(N):
        for j in range(N):
            if land[i][j] == "X":
                y, x = i, j

    for _ in range(Q):
        C, commands = input().split()
        C = int(C)

        arrived.append(move(x, y, commands))

    print(f"#{tc}", *arrived)

"""
1
5
GGGGG
GXGTG
GGTTG
GGGYG
GTGGG
3
7 RRAALAA
8 RRAALAAA
12 RAARRALAALAA
"""