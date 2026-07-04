"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""
# V : 정점의 개수, E : 간선의 개수
V, E = map(int, input().split())

# G : 인접 행렬
# G[a][b] = 2
# G[a][c] = 4

# G : 인접 리스트
# G[i] : i번 정점과 연결되어 있는 정점 번호, 간선의 가중치
# G[a] = [(b,2), (c,4)]
G = [[] for _ in range(V)]

for i in range(E):
    # s와 e를 잇는 간선의 가중치 w ( s -> e )
    s, e, w = map(int, input().split())
    G[s].append((e, w))

import heapq

INF = 1e9

# D : 최단 거리를 저장할 리스트
# D[i] : 시작정점에서 i정점까지 가는데 최단 거리(가중치 합)
D = [INF] * V


# start : 시작 정점 번호
# start 정점에서 시작해서 다른 모든 정점까지 가는데 최단거리를 구하는 함수
def dijkstra(start):
    # 가중치가 가장 작은 간선을 선택하는데 최소힙의 도움을..
    heap = []

    # 처음상태에서 시작정점 처리
    heapq.heappush(heap, (0, start))

    # 시작정점에서 시작정점까지의 최단거리는 0
    D[start] = 0

    # 힙에 간선 정보가 남아있으면 계속 반복
    while heap:
        # 다음에 도착가능한 정점중에 최단거리인 정점을 선택
        # heap 에서 하나 꺼내오기만 하면 된다!!
        # w : 최소 가중치, v : 정점 번호
        w, v = heapq.heappop(heap)

        # v 까지 가는 경로는 여러개가 있다. (heap 안에 v까지 가는 경로의 정보가 여러개)
        # 힙에서 꺼낼때 가장 먼저 튀어나오는 v까지의 간선 정보는 거리가 최소 인 정보
        # 나머지 v까지 가는데 걸리는 거리정보는 필요 없다(이미 최소를 먼저 꺼냈으므로)
        # 힙안에 남아있는 v까지 가는 다른 경로들은 이제 고려할 필요가 없다.
        if w > D[v]:
            continue


        # v 를 선택, v를 거쳐서 갈 수 있는 새로운 간선들이 생겼다.
        # 이 새로운길을 선택해서 이전에 계산했던 거리보다 더 작아질수 있는지 확인

        # v와 인접한 정점들을 조사
        # nv : v와 인접한 정점 번호, nw : 그때 가중치
        for nv, nw in G[v]:
            # v를 거쳐서 nv로 가는 새로운 길 발견!
            # 이 새로운 길을 사용하면 최단거리가 되는지??

            # w = s에서 v까지 최단 거리
            # nw = v 에서 nv 로 이어진 간선의 가중치
            new_distance = w + nw

            # 새로운 길로 가는 거리가 최단거리였다
            if new_distance < D[nv]:
                # 최단거리 갱신
                D[nv] = new_distance
                # 힙에 최단거리를 사용해서 nv까지 도착한 정보를 추가
                heapq.heappush(heap, (new_distance, nv))

dijkstra(0)

print(D)







