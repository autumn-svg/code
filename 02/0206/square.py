T = int(input())

for tc in range(1, T + 1):
    # 큰 정사각형의 크기 N
    # 작은 정사각형의 크기 M
    N, M = map(int, input().split())

    # 크기 N*N 짜리 정사각형 만들기
    big = [[0] * N for _ in range(N)]

    # 작은 정사각형 안에 쓸 숫자
    num = 1

    # 이 큰 정사각형 안에서 M*M 정사각형 만큼 순회
    # 작은 정사각형의 시작지점 (맨왼쪽 위 좌표 행번호, 열번호를 기준)
    # 시작지점을 (i,j) 라고 하면 가능한 i와 j의 범위는 어떻게 될까?
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 작은 정사각형의 시작 위치 (i,j)
            # 가로세로크기 M짜리 작은 정사각형을 순회

            # 작은 정사각형의 좌표 (si, sj)
            # 이 (si, sj)의 유효한 범위 (i+0,i+1,...i+M-1,j+0,j+1,..j+M-1)
            for si in range(i, i + M):
                for sj in range(j, j + M):
                    # 작은 정사각형 안에서 하고싶은 코드 작성
                    big[si][sj] = num

            # 다음 정사각형을 위해 num + 1
            num += 1

    # 2차원배열출력
    print(f"#{tc}")

    for i in range(N):
        print(*big[i])