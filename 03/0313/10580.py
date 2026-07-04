T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    matrix.sort() # 리스트 정렬
    arrive = []

    for i, j in matrix:
        arrive.append(j)
    # print(arrive)

    # while 문 만듦
    # 리스트 안에서 값을 하나 정해서
        # 그 값보다 뒤에 있는 값들이랑 비교
        # 그리고 count
    # print(count)

    cnt = 0
    idx = 0
    while len(arrive) - 1 > idx:
        idx += 1
        target = arrive[idx-1]
        for d in range(idx, N):
            if target > arrive[d]:
                cnt += 1

    print(f"#{test_case} {cnt}")