A, B = map(int, input().split())

sum_v = 0

for i in range(A, B+1):
    if i % 2 == 0:
        sum_v += i

print(sum_v)