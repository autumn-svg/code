import sys
sys.stdin = open("algo1_sample_in.txt")

T = int(input())

for tc in range(1, T+1):
    # 행성(정점) 개수 V, 우주항로(간선) 개수 E
    V, E = map(int, input().split())
    # 모든 항로 정보가 한줄로
    # 행성번호1 행성번호2 행성번호3 행성번호4 ...
    # 행성1번과 2번인접, 3번과 4번 인접, ...
    # 2개씩 잘라서 연결
    data = list(map(int, input().split()))

    # 인접행렬 or 인접리스트
    # G[2] : 2번행성에서 갈수 있는 행성 번호 개수
    G = [[0] for _ in range(V+1)]
    

    # 한줄로 주어진 연결 정보를 두개씩 묶어서 처리
    for i in range(0,E*2,2):
        # 행성 두개 자르는데 앞 행성 번호 i
        # 뒤 행성 번호는 i + 1
        # 앞 행성 s, 뒤 행성 e
        s = data[i]
        e = data[i+1]

        # 양방향 그래프
        # G[s].append(e)

        # e번으로 갈수 있는 행성은 s다.
        # G[e].append(s)
        G[e] += 1


    # 갈수 있는 행성이 가장 많은곳(유향그래프)은 몇개?
    # 3번 행성으로 갈수 있는 행성 : 1,2,4
    # 4번 행성으로 갈수 있는 행성 : 1,2,5,6
    # 답 : 4개 (4번행성으로 갈수 있는 행성이 4개로 가장 많음)
    answer = 0

    for i in range(V):
        if answer < G[i]:
            answer = G[i]

    print(f"#{tc} {answer}")