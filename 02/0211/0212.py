lst = [1, 2, 3, 4, 5]
N = 5

# 부분집합 구하기 (재귀함수)
# idx : 내가 현재 idx번째 원소를 부분집합에 넣을지 말지 고민중...
# selected : 내가 고른 원소의 상태를 나타낸다.
# selected[x] == 1 : x번째 원소를 부분집합에 넣기로 했다.
# selected[y] == 0 : y번째 원소를 부분집합에 넣지 않기로 했다.
def make_set(idx, selected):

    # 1. 종료 조건
    # 원소의 개수가 총 N개니까
    # 선택을 N번 했다면 종료
    if idx == N:
        # 부분집합 하나가 완성 되었다.
        for i in range(N):
            if selected[i]:
                print(lst[i], end=" ")
        print()
        return

    # 2. 재귀 호출
    # idx 번 원소를 부분집합에 넣기로 하고 idx+1 번 원소를 고민하러
    selected[idx] = 1
    make_set(idx+1, selected)

    # idx 번 원소를 부분집합에 넣지 않기로 하고 idx+1 번 원소를 고민하러
    selected[idx] = 0
    make_set(idx+1, selected)

make_set(0, [0]*N)