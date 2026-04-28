T = int(input())
for test_case in range(1, T+1):
    n, m, k = map(int,input().split()) # n: 예약 손님 수 m: 붕어빵 만든 시간(초) k: 만든 붕어빵 개수
    arrive = [map(int,input().split())] # 손님들이 도착하는 시간(초)

    arrive.sort() # 온 손님들 정렬

    possible = True

    for i in range(n): # 손님 한 명씩 확인
        time = arrive[i] # i번째 손님이 도착한 시간
        bread = (time // m) * k # 손님이 도착한 그 시간까지 붕어빵이 몇 개 만들어졌는가

        if bread < i + 1: # 만든 빵이 손님 수보다 작으면
            possible = False # 다 주는 건 불가능함
            break

    if possible:
        print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")
