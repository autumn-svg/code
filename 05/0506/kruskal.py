def find_x(x):
    if p[x] != x:
        p[x] = find_x(p[x])
    return p[x]
def union(x, y):
    a = find_x(x)
    b = find_x(y)
    if a != b:
        p[a] = b

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    p = [i for i in range(V+1)]
    line = []

    result = 0

    for _ in range(E):
        # 일단 입력을 다 모은다 가중치를 앞세워서
        a, b, w = map(int, input().split())
        line.append((w, a, b))

    line.sort()
    # 가중치를 기준으로 팝을 할 것이기 때문에 정렬을 한다
    # print(line)
    while line:
        w, a, b = line.pop(0)
        # 가중치가 적은것 부터 뽑는다!

        if find_x(a) != find_x(b):
            # 둘의 대장을 비교한다
            # 둘의 대장이 다르면 둘이 같은 그룹이 아니란거니까
            result += w
            union(a, b)

    for i in range(1, V):
        if find_x(i) != find_x(i+1):
            result = -1
            break

    print(result)
