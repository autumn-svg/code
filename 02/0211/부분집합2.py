lst = [1, 2, 3, 4, 5]
N = 5

# 합이 S이하인 부분집합만 구하세요.
S = 10

# 부분집합 구하기 (재귀함수)
# idx : 내가 현재 idx번째 원소를 부분집합에 넣을지 말지 고민중...
# selected : 내가 고른 원소의 상태를 나타낸다.
# selected[x] == 1 : x번째 원소를 부분집합에 넣기로 했다.
# selected[y] == 0 : y번째 원소를 부분집합에 넣지 않기로 했다.
# s : 지금까지 내가 만든 부분집합의 합
def make_set(idx, selected, s):

    # 0. 가지치기
    # 답이 될 가능성이 없으면 더이상 진행하지 않도록
    # 지금까지 내가 만든 부분집합의 합이 S보다 크면 진행 x
    if s >= S:
        return


    # 1. 종료 조건
    # 원소의 개수가 총 N개니까
    # 선택을 N번 했다면 종료
    if idx == N:
        # 부분집합 하나가 완성 되었다.
        subset = []
        for i in range(N):
            # i 번 원소는 골랐다
            if selected[i]:
                subset.append(lst[i])
        # if sum(subset) <= 10:
        print(subset, sum(subset))
        return

    # 2. 재귀 호출
    # idx 번 원소를 부분집합에 넣기로 하고 idx+1 번 원소를 고민하러

    selected[idx] = 1
    make_set(idx+1, selected, s + lst[idx])

    # idx 번 원소를 부분집합에 넣지 않기로 하고 idx+1 번 원소를 고민하러
    selected[idx] = 0
    make_set(idx+1, selected, s + 0)

make_set(0, [0]*N, 0)