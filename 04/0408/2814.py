T = int(input())

for tc in range(1, T+1):
    # N : 정점 개수
    # M : 간선 개수
    N, M = map(int, input().split())

    # 인접 행렬
    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        s, e = map(int, input().split())

        G[s].append(e)
        G[e].append(s)

    # D[x][y] => x정점에서 시작했을때 y정점까지 도착하는데 걸리는 최장 거리
    D = [[0] * (N+1) for _ in range(N+1)]


    # s : 시작 정점번호
    # v : 현재 정점번호
    # path : 지금까지 거쳐온 정점 번호 리스트
    def dfs(s,v,path):

        # 현재 있는 정점 번호 v

        # v에서 갈수 있는 다른 정점 nv를 발견하면
        # 바로 nv로 이동
        for nv in G[v]:
            # nv 번호는 지금까지 왔던길에 없었다.
            # 이동 가능
            if nv not in path:
                path.append(nv)
                # 이전에 nv까지 왔었다면, 지나친 정점의 개수가 D[s][nv] 에 있다.
                # 이번에 새로 만든 경로 path안에 지금까지 지나친 정점이 저장되어 있다.
                # 둘중에 큰 값으로 갱신
                D[s][nv] = max(D[s][nv] , len(path))
                dfs(s,nv,path)
                path.pop()


    # 모든 정점에서 dfs 탐색 시작
    for i in range(1, N+1):
        D[i][i] = 1
        # i번 정점에서 시작, 현재 정점번호도 i, 지나친 정점 번호 i 추가한 상태로
        dfs(i,i,[i])

    # 모든 경로 다 확인해보기
    max_D = 0
    for i in range(1,N+1):
        for j in range(1, N+1):
            max_D = max(max_D, D[i][j])

    print(f"#{tc} {max_D}")







