import sys
from collections import Counter
input = sys.stdin.readline

N1 = int(input())
N2 = list(map(int,input().split()))
M1 = int(input())
M2 = list(map(int,input().split()))

count = Counter(N2)
for i in range(0,M1):
    if M2[i] in count:
        print(count[M2[i]],end=" ")
    else:
        print(0,end=" ")
