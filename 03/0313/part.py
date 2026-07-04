# A = [1,2,3,4,5,6,7,8,9,10,11,12]

A = [i for i in range(1,13)]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 부분집합 중에 원소의 개수가 N개
    # 합이 K인 부분집합의 개수
    count = 0

    def comb(cnt, selected, start):
        global count
        # 원소의 개수가 N개 => 12개 중에 3개 고른것과 같음
        if cnt == N:
            # 그 N개의 원소의 합이 K 인 것만
            if sum(selected) == K:
                count += 1
            return

        for i in range(start, 12):
            comb(cnt + 1, selected + [A[i]], i + 1)


    comb(0,[],0)

    print(f"#{tc} {count}")
