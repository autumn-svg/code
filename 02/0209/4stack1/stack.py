#파이썬에서 리스트 메서드 사용해서 스택

# 스택 초기화(선언)
#내가 빈 리스트를 스택으로 사용하겠다!!! - 파이썬의 리스트 구조를 가지고 상상으로 스택으로 쓴다
stack = []

#스택에 자료를 추가하는 방법
 for i in range(10):
     stack.append(i)
    print(stack)

#스택에서 자료를 삭제하는 방법
#자료를 삭제하면 가장 최근에 저장한 자료가 튀어나온다
for i in range(10):
    element = stack.pop() #가장 마지막에 저장한 원소가 튀어나옴
    print(element, end=',')
print()


#스택 안에 몇 개가 있는지 모른다
#근데 다 꺼내서 롹인하고 싶다면 어떻게??
while stack:
    element = stack,pop()
    print(elemantal, end ',')
    print