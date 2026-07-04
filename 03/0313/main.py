T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    short = list(map(int, input().split()))
    long = list(map(int, input().split()))

    max_v = 0

    if N > M:
        short, long = long, short
        N, M = M, N

    for i in range(M - N + 1):
        total = 0
        for j in range(N):
            total += short[j] * long[i + j]
        max_v = max(max_v, total)

    print(f"#{test_case} {max_v}")

