T = int(input())

for tc in range(1, T + 1):
    #가로 M, 세로 N
    N, M = map(int,input().split())

    #2차원 배열 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]

    #문제에서 원하는 답(상하좌우 풍선 터졌을 때 최대 꽃가루pollen 개수)
    max_pollen = 0

    #상하좌우 탐색용 델타배열
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    # 행 우선 순회
    for i in range(N):
        for j in range(M):
            #i, j 위치에 있던 꽃가루ㅐ 개수
            cnt = matrix[i][j]
            #(i, j) 위치에서 상하좌우 풍선 터뜨려서 꽃가루 합 구하기
            #4방향으로 이동하니까 이동 4번 반복, 대각선 활용 8방향

            #상하좌우로 뻗어나갈 수 있는 최대 칸 수 = 현재 위치 꽃가루 수
            k = matrix[i][j]

            for d in range(4):
                for c in range(1, k+1):
                    # (i, j)에서 d방향으로 c칸 이동한 좌표(ni, nj)
                    ni = i + di[d] * c
                    nj = j + dj[d] * c
                    #(ni, nj)가 유효한 좌표인지 검사
                    if 0 <= ni < N and 0 <= nj < M:
                        #ni, nj 위치에 있던 꽃가루 개수
                        cnt += matrix[ni][nj]

            #상하좌우 탐색 끝나고 최대값 경신
            if max_pollen < cnt:
                max_pollen = cnt

    #모든 위치에서 최대값 계사ㅏㄴ 후 답 출ㄹ력
    print(f'#{tc} {max_pollen}')