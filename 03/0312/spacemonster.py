T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    idx = jdx = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                idx = i
                jdx = j

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for dx in range(4):
        m = 1
        while True:
            ni = idx + di[dx] * m
            nj = jdx + dj[dx] * m
            m += 1
            if 0 <= ni < N and 0 <= nj < N:
                if matrix[ni][nj] == 1:
                    break
                if matrix[ni][nj] == 0:
                    matrix[ni][nj] = 3
                continue
            break

    safe = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                safe += 1

    print(f"#{test_case} {safe}")
