N = int(input())

for i in range(N, 101):
    if i >= 90:
        print("A", end=" ")
    if 90 > i >= 80:
        print("B", end=" ")
    if 80 > i >= 70:
        print("C", end=" ")
    if 70 > i >= 60:
        print("D", end=" ")
    if 60 > i:
        print("F", end=" ")