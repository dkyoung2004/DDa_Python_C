from collections import deque


N = str(input())
N = list(N)
N = deque(N)
check = 1
for i in range(0,int(len(N)/2)):
    if (N.popleft() != N.pop()):
        check = 0
print(check)
