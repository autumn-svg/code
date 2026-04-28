

    '''
    가로 세로 길이는 최대 100이다
    한 칸 한 칸씩 떨어져
    근데 거기에 블럭이 있으면 +0이야

    '''


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    # 가장 큰 수와 가장 작은 수의 차이
    max_num = arr[0]
    min_num = arr[0]
    for i in range(1, N):
        if max_num < arr[i]:
            max_num = arr[i]
        elif min_num > arr[i]:
            min_num = arr[i]
        max_minus_min = max_num - min_num

    print(f'#{test_case} {max_minus_min}')



    T = int