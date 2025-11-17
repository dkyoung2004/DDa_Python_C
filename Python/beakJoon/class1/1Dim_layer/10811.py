N, M = map(int,input().split())
arr = list(range(1,N+1))
for i in range(M):
    a , b = map(int,input().split())
    temp = arr[a-1: b]
    temp.reverse()
    arr[a-1:b] = temp
print(*arr)