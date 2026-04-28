T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    # P : 총 페이지수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지

    # 문제에서 원하는 답 = 누가 더 빨리찾느냐(승자)
    winner = ""

    # A의 이진탐색 범위
    a_start, a_end = 1, P
    # B의 이진탐색 범위
    b_start, b_end = 1, P

    # A와 B가 번갈아 가며 가운데를 찍는다.
    while True:
        # A가 원하는 페이지를 찾았는가 여부
        a_find = False
        # B가 원하는 페이지를 찾았는가 여부
        b_find = False
        # A또는 B가 원하는 페이지를 찾으면 종료 break

        # A가 가운데 페이지 찍어보기
        mid = (a_start + a_end) // 2
        # 가운데 찍었는데 원하는 페이지 찾은 경우
        if mid == A:
            a_find = True
        # 가운데 찍었는데 원하는 페이지보다 작은 경우
        elif mid < A:
            # A의 탐색 시작 범위를 가운데로 땡겨오기
            # mid 왼쪽에는 A가 찾는 페이지가 없다
            a_start = mid
        # 가운데 찍었는데 원하는 페이지보다 큰 경우
        else:
            a_end = mid

        # B가 가운데 페이지 찍어보기
        mid = (b_start + b_end) // 2
        # 가운데 찍었는데 원하는 페이지 찾은 경우
        if mid == B:
            b_find = True
        # 가운데 찍었는데 원하는 페이지보다 작은 경우
        elif mid < B:
            b_start = mid
        # 가운데 찍었는데 원하는 페이지보다 큰 경우
        else:
            b_end = mid

        # A나 B가 원하는 페이지를 찾았으면 승자 결정 하고
        # break
        # A가 승
        if a_find and not b_find:
            winner = "A"
            break
        # B가 승
        elif b_find and not a_find:
            winner = "B"
            break
        # A,B 둘다 찾아서 무승부
        elif a_find and b_find:
            winner = 0
            break

    print(f"#{tc} {winner}")