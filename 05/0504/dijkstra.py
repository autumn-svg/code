import sys
sys.stdin = open("input.txt", "r")

from heapq import heappop, heappush

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    visited = [float('inf')] * (V+1)

    for i in range(E):
        a, b, w = lst[i]
        graph[a].append((w,b))
        graph[b].append((w,a))
    # print(graph)

    pq = [(0,1)]
    visited[0] = 0
    result = -1
    while pq:
        w, n = heappop(pq)

        if n == V:
            result = w
            break

        for nw, nn in graph[n]:
            if visited[nn] > nw + w:
                heappush(pq, ((w + nw), nn))
                visited[nn] = w + nw

    print(result)

