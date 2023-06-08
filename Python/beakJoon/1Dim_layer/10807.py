V = 0
N = 0
N = int(input())
Count = 0

a = []
a.extend(input().split())
a = list(map(int,a))
for i in range(0,N):
    if a[i] == V:
        Count += 1
print(a)
print(Count)