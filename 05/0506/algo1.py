import sys
sys.stdin = open("algo1_in.txt")

T = int(input())

for tc in range(1, T + 1):
    # 정점 개수, 간선 개수 입력
    V, E = map(int, input().split())
    # 모든 간선 정보가 한줄로 들어옴, 짝수인덱스 - 홀수인덱스 두개씩 잘라서 처리 필요
    data = list(map(int, input().split()))

    # 각 행성의 직접 연결 수를 저장할 인접 리스트
    # adj_lst[i] : i번 행성과 연결된 행성 번호 리스트
    adj_lst = [[] for _ in range(V+1)]

    # 한 줄에 주어진 항로 정보를 2개씩 묶어서 처리
    for i in range(0, 2 * E, 2):
        a = data[i]
        b = data[i + 1]

        # 양방향 연결이므로 둘 다 1씩 증가
        adj_lst[a].append(b)
        adj_lst[b].append(a)

    # 인접 리스트 완성 후 각 정점의 리스트의 길이 == 각 정점과 연결된 다른 정점의 개수
    # 허브 건설은 연결된 행성이 가장 많은곳 == 연결된 정점이 가장 많은 정점
    answer = 0

    # print(adj_lst)

    for i in range(V):
        if answer < len(adj_lst[i]):
            answer = len(adj_lst[i])

    print(f"#{tc} {answer}")