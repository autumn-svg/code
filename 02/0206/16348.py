T = int(input())

for tc in range(1, T+1):
    #N: 문자열 길이, N개의 문자열
    #M: 우리가 찾아야 하는 회문의 길이
    N, M = map(int, input().split())

    text = [input() for _ in range(N)]
    #N과 M이 같을 때는 가로 세로 한 번만 보면 됨. 아니면...?
    #회문이 가능한 위치를 계산해야 한다...?
    #회문 문자열 찾기
    answer = ''

    #모든 열, 모든 행을 뒤져가며 길이 M짜리 회문을 찾기


# 가로 먼저
for i in range(N): #N은 가로세로 길이고 그 값을 i에 하나하ㅏ난나나나나나날ㅈ 넣어
    for j in range(N-M+1): #전체 길이(N)에서 회문 길이(M)을 빼고 +1(그 번호 포함) 그거를 j에 넣어
        for k in range(M//2): #회문의 반 위치를 k에 하나난나나나ㅏ나나나나난 넣어
            if text[i][j+k] != text[i][j+M-1-k]: #행 고정, 열 k(회문 반에서 하나하난나나나)가 하나나난나나나ㅏ추가된 게 텍열의 위치에 회문 위치랑 추가된 거 빼(뒤에서 오니까, 근데 ㄱ인덱스는 0부터니까 1빼야 돼)
                break #양쪽 값이 서로 같지 않으면 반복문 멈춰
        else:
            answer = text[i][j:j+M] #열은 고정이고 행이 움직인 회문을 답으로 바꿈
# 세로
        for k in range(M//2):#회문의 반 위치를 k에 하나란라나난나
            if text[j+k][i] != text[j+M-1-k][i]: #이거 옆으로 뒤집었을 때 생각으로 보면 됨 그래서 j+k가 행이 되고 i가 열처럼 됨
                break
        else:
            for x in range(M):#회문 만큼 x를 계속ㄱㄱㄷㄻㄷㄱ럳ㅁㄱㄹ
                answer += text[j+x][i]

print(f'#{tc} {answer}')


