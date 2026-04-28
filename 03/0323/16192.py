T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    road = [0] * (N + 1)

    for s in station:
        road[s] = 1

    idx = 0
    result = 0

    while idx + K < N:
        move = False
        for i in range(idx + K, idx, -1):
            if road[i] == 1:
                result += 1
                move = True
                idx = i
                break

        if not move:
            result = 0
            break

    print(f"#{test_case}", result)