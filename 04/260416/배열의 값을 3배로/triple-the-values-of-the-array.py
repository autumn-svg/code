n = 3
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in matrix:
    for j in i:
        print(j * 3, end=" ")
    print()