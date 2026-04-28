T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    #인덱스가 짝수 -> 큰 애들
    #인덱스가 홀수 -> 작은 애들



    #앞에서부터 10개의 자리만 확정하면 된다.
    for i in range(10):
        # 큰 애들 or 작은 애들의 위치를 i라고 하자
        idx = i
        for j in range(i+1, N):

            #i가 짝수면 => 큰 애 위치 찾기

            if i % 2 == 0 and arr[j] > arr[idx]:
                #j위치에 있는 원소가 이전 최대값보다 크면 갱신
                idx = j

            #i가 홀수면 -> 작은 애 위치 찾기

            if i % 2 == 1 and arr[j]<arr[idx]:
                #j위치에 있는 원소가 이전 최소값보다 작으면 갱신
                idx = j


        #i자리에 올 원소는 idx 위치에 있는 원소(최대값 or 최소값)
        arr[i], arr[idx] = arr[idx], arr[i]

        #앞에서부터 10개만 잘라서 출력
    print(f'#{tc}', *arr[:10])