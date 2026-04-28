# N = int(input())
# # arr = [list(map(int, input().split())) for _ in range(N)] #들어오는 숫자가 공백이 있을 때
# arr = [list(map(int, input())) for _ in range(N)] #공백이 없을 때
# print(arr)


# arr = [[0]*4 for _ in range(3)]
# print(len(arr), len(arr[0]))

# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # N = 3 #행의 크기
# # M = 4 #열의 크기
# # for i in range(N):
# #     for j in range(M):
# #         print(arr[i][j], end = ' ')
# #     print()
# # for row in arr:
# #     print(*row) #언팩

# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# N = 3 #행의 크기
# M = 4 #열의 크기
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# for i in range(N):
#     for j in range(M):
#         # for d in range(4): #방향별로
#         #     ni = i+ di[d]
#         #     nj = j + dj[d]
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]
#             ni, nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<M:
#                 print(arr[ni][nj])

