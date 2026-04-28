import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


T = int(input())
for test_case in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0

    while True:
        if A >= B:
            A -= 1
            cnt += 1
            continue
        if B >= C:
            B -= 1
            cnt += 1
            continue
        break

    if A <= 0 or B <= 0 or C <= 0:
        cnt = -1

    print(f"#{test_case} {cnt}")