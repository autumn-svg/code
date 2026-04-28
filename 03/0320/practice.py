T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    rank = list(map(int, input().split()))

    cnt = 0
    rank.sort()

    for i in range(N):
        team = 0
        for j in range(i, N):
            if rank[j] - rank[i] <= K:
                team += 1
            if team > cnt:
                cnt = team

    print(f"#{test_case}", cnt)