def find_set(x):

    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    result = []

    for _ in range(m):
        c, a, b = map(int, input().split())

        if c == 0:
            union(a, b)

        elif c == 1:
            if find_set(a) == find_set(b):
                result.append('1')
            else:
                result.append('0')


    print(f"#{test_case} {''.join(result)}")