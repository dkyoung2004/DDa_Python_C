from math import ceil

T = int(input())


for i in range(T):
    floor , room , guest = map(int,input().split())
    a = guest % floor
    b = (guest // floor) +1
    if a == 0:
        a = floor
        b -= 1
    print(a*100 + b)