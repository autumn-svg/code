N = int(input())
number = list(map(int, input().split()))

even_n = []

for i in number:
    if i % 2 == 0:
        even_n.append(i)

even = even_n[::-1]

print(*even, end=" ")
