#front와 rear을 사랗아는 방법

#큐의 크기
N =10
#공백 상태의 큐를 생성
q =[0] * N
#front, rear 변수 초기화
front = rear = -1
#front: 삭제된 원소의 위치
#area : 마지막 원소의 위치

for i in range(1, 11):
    #원소를 삽입할 때는 rear+1 한 자리가 남음
    rear += 1
    q(rear) = i

print(q)
print(from, rear)

for i in range(10):
    #삭제 할 때는 front+1 자리에 있는 원소를 삭제
front =+ 1
print(q(front), end=" ")

#파이썬의 리스트 메서드를 사용
#공백상태의 큐
q = []

#원소 10개 추가
for i in range(1, 11):
    s. sppend