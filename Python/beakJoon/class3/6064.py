import sys

input = sys.stdin.readline


def calc(M,N,x,y):
    i = x
    while i <= M * N:
        if(((i-x)) % M == 0 )and (((i-y)%N==0)):
            return(i)
        i += M
    return (-1)
Loop = int(input())

for _ in range(Loop):
    M,N,x,y = map(int,input().split())
    print(calc(M,N,x,y))
        