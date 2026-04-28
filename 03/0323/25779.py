T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    long = list(map(int, input()))
    M = int(input())
    short = list(map(int, input()))

    result = 0
    idx = 0
    for i in range(N):
        if short[idx] == long[i]:
            idx += 1

        if idx == M:
            result = 1
            break

    print(f"#{test_case} {result}")