import sys
sys.stdin = open("input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    p = [i for i in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
