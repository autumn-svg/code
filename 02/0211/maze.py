T = int(input())

for tc in range(1, T + 1):
    # 미로의 크기 N
    N = int(input())

    # 미로의 정보
    # 0 : 이동가능
    # 1 : 벽(이동불가)
    # 2 : 시작지점
    # 3 : 출구지점
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작지점 찾기
    si, sj = 0, 0

    # 행 우선순회로 일단 2차원 배열 순회해서 시작지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    def dfs(si, sj):

        visited = [[0] * N for _ in range(N)]
        # visited[5][5] = 1 : 5행5열 방문 한적 있다.
        # visited[1][2] = 0 : 1행2열 방문 한적 없다.

        stack = []

        # 시작지점 방문 체크
        visited[si][sj] = 1

        # 현재 방문중인 위치 i, j
        i, j = si, sj

        while True:

            # 현재 있는 위치가 출구면 반복중단
            if maze[i][j] == 3:
                # 출구 찾음, 정답 1
                return 1

            # 현재 위치에서 인접한 4방향 탐색
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                # (i,j) 위치와 인접한 (ni,nj)위치가 이동 가능한가???
                # 2차원 배열 인덱스 범위 안
                # 방문한적 없어야 함
                # 벽이 아니어야 함
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                    # ni,nj 방문체크
                    visited[ni][nj] = 1
                    # 돌아올 위치 기억
                    stack.append((i, j))
                    # ni,nj 이동
                    i, j = ni, nj
                    break
            else:
                # 중간에 break 한적이 없다 => 갈곳을 발견하지 못했다. 이전 방문지점으로 돌아감
                if stack:
                    i, j = stack.pop()
                else:
                    # 스택 비었으면 갈수 있는곳 다 가본거
                    break

        # 반복문 다 돌았는데 return 1 못하면 출구를 찾지 못함
        return 0


    print(f"#{tc} {dfs(si, sj)}")