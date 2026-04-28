T = int(input())

for tc in range(1, T+1):
    #N: 세로길이(행 번호)
    #M: 가로길이(열번호)
    N, M = map(int, input(). split())

    #2차원 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]

    #2차원 배열의 모든 위치를 탐색
    #0인 칸에서만 상하좌우 델타 탐색
    #상하좌우합을 구하고 그 중에 최대값을 구하는 문제

    #문제에서 원하는 답(최대로 잡을 수 있는 파리 수)
    max_fly = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            #(i, j) 위치가 0인지(파리 트랩 놓을 수 있는지 확인 -> 파리트랩 설치 해 보기)
            if matrix[i][j] == 0:
                #(i, j)위치에 잡힌 파리 수
            ij_fly_cnt = 0

                #상하좌우탐색
            for d in range(4):
                #d방향으로 움직이고 난 후 좌표를 (ni, nj)라고 하면
                #ni = 현재 행 번호 + d 방향으로 움직일 때 행 번호의 변화량
                ni = i + di[d]
                #nj = 현재 열번호 + d방향으로 움직일 때 열 번호의 변화량량
                nj = j + dj[d]
                if 0 <= ni < N and 0<= nj < M:
                    #(ni, nj)는 유효한 좌표이므로 파리수+
                    #(ni, nj)에 있던 파리들 추가
            ij_fly_cnt += matrix[ni][nj]

        #상하좌우 탐색이 끝나고 최대값 비교
        if max_fly < ij_fly_cnt:
            # (i, j)에서 잡은 파리 수가 최대값
            max_fly = ij_fly_cnt

    print(f'#{tc} {max_fly}')