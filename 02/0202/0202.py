# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#
#     max_v = arr[0]
#     min_v = arr[0]
#         #이 부분에 코드 구현
#     # if tc >
#
#     print(N, arr)
#     print(f'#{tc} {max_v - min_v}')

# N = int(input())
#
# print(N)
#
# arr = list(map(int,input().split()))
# print(arr)


#찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1
N, V=  map(int,input().split()
           print(N,V)
arr = list(map(int, input()).split()))
print(arr)


# 일단 없다고 생각
idx = -1
#반복문을 돌다가 리스트인 거 v를 발견하면 그 때 바꾸면 된다.
for i in range(N):
    if arr[i] == V:
        idx = 1
        break

print(idx)