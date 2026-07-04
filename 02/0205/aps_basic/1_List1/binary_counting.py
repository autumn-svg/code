arr = [1, 2, 3]
n = len(arr) #n: 원소의 개수



for i in range(1, 1<<n): #1<<n: 부분 집합의 개수 공집합 제외
    s = 0  #부분집합의 합
    for j in range(n):  #원소의 수만큼 비트를 비교함
        if i&(1<<j):  #i의 j번 비트가 1인 경우
            #print(arr[j], end= ', ')         #j번 원소 출력
            s += arr[j]
    if s == 0:
        answer = 'YES'
        break
print(answer)