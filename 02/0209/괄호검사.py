T = int(input())

for tc in range(1, T + 1):
    # 검사할 코드 입력
    code = input()

    # 스택을 사용해서 괄호검사를 할것이다.
    stack = []

    pair = {"(": ")", "{": "}"}
    # pair["("] => ")"

    # 문제에서 원하는 답 : 일단 제대로 되어있다고 가정
    answer = 1

    # 한글자 한글자 꺼내서 확인
    for c in code:
        # 한글자 꺼내서 c라고 하면
        # 우리가 관심있는거는 괄호 ({ })

        # 여는 괄호를 만나면 스택에 push
        if c in "({":
            stack.append(c)
        # 닫는 괄호를 만나면
        # 스택에서 여는괄호 하나 꺼낸 다음 짝이 맞는지 검사
        # 단!!!! 꺼내기전에 스택이 비어있나 확인
        # 비어있다면 괄호가 잘못되어 있다.
        if c in ")}":
            # 여는괄호가 스택에 남아있나 확인
            if not stack:
                # 스택이 비었으면 괄호 짝 안맞음!!
                answer = 0
                break

            # 스택안에 여는괄호가 남아있다.
            # 가장 최근에 만난 여는 괄호 하나 꺼내서
            # c와 짝이 맞는지 검사
            left = stack.pop()
            if pair[left] != c:
                answer = 0
                break
    # 모든 글자를 검색하고 나서 스택에 여는 괄호가 남아있어도 오류
    if stack:
        answer = 0

    print(f"#{tc} {answer}")