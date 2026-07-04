number = [int(input()) for _ in range(9)]

max_v = 0
cnt = 0
cnt_v = 0

for i in number:
    for j in i:
        cnt += 1
    if j > max_v:
        max_v = j
        cnt_v = cnt
            
print(max_v)
print(cnt_v)        
        