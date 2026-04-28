max_v = arr[0]

for i in range(1,N):
    if max < arr[i]:
        max_v = arr[i] #arr[i]가 더 크면 갱신 된다

for i in range(1,N):
    if arr[max_idx] <= arr[i]:
        max_idx = i

N, V = map(int, input().split())
arr = list(map(int. input().split()))

idx = -1
for i in range(N):
    if [i] == V:
    idx = 1
    break #for i

max_v = arr[0] #최댓값은 배열 중 가장 첫번째 단어, 숫자 머 등등

for i in range(1, N): #1에서 N번째까지를 i에 집어 넣음