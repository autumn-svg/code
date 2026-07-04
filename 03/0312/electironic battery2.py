import sys
open stdin

T = int(input())

for tc in range(1, T+1):
    N, *lst = map(int, input().split())

    # print(N, lst)
    # 문제에서 원하는 답 : 최소 충전 횟수
    min_count = 101

    # 백트래킹
    # idx : 현재 버스 정류장 번호
    # cnt : 현재 idx번 정류장 까지 오는데 충전한 횟수
    def backtracking(idx,cnt):

        # 0. 가지 치기
        # 지금까지 충전한 횟수가 얼마 이상이라면 더이상 진행할 필요가 없다.
        if cnt ???:
            pass

        # 1. 종료 조건
        # 목적지에 도달하기
        if idx >= N-1:
            # 지금까지 충전한 횟수가 최소 충전 횟수인지 확인, 갱신
            min_count = min(cnt, min_count)
        #"f

        # 2. 재귀 호출
        # 현재 정류장에서 갈수 있는 정류장 선택해서 이동
        # idx위치에서 갈 수 있는 정류장이 어딘지 보고, 선택
        for i in range(lst[idx],0,-1):
            # i만큼 이동해서 다음 정류장으로
            backtraking(idx+1, cnt + 1)




"""
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
