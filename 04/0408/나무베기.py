import heapq

T = int(input())

U, R, D, L = 0, 1, 2, 3
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

INF = int(1e9)

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    land = [input().strip() for _ in range(N)]

    sx = sy = ex = ey = -1
    tree_idx = {}
    tree_count = 0

    # 시작점, 도착점, 나무 번호 매기기
    for y in range(N):
        for x in range(N):
            if land[y][x] == 'X':
                sx, sy = x, y
            elif land[y][x] == 'Y':
                ex, ey = x, y
            elif land[y][x] == 'T':
                tree_idx[(x, y)] = tree_count
                tree_count += 1

    # dist[(x, y, dir, mask)] = 최소 조작 수
    dist = {}
    pq = []

    start = (sx, sy, U, 0)
    dist[start] = 0
    heapq.heappush(pq, (0, sx, sy, U, 0))

    ans = INF

    while pq:
        cost, x, y, d, mask = heapq.heappop(pq)

        state = (x, y, d, mask)
        if dist.get(state, INF) < cost:
            continue

        if x == ex and y == ey:
            ans = cost
            break

        # 1) 좌회전
        nd = (d - 1) % 4
        nstate = (x, y, nd, mask)
        ncost = cost + 1
        if dist.get(nstate, INF) > ncost:
            dist[nstate] = ncost
            heapq.heappush(pq, (ncost, x, y, nd, mask))

        # 2) 우회전
        nd = (d + 1) % 4
        nstate = (x, y, nd, mask)
        ncost = cost + 1
        if dist.get(nstate, INF) > ncost:
            dist[nstate] = ncost
            heapq.heappush(pq, (ncost, x, y, nd, mask))

        # 3) 전진
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            cell = land[ny][nx]

            # 그냥 갈 수 있는 칸
            if cell != 'T':
                nstate = (nx, ny, d, mask)
                ncost = cost + 1
                if dist.get(nstate, INF) > ncost:
                    dist[nstate] = ncost
                    heapq.heappush(pq, (ncost, nx, ny, d, mask))

            # 나무 칸이면:
            else:
                idx = tree_idx[(nx, ny)]

                # 이미 벤 나무면 그냥 통과
                if mask & (1 << idx):
                    nstate = (nx, ny, d, mask)
                    ncost = cost + 1
                    if dist.get(nstate, INF) > ncost:
                        dist[nstate] = ncost
                        heapq.heappush(pq, (ncost, nx, ny, d, mask))

                # 아직 안 벤 나무면, K개 이하일 때만 새로 베고 통과
                else:
                    if mask.bit_count() < K:
                        nmask = mask | (1 << idx)
                        nstate = (nx, ny, d, nmask)
                        ncost = cost + 1
                        if dist.get(nstate, INF) > ncost:
                            dist[nstate] = ncost
                            heapq.heappush(pq, (ncost, nx, ny, d, nmask))

    print(f"#{tc} {-1 if ans == INF else ans}")
"""
2
5 2
GGTGG
GXTTG
GGTTG
GGTYG
GGTGG
8 3
XGGTTGGT
GGTGTTGT
GTTGGTGT
GGGTGGTT
TGTTTGGG
TTGGTTTG
GGTGGTTT
GGTTTGGY
"""
