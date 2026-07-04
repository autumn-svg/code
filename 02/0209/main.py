T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input())
    arr = list(input())
    word = list(input())

    idx = 0
    result = -1

    '''
    테스트 개수 주어짐
    N과 M이 구분되어 주어짐
    N개의 글자 카드가 주어짐
    스타티가 만들려는 단어가 주어짐
    
    단어를 완성할 수 없다면 -1을 출력
    계속 세 져야 하니까 인덱스는 0 미리 세팅
    문자를 비교 해야 하니 인덱싱한 거끼리 비교
    
    인덱스값끼리 서로 같다면 idx가 증가함
    
    내가 원하는 단어의 인덱스 j가 길이 M만큼 증가했다면, 단어가 완성되었다, 
    반복 중단하고 정답 기록
    
    '''

    for i in range(N):
        if arr[i] == word[idx]:
            idx += 1
        if idx == M:
            result = i
            break

    print(f'#{test_case} {result}')