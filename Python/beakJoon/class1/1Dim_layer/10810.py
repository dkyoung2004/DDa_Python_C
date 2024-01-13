N , M = map(int,input().split())
arr = [0] * N
for _ in range(M):
    i , j, k = map(int,input().split())
    for l in range(i-1,j):
        arr[l] = k
for value in arr:
    print(value,end=' ')