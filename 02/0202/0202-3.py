T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):

    max_idx = 0
    N = int(input())
    test = list(map(int, input().split()))

    for i in range(1,N):
        if test[max_idx] < test[i]:
            max_idx = i

    max_num = test[max_idx]

    print(f'#{test_case} {max_num} {max_idx}')

