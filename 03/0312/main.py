T = int(input())
for test_case in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))

    score = [0] * 101

    for i in arr:
        score[i] += 1

    mode = 0
    max_count = 0

    for i in range(len(score)):
        if score[i] >= max_count:
            max_count = score[i]
            mode = i

    print(f"#{test_case} {mode}")