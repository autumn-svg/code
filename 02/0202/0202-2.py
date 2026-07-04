T = int(input())
#테스트케이스 개수

for tc in range(1, T+1):
    #테스트 케이스 수만큼 반복, 출력형식 맞추기 위해서 1부터

    N = int(input())
    #리스트 길이 N
    arr = list(map(int, input().split()))
    #N개의 숫자

#문제에서 원하는 답(최대값)
    #맨 앞에 있는 원소가 가장 크다고 가정
    max_value = arr[0]
    #반복문을 돌면서 더 큰 값을 발견하면 갱신
    for i in range(1, N)
        if arr[i] > max_value:
            max_value = arr[i]

            #반복문이 끝나면 최대값이 구해진다
            #문제에서 원하는 출력형식에 맞게 답 출력

    print(f'#{tc} {max_value}') # #옆에 띄우면 안 됨 출력 형식 잘 확인해야 함
   

