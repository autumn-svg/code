T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    cdi = [-1, -1, 1, 1]
    cdj = [-1, 1, -1, 1]
    max_fly = 0

    for i in range(N):
        for j in range(N):
            kill_fly = matrix[i][j]
            c_kill_fly = matrix[i][j]

            for idx in range(4):
                for m in range(1,M):

                    ni = i + di[idx] * m
                    nj = j + dj[idx] * m
                    cni = i + cdi[idx] * m
                    cnj = j + cdj[idx] * m

                    if 0 <= ni < N and 0 <= nj < N:
                        kill_fly += matrix[ni][nj]
                    if 0 <= cni < N and 0 <= cnj < N:
                        c_kill_fly += matrix[cni][cnj]

            if max_fly < kill_fly:
                max_fly = kill_fly
            if max_fly < c_kill_fly:
                max_fly = c_kill_fly

    print(f"#{test_case}", max_fly)