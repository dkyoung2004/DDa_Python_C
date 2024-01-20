import sys

input = sys.stdin.readline

X = int(input())
i=0
j=0
while(X>j):
    i += 1
    j += i
if (i % 2== 0):
    print(i+(X-j),1-X+j,sep='/')
else:
    print(1-X+j,i+(X-j),sep='/')