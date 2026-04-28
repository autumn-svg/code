T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    M = int(input())
    code = list(map(int, input()))

    idx = 0
    for i in range(N):
        if code[idx] == arr[i]:
            idx += 1

        if idx == M:
            result = 1
            break
        else:
            result = 0

    print(f"#{test_case}", result)


'''

if / else로 result 를 설정할 수 없냐는 궁금증이 생겼음

순철쌤 왈

문제를 풀 때 if else를 쓰면 안 된다는 의문이 들었음
->  이렇게 짜면 문제가 딱히 없긴하지만.... 

첫째, result가 선언되지 않은 라인에서 print 가 된다는거
둘째, 전역으로 선언해 두면 조건 맞을 때 1로 바뀌고 나와서 프린트 하기때문에 이 코드보다 훨 명시적

파이참에서 오류처럼 노란색이 뜨지만
사실 else라서 저  for문에 들어가는 순간 무조건 정의는 되기 때문에 테스트 케이스에서 틀릴 일은 없음
for문 밖에 정의를 해 둬야 말도 안되는 테스트 케이스가 들어있을때 result는 0을 주기때문에
정말 특별한 테케에서 오류가 안터지는 정도?? 사실 문제의 의도와는 다르지 않고, 저 코드가 솔직히
조건을 다 따져서 넣은 코드라서 이질적인 테스트케이스가 왔을때는 오류가 터지도록 '일부러' 설정한 거라면ㅋㅋㅋㅋㅋㅋㅋ 똑똑한거고
되도록이면 코드가 터지지 않게 for문 앞에서 선언하는게 제일 좋아보임
'''
