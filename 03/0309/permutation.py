arr = [1, 2, 3, 4, 5, 6]
N = 3

selected = [0] * len(arr)
# selected[1] = 0 : arr의 1번 위치에 있는 숫자(숫자 2)는 쓴 적 없다
# selected[2] = 0 : arr의 2번 위치에 있는 숫자(숫자 3)는 쓴 적 없다

# 재귀 함수
# 숫자를 3번 선택하면 끝
# 한 번 선택할 때 1~6 사이의 숫자를 선택 * 3
# 내가 지금까지 몇 번 선택했는지 나타낼 변수 : i
# 내가 지금까지 선택한 숫자를 저장할 리스트 : path
# 이전에 골랐던 숫자는 다시 못 고른다.
# 내가 이전에 어떤 숫자를 골랐었는지 아닌지 체크: selected
def per(i, path, selected):
    # 1. 종료 조건
    if i == N:
        print(path)
        return

    #2. 재귀 호출
    # i번 단계에서 할 작업을 처리(숫자 1~6 사이에서 하나 골라서 path에 추가)
    # 단 0~(i-1) 단계에서 고른 적이 없는 숫자여야 가능

    # 다음 단계(i+1)로 재귀 호출
    # i번 단계에서 한 번 골랐던 숫자를 빼고 다시 다른 숫자를 넣을 수 있도록 처리
    for j in range(len(arr)):
        # arr 안에서 j번 인덱스에 있는 숫자를 i 번 위치에 놓겠다
        #j번 인덱스에 있는 숫자는 이전 단계에서 쓴 적 없어야 함
        if not selected[j]:
            #j번 인덱스에 있는 숫자 선택
            path.append(arr[j])
            # 선택했다고 표시
            selected[j] = 1
            per(i+1, path, selected)
            #순열의 i번 위치에 arr의 j번 인덱스에 있던 숫자를 빼고 다른 숫자를 넣기 위한 자리
            path.pop()
            selected[j] = 0

#0단계, 아직 아무것도 안 고른 상태에서 시작
per(0, [], selected)
