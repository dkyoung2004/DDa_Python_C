from collections import deque


N =  int(input())
a = deque([i for i in range(1,N+1)])
for i in range(0,N-1):
    a.popleft()
    spare = a.popleft()
    a.append(spare)
print(a[0])
