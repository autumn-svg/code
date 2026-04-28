def countingsort(arr, n, k):
    #arr : 정렬할 배열(원소는 0이상 k이하의 정수, 최대값:k)

    #정렬 결과를 저장할 배열
    sorted_arr = [0] * n

    #숫자의 등장 횟수를 세서 저장할 카운팅 배열
    counts = [0] * (k+1)
    #arr 안에 있는 0의 개수, 1의 개수, ..., k의 개수
    #counts[0] : 0의 개수
    #counts[1] : 1의 개수
    #...
    #counts[k] : k의 개수

    #1. arr 안에 있는 숫자들의 등장 횟수(개수) 세기
    for i in range(n):
        #i 번 인덱스에 있는 숫자를 x라고 하자
        x = arr[i]
        #x의 개수를 1증가 시켜줘야 한다.
        counts[x] += 1

    #2. counts 배열의 값 조정(누적합)

    #카운팅 정렬의 원리는 숫자의 자리를 배치하는 것
    #어떤 숫자 x가 있을 때, x보다 작거나 같은 숫자의 개수를 알고 있다면
    #x는 그 갯수만큼의 인덱스 위치에 놓으면 된다.

    #1이 2개, 2가 1개, 3이 1개, 4가 2개있다면?
    #4는 어디에 놓아야 될까?
    #4보다 작거나 같은 숫자가 6개 -> 6번째 위치부터 4를 놓으면 된다.
    #인덱스는 0부터 시작하고, 같은 숫자가 여러 번 등장하니 다음 4를 위해 -1씩 감소
    #각 숫자의 정렬 후 위치를 계산하기 위해 누적합을 구해나간다.
    for i in range(1, k+1):
        #숫자 i보다 같거나 작은 숫자의 개수
        counts[i] += counts[i - 1]


    #3. counts 배열을 참고해서 각 숫자의 자리 배치 시작(정렬)
    #안정 정렬을 위해서 뒤에서부터 배치
    for i in range(n-1, -1, -1): #!= 버블정렬, 가장 첫 자리가 자동 배정되는 것 아님
        #arr에 있는 i번째 숫자를 x라고 하면
        x = arr[i]
        # x의 자리는 어떻게 알아?? -> counts[x] (x보다 작거나 같았던 원소의 개수)
        counts[x] -= 1
        #1 감소한 위치에 x를 놓는다.
        sorted_arr[counts[x]] = x

    return sorted_arr

data = [0,4,1,3,1,2,4,1]
print(countingsort(data, len(data), max(data)))

import random
data2 = [random.randint(0,10) for _ in range(10)]
print(data2)
print(countingsort(data2, len(data2), max(data2)))