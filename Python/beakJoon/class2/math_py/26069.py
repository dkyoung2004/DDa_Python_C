import sys

input = sys.stdin.readline

N = int(input())
rainbow = set()
rainbow.add("ChongChong")
for _ in range(N):
    A , B = map(str,input().split())
    if(A in rainbow and B not in rainbow):
        rainbow.add(B)
    elif(B in rainbow and A not in rainbow):
        rainbow.add(A)
print(len(rainbow))