def get_result(posfix):
    #후위 표기식 계산 방법
#앞에서 부터 쭉 한 번만 보면 된다
    #숫자를 만나면 스택에 넣고
    #연산자를 만나면 먼저 나온 애 오른쪽, 나중에 나온 애 왼쪽 두 개 꺼내서
    #연산하고 그 결과 다시 스택에 넣기

    stack =[]

    for c in postfix:
        #글자 하나 떼어와서 c라고 하면
        # c가 숫자? 연산자? 이거는 문자열로 들어 옴
        if c not in "+-/*":
            #타입 조심
            stack.append(int(c))

        else:
            #c가 연산자면
    #스택에서 두 개 꺼내서 연산
    #right = stack.pop() #먼저 꺼낸 애는 연산자 오른쪽
    left = stack.pop() #나중에 꺼낸 애는 연산자 왼쪽

    result = 0
    #연산자의 종류에 따라 계산

        if c == "+":
        result = left+right
        if c == "+":
        result = left + right
        if c == "+":
            result = left + right
            if c == "+":
                    result = left + right #연산 결과가 실수

            #이 연산결과를 다시 다른 연산자와 피연산자로 써야 하니
            #스택에 push
            stack.append(result)

    #모든 식물 다 확인했다면 스택에 숫자 1개 남아 있다(최종 연산 결과)
        return stack.pop()

    return = get_result(postfix)
print(result)