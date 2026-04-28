# T = int(input()) #첫번째 줄에 테스트 케이스 번호가 주어짐
#
#     N = map(int, input().split()) #얘 N은 100 통일 아닌가??? 100*100 크기라는디
#     arr = [list(map(int, input().split())) for _ in range(N)] #2차원 배열 입력 받기
#
#     max_v = 0 #최대값 넣을 변수
#
#     for i in range(N):
#         for j in range(N): #for j in range(i):인 경우
#             s = arr[i][j] #i, j 좌표에 해당하는 값을 넣어주는 거
#             for di, dj in [[0,1][1,0][0,-1][-1,0]]: #상하좌우 각 방향별로 더할 값
#                 for c in range(1, k+1): #거리별, 왜 1부터냐면 0을 하면 제자리기 때문에, k+1은 k포함시키기 위해
#                     ni, nj = i+di*c, j+dj*c #i,j가 내 현재 좌표, di,dj가 내가 움직일 정도, c가 몇 번 반복할 건지(di*3 일케하면 3번 가는 거임)
#                     if 0<=ni<N and 0<=nj<N:
#                         s += arr[ni][nj]
#             if max_v < s: #최대값이 s보다 작으면
#                 max_v = s #s를 최대값으로 갱신

T = 10 #테스트케이스가 10개로 주어짐.(인풋 받을 필요 ㄴㄴ)
for test_case in range(T):
    tc = int(input()) #
    n = 100 #가로세로가 100이라고 명시되어 있음(얘도 인풋 ㄴㄴ)
    arr = [list(map(int, input().split())) for _ in range(n)]    #리스트 컨프리헨션
    # n*n의 리스트를 i,j로
    max_v = 0
    for i in range(n):
        sum_v = 0
        sum_v2 = 0
        for j in range(n):
            sum_v += arr[i][j]
            if sum_v > max_v:
                max_v = sum_v
            sum_v2 += arr[j][i]
            if sum_v2 > max_v:
                max_v = sum_v2



    print(f"#{tc} {}")
