'''
0부터 9까지 숫자가 적힌 N장의 카드가 주어짐
가장 많은 카드에 적힌 숫자와 장수를 출력하고 장수가 같으면 숫자가 큰 쪽 출력

'''

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    vacant = [0] * N
    max_n = 0
    items = 0

    for i in a:

        vacant[i] += i
        items += 1

        if max_n <= i:
            max_n = i

    print(f'#{test_case} {max_n} {items}')