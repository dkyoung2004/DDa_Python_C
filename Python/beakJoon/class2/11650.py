import sys

input = sys.stdin.readline
text = []
n = int(input())
b= []
for i in range(0,n):
    text.append(input().split())
b = sorted(text,key = lambda x: (x[0] , x[1]))
for j in range(0,n):
    print(b[j])
