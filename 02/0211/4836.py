# 색칠하기

'''
첫 줄에 테스트케이스가 주어짐.
다음 줄에 칠할 영역의 개수 N이 주어짐
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, r2, c2와 색상 정보 컬러가 주어짐
한 줄 한 줄 색 별로 제공되네
시작지점 끝지점이 표기되어 있고 ri, rj, ci, cj 지정할까봐
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 ... 칠할 색상이 주어질 때 색이 겹쳐 보라색이 된 칸 수 구하기

'''

T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]    # 흰 도화지 리스트 컨프리헨션
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())   # 입력! 왼쪽 모서리 r1,c1 오른쪽 모서리 r2,c2 그리고 색깔 color

        for i in range(r2 - r1 + 1):   # 색의 영역 2,2 칠하고 2,3 칠하고 2,4 칠하고
            for j in range(c2 - c1 + 1):  # 색의 영역 3,2 칠하고 3,3 칠하고 3,4 칠하고
                # 즉, i가 하나오를때 j가 순차적으로 다 오른다!
                matrix[r1 + i][c1 + j] += color  # 해당 영역 1칸! 에 컬러를 칠한다

    for idx in range(10):    # 흰 도화지를 순회하면서
        for jdx in range(10):
            if matrix[idx][jdx] == 3:   # 보라색을 찾아서 *같은색은 겹치지 않는다~~*
                cnt += 1    # 카운트를 한다!

    print(f"#{test_case} {cnt}")

