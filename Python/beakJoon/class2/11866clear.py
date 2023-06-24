from collections import deque

N , K = map(int,input().split())
arr = []
index = 0
print("<",end="")
for i in range(1,N+1):
    arr.append(i)
arr = deque(arr)
while len(arr) > 1:
    arr.rotate((-(K-1)))
    print(arr.popleft(),end=", ")
print(arr[0],end="")
print(">")