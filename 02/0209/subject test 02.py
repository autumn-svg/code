# T = int(input())
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     metrix = [list(map(int, input().split())) for _ in range(n)]  # split 쓰는 습관 기르기
#
#     flapper = []  # 파리채 범위 모음집
#     for kill in range(m):  # 파리채 설정 i랑 j에 더할 수들
#         for fly in range(m):
#             flapper.append((kill, fly))  # 파리채 범위만큼 i랑 j에 추가할 값 추가
#
#     max_kill = 0
#     for i in range(n + 1 - m):  # 설정 파리채가 영역을 벗어나지 않게
#         for j in range(n + 1 - m):  # n - m 하지만 n(0,0) 이랑 m(0,0)이랑 겹침 -> 1 더함
#             sum_kill = 0
#             # sum_kill += metrix[i][j]    #   <- 중복,,, 찾느라 힘듦
#             for x, y in flapper:  # 파리채 범위만큼 반복
#                 sum_kill += metrix[i + x][j + y]  # 파리채 범위를 모두 썸킬로 추가
#             if max_kill < sum_kill:  # 파리채 최다킬 갱신
#                 max_kill = sum_kill
#             pass
#
#     print(f"#{test_case} {max_kill}")

    import sys

    sys.stdin = open('input.txt', 'r')

    T = int(input())
    '''
    N * M 의 격자에서 0을 찾는다!
    0인 칸에서 트랩을 설치하고, 상하좌우에 있는 파리를 모두 잡는다!
    최대로 몇마리 잡을수 있는지를 구하라!
    '''
    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(N)]

        di = [-1, 1, 0, 0]  # -> 0번 위쪽 1번 아래쪽 2번 왼쪽 3번 오른쪽
        dj = [0, 0, -1, 1]
        most_kill = 0

        for i in range(N):
            for j in range(M):

                if matrix[i][j] == 0:
                    kill_fly = matrix[i][j]  # 해당문제에서는 0이라서 0을 해도 되지만, 파리트랩이면 해당칸에 파리가 있었으면 죽어야지?? ㅇㅈ?

                    for idx in range(4):
                        if 0 <= i + di[idx] < N and 0 <= j + dj[idx] < M:
                            kill_fly += matrix[i + di[idx]][j + dj[idx]]

                    if most_kill < kill_fly:
                        most_kill = kill_fly

        print(f"#{test_case} {most_kill}")