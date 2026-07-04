#A 인덱스를 i
#B인덱스를 j
T = int(input())

for tc in range(1, T+1):
    # A의 길이 N, B의 길이 M
    N, M = map(int, input().split())
    #A
    A = list(map(int, input().split()))
    #B
    B = list(map(int, input().split()))

    #문제에서 원하는 답 -> B가 A의 부분수열인가?
    #No라고 생각하고 시작, 상황에서 내가 받고 싶은 답이 A면 B로 하고 yes면 no
    answer = 'No'

    #A의 인덱스 i, B의 인덱스 j
    #A[0] : B[0] => 1:3
    #A[1] : B[0] -> 3:3 (o)
    #A[2]:B[1] -> 2: 4
    #B의 인덱스 j는 1씩 증가하지 않으니 변수로 따로 관리
    j=0

    #A의 인덱스 i는 아무제한 없이 1씩 증가하니 for문 사용
    for i in range (N):
        #A의 i번 원소와 B의 j번 원소를 비교


        #같지 않음 -> i만 증가(이미 for문에서 하고 있음)

        #같음 -> 둘 다 증가
        if A[i] == B[j]:
            j += 1
        #B 원소 M개 만큼 증가 해 버렸으면 같다는 뜻, 증가 횟수가 즉 원소의 갯수
        #부분 수열이 완성되는 조건
        if j == M:
            #A안에서 B의 원소를 모두 발견했다 -> 부분수열
            answer = 'Yes'
            #나머지는 볼 필요 없음
            break

    print(f'#{tc} {answer}')