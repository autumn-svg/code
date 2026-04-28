T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    road = [0] * (N + 1)

    for i in station:
        road[i] = 1

    charge = 0
    idx = 0

    while idx + K < N:
        move = False
        for j in range(idx + K, idx, -1):
            if road[j] != 0:
                idx = j
                charge += 1
                move = True
                break
        if not move:
            charge = 0
            break

    print(f"#{test_case} {charge}")