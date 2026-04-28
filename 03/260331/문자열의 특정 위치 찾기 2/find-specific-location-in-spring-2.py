word = ["apple", "banana", "grape", "blueberry", "orange"]

w = input()

cnt = 0


for i in word:
    if i[2] == w:
        
        cnt += 1
        print(i)
    elif i[3] == w:
        
        cnt += 1
        print(i)

print(cnt)

