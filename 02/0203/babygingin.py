# 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때,
# 3 장의 카드가 연속적인 번호를 갖는 경우를 run이라고 하고
# 3 장의 카드가 동일한 번호를 갖는 경우를 triplet이라 함
# 그리고 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다
# 6자리 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성

# 667767은 두 개의 triplet이므로 baby-gin
# 054060은 한 개의 run과 한개의 triplet이므로 역시 baby-gin
# 101123은 한 개의 triplet이 존재하나, 023이 run이 아니므로 baby-gin이 아님
# (123을 run으로 사용하더라도 011이 run이나 triplet이 아님)

# 첫 줄에 테스트케이스의 개수 T
# 두 번째 줄 부터 각 테스트케이스의 입력
# 각 테스트케이스의 첫 번째 줄에 카드 6장의 숫자가 입력으로 주어짐
# 카드 6장으로 완성되면 "Baby Gin" 아니면 "Lose"

T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T + 1):

    num = int(input())   # 6자리 숫자 입력
    c = [0] * 12         # 숫자 개수를 저장할 배열 (0~11까지)
                         # i+2 접근 때문에 여유로 12칸 생성

    # 입력받은 6자리 숫자를 한 자리씩 꺼내서
    # 해당 숫자의 개수를 카운팅
    for _ in range(6):
        c[num % 10] += 1   # 마지막 자리 숫자 개수 증가
        num //= 10         # 마지막 자리 제거

    i = 0          # 기준 숫자
    tri = 0        # triplet 개수
    run_v = 0      # run 개수

    # 0부터 9까지 검사
    # while문: 반복 횟수 예상이 되지 않을 때(좀 더 확실히 for문이랑 차이점 정리하기)
    while i < 10:

        # triplet 먼저 검사
        # 같은 숫자가 3개 이상이면 3개 제거하고 triplet 1개 증가
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue   # 같은 i에서 다시 검사 (남은 숫자 있을 수 있음)

        # run 검사
        # i, i+1, i+2가 각각 1개 이상 있으면
        # 하나씩 제거하고 run 1개 증가
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run_v += 1
            continue   # 같은 i에서 다시 검사

        # triplet도 run도 아니면 다음 숫자로 이동
        # while문은 i를 직접 증가시켜줘야 함
        # 들여쓰기하면 run 일대만 증가하게 됨
        i += 1

    # triplet + run 총 2세트면 Baby Gin
    if run_v + tri == 2:
        print(f'#{test_case} Baby Gin')
    else:
        print(f'#{test_case} Lose')