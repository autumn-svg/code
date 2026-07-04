T = int(input())
for test_case in range(1, T+1):
    V, E = map(int,input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    result = 0
    for i in range(0, 2*E, 2):
        n1 = lst[i]
        n2 = lst[i+1]

        graph[n1].append(n2)
        graph[n2].append(n1)
    # print(graph)
    for i in range(1, V+1):
        result = max(result, len(graph[i]))

    print(result)