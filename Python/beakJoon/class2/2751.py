import sys

input = sys.stdin.readline

numer = int(input())
a = []
for i in range(0,numer):
    a.append(int(input()))
for j in sorted(a):
    print(j)