T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]
    for i in range