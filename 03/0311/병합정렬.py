arr = [69,10,30,2,16,8,31,22]
N = len(arr)

# 병합정렬 함수
# 정렬할 범위를 지정(인덱스)
# 시작(start) ~ 종료(end)
def merge_sort(start, end):
    # 1. 종료 조건
    # 원소가 하나 남았을때
    # 더이상 분할이 불가능함
    if start == end - 1:
        return start, end

    # 2. 재귀 호출
    # 두 부분으로 나누고
    # 합칠때 정렬이 이루어진다.
    # 두 두분으로 나누는 기준은 가운데
    mid = (start + end) // 2

    # 왼쪽부분 다시 분할후 정렬
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽부분 다시 분할후 정렬
    right_s, right_e = merge_sort(mid, end)

    # 합치면 된다.
    merge(left_s, left_e, right_s, right_e)
    # 정렬된 범위 리턴
    return start, end

# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    # 왼쪽부분의 가장 작은 원소가 있는 인덱스
    l = left_s
    # 오른쪽부분의 가장 작은 원소가 있는 인덱스
    r = right_s

    # 왼쪽 부분과 오른쪽 부분을 합친 결과의 길이: N
    N = right_e - left_s
    result = [0] * N

    #result배열에 들어 갈 원소의 다음 자리(작은 순서)
    idx = 0

    # 병합 시작(병합을 하면서 정렬이 된다)
    # 왼쪽 부분의 최소값 vs 오른쪽 부분의 최소값 비교
    # 둘 중에 작은 거 선택해서 result의 idx 위치에 넣기

    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            # 왼쪽 부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            # 오른쪽 부분의 맨 앞에 최소값이 있다.
            result[idx] = arr[r]
            r += 1
            idx += 1

    # 둘 중 한 부분에만 원소가 남아있는 경우
    # 남아 있는 원소 주ㅜ룩 추가

    # 오른쪽만 남은 경우
    if r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    #왼쪽만 남은 경우
    if l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    #result 안에는 left_s에서 right_e까지의 원소들이 오름차순으로 정렬이 되어 있고, 이 부분을 원본 arr에 반영

    for i in range(N):
        