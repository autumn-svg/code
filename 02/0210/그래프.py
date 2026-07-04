T = int(input())

for test_case in range(1, T+1):
    #V, E = 정점의 개수, 간선의 개수
    V, E = map(int, input().split())

    #인접 행렬
    #adj_m[1][2] == 1 => 1번에서 2번 가는 길 o
    adj_m = [[0]] * (V + 1) for _ in range(V+1):

    #그래프 정보 입력
    #출발-도착 정점 쌍(간선) 정보가 E개 입력으로 들어온다
    for i in range(E):
        s, e = map(int, input().split())
        adj_m[s][e] = 1
        # adj_m[e][s] = 1 요건 안 됨(무향 그래프에서 사용)

        #테스트케이스 입력 마지막에 출발 정점 번호, 목표 정점 번호
        S, G = map(int, input().split())

        #S에서 출발하는 DFS 탐색, 탐색 중 G를 만나면 탐색 종료

        #처음엔 도착 불가능이라고 가정, dfs 탐색 중 g를 만나면 1로
        answer = 0

        ####DFS

        print(f'#{test_case} {answer}')