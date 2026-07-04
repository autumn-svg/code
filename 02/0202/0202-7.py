T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #테스트케이스 하나를 처리하는 코드 완성
    #작은 배열의 시작 인덱스 range(0, N-M+1)
    #작은 배열의 순회 인덱스 range(M)

    #길이 N짜리 배열에서 길이가 M인 작은 배열을 구하고
    #작은 배열의 합의 최소, 최대 구하는 문제
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    maxv = 0 #작은 배열의 합 중에 큰 값
    minv = 10000 * N #작은 배열의 합 중에 작은 값, flat(int) 하면 파이썬이 가지고 있는 무한대의 수, 작은 값은 가장 큰 수를 할당 해 놓으면 어떤 수든 제일 작게 나옴

    #작은 배열의 시작 인덱스를 기준으로 삼자.
    #가능한 시작 인덱스의 범위는?? -> 0~N-M ==range(N-M+1)
    # 시작 인덱스를 i라고 하자
    for i in range(N-M+1):
        #이 작은 배열의 시작 인덱스가 i
    #이 작은 배열의 길이가 M이니까 M번 반복하는 코드 작성

        # 시작 인덱스가 i인 작은 배열의 합
        sub_sum = 0
        for j in range(i,i+M):
            #if M = 3, i=0: [0,1,2], i=1: [1,2,3] / 작은 배열 인덱스 [i+j] / for j in range(i, i+M):도 같은 말
            #j는 작은 배열의 인덱스
            sub_sum += arr[j]

        #반복이 끝나면 작은 배열의 합이 구해져 있다.

        #비교해서 최대값보다 크면 갱신
        if sub_sum > maxv:
            maxv = sub_sum
        #최소값 보다 작으면 갱신
        if sub_sum < minv: #최솟값 최대값 할 때는 if elif x
            minv = sub_sum

    print(f'#{test_case} {maxv-minv}')
