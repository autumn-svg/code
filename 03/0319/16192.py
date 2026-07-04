
T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    road = [0] * (N + 1)
    # 길 생성! 0 ~ N 까지 길 이기 때문에
    # 인덱스로 0 ~ N 까지 길이가 N + 1인 배열 생성

    for i in station:
        road[i] = 1
        # 충전기 설치된 위치 표시

    result = 0
    # 몇번 충전해야하는지 표시

    idx = 0
    can_go = True
    # 갈 수 있는지 판단
    while idx + K < N:
        # 끝까지 도착하면 끝
        # 유효한 영역일때만 반복

        can_go = False
        # 갈 수 있는지 없는지 판단!
        # 충전기가 없으면 갈 수 없다고 판단하기 위함

        for i in range(idx + K, idx, -1):
            # 충전 한 곳으로 부터 K거리 만큼 역으로 보면서
            # 제일 먼 충전기부터 찾으면서 라는 뜻
            if road[i] != 0:
                # 충전기가 있다면!
                idx = i
                # 현재 위치를 그 충전기로 변경
                result += 1
                # 충전을 하고
                can_go = True
                # 갈 수 있음 선언
                break
                # 더 가까운 충전기 안보고 현재 인덱스 변환한 걸로
                # 다시 while문 돌림

        if not can_go:
            # 만약 충전기 발견 못하면
            result = 0
            # 결과를 0으로 바꾸고
            break
            # while 문 파괴

    print(f"#{test_case}", result)

