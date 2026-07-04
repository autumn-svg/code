T=int(input())

for tc in range(1, T+1):
    # 이 문제는 문자열 내용을 바꿀 필요 x
    s1 = input()  # 첫 번째 문자열
    s2 = input()  # 두 번째 문자열

    # s1 안에 있는 글자들이  s2 안에 몇개씩 들어있는지 찾기
    # 그 중에 가장 많은 글자의 개수

    # 알파벳은 26개, 각 알파벳의 존재여부를 나타내는 배열
    s1_count=[0]*26
    # s1_count[25]=1 -> "Z"가 s1 안에 존재한다.
    # s1_count[14]=0 -> "O"가 s1 안에 존재하지 않는다.

    for c in s1:
        # s1에서 글자 하나 꺼내서 c라고 해야하는데..
        # 알파벳  c의 숫자코드를 알아내서 'A'의 숫자코드인 65와의 차이를 구하면
        # 이 알파벳이 가져야할 인덱스 번호를 구할수 있다.
        s1_count[ord(c)-65]=1

    # s1 안에 있는 알파벳이 s2 안에 몇개 포함되어있는지
    s2_count=[0]*26

    max_count=0
    # s2 안에 있는 알파벳 하나 가져와서
    for alphabet in s2:
        if s1_count[ord(alphabet)-65] == 1:
            s2_count[ord(alphabet)-65] += 1 # 이 알파벳이 s1에 있었으면 개수 +1

    # s2_count에서 가장 큰 값 찾기
    max_count += max(s2_count)  # 가장 많이 등장한 문자의 개수

    # 결과 출력
    print(f"#{tc} {max_count}")