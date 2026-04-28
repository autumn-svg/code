A, B = map(int, input().split())

n = A
print(n, end=" ")

while n < B:
    if n % 2 == 1:
        n = n * 2
    else:
        n = n + 3

    if n <= B:
        print(n, end=" ")
    else:
        break