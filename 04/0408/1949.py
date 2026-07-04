T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 곳에서만 등산로를 만들 수 있다.
    # 가장 높은 곳의 높이
    max_h = 0
    # 가장 높은 곳 좌표 리스트(여러 곳이 있을 수 있음)
    h_list = []
    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]
                h_list = [(i, j)]
            elif max_h == mountain[i][j]:
                h_list.append((i, j))

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_l = 0


    # (i,j) : 현재 위치
    # cut : 내가 깎기 기회를 썼는지 여부
    # l : 지금 내가 만들고 있는 등산로의 길이
    # path : 내가 지금까지 등산로를 만들었던 좌표
    # h : 현재 높이 (깎고 난 이후 높이)
    def dfs(i, j, cut, l, path):
        global max_l
        max_l = max(l, max_l)

        # print(path)
        # 4방향 탐색해서 갈수 있으면 가고 못가면 안가
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in path:
                # (ni,nj)가 내 현재 위치보다 높이가 낮으면 그냥 가면 된다.
                if mountain[ni][nj] < mountain[i][j]:
                    path.append((ni, nj))
                    dfs(ni, nj, cut, l + 1, path)
                    path.pop()

                # 깎을 기회가 남아있다면 깎아보고 진행
                elif cut:
                    # 깎을수 있는 높이는 1부터 K까지 가능
                    for nh in range(mountain[ni][nj] - K, mountain[ni][nj]):
                        # 깎은높이가 내 현재 높이보다 낮아야 이동 가능
                        if nh < mountain[i][j]:
                            h = mountain[ni][nj]
                            mountain[ni][nj] = nh
                            path.append((ni, nj))
                            dfs(ni, nj, 0, l + 1, path)
                            path.pop()
                            mountain[ni][nj] = h


    # 등산로 조성 시작
    for si, sj in h_list:
        # 깎기 기회 1번, 등산로 길이 1부터 시작
        dfs(si, sj, 1, 1, [(si, sj)])

    print(f"#{tc} {max_l}")







