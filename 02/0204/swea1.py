T = int(input())

for tc in range(1, T+1):
    N = int(input())

    #2차원 배열 입력받기
    #한 줄에 1차원 배열 하나
    #N줄
    matrix = [list(map(int,input().split())) for _ in range(N)]

    answer = 0

    # 행 우선 순회 [0][0]-[0][1]-[0][2]...[1][0]
    #i를 행 번호, j를 열 번호

    for i in range(N):
        for j in range(N):
            answer += matrix[i][j]
    print(f'#{tc} {answer}')