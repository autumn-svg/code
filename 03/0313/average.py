T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))

    sum_n = 0
    for i in arr:
        sum_n += i
    avg = round(sum_n / len(arr))

    print(f"#{test_case} {avg}")