T = int(input())

for test_case in range(1, T+1):
    # 구역의 개수
    # 0 : 사무실
    # 2~N-1 : 나머지 구역
    N = int(input())

    # E[i][j] : i번 구역에서 출발해서 j번 구역으로 갈 때 에너지 사용량
    # E[i][j] 는 E[j][i] 와 다를 수도 있다.
    E = [list(map(int, input().split())) for _ in range(N)]

    # 최소 에너지 사용량
    min_e = float("inf")

    # 방문 체크 배열(이전에 방문한 구역은 다시 방문X)
    visited = [0] * N
    # 첫번째 방은 사무실, 방문 체크 미리 해 두자.
    visited[0] = 1

    # current_room : 현재 위치한 방 번호
    # e : 현재 방 번호까지 오는데 사용한 에너지 양
    def patrol(current_room, e, path):
        global min_e

        # 0. 가지치기
        # 현재까지 구한 에너지의 합이 내가 알고 있는 최소 에너지보다 크면??
        # 더 이상 진행할 필요가 없다
        if e >= min_e:
            return

        # 1. 종료조건
        if 0 not in visited:
            # 남은 방문할 구역이 없다면 종료
            # 끝에 첫번째 방까지 돌아오는 것까지 생각
            e += E[current_room][0]
            # 현재 완성한 경로의 에너지 사용량과 이전에 최소였던 에너지 중에서 최소값
            min_e = min(e, min_e)
            return

        # 2. 재귀호출
        # 내가 지금까지 선택하지 않은 구역 중 하나 선택
        # 다음 단계로
        for next_room in range(N):
            # next_room : 이번에 방문할 방 번호
            if not visited[next_room]:
                # 방문하지 않았다면 이번에 방문
                visited[next_room] = 1
                # 다음에 방문할 방 번호 선택하러 재귀호출
                # 현재 방 번호를 알고 있어야 에너지 사용량을 계산
                path.append(next_room)
                e_sum = E[current_room][next_room]
                patrol(next_room, e + e_sum, path)
                #주의!! 에너지 사용량 되돌리기
                visited[next_room] = 0
                path.pop()
        # 0번(사무실)에서 출발, 에너지 사용량 0부터 시작
    patrol(0, 0,[])

    print(f"#{test_case} {min_e}")
