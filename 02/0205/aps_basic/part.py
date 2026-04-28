T = int(input())

for tc in range(1, T+1):
    #1부터 12까지의 자연수를 원소로 가진 집합 A
    A = [i for i in range(1,13)] # == list(range(1,13) 리스트 컴프리헨션 할 때는 밑에 표현식이 올 수 없어서 for 문 앞에 옴. for i in range(1,13) \n print(i)랑 같은 말
#_를 변수로 쓰면 안 되는 이유:
    #부분집합의 개수 N, 부분 집합의 원소의 합 K
    N, K = map(int, input().split())

    #문제에서 원하는 답: 원소가 N개, 합이 K인
    #A의 부분 집합의 개수
    answer = 0
    #A의 부분집합의 개수는 총 2**12개, 1<<12
    for i in range(1<<12):
        #A의 i번 부분집합에 대해...
        #i번 부분집합의 원소의 개수, 합을 구해야 한다
        ith_cnt = 0 # 원소의 개수
        ith_sum = 0 # 원소의 합

        #i번 부분집합에 A의 어떤 원소들이 포함되어 있을까??
        #i와 1(2)을 bit & 연산을 통해 결과가 0이 아니면
        #0번 원소를 포함하고 있다.
        # i와 10(2)을 bit & 연산을 통해 결과가 0이 아니면
        # 1번 원소를 포함하고 있다.
        # i와 100(4)을 bit & 연산을 통해 결과가 0이 아니면
        # 2번 원소를 포함하고 있다.
        #i와 1을 왼쪽으로 j번 시프트한 결과와 bit&연산을 통해
        #결과가 0이 아니면 j번 원소를 포함하고 있다

        for j in range(12):
            if i & (1<<j):
                #j번 원소 부분집합에 추가
            ith_cnt += 1
            ith_sum += A[j]

        if ith_sum == K and ith_cnt == N:
            answer += 1
    print(f'#{tc} {answer}')