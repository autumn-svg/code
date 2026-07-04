def selection_sort(arr, N):
    #arr : 정렬하고 싶은 배열
    #N: 배열의 원소의 개수

    #arr 안에서 제일 작은 원소를 0번 인덱스로
    #그 다음으로 작은 원소를 1번 인덱스로
    #그 다음으로 작은 원소를 2번 인덱스로
    #...
    #가장 큰 원소는 마지막 인덱스로
    #(오름차순 기준)
    #(내림차순은 최댓값)
    for i in range(N-1):
        #i번 자리의 주인은 arr 안에서 i번째로 작은 원소
        #arr 안에 있는 최소값의 위치는 i라고 가정하고
        #나머지 구간에서(i+1, N) 최소값 찾기
        min_idx = i
        for j in range(i+1, N):
            #j번 위치에 있는 값이 min_idx에 있는 값보다 작으면
            #최소값 위치 갱신
            if arr[min_idx] > arr[j]:
                min_idx = j
        #최소값을 i위치에 있는 원소와 자리 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]