from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    visited = [[0] * M for _ in range(N)]
    matrix = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                cnt += 1

                q = deque()
                q.append((i, j))
                visited[i][j] = 1

                while q:
                    i, j = q.popleft()
                    for idx in range(4):
                        ni = i + di[idx]
                        nj = j + dj[idx]

                        if 0 <= ni < N and 0 <= nj < M:
                            if matrix[ni][nj] == 1 and visited[ni][nj] == 0:
                                q.append((ni, nj))
                                visited[ni][nj] = 1
    print(cnt)