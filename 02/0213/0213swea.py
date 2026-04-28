'''
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 반복 후 수열의 맨 앞에 있는 숫자를 출력하라

'''

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q= [0]*(N+M+100)
    rear = front = -1

    #arr의 원소를 맨 앞부터 차례대로 q에 삽입한다.
    for i in arr:
        rear += 1
        q[rear] = i

    #q의 맨 앞에서 원소를 꺼내서 그 원소를 다시 맨 뒤로 삽입하는 연산을 M번
    for i in range(M):
        front += 1
        i = q[front] #하나 꺼내오기
        rear += 1
        q[rear] = i #꺼내온 거 다시 뒤에 넣기
    # 원형 큐로 삽입


    #q의 맨 앞에 있는 원소를 출력
    print(f'#{tc} {q[front+1]}')