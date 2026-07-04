start, end = map(int, input().split())

'''
연습 문제 1: 완전수(Perfect Number) 흉내 내기
문제: start 이상 end 이하인 정수 중에서, 자신을 제외한 약수들의 합이 자기 자신보다 큰 수는 총 몇 개인지 구하기.

input: 10 20
output: 3
'''

# Please write your code here.





cnt = 0
for i in range(start, end+1):
    measure = 0
    
    for j in range(1, i):
        if i % j == 0:
            measure += j
            
    if measure > i:
        cnt += 1
print(cnt)
