from heapq import heappush, heappop

T= int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(E)]

    print(lst)
    for i in range(E):
        (a, b, w) = lst[i].pop(i)



