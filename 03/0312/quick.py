def quick_sort(l, r):
    if l >= r - 1:
        return

    pivot = arr[l]
    left = l + 1
    right = r - 1

    while left <= right:
        while left <= right and pivot >= arr[left]:
            left += 1

        while left <= right and pivot <= arr[right]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[right], arr[l] = arr[l], arr[right]

    quick_sort(l, right)
    quick_sort(right + 1, r)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, N)

    print(f"#{test_case} {arr[N//2]}")