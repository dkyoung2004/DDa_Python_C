import sys
input = sys.stdin.readline

N = int(input())
entrance = {}
for i in range(0,N):
    name , query= input().split()
    if(query == "enter"):
        entrance[name] = 'enter'
    else:
        del entrance[name]
for i in sorted(entrance,reverse=True):
    print(i)