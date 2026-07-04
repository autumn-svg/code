number = [int(input()) for _ in range(9)]

cnt = 0
max_v = 0
max_idx = 0

for i in number:
    cnt += 1
    
    if i > max_v:
        max_v = i
        max_idx = cnt
                
print(max_v)
print(max_idx)
        