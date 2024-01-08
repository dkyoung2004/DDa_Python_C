V = 0
N = 0
N = int(input())
Count = 0

a = []
a.extend(input().split( ))
a_int= list(map(int,a))
V = int(input())
for i in range(0,N):
    if a_int[i] == V:
        Count += 1
print(Count)