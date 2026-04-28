cq = [0] * N
front = rear = 0
#원형큐는 공백과 포화상채 구분을 쉽게하기 위해 front 자리를 한 개 비워준다
def is_full():
    return (rear + 1) % M == front
#원형큐에 원소를 10개 삽입
for i in range(1,11):
    if not is_full():
        rear = (rear + 1 )% N
        cq[rear] = i

print(cq)
print(front, rear)

for i in range(9):
    front = (front + 1) % N
    print(cq[front], end= " ")

    print()
    print(cq)
    print(front, rear)