T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]


    jdx = N // 2 #센터 부분
    total = 0 #색칠하기 전
    di = 1 #위쪽에서 j가 움직이는 부분? 만큼?
    dj = 1 #아래쪽에서 j가 움직이는 정도
    # print(jdx)

    for i in range((N // 2) + 1): #
        total += matrix[i][jdx]
        for j in range(1, di):
            total += matrix[i][jdx - j]
            total += matrix[i][jdx + j]
        di += 1

    for i in range(N - 1, N // 2, -1):
        total += matrix[i][jdx]
        for j in range(1, dj):
            total += matrix[i][jdx - j]
            total += matrix[i][jdx + j]
        dj += 1

    # for i in range(N):
    #     print(matrix[i])

    print(f"#{test_case} {total}")