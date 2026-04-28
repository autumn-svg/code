# 테스트 케이스 받기
T = int(input())
for tc in range(1, T + 1):
    # 학생수와 알고 싶은 학생 번호
    N, K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # 중 , 기, 과 성적 리스트 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_cnt = []
    # 행 우선 순회 하며 카운트
    for i in range(N):
        cnt = 0 #사람별 점수를 넣을 만한 변수를 하나 만들었음
        for j in range(3): #중간 기말 과제?
            if j == 0:
                cnt += (35 * arr[i][0]) / 100 #중간고사 35% 곱하기, arr[i]는 학생 하나하나, [숫자]는 점수가 해당하는 위치
            if j == 1:
                cnt += (45 * arr[i][1]) / 100 #기말고사 45% 계산하는 거, arr[i]는 학생 하나하나
            if j == 2:
                cnt += (20 * arr[i][2]) / 100 #과제 20프로
        # 학생들의 종합 점수를 빈리스트에 넣기
        total_cnt.append(cnt)
        if i == K - 1:  # 만약 k번째 학생이라면
            k_std = 0 #k번째 학생의 카운트를 셀 거임
            for k_j in range(3): #중간 기말 과제
                if k_j == 0:
                    k_std += (35 * arr[i][0]) / 100
                if k_j == 1:
                    k_std += (45 * arr[i][1]) / 100
                if k_j == 2:
                    k_std += (20 * arr[i][2]) / 100
    # 총점 기준으로 오름차순 정리 점점점점 많아지는 거
    total_cnt.sort(reverse=True)
    # k 학생 점수의 인덱스 값 구하기, index는 리스트에서 특정 값이 몇 번째 위치에 있는지 알려주는 메서드
    num = total_cnt.index(k_std)

    answer = grade[num // (N // 10)]
    print(f'#{tc} {answer}')