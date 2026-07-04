def merge(left, right):
    l = r = 0
    result = []
    if left[l] > l and right[r] > r:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = merge_sort(arr)
    print(f"#{test_case} {result[N//2]} {cnt}")