import sys
sys.stdin = open("input.txt", "r")

from heapq import heappush, heappop

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [float('inf')] * (V+1)
    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
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
            if visited[nn] > w + nw:
                heappush(pq, ((w+nw), nn))
                visited[nn] = w+nw

    print(result)