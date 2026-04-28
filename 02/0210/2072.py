T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split))
    B = list(map(int,input().split))

    for i in range(N):
        for j in range(N-M+1):
            if