def buble(test_case, N, arr):  # 버블 정렬
    for i in range(N):
        for di in range(N - i - 1):  # 가장 큰 값이 이미 뒤로 정해진 상태
            if arr[di + 1] < arr[di]:  # 현재 인덱스 보다 이웃하는 인덱스가 크면
                arr[di], arr[di + 1] = arr[di + 1], arr[di]
    print(f"#{test_case}", *arr)


def choice(test_case, N, arr):  # 선택 정렬
    for i in range(N - 1):
        min_idx = i  # 최소 인덱스 처음 인덱스로 둠
        for idx in range(i, N):  # 가장 작은 값이 이미 앞에 정해진 상태
            if arr[min_idx] > arr[idx]:
                min_idx = idx  # 최소 인덱스 갱신

        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(f"#{test_case}", *arr)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    buble(test_case, N, arr)
