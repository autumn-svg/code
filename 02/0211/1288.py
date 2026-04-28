T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    cnt = [0] * 10
    x = 0
    result = 0

    while True:
        x += 1
        sheeps = N * x
        word = str(sheeps)
        for i in word:   # 문자로 바꿔서 넣어서
            cnt[int(i)] += 1   # 숫자로 다시 바꿔서 인덱싱


        if 0 not in cnt:
            break

    print(f"#{test_case} {N*x}")