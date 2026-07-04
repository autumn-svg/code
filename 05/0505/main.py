import sys
sys.stdin = open("input.txt","r")

from heapq import heappop,heappush
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(V+1)]
    visited = [float('inf')] * (V+1)
    S, G = map(int, input().split())
    w = 1
    for i in range(E):
        n1, n2 = lst[i]
        graph[n1].append((w, n2))
        graph[n2].append((w, n1))
    # print(graph)
    pq = [(0,S)]
    visited[S] = 0
    result = 0
    while pq:
        w, n = heappop(pq)
        if n == G:
            result = w
            break
        for nw, nn in graph[n]:

            if visited[nn] > nw+w:
                heappush(pq, ((nw + w), nn))
                visited[nn] = nw+w
    print(result)