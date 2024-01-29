import math

def lcm(a,b):
    return a*b/math.gcd(a,b)

Loop = int(input())

for _ in range(Loop):
    M,N,x,y = map(int,input().split())
    find = False
    dot = int(lcm(M,N))
    for i in range(1,dot+1):
        if ((i % M == x )and (i % N == y)):
            print(i)
            find=True
            break
    if(find == 0):
        print(-1)

        