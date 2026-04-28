import sys
sys.stdin = open('input.txt', 'r')

'''
N 이 주어질 때, abcde를 출력하라
테스트케이스 주어짐
숫자들이 주어짐

'''

T = int(input()) #테케 받음

for tc in range(1, T+1):  # 테스트케이스 개수 주어짐
    N = int(input())  # 첫번째 줄 N이 주어짐
    primes = [2, 3, 5, 7, 11]  # 소인수
    lst = []

    for p in primes:
        count = 0

        while N % p == 0:  # N을 p로 나누었을때 나머지가 0 일때만 돌아가는 반복문
            N //= p  # N을 p로 나눈 몫으로 다시 재할당
            count += 1

        lst.append(count)


    print(f"#{tc}", *lst)

