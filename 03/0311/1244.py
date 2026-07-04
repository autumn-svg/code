n = int(input())  # 스위치 개수

switch = list(map(int, input().split()))  # 스위치 상태 저장

student = int(input())  # 학생 수

for _ in range(student):
    gender, num = map(int, input().split())

    # 남학생
    if gender == 1:
        # num의 배수 위치 스위치 뒤집기
        for i in range(num-1, n, num):
            switch[i] = 1 - switch[i]  # 0 -> 1, 1 -> 0

    # 여학생
    else:
        idx = num - 1  # 파이썬은 인덱스가 0부터라서 -1

        # 자기 스위치 먼저 뒤집기
        switch[idx] = 1 - switch[idx]

        left = idx - 1
        right = idx + 1

        # 좌우가 같은 동안 확장
        while left >= 0 and right < n:
            if switch[left] == switch[right]:
                switch[left] = 1 - switch[left]
                switch[right] = 1 - switch[right]
                left -= 1
                right += 1
            else:
                break

# 출력 (20개씩 줄바꿈)
for i in range(n):
    print(switch[i], end=" ")
    if (i+1) % 20 == 0:
        print()