import sys

input = sys.stdin.readline

N = int(input())
N_arr = set(map(int,input().split()))
M=int(input())
M_arr = list(map(int,input().split()))

for i in M_arr:
    if i in N_arr:
        print(1)
    else:
        print(0)
