#top이라는 키워드와(크기ㅏ 고정된)배열을 활용한 스택

#스택 초기화(선언)
top :
# 스택에 마지막으로 삽입된 자료의 위치(인덱스)를 나타냄
top = -1
#m :스텍 크기
N = 10
#리스트로 스택을 만들기
stack = [0]*N

#스택에 자료 삽입하기
for i in range(1, 11):
    top += 1
    stack[top] = i

#스택에 자료를 추가하기 전에 스택이 꽉 찼나 확인
if top < N - 1: #넣을 수 있다면 추가, 밑에서 더하고 넣고 있어서 더하기 해도 10보단 작아야 됨. 그래서 -1
    top += 1
    stack[top] = 11

else:
    #스택에 더 이상 원소를 넣을 수 없음
    print('overflow')

print(stack, top)

#스택에서 자료 삭제
for i in range(10):
    element = stack[top]
    top -= 1 #위에서 하나 뺐으니까 아래에서 하나 빼 주면 됨
    print(element, end=',')
print()

 #다 꺼내고 나면 -1을 가리킴
# top이 있으면 얘는 스택이고 자료 삭제했으면 뭔가 남아 있어도 우리는 이 스택이 이제 비었다고 판단해야 함 이유는: 탑이 -1이니까
print(stack[top], top)
print(stack)



