start, end = map(int, input().split())

'''
연습 문제 2: 소수(Prime Number) 감별사
문제: start 이상 end 이하인 정수 중에서 **소수(약수가 딱 1과 자기 자신, 즉 2개뿐인 수)**의 개수를 구하는 프로그램을 작성해 보세요.

입력 예시: 2 10
출력 예시: 4
'''

# Please write your code here.
cnt = 0
for i in range(start, end+1):
    m_cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            m_cnt += 1
    if m_cnt == 2:
        cnt += 1
print(cnt)