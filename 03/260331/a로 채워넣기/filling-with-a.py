T = input()
T_lst = list(T)
T_lst[1] = "a"
T_lst[-2] = "a"

print(*T_lst, sep="")
