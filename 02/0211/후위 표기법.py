#중위 표기법(infix) => 후위표기법(postfix)

#우선순위 표(스택 밖:icp), (스택 안: isp)
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(":3}
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(":0}
#infix: 바꾸고 싶은 중위 표기식
#n: 식의 길이
def get_postfix(infix, n):
    #결과로 출력할 후위표기식
    postfix = ""
    stack = []

    #infix 에서 한 글자씩 떼어와서 식을 만들자
    for i in range(n):
        #i번째 글자 확인
        #연산자? 피연산자?
        if infix[i] not in "()+=*/"
            #i번 글자가 연산자 아니었다(숫자, 피연산자)
            #결과로 출력(후위 표기식에)
            postfix += infix[i]
        else:
            #i번 글자가 연산자였다
            #i번 글자가 오른쪽 괄호(닫는 괄호)라면
            if infix[i] == ")":
                #"(" 여는 괄호가 나올 때까지 스택에서 연산자 계속 pop
                #() 안의 연산자가 먼저 연산되어야 하기 때문에
                #꺼내서 쓴다(식에 먼저 써 줘야 함)
                while stack:
                    #연산자 꺼내기
                    op = stack.pop()
                    #꺼냈는데 여는 괄호 만나면 중단
                    if op == "(":
                        break

                    #후위표기식에 써 주기
                    postfix += op
            else:
                #i번 글자가 닫는 괄호가 아닌 연산자
                #i번 글자의 우선 순위를 알아내서 (icp[infix[i]])
                #스택의 꼭대기에 있는 연산자와 비교 (isp[stack[-1]])
                #icp[infix[i]] 얘랑 isp[stack[-1]] stack에서 제일 위에 있는 애 비교

                #1. 현재 i번 글자의 연산자의 우선순위 보다
                #스택의 꼭대기에 있는 우선순위가 같거나 높다면
                #i번 글자보다 우선순위가 같거나 높은 애들은 스택에서 모두 꺼내 쓴다.
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop() #더하기가 들어왔는데 스택에 곱하기 나누기가 있기 때문에 곱하기 나누기를 먼저 쓰는 상황

                #2. 현재 i번 글자의 연산자의 우선순위가
                # 스택의 꼭대기에 있는 우선순위보다 높다면
                #스택에 push
                stack.append(infix[i])

    #스택에 연산자가 남아 있다면 다 꺼내서 쓰면 된다
    while stack:
        postfix += stack.pop()
    return postfix

infix = "(6+5*(2-8)/2"
postfix = get_postfix(infix, len(infix))
print(postfix)

