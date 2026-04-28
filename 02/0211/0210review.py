T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N<M:
        A, B = B, A
        N, M = M, N
    max_v = 0
    for i in range(N - M + 1):
        sum_v = 0
        for j in range(M):
            sum_v += a[i+j] * b[j]
        if sum_v > max_v:
            max_v = sum_v
    print(f'#{test_case} {max_v}')